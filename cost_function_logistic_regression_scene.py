from manim import *
import numpy as np

class CostFunctionLogisticRegressionScene(Scene):
    def construct(self):
        # Title
        title = Text("Cost Function for Logistic Regression", font_size=44, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Why not MSE?
        mse_text = Text(
            "What if we use MSE (Mean Squared Error)\nfor logistic regression?",
            font_size=32
        )
        self.play(Write(mse_text))
        self.wait(2)
        self.play(FadeOut(mse_text))

        # Show convex cost surface with local minima
        mse_graph_axes = Axes(
            x_range=[-3, 3], y_range=[0, 5, 1],
            x_length=6, y_length=3.2,
            axis_config={"color": WHITE},
            tips=False
        ).to_edge(DOWN, buff=1.1)
        mse_curve = mse_graph_axes.plot(lambda x: (x**4 - 2*x**2 + 2), color=YELLOW)
        mse_label = Text("MSE Cost Surface\n(multiple minima!)", font_size=26, color=YELLOW).next_to(mse_graph_axes, UP)
        self.play(Create(mse_graph_axes), Create(mse_curve), FadeIn(mse_label))
        self.wait(2)
        # Place local minima and global minimum at correct points
        # For f(x) = x^4 - 2x^2 + 2, local minima at x = -1, 1, global min at both
        local_min1 = Dot(mse_graph_axes.c2p(-1, 1), color=RED, radius=0.11)
        local_min2 = Dot(mse_graph_axes.c2p(1, 1), color=RED, radius=0.11)
        # Both are global minima for this function
        self.play(FadeIn(local_min1), FadeIn(local_min2))
        self.wait(1)
        self.play(FadeOut(mse_graph_axes), FadeOut(mse_curve), FadeOut(mse_label), FadeOut(local_min1), FadeOut(local_min2))

        # Introduce log loss
        logloss_intro = Text(
            "To solve this, we use Log Loss\n(also called Cross-Entropy Loss)",
            font_size=32, color=YELLOW
        )
        self.play(Write(logloss_intro))
        self.wait(2)
        self.play(FadeOut(logloss_intro))

        # Show correct log loss formula
        logloss_formula = MathTex(
            r"\text{Log Loss} = -\frac{1}{N} \sum_{i=1}^N \left[ y_i \log(p_i) + (1-y_i) \log(1-p_i) \right]",
            font_size=44
        )
        self.play(Write(logloss_formula))
        self.wait(2)
        logloss_explain = Text(
            "N: number of samples\ny: true label (0 or 1)\np: predicted probability",
            font_size=28
        ).next_to(logloss_formula, DOWN, buff=0.4)
        self.play(FadeIn(logloss_explain))
        self.wait(2)
        self.play(FadeOut(logloss_formula), FadeOut(logloss_explain))

        # Graph log loss for y=1, y=0, and general
        axes = Axes(
            x_range=[0.01, 0.99], y_range=[0, 5, 1],
            x_length=7, y_length=3.5,
            axis_config={"color": WHITE},
            tips=False
        ).to_edge(DOWN, buff=1)
        x_label = Text("Predicted probability (p)", font_size=26).next_to(axes.x_axis.get_end(), DOWN, buff=0.2)
        y_label = Text("Log Loss", font_size=26).next_to(axes.y_axis.get_start(), LEFT, buff=0.2)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        # y=1: -log(p)
        logloss_y1 = axes.plot(lambda p: -np.log(p), color=GREEN, x_range=[0.01, 0.99])
        label_y1 = Text("y=1", font_size=24, color=GREEN).next_to(logloss_y1, RIGHT, buff=0.2)
        self.play(Create(logloss_y1), FadeIn(label_y1))
        self.wait(1)

        # y=0: -log(1-p)
        logloss_y0 = axes.plot(lambda p: -np.log(1-p), color=RED, x_range=[0.01, 0.99])
        label_y0 = Text("y=0", font_size=24, color=RED).next_to(logloss_y0, LEFT, buff=0.2)
        self.play(Create(logloss_y0), FadeIn(label_y0))
        self.wait(2)

        # Explain total log loss
        explain = Text(
            "Log loss penalizes wrong confident predictions\nvery strongly, and is convex!",
            font_size=30, color=YELLOW
        ).to_edge(RIGHT)
        self.play(FadeIn(explain))
        self.wait(2)
        self.play(FadeOut(explain), FadeOut(logloss_y1), FadeOut(logloss_y0), FadeOut(label_y1), FadeOut(label_y0), FadeOut(axes), FadeOut(x_label), FadeOut(y_label), FadeOut(logloss_formula), FadeOut(title))
