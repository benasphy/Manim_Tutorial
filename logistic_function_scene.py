from manim import *
import numpy as np

class LogisticFunctionScene(Scene):
    def construct(self):
        # Title
        title = Text("Logistic Function", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Intro
        intro = Text(
            "How does logistic regression\nsqueeze output between 0 and 1?",
            font_size=32
        )
        self.play(Write(intro))
        self.wait(2)
        self.play(FadeOut(intro))

        # Math is interesting!
        math_text = Text(
            "There's a little bit of math\nbehind this — and it's pretty interesting!",
            font_size=30
        )
        self.play(Write(math_text))
        self.wait(2)
        self.play(FadeOut(math_text))

        # Show the logistic function formula
        formula = MathTex(r"\text{Logistic (Sigmoid) Function: } \\ \\ \sigma(x) = \frac{1}{1 + e^{-x}}", font_size=44)
        self.play(Write(formula))
        self.wait(2)

        # Note about sigmoid
        sigmoid_note = Text("It's more commonly called\nthe sigmoid function.", font_size=30, color=YELLOW)
        sigmoid_note.next_to(formula, DOWN, buff=0.6)
        self.play(FadeIn(sigmoid_note))
        self.wait(2)
        self.play(FadeOut(formula), FadeOut(sigmoid_note))

        # Draw graph comparing linear and logistic function
        axes = Axes(
            x_range=[-7, 7], y_range=[-1, 1.2, 0.2],
            x_length=7, y_length=4,
            axis_config={"color": WHITE},
            tips=False
        ).to_edge(DOWN, buff=1)
        # Place axis labels anchored to axes
        x_label = Text("x", font_size=28).next_to(axes.x_axis.get_end(), DOWN, buff=0.2)
        y_label = Text("output", font_size=28).next_to(axes.y_axis.get_start(), LEFT, buff=0.2)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        # Linear function
        linear_graph = axes.plot(lambda x: x/5, color=GREEN, x_range=[-7, 7])
        linear_label = Text("Linear", font_size=28, color=GREEN).next_to(axes, UP+LEFT, buff=0.5)
        self.play(Create(linear_graph), FadeIn(linear_label))

        # Logistic (sigmoid) function
        sigmoid_graph = axes.plot(lambda x: 1/(1 + np.exp(-x)), color=RED, x_range=[-7, 7])
        sigmoid_label = Text("Logistic (Sigmoid)", font_size=28, color=RED).next_to(axes, UP+RIGHT, buff=0.5)
        self.play(Create(sigmoid_graph), FadeIn(sigmoid_label))
        self.wait(3)

        # Highlight the squeeze
        squeeze_text = Text(
            "Sigmoid squashes any input\nbetween 0 and 1!",
            font_size=32, color=YELLOW
        ).to_edge(RIGHT)
        self.play(FadeIn(squeeze_text))
        self.wait(2)

        # Outro
        self.play(FadeOut(squeeze_text), FadeOut(linear_label), FadeOut(sigmoid_label), FadeOut(linear_graph), FadeOut(sigmoid_graph), FadeOut(axes), FadeOut(x_label), FadeOut(y_label), FadeOut(title))
