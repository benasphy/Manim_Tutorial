from manim import *
import numpy as np

class UnderfittingOverfittingExplanation(Scene):
    def construct(self):
        # Title
        title = Text("Underfitting vs Overfitting", font_size=44)
        self.play(FadeIn(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Underfitting Section
        under_title = Text("What is Underfitting?", font_size=36, color=YELLOW).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(under_title))
        under_text = Text("Model too simple to capture patterns.\nHigh train & test error.", font_size=28).next_to(under_title, DOWN, buff=0.3)
        self.play(FadeIn(under_text))
        self.wait(1.2)
        under_example = Text("Example: Predicting house prices using only bedrooms\n(ignoring size, location, etc.)", font_size=24, color=GREY).next_to(under_text, DOWN, buff=0.2)
        self.play(FadeIn(under_example))
        self.wait(1.3)
        self.play(FadeOut(under_title), FadeOut(under_text), FadeOut(under_example))

        # Overfitting Section
        over_title = Text("What is Overfitting?", font_size=36, color=BLUE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(over_title))
        over_text = Text("Model too complex, memorizes data.\nLow train error, high test error.", font_size=28).next_to(over_title, DOWN, buff=0.3)
        self.play(FadeIn(over_text))
        self.wait(1.2)
        over_example = Text("Example: Model fits all noise,\nfails on new data.", font_size=24, color=GREY).next_to(over_text, DOWN, buff=0.2)
        self.play(FadeIn(over_example))
        self.wait(1.3)
        self.play(FadeOut(over_title), FadeOut(over_text), FadeOut(over_example))

        # Visual: Underfitting, Good Fit, Overfitting
        visual_title = Text("Visual Analogy", font_size=32, color=PURPLE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(visual_title))
        self.wait(0.5)
        axes = Axes(
            x_range=[0, 8],
            y_range=[0, 8],
            x_length=3,
            y_length=3,
            axis_config={"color": WHITE, "font_size": 20},
            tips=False,
        )
        # Example data
        x = np.linspace(0.5, 7.5, 8)
        y = 2 + 0.6*x + 0.5*np.sin(x)
        scatter = VGroup(*[Dot(axes.c2p(xi, yi), color=WHITE, radius=0.09) for xi, yi in zip(x, y)])
        # Underfit: straight line
        underfit_curve = axes.plot(lambda x: 2 + 0.6*x, color=YELLOW, x_range=[0, 8], stroke_width=4)
        # Good fit: smooth curve
        goodfit_curve = axes.plot(lambda x: 2 + 0.6*x + 0.5*np.sin(x), color=GREEN, x_range=[0, 8], stroke_width=4)
        # Overfit: wiggly curve
        overfit_curve = axes.plot(lambda x: 2 + 0.6*x + 0.5*np.sin(x) + 0.22*np.sin(4*x), color=BLUE, x_range=[0, 8], stroke_width=4)
        # Arrange visuals
        visuals = VGroup()
        for i, (curve, label, col) in enumerate([
            (underfit_curve, "Underfitting", YELLOW),
            (goodfit_curve, "Good Fit", GREEN),
            (overfit_curve, "Overfitting", BLUE),
        ]):
            axes_i = axes.copy().shift(RIGHT*4*(i-1))
            scatter_i = scatter.copy().shift(RIGHT*4*(i-1))
            curve_i = curve.copy().shift(RIGHT*4*(i-1))
            label_i = Text(label, font_size=22, color=col).next_to(axes_i, DOWN, buff=0.18)
            visuals.add(VGroup(axes_i, scatter_i, curve_i, label_i))
        visuals.arrange(RIGHT, buff=1.2).next_to(visual_title, DOWN, buff=0.6)
        self.play(FadeIn(visuals))
        self.wait(2.5)
        self.play(FadeOut(visual_title), FadeOut(visuals))

        # Summary Table
        table_title = Text("Underfitting vs Overfitting", font_size=32, color=GREEN).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(table_title))
        table_data = [
            ["Property", "Underfitting", "Overfitting"],
            ["Model Complexity", "Too Low", "Too High"],
            ["Training Error", "High", "Low"],
            ["Test Error", "High", "High"],
            ["Cause", "Oversimplification", "Over-memorization"],
            ["Solution", "Increase complexity", "Simplify, regularize"],
        ]
        table = Table(table_data, include_outer_lines=True, element_to_mobject_config={"font_size": 22})
        table.scale(0.9).next_to(table_title, DOWN, buff=0.3)
        self.play(FadeIn(table))
        self.wait(2.5)
        self.play(FadeOut(table_title), FadeOut(table))

        # How to Fix
        fix_title = Text("How to Fix Them", font_size=32, color=ORANGE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(fix_title))
        fix_text = Text(
            "Underfitting: Use complex model, more features, train longer.\nOverfitting: Regularize, get more data, simplify, cross-validate.",
            font_size=26
        ).next_to(fix_title, DOWN, buff=0.3)
        self.play(FadeIn(fix_text))
        self.wait(2)
        self.play(FadeOut(fix_title), FadeOut(fix_text))

        # Final Thoughts
        final = VGroup(
            Text("Underfitting: Student didn't study.", font_size=27, color=YELLOW),
            Text("Overfitting: Student memorized, not understood.", font_size=27, color=BLUE),
            Text("Good Model: Learned & can generalize!", font_size=27, color=GREEN),
            Text("Balancing both is key to ML success!", font_size=28, color=PURPLE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(ORIGIN)
        self.play(FadeIn(final))
        self.wait(2.5)
        self.play(FadeOut(final), FadeOut(title))
        self.wait(0.5)
