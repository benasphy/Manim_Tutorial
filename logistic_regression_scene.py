from manim import *

class LogisticRegressionExplanation(Scene):
    def construct(self):
        # Title
        title = Text("Logistic Regression Explained", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Step 1: What is Logistic Regression?
        step1 = Text("Logistic regression is a machine learning algorithm\nused for binary classification — yes/no, spam/not spam.", font_size=32)
        self.play(Write(step1))
        self.wait(2)
        self.play(FadeOut(step1))

        # Step 2: Linear vs Logistic Regression
        linear_vs_logistic = VGroup(
            Text("Linear Regression", font_size=28, color=YELLOW),
            Text("Logistic Regression", font_size=28, color=GREEN)
        ).arrange(RIGHT, buff=2)
        self.play(FadeIn(linear_vs_logistic))
        self.wait(1)

        # Linear regression visual (line)
        axes1 = Axes(
            x_range=[-3, 3], y_range=[-1, 1, 1],
            x_length=3, y_length=2,
            axis_config={"color": WHITE}
        ).shift(LEFT*3)
        line = axes1.plot(lambda x: 0.3*x, color=YELLOW)
        linear_label = Text("Continuous Output", font_size=20).next_to(axes1, DOWN)
        self.play(Create(axes1), Create(line), FadeIn(linear_label))

        # Logistic regression visual (sigmoid)
        axes2 = Axes(
            x_range=[-6, 6], y_range=[0, 1, 0.2],
            x_length=3, y_length=2,
            axis_config={"color": WHITE}
        ).shift(RIGHT*3)
        sigmoid = axes2.plot(lambda x: 1/(1 + np.exp(-x)), color=GREEN)
        logistic_label = Text("Probability Output", font_size=20).next_to(axes2, DOWN)
        self.play(Create(axes2), Create(sigmoid), FadeIn(logistic_label))
        self.wait(2)
        self.play(FadeOut(linear_vs_logistic), FadeOut(axes1), FadeOut(line), FadeOut(linear_label),
                  FadeOut(axes2), FadeOut(sigmoid), FadeOut(logistic_label))

        # Step 3: Sigmoid Function
        sigmoid_text = Text(
            "Sigmoid function squashes any number\nbetween 0 and 1 (probability)", font_size=32
        )
        self.play(Write(sigmoid_text))
        self.wait(1)
        self.play(FadeOut(sigmoid_text))

        # Show sigmoid formula below the header and above threshold description
        formula = MathTex(r"\sigma(x) = \frac{1}{1 + e^{-x}}", font_size=48)
        formula.next_to(title, DOWN, buff=0.7)
        self.play(Write(formula))
        self.wait(2)

        # Step 4: Thresholding (place below the formula)
        threshold_text = Text(
            "If output > 0.5 → Class 1\nIf output ≤ 0.5 → Class 0",
            font_size=32,
            color=WHITE
        )
        threshold_text.next_to(formula, DOWN, buff=0.7)
        self.play(Write(threshold_text))
        self.wait(2)
        self.play(FadeOut(threshold_text), FadeOut(formula))

        # Step 5: Real-world Example
        example_text = Text(
            "Using features, logistic regression can predict\nif you have diabetes or not!",
            font_size=32,
            color=BLUE
        )
        self.play(Write(example_text))
        self.wait(2)
        self.play(FadeOut(example_text))

        # Outro
        outro = Text("Let's see how it works in code!", font_size=36, color=YELLOW)
        self.play(Write(outro))
        self.wait(2)
        self.play(FadeOut(outro), FadeOut(title))
