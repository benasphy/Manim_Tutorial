from manim import *
import numpy as np

class GradientDescentLogisticRegressionScene(Scene):
    def construct(self):
        # Title
        title = Text("Gradient Descent in Logistic Regression", font_size=44, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Show cost curve (convex log loss)
        axes = Axes(
            x_range=[-3, 3], y_range=[0, 5, 1],
            x_length=7, y_length=3.5,
            axis_config={"color": WHITE},
            tips=False
        ).to_edge(DOWN, buff=1)
        cost_curve = axes.plot(lambda w: w**2 + 1, color=YELLOW)
        cost_label = Text("Log Loss (Cost) Curve", font_size=28, color=YELLOW).next_to(axes, UP)
        x_label = Text("Parameter (weight)", font_size=26).next_to(axes.x_axis.get_end(), DOWN, buff=0.2)
        y_label = Text("Cost", font_size=26).next_to(axes.y_axis.get_start(), LEFT, buff=0.2)
        self.play(Create(axes), Create(cost_curve), FadeIn(cost_label), FadeIn(x_label), FadeIn(y_label))
        self.wait(1)

        # Starting point
        start_x = 2.5
        point = Dot(axes.c2p(start_x, cost_curve.underlying_function(start_x)), color=RED, radius=0.13)
        self.play(FadeIn(point))

        # Explanatory text
        gd_text = Text(
            "Gradient descent moves the parameter\ndown the cost curve step by step",
            font_size=30, color=WHITE
        ).to_edge(RIGHT)
        self.play(FadeIn(gd_text))
        self.wait(1)

        # Animate gradient descent steps
        steps = 7
        lr = 0.45
        x = start_x
        for i in range(steps):
            # Gradient of cost: d/dw (w^2 + 1) = 2w
            grad = 2 * x
            new_x = x - lr * grad
            new_y = cost_curve.underlying_function(new_x)
            tangent = always_redraw(lambda: axes.get_secant_slope_group(
                new_x, cost_curve, dx=0.4, secant_line_color=GREEN, secant_line_length=2.5
            ))
            arrow = Arrow(
                axes.c2p(x, cost_curve.underlying_function(x)),
                axes.c2p(new_x, new_y),
                buff=0.01,
                color=ORANGE
            )
            self.play(Create(arrow), MoveAlongPath(point, arrow), Create(tangent))
            self.wait(0.5)
            self.play(FadeOut(arrow), FadeOut(tangent))
            x = new_x
        self.wait(1)

        # Arrived at minimum
        min_text = Text("Arrived at minimum cost!", font_size=32, color=GREEN).next_to(point, UP, buff=0.5)
        self.play(FadeIn(min_text))
        self.wait(2)

        # Outro
        self.play(FadeOut(min_text), FadeOut(point), FadeOut(gd_text), FadeOut(cost_curve), FadeOut(cost_label), FadeOut(axes), FadeOut(x_label), FadeOut(y_label), FadeOut(title))
