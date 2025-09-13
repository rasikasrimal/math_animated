from manim import *
import numpy as np

class DerivativeVisualization(Scene):
    def construct(self):
        # Create title
        title = Text("Derivative: Rate of Change", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create axes
        axes = Axes(
            x_range=[-2, 4, 1],
            y_range=[-1, 9, 1],
            x_length=8,
            y_length=6,
            axis_config={"color": BLUE},
        )
        
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        
        self.play(Create(axes), Write(axes_labels))
        self.wait(1)
        
        # Define function f(x) = x^2
        def func(x):
            return x**2
            
        # Create the curve
        curve = axes.plot(func, color=RED, x_range=[-1.5, 3.5])
        function_label = MathTex(r"f(x) = x^2").next_to(axes, RIGHT).shift(UP*2)
        
        self.play(Create(curve), Write(function_label))
        self.wait(2)
        
        # Show a point on the curve
        x_val = 1.5
        point = Dot(axes.coords_to_point(x_val, func(x_val)), color=YELLOW)
        point_label = MathTex(f"({x_val:.1f}, {func(x_val):.1f})").next_to(point, UR)
        
        self.play(FadeIn(point), Write(point_label))
        self.wait(1)
        
        # Show secant line
        h = 1.0
        x2 = x_val + h
        secant_line = Line(
            axes.coords_to_point(x_val, func(x_val)),
            axes.coords_to_point(x2, func(x2)),
            color=GREEN
        )
        
        # Calculate slope
        slope = (func(x2) - func(x_val)) / h
        slope_text = MathTex(f"\\text{{Slope}} = \\frac{{{func(x2):.1f} - {func(x_val):.1f}}}{{{h:.1f}}} = {slope:.1f}").to_edge(DOWN)
        
        self.play(Create(secant_line), Write(slope_text))
        self.wait(2)
        
        # Animate h getting smaller
        for new_h in [0.5, 0.2, 0.1]:
            new_x2 = x_val + new_h
            new_secant = Line(
                axes.coords_to_point(x_val, func(x_val)),
                axes.coords_to_point(new_x2, func(new_x2)),
                color=GREEN
            )
            new_slope = (func(new_x2) - func(x_val)) / new_h
            new_slope_text = MathTex(f"\\text{{Slope}} = {new_slope:.1f}").to_edge(DOWN)
            
            self.play(
                Transform(secant_line, new_secant),
                Transform(slope_text, new_slope_text),
                run_time=1
            )
            self.wait(0.5)
        
        # Show tangent line (derivative)
        derivative_slope = 2 * x_val  # derivative of x^2 is 2x
        tangent_point1 = axes.coords_to_point(x_val - 0.5, func(x_val) - 0.5 * derivative_slope)
        tangent_point2 = axes.coords_to_point(x_val + 0.5, func(x_val) + 0.5 * derivative_slope)
        tangent_line = Line(tangent_point1, tangent_point2, color=ORANGE)
        
        derivative_text = MathTex(f"f'({x_val:.1f}) = {derivative_slope:.1f}").to_edge(DOWN)
        derivative_formula = MathTex(r"f'(x) = 2x").next_to(function_label, DOWN)
        
        self.play(
            Transform(secant_line, tangent_line),
            Transform(slope_text, derivative_text),
            Write(derivative_formula)
        )
        self.wait(2)
        
        # Show interpretation
        interpretation = Text("The derivative represents the instantaneous rate of change", 
                            font_size=24).to_edge(DOWN).shift(DOWN*0.5)
        self.play(Write(interpretation))
        self.wait(3)
        
        self.play(FadeOut(*self.mobjects))