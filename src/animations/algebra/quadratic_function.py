from manim import *
import numpy as np

class QuadraticFunctionAnimation(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 8, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": BLUE},
        )
        
        # Add labels
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Create title
        title = Text("Quadratic Function Animation", font_size=36).to_edge(UP)
        
        # Display axes and title
        self.play(Create(axes), Write(axes_labels), Write(title))
        self.wait(1)
        
        # Define quadratic function
        def quadratic(x):
            return x**2 - 2*x + 1
            
        # Create the initial parabola
        parabola = axes.plot(quadratic, color=RED, x_range=[-3, 5])
        equation = MathTex(r"f(x) = x^2 - 2x + 1").next_to(axes, RIGHT).shift(UP*2)
        
        self.play(Create(parabola), Write(equation))
        self.wait(2)
        
        # Show vertex
        vertex_point = Dot(axes.coords_to_point(1, 0), color=YELLOW)
        vertex_label = Text("Vertex (1, 0)", font_size=24).next_to(vertex_point, DOWN)
        
        self.play(FadeIn(vertex_point), Write(vertex_label))
        self.wait(2)
        
        # Transform to different quadratic
        new_equation = MathTex(r"f(x) = 2x^2 - 4x + 3").next_to(axes, RIGHT).shift(UP*2)
        
        def new_quadratic(x):
            return 2*x**2 - 4*x + 3
            
        new_parabola = axes.plot(new_quadratic, color=GREEN, x_range=[-2, 4])
        new_vertex_point = Dot(axes.coords_to_point(1, 1), color=YELLOW)
        new_vertex_label = Text("Vertex (1, 1)", font_size=24).next_to(new_vertex_point, DOWN)
        
        self.play(
            Transform(parabola, new_parabola),
            Transform(equation, new_equation),
            Transform(vertex_point, new_vertex_point),
            Transform(vertex_label, new_vertex_label)
        )
        self.wait(2)
        
        # Add focus on coefficients
        coeff_text = Text("Coefficient 'a' affects width and direction", font_size=24).to_edge(DOWN)
        self.play(Write(coeff_text))
        self.wait(3)
        
        self.play(FadeOut(*self.mobjects))