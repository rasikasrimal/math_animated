# Dark Theme Manim CE Scripts: Derivatives (Titles/Subtitles fixed)
# ---------------------------------------------------------------
# How to render (examples):
#   manim -pqh derivatives_dark.py DerivativeExplanation
#   manim -p   derivatives_dark.py DerivativeApplications
#
# Notes:
# - Clean dark theme optimized for YouTube.
# - Consistent title/subtitle styling via helper.
# - Color palette chosen for contrast on dark background.

from manim import *
import numpy as np

# ---------- Global Config ----------
config.pixel_width  = 1920
config.pixel_height = 1080
config.frame_rate   = 60
config.background_color = "#0f0f0f"  # deep gray (dark theme)

# ---------- Palette ----------
FG          = "#F0F3F6"  # near-white text
MUTED       = GREY_B
PRIMARY     = BLUE_C
ACCENT      = YELLOW_C
GOOD        = GREEN_C
BAD         = RED_C
INFO        = TEAL_A

TITLE_SIZE     = 66
SUBTITLE_SIZE  = 36
LABEL_SIZE     = 28

# ---------- Helpers ----------
def title_card(title_text: str, subtitle_text: str) -> VGroup:
    """Create a centered title + subtitle group with an accent divider."""
    title = Text(title_text, font="Roboto", weight=BOLD, color=FG).scale(TITLE_SIZE / 48)
    subtitle = Text(subtitle_text, font="Roboto", color=MUTED).scale(SUBTITLE_SIZE / 48)
    divider = Line(LEFT, RIGHT, color=ACCENT, stroke_width=6).match_width(title).scale(0.6)
    group = VGroup(title, divider, subtitle).arrange(DOWN, buff=0.35).to_edge(UP, buff=0.8)
    return group

def axis_labels(axes: Axes) -> VGroup:
    """Axis labels styled for dark theme."""
    x_lab = axes.get_x_axis_label(MathTex("x", color=FG), edge=DOWN, direction=DOWN, buff=0.4)
    y_lab = axes.get_y_axis_label(MathTex("y", color=FG), edge=LEFT, direction=LEFT, buff=0.4)
    return VGroup(x_lab, y_lab)

# ============================================================
# Scene 1: Understanding Derivatives (Dark Theme)
# ============================================================

class DerivativeExplanation(Scene):
    def construct(self):
        # ----- Title Card -----
        tc = title_card("Understanding Derivatives", "The slope of the tangent line")
        self.play(FadeIn(tc[0], shift=UP*0.3), GrowFromCenter(tc[1]), FadeIn(tc[2], shift=DOWN*0.2))
        self.wait(1.2)
        self.play(FadeOut(tc, shift=UP*0.2))

        # ----- Axes -----
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=11,
            y_length=6.2,
            axis_config={"color": MUTED, "stroke_width": 3},
            tips=False,
        ).to_edge(DOWN, buff=0.9)

        labs = axis_labels(axes)
        self.play(Create(axes), FadeIn(labs[0], shift=DOWN*0.1), FadeIn(labs[1], shift=LEFT*0.1))

        # ----- Functions -----
        def func(x): return x**3 - 3*x + 1
        def derivative_func(x): return 3*x**2 - 3

        func_graph = axes.plot(func, x_range=[-2.7, 2.7], color=PRIMARY, stroke_width=6)
        derivative_graph = axes.plot(derivative_func, x_range=[-2.7, 2.7], color=BAD, stroke_width=4)

        func_label = MathTex(r"f(x)=x^3-3x+1", color=PRIMARY).scale(0.9).to_corner(UR).shift(LEFT*0.6+DOWN*0.2)
        d_label    = MathTex(r"f'(x)=3x^2-3", color=BAD).scale(0.9).next_to(func_label, DOWN, buff=0.35).align_to(func_label, LEFT)

        self.play(Create(func_graph), Write(func_label))
        self.play(Create(derivative_graph), Write(d_label))
        self.wait(0.4)

        # ----- Explanation footer -----
        explanation = Text(
            "The derivative gives the slope of the tangent line at each point.",
            font="Roboto",
            color=FG
        ).scale(LABEL_SIZE/48).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(explanation, shift=UP*0.1))

        # ----- Moving point + tangent line -----
        x_tracker = ValueTracker(-2.2)
        dot = Dot(color=ACCENT, radius=0.08)
        dot.add_updater(lambda m: m.move_to(axes.c2p(x_tracker.get_value(), func(x_tracker.get_value()))))

        tangent_line = always_redraw(
            lambda: axes.plot(
                lambda t: func(x_tracker.get_value())
                          + derivative_func(x_tracker.get_value()) * (t - x_tracker.get_value()),
                x_range=[x_tracker.get_value()-1, x_tracker.get_value()+1],
                color=GOOD,
                stroke_width=3
            )
        )

        slope_text = always_redraw(
            lambda: VGroup(
                MathTex(r"\text{Slope }=\,", color=FG),
                MathTex(f"{derivative_func(x_tracker.get_value()):.2f}", color=GOOD)
            ).arrange(RIGHT, buff=0.1).to_corner(UL).shift(DOWN*0.2+RIGHT*0.2)
        )

        self.play(FadeIn(dot), Create(tangent_line), FadeIn(slope_text))
        self.play(x_tracker.animate.set_value(2.2), run_time=4, rate_func=linear)
        self.wait(0.4)

        # ----- Critical points -----
        critical_x_values = [-1, 1]  # where f'(x)=0
        crit_group = VGroup()
        for xv in critical_x_values:
            p = Dot(axes.c2p(xv, func(xv)), color=ACCENT, radius=0.1)
            lbl = MathTex(fr"x={xv}", color=ACCENT).scale(0.7).next_to(p, UP, buff=0.12)
            crit_group.add(p, lbl)

        crit_title = Text("Critical points: where  f'(x) = 0", font="Roboto", color=ACCENT)\
            .scale((LABEL_SIZE-2)/48)\
            .next_to(explanation, UP, buff=0.25)

        self.play(FadeIn(crit_group, lag_ratio=0.2), Write(crit_title))
        self.wait(0.6)

        # ----- Color-coded increasing/decreasing regions -----
        inc1 = axes.plot(func, x_range=[-2.7, -1], color=GOOD, stroke_width=6)
        dec  = axes.plot(func, x_range=[-1, 1],   color=BAD,  stroke_width=6)
        inc2 = axes.plot(func, x_range=[1, 2.7],  color=GOOD, stroke_width=6)
        self.play(Create(inc1), Create(dec), Create(inc2))

        legend = VGroup(
            VGroup(Dot(color=GOOD), Text("Increasing  (f'(x)>0)", color=FG, font="Roboto").scale(0.55)).arrange(RIGHT, buff=0.15),
            VGroup(Dot(color=BAD),  Text("Decreasing (f'(x)<0)", color=FG, font="Roboto").scale(0.55)).arrange(RIGHT, buff=0.15),
            VGroup(Dot(color=ACCENT), Text("f'(x)=0  → critical", color=FG, font="Roboto").scale(0.55)).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_corner(UR).shift(LEFT*0.6+DOWN*0.2)
        self.play(FadeIn(legend, shift=LEFT*0.2))
        self.wait(1.0)

        # ----- Summary card -----
        self.play(FadeOut(VGroup(legend, crit_title)))
        summary = VGroup(
            Text("Key Insights", font="Roboto", weight=BOLD, color=FG).scale(0.85),
            Text("• Derivative = slope of tangent line", font="Roboto", color=FG).scale(0.7),
            Text("• f'(x) > 0  → function increasing", font="Roboto", color=GOOD).scale(0.7),
            Text("• f'(x) < 0  → function decreasing", font="Roboto", color=BAD).scale(0.7),
            Text("• f'(x) = 0  → critical point", font="Roboto", color=ACCENT).scale(0.7),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).to_corner(UL).shift(DOWN*0.1+RIGHT*0.2)

        box = SurroundingRectangle(summary, color=MUTED, corner_radius=0.12, buff=0.3)
        self.play(FadeIn(box, shift=UP*0.1), FadeIn(summary, shift=UP*0.1))
        self.wait(1.4)

        # ----- Clean exit -----
        self.play(FadeOut(VGroup(
            axes, labs, func_graph, derivative_graph, func_label, d_label,
            explanation, dot, tangent_line, slope_text, crit_group, inc1, dec, inc2, box, summary
        )), run_time=0.8)

# ============================================================
# Scene 2: Derivative Applications (Dark Theme)
# ============================================================

class DerivativeApplications(Scene):
    """Practical applications: optimization + kinematics"""
    def construct(self):
        # ----- Title Card -----
        tc = title_card("Derivative Applications", "Optimization • Motion • Rates of Change")
        self.play(FadeIn(tc[0], shift=UP*0.3), GrowFromCenter(tc[1]), FadeIn(tc[2], shift=DOWN*0.2))
        self.wait(1.0)
        self.play(FadeOut(tc, shift=UP*0.2))

        # ---------- Optimization Example ----------
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 8, 1],
            x_length=9.5,
            y_length=6.0,
            axis_config={"color": MUTED, "stroke_width": 3},
            tips=False,
        ).to_edge(LEFT, buff=0.7).shift(DOWN*0.2)

        def P(x): return -x**2 + 4*x + 3  # Profit
        def dP(x): return -2*x + 4

        p_graph = axes.plot(P, x_range=[0, 5.2], color=GOOD, stroke_width=6)
        p_label = MathTex(r"P(x)=-x^2+4x+3", color=GOOD).scale(0.9).to_corner(UR).shift(LEFT*0.6+DOWN*0.2)

        self.play(Create(axes), Create(p_graph), Write(p_label))

        # Maximum at P'(x)=0 -> x=2
        x_star = 2
        max_pt = Dot(axes.c2p(x_star, P(x_star)), color=ACCENT, radius=0.1)
        max_lab = Text("Maximum Profit", font="Roboto", color=ACCENT).scale(0.7).next_to(max_pt, UP, buff=0.15)
        d_at_max = MathTex("P'(2)=0", color=ACCENT).scale(0.8).next_to(max_lab, DOWN, buff=0.15)
        arrow = Arrow(axes.c2p(0.8, 6.2), axes.c2p(x_star, P(x_star)), color=ACCENT, stroke_width=5, max_tip_length_to_length_ratio=0.12)

        self.play(FadeIn(max_pt), Write(max_lab), Write(d_at_max), Create(arrow))
        self.wait(0.8)
        self.play(FadeOut(VGroup(arrow, max_lab, d_at_max)))

        # Transition out
        self.play(FadeOut(VGroup(axes, p_graph, p_label, max_pt)))

        # ---------- Motion: s(t), v(t), a(t) ----------
        axes2 = Axes(
            x_range=[0, 4, 1],
            y_range=[-2, 6, 1],
            x_length=11,
            y_length=6.0,
            axis_config={"color": MUTED, "stroke_width": 3},
            tips=False,
        ).to_edge(DOWN, buff=0.8)

        def s(t): return t**3 - 3*t**2 + 2*t
        def v(t): return 3*t**2 - 6*t + 2
        def a(t): return 6*t - 6

        s_graph = axes2.plot(s, x_range=[0, 3.2], color=PRIMARY, stroke_width=5)
        v_graph = axes2.plot(v, x_range=[0, 3.2], color=GOOD,   stroke_width=4)
        a_graph = axes2.plot(a, x_range=[0, 3.2], color=BAD,    stroke_width=3)

        labels = VGroup(
            MathTex(r"s(t)=t^3-3t^2+2t", color=PRIMARY),
            MathTex(r"v(t)=s'(t)=3t^2-6t+2", color=GOOD),
            MathTex(r"a(t)=v'(t)=6t-6", color=BAD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_corner(UR).shift(LEFT*0.6+DOWN*0.2)

        self.play(Create(axes2), Create(s_graph), Create(v_graph), Create(a_graph), FadeIn(labels, shift=UP*0.1))

        foot = Text("Position → Velocity → Acceleration (differentiate each step)",
                    font="Roboto", color=FG).scale(LABEL_SIZE/48).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(foot, shift=UP*0.1))
        self.wait(1.4)

        # Clean exit
        self.play(FadeOut(VGroup(axes2, s_graph, v_graph, a_graph, labels, foot)), run_time=0.8)
