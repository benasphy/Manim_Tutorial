from manim import *

class PoissonRegressionExplanation(Scene):
    def construct(self):
        # Title
        title = Text("Poisson Regression Explained", font_size=48)
        self.play(FadeIn(title))
        self.wait(0.7)
        self.play(title.animate.to_edge(UP))

        # Introduction
        intro = VGroup(
            Text("How can we predict the number of events?", font_size=32),
            Text("(e.g., patients per day, calls per hour, accidents per week)", font_size=28, color=GREY_B)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(intro))
        self.wait(1.2)

        # What is Poisson Regression?
        self.play(FadeOut(intro))
        poisson_reg = Text("Poisson Regression models COUNT data", font_size=36).next_to(title, DOWN, buff=0.7)
        self.play(FadeIn(poisson_reg))
        self.wait(1.2)
        self.play(FadeOut(poisson_reg))

        # When and Why Use Poisson Regression
        when_why_title = Text("When and Why Do We Use Poisson Regression?", font_size=32, color=BLUE)
        bullets = VGroup(
            Text("1. When the outcome is a count (0, 1, 2, ...)", font_size=28),
            Text("2. When counts happen over time or space", font_size=28),
            Text("   e.g., website clicks per day, deaths per year", font_size=24, color=GREY_B),
            Text("3. When counts increase exponentially with features", font_size=28),
            Text("   Poisson regression handles multiplicative effects", font_size=24, color=GREY_B)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(when_why_title, DOWN, buff=0.2)
        self.play(FadeIn(when_why_title, shift=UP))
        self.play(FadeIn(bullets, shift=UP))
        self.wait(1.8)
        self.play(FadeOut(when_why_title), FadeOut(bullets))

        # Poisson Distribution
        dist_title = Text("The Poisson Distribution", font_size=32, color=YELLOW)
        self.play(FadeIn(dist_title.next_to(title, DOWN, buff=0.7)))
        poisson_formula = MathTex(r"P(Y=k) = \frac{\lambda^k e^{-\lambda}}{k!}", font_size=36)
        self.play(FadeIn(poisson_formula.next_to(dist_title, DOWN, buff=0.4)))
        self.wait(1.2)
        dist_explain = Text("Models the probability of k events in a fixed interval,\nwith average rate λ.", font_size=28).next_to(poisson_formula, DOWN, buff=0.3)
        self.play(FadeIn(dist_explain))
        self.wait(1.2)
        self.play(FadeOut(dist_title), FadeOut(poisson_formula), FadeOut(dist_explain))

        # Poisson Regression Formula
        reg_title = Text("Poisson Regression Formula", font_size=32, color=GREEN)
        self.play(FadeIn(reg_title.next_to(title, DOWN, buff=0.7)))
        reg_formula = MathTex(r"\log(\lambda) = \beta_0 + \beta_1 x_1 + \cdots + \beta_p x_p", font_size=36)
        self.play(FadeIn(reg_formula.next_to(reg_title, DOWN, buff=0.4)))
        self.wait(1.2)
        reg_explain = Text("The log of the expected count (λ) is modeled as a linear function\nof the predictors.", font_size=28).next_to(reg_formula, DOWN, buff=0.3)
        self.play(FadeIn(reg_explain))
        self.wait(1.5)
        self.play(FadeOut(reg_title), FadeOut(reg_formula), FadeOut(reg_explain))

        # Example
        example_title = Text("Example: Predicting Clinic Visits", font_size=32, color=PURPLE)
        self.play(FadeIn(example_title.next_to(title, DOWN, buff=0.7)))
        example_text = Text(
            "Suppose we want to predict the number of patients visiting a clinic per day\nusing day of week and temperature as predictors.",
            font_size=28
        ).next_to(example_title, DOWN, buff=0.3)
        self.play(FadeIn(example_text))
        self.wait(1.2)

        # Show the Poisson regression formula for this example
        example_formula = MathTex(r"\log(\lambda) = \beta_0 + \beta_1 x_{\text{weekend}} + \beta_2 x_{\text{temp}}", font_size=36)
        self.play(FadeIn(example_formula.next_to(example_text, DOWN, buff=0.3)))
        self.wait(1.2)

        # Substitute example coefficients
        example_coeff = MathTex(r"\log(\lambda) = 1.2 - 0.3 x_{\text{weekend}} + 0.05 x_{\text{temp}}", font_size=36)
        self.play(Transform(example_formula, example_coeff))
        self.wait(1.2)

        # Step-by-step calculation
        calc1 = Text("Suppose it is a weekend (x_{weekend}=1) and temperature is 30°C (x_{temp}=30):", font_size=26).next_to(example_formula, DOWN, buff=0.3)
        self.play(FadeIn(calc1))
        self.wait(1.2)
        calc2 = MathTex(r"\log(\lambda) = 1.2 - 0.3 \times 1 + 0.05 \times 30", font_size=34).next_to(calc1, DOWN, buff=0.2)
        self.play(FadeIn(calc2))
        self.wait(0.8)
        calc3 = MathTex(r"\log(\lambda) = 1.2 - 0.3 + 1.5 = 2.4", font_size=34).next_to(calc2, DOWN, buff=0.2)
        self.play(FadeIn(calc3))
        self.wait(0.8)
        calc4 = MathTex(r"\lambda = e^{2.4} \approx 11.0", font_size=34).next_to(calc3, DOWN, buff=0.2)
        self.play(FadeIn(calc4))
        self.wait(1.2)
        result = Text("So, the expected number of patients is about 11 per day.", font_size=28, color=GREEN).next_to(calc4, DOWN, buff=0.3)
        self.play(FadeIn(result))
        self.wait(2.2)
        self.play(FadeOut(example_title), FadeOut(example_text), FadeOut(example_formula), FadeOut(calc1), FadeOut(calc2), FadeOut(calc3), FadeOut(calc4), FadeOut(result))

        # Summary
        summary = VGroup(
            Text("Poisson Regression is ideal for modeling counts!", font_size=32, color=BLUE),
            Text("Outcome: non-negative integer counts", font_size=28),
            Text("Uses Poisson distribution for probability", font_size=28),
            Text("Formula: log(λ) = linear predictors", font_size=28),
            Text("Example: predicting events per time/space", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(title, DOWN, buff=0.7)
        self.play(FadeIn(summary))
        self.wait(2.5)
        self.play(FadeOut(summary), FadeOut(title))
        self.wait(0.5)
