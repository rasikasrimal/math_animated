from manim import *
import numpy as np

class CircleGeometryAnimation(Scene):
    def construct(self):
        # Create title
        title = Text("Circle Geometry: Area and Circumference", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create a circle
        circle = Circle(radius=2, color=BLUE, fill_opacity=0.3)
        circle_center = Dot(ORIGIN, color=RED)
        center_label = Text("Center", font_size=20).next_to(circle_center, DOWN)
        
        self.play(Create(circle), FadeIn(circle_center), Write(center_label))
        self.wait(1)
        
        # Show radius
        radius_line = Line(ORIGIN, circle.point_at_angle(PI/4), color=YELLOW)
        radius_label = Text("r", font_size=24, color=YELLOW).next_to(radius_line, UR)
        
        self.play(Create(radius_line), Write(radius_label))
        self.wait(1)
        
        # Show diameter
        diameter_line = Line(circle.point_at_angle(0), circle.point_at_angle(PI), color=GREEN)
        diameter_label = Text("d = 2r", font_size=24, color=GREEN).next_to(diameter_line, DOWN)
        
        self.play(Create(diameter_line), Write(diameter_label))
        self.wait(2)
        
        # Formulas
        circumference_formula = MathTex(r"C = 2\pi r", color=BLUE).to_edge(LEFT).shift(UP*1)
        area_formula = MathTex(r"A = \pi r^2", color=ORANGE).to_edge(LEFT).shift(DOWN*1)
        
        self.play(Write(circumference_formula))
        self.wait(1)
        self.play(Write(area_formula))
        self.wait(2)
        
        # Animate circumference calculation
        if hasattr(circle, 'get_arc_length'):
            circumference_value = MathTex(r"C = 2\pi \cdot 2 = 4\pi", color=BLUE).next_to(circumference_formula, DOWN)
        else:
            circumference_value = MathTex(r"C = 2\pi \cdot 2 = 4\pi", color=BLUE).next_to(circumference_formula, DOWN)
        
        self.play(Write(circumference_value))
        self.wait(1)
        
        # Animate area calculation
        area_value = MathTex(r"A = \pi \cdot 2^2 = 4\pi", color=ORANGE).next_to(area_formula, DOWN)
        self.play(Write(area_value))
        self.wait(2)
        
        # Transform circle to show different radius
        new_circle = Circle(radius=3, color=PURPLE, fill_opacity=0.3)
        new_radius_line = Line(ORIGIN, new_circle.point_at_angle(PI/4), color=YELLOW)
        new_radius_label = Text("r = 3", font_size=24, color=YELLOW).next_to(new_radius_line, UR)
        
        self.play(
            Transform(circle, new_circle),
            Transform(radius_line, new_radius_line),
            Transform(radius_label, new_radius_label)
        )
        
        # Update calculations
        new_circumference = MathTex(r"C = 2\pi \cdot 3 = 6\pi", color=BLUE).next_to(circumference_formula, DOWN)
        new_area = MathTex(r"A = \pi \cdot 3^2 = 9\pi", color=ORANGE).next_to(area_formula, DOWN)
        
        self.play(
            Transform(circumference_value, new_circumference),
            Transform(area_value, new_area)
        )
        self.wait(3)
        
        self.play(FadeOut(*self.mobjects))