from manim import *
import numpy as np

class BiasVarianceExplanation(Scene):
    def construct(self):
        # Title
        title = Text("Bias and Variance in Machine Learning", font_size=44)
        self.play(FadeIn(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Bias section
        bias_title = Text("What is Bias?", font_size=36, color=YELLOW).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(bias_title))
        bias_text = Text("Bias is error from overly simple assumptions.\nHigh bias → underfitting.", font_size=28).next_to(bias_title, DOWN, buff=0.3)
        self.play(FadeIn(bias_text))
        self.wait(1.2)
        bias_example = Text("Example: Predicting house prices using only bedrooms\n(ignoring location, size, etc.)", font_size=24, color=GREY).next_to(bias_text, DOWN, buff=0.2)
        self.play(FadeIn(bias_example))
        self.wait(1.5)
        self.play(FadeOut(bias_title), FadeOut(bias_text), FadeOut(bias_example))

        # Variance section
        variance_title = Text("What is Variance?", font_size=36, color=BLUE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(variance_title))
        variance_text = Text("Variance is sensitivity to data fluctuations.\nHigh variance → overfitting.", font_size=28).next_to(variance_title, DOWN, buff=0.3)
        self.play(FadeIn(variance_text))
        self.wait(1.2)
        variance_example = Text("Example: Model fits every training point with a wiggly curve\nbut fails on new data.", font_size=24, color=GREY).next_to(variance_text, DOWN, buff=0.2)
        self.play(FadeIn(variance_example))
        self.wait(1.5)
        self.play(FadeOut(variance_title), FadeOut(variance_text), FadeOut(variance_example))

        # Bias-Variance Tradeoff
        tradeoff_title = Text("The Bias-Variance Tradeoff", font_size=36, color=PURPLE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(tradeoff_title))
        tradeoff_text = Text(
            "High bias + low variance → underfitting\nLow bias + high variance → overfitting\nBest: balance both for good generalization!",
            font_size=28
        ).next_to(tradeoff_title, DOWN, buff=0.3)
        self.play(FadeIn(tradeoff_text))
        self.wait(2)
        self.play(FadeOut(tradeoff_title), FadeOut(tradeoff_text))

        # Clean,  Bias-Variance Tradeoff chart
        graph_title = Text("Bias-Variance Tradeoff", font_size=32, color=GREEN).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(graph_title))
        self.wait(0.5)

        axes = Axes(
            x_range=[0, 10],
            y_range=[0, 3.5],
            x_length=7,
            y_length=3.2,
            axis_config={"color": WHITE, "font_size": 22},
            tips=False,
        ).next_to(graph_title, DOWN, buff=0.7)
        x_label = Text("Model Complexity", font_size=24).next_to(axes.x_axis.get_right(), RIGHT, buff=0.18)
        y_label = Text("Error", font_size=24).next_to(axes.y_axis.get_top(), UP, buff=0.18)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        # Bias^2: Exponential decay (full range)
        bias_curve = axes.plot(lambda x: 1.5 * np.exp(-0.35*x) + 0.18, color=YELLOW, x_range=[0, 10], stroke_width=4)
        # Variance: Exponential growth (stop at label)
        variance_curve = axes.plot(lambda x: 0.12 * np.exp(0.42*x) - 0.13, color=BLUE, x_range=[0, 8.5], stroke_width=4)
        # Total Error: U shape (stop at label)
        total_curve = axes.plot(lambda x: 1.5 * np.exp(-0.35*x) + 0.18 + 0.12 * np.exp(0.42*x) - 0.13, color=RED, x_range=[0, 8.5], stroke_width=4)

        # Legend
        bias_legend = Line(color=YELLOW, stroke_width=7).next_to(axes, UP, buff=0.3).shift(LEFT*2.5)
        bias_label = Text("Bias²", font_size=22, color=YELLOW).next_to(bias_legend, RIGHT, buff=0.15)
        var_legend = Line(color=BLUE, stroke_width=7).next_to(bias_label, RIGHT, buff=0.8)
        var_label = Text("Variance", font_size=22, color=BLUE).next_to(var_legend, RIGHT, buff=0.15)
        tot_legend = Line(color=RED, stroke_width=7).next_to(var_label, RIGHT, buff=0.8)
        tot_label = Text("Total Error", font_size=22, color=RED).next_to(tot_legend, RIGHT, buff=0.15)
        legend = VGroup(bias_legend, bias_label, var_legend, var_label, tot_legend, tot_label)
        self.play(Create(bias_curve), Create(variance_curve), Create(total_curve), FadeIn(legend))
        self.wait(0.8)

        # Compute intersection of bias² and variance curves
        def bias_fn(x):
            return 1.5 * np.exp(-0.35*x) + 0.18
        def var_fn(x):
            return 0.12 * np.exp(0.42*x) - 0.13
        # Find intersection numerically in [0, 8.5]
        from scipy.optimize import brentq
        try:
            x_inter = brentq(lambda x: bias_fn(x) - var_fn(x), 0, 8.5)
        except Exception:
            x_inter = 3.7  # fallback if scipy unavailable
        y_inter = bias_fn(x_inter)
        opt_dot = Dot(axes.c2p(x_inter, y_inter), color=GREEN, radius=0.13)
        opt_label = Text("Optimal\nModel Complexity", font_size=20, color=GREEN).next_to(opt_dot, DOWN+RIGHT, buff=0.18)
        self.play(FadeIn(opt_dot), FadeIn(opt_label))
        self.wait(2.2)

        # Fade out chart
        self.play(FadeOut(graph_title), FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
                  FadeOut(bias_curve), FadeOut(variance_curve), FadeOut(total_curve),
                  FadeOut(legend), FadeOut(opt_dot), FadeOut(opt_label))

        # How to handle bias and variance
        handle_title = Text("How to Handle Bias & Variance", font_size=34, color=ORANGE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(handle_title))
        handle_text = Text(
            "High bias? → Use a more complex model\nHigh variance? → Use regularization, cross-validation, or more data",
            font_size=26
        ).next_to(handle_title, DOWN, buff=0.3)
        self.play(FadeIn(handle_text))
        self.wait(2)
        self.play(FadeOut(handle_title), FadeOut(handle_text))

        # Final message
        final = Text(
            "Bias and Variance are two sides of the same coin.\nYou can't eliminate both, but you can balance them!",
            font_size=30, color=GREEN
        ).next_to(title, DOWN, buff=1.2)
        self.play(FadeIn(final))
        self.wait(2.5)
        self.play(FadeOut(final), FadeOut(title))
        self.wait(0.5)
