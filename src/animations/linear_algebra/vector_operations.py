from manim import *
import numpy as np

class VectorOperations(Scene):
    def construct(self):
        # Create title
        title = Text("Vector Operations", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create coordinate system
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            x_length=8,
            y_length=6,
            axis_config={"color": BLUE}
        )
        
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        self.play(Create(axes), Write(axes_labels))
        self.wait(1)
        
        # Define vectors
        vector_a = np.array([3, 2])
        vector_b = np.array([1, 3])
        
        # Create vector A
        arrow_a = Arrow(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(vector_a[0], vector_a[1]),
            color=RED,
            buff=0
        )
        label_a = MathTex(r"\vec{a} = (3, 2)", color=RED).to_edge(LEFT).shift(UP*2)
        
        self.play(Create(arrow_a), Write(label_a))
        self.wait(1)
        
        # Create vector B
        arrow_b = Arrow(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(vector_b[0], vector_b[1]),
            color=GREEN,
            buff=0
        )
        label_b = MathTex(r"\vec{b} = (1, 3)", color=GREEN).next_to(label_a, DOWN)
        
        self.play(Create(arrow_b), Write(label_b))
        self.wait(2)
        
        # Vector addition - show parallelogram method
        addition_title = Text("Vector Addition", font_size=24).to_edge(RIGHT).shift(UP*2)
        self.play(Write(addition_title))
        
        # Move vector B to the tip of vector A
        arrow_b_translated = Arrow(
            axes.coords_to_point(vector_a[0], vector_a[1]),
            axes.coords_to_point(vector_a[0] + vector_b[0], vector_a[1] + vector_b[1]),
            color=GREEN,
            buff=0
        )
        
        self.play(Transform(arrow_b.copy(), arrow_b_translated))
        self.wait(1)
        
        # Show resultant vector
        vector_sum = vector_a + vector_b
        arrow_sum = Arrow(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(vector_sum[0], vector_sum[1]),
            color=YELLOW,
            buff=0
        )
        label_sum = MathTex(r"\vec{a} + \vec{b} = (4, 5)", color=YELLOW).next_to(label_b, DOWN)
        
        self.play(Create(arrow_sum), Write(label_sum))
        self.wait(2)
        
        # Clear addition visualization
        self.play(FadeOut(arrow_b_translated), FadeOut(addition_title))
        
        # Vector subtraction
        subtraction_title = Text("Vector Subtraction", font_size=24).to_edge(RIGHT).shift(UP*2)
        self.play(Write(subtraction_title))
        
        vector_diff = vector_a - vector_b
        arrow_diff = Arrow(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(vector_diff[0], vector_diff[1]),
            color=PURPLE,
            buff=0
        )
        label_diff = MathTex(r"\vec{a} - \vec{b} = (2, -1)", color=PURPLE).next_to(label_sum, DOWN)
        
        self.play(Create(arrow_diff), Write(label_diff))
        self.wait(2)
        
        # Scalar multiplication
        self.play(FadeOut(subtraction_title))
        scalar_title = Text("Scalar Multiplication", font_size=24).to_edge(RIGHT).shift(UP*2)
        self.play(Write(scalar_title))
        
        # Scale vector A by 1.5
        scaled_vector = 1.5 * vector_a
        arrow_scaled = Arrow(
            axes.coords_to_point(0, 0),
            axes.coords_to_point(scaled_vector[0], scaled_vector[1]),
            color=ORANGE,
            buff=0
        )
        label_scaled = MathTex(r"1.5\vec{a} = (4.5, 3)", color=ORANGE).next_to(label_diff, DOWN)
        
        self.play(Create(arrow_scaled), Write(label_scaled))
        self.wait(2)
        
        # Dot product visualization
        self.play(FadeOut(scalar_title))
        dot_title = Text("Dot Product", font_size=24).to_edge(RIGHT).shift(UP*2)
        self.play(Write(dot_title))
        
        dot_product = np.dot(vector_a, vector_b)
        label_dot = MathTex(f"\\vec{{a}} \\cdot \\vec{{b}} = {dot_product}", color=WHITE).next_to(label_scaled, DOWN)
        dot_formula = MathTex(r"\vec{a} \cdot \vec{b} = ||\vec{a}|| \cdot ||\vec{b}|| \cos(\theta)").next_to(label_dot, DOWN)
        
        self.play(Write(label_dot), Write(dot_formula))
        self.wait(3)
        
        self.play(FadeOut(*self.mobjects))