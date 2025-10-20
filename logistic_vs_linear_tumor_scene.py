from manim import *
import numpy as np

class LogisticVsLinearTumor(Scene):
    def construct(self):
        # Title
        title = Text("Why Use Logistic Regression?", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Intro
        intro = Text(
            "Linear regression isn't ideal for yes/no questions.\nLet's see why, using a tumor example...",
            font_size=32
        )
        self.play(Write(intro))
        self.wait(2)
        self.play(FadeOut(intro))

        # Axes setup
        axes = Axes(
            x_range=[0, 10], y_range=[-0.5, 1.5, 0.5],
            x_length=7, y_length=4,
            axis_config={"color": WHITE},
            tips=False
        ).to_edge(LEFT, buff=0.7)
        x_label = axes.get_x_axis_label("Tumor Size", edge=DOWN, direction=DOWN, buff=0.4)
        # Make y-axis label vertical
        y_label = Text("Malignant? (0/1)", font_size=28).rotate(PI/2).next_to(axes.y_axis, LEFT, buff=0.4)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        # Example data (tumor size vs malignant)
        x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        y_data = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])
        dots = VGroup(*[
            Dot(axes.c2p(x, y), color=YELLOW, radius=0.08) for x, y in zip(x_data, y_data)
        ])
        self.play(FadeIn(dots))
        self.wait(1)

        # Linear regression line
        linear_line = axes.plot(lambda x: 0.15 * x - 0.25, color=GREEN)
        linear_label = Text("Linear Regression", font_size=24, color=GREEN).next_to(axes, UP, buff=0.2)
        self.play(Create(linear_line), FadeIn(linear_label))
        self.wait(1)

        # Logistic regression curve
        sigmoid_curve = axes.plot(lambda x: 1/(1 + np.exp(-2*(x-5))), color=RED)
        logistic_label = Text("Logistic Regression (Sigmoid)", font_size=24, color=RED).next_to(linear_label, RIGHT, buff=1.2)
        self.play(Create(sigmoid_curve), FadeIn(logistic_label))
        self.wait(2)

        # Explanation text
        explain = Text(
            "Linear regression can predict values <0 or >1,\nwhich doesn't make sense for probability!\nLogistic regression always outputs between 0 and 1.",
            font_size=28
        )
        explain.to_edge(RIGHT)
        self.play(FadeIn(explain))
        self.wait(2)
        self.play(FadeOut(explain))

        # Add an outlier
        outlier = Dot(axes.c2p(9.5, 0), color=PURPLE, radius=0.12)
        # Move 'Outlier' label further right
        outlier_label = Text("Outlier", font_size=22, color=PURPLE).next_to(outlier, RIGHT, buff=0.5)
        self.play(FadeIn(outlier), FadeIn(outlier_label))
        self.wait(1)

        # Animate linear regression line shifting (showing sensitivity)
        new_linear_line = axes.plot(lambda x: 0.08 * x + 0.1, color=GREEN, stroke_width=6, z_index=3)
        self.play(Transform(linear_line, new_linear_line))
        self.wait(1)

        # Show logistic regression is robust
        robust_text = Text(
            "Logistic regression is robust to outliers\nand still predicts probability!",
            font_size=28, color=RED
        )
        robust_text.to_edge(RIGHT)
        self.play(FadeIn(robust_text))
        self.wait(2)
        self.play(FadeOut(robust_text), FadeOut(outlier), FadeOut(outlier_label))

        # Outro
        # Move outro text to the right, away from the graph
        outro = Text(
            "That's why we use logistic regression\nfor binary outcomes like tumor classification!",
            font_size=32, color=BLUE
        ).to_edge(RIGHT)
        self.play(FadeIn(outro))
        self.wait(2)
        self.play(FadeOut(outro), FadeOut(title), FadeOut(linear_label), FadeOut(logistic_label), FadeOut(linear_line), FadeOut(sigmoid_curve), FadeOut(dots), FadeOut(axes), FadeOut(x_label), FadeOut(y_label))
