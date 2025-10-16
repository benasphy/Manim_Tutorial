from manim import *
import numpy as np
from scipy.stats import norm

class GMMCentralTendencyExplanation(Scene):
    def construct(self):
        # Title
        title = Text("Gaussian Mixture Models (GMM) & Central Tendency", font_size=40)
        self.play(FadeIn(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # GMM Introduction
        intro = Text("GMM: Flexible, probabilistic clustering", font_size=32, color=BLUE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(intro))
        self.wait(1)
        self.play(FadeOut(intro))

        # What is GMM?
        gmm_title = Text("What is GMM?", font_size=34, color=YELLOW).next_to(title, DOWN, buff=0.4)
        gmm_text = Text(
            "GMM assumes data comes from a mixture\nof several Gaussian distributions.", font_size=28
        ).next_to(gmm_title, DOWN, buff=0.2)
        self.play(FadeIn(gmm_title), FadeIn(gmm_text))
        self.wait(1.5)
        self.play(FadeOut(gmm_title), FadeOut(gmm_text))

        # GMM formula
        formula = MathTex(r"p(x) = \sum_{k=1}^K \pi_k \, \mathcal{N}(x|\mu_k, \Sigma_k)", font_size=36).next_to(title, DOWN, buff=0.7)
        self.play(FadeIn(formula))
        self.wait(1.5)
        self.play(FadeOut(formula))

        # Real-world analogy
        analogy = Text("Analogy: Students from different departments\nclustered by GPA & study hours", font_size=28, color=GREY).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(analogy))
        self.wait(1.5)
        self.play(FadeOut(analogy))

        # GMM vs K-Means Table
        table_title = Text("GMM vs K-Means", font_size=32, color=GREEN).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(table_title))
        table_data = [
            ["Feature", "K-Means", "GMM"],
            ["Assignment", "Hard", "Soft (probabilistic)"],
            ["Cluster Shape", "Circular", "Elliptical/flexible"],
            ["Model", "Distance-based", "Probabilistic"],
            ["Handles Overlap?", "No", "Yes"]
        ]
        table = Table(table_data, include_outer_lines=True, element_to_mobject_config={"font_size": 22})
        table.scale(0.9).next_to(table_title, DOWN, buff=0.3)
        self.play(FadeIn(table))
        self.wait(2.2)
        self.play(FadeOut(table_title), FadeOut(table))

        # GMM 1D Distribution Visual
        gmm1d_title = Text("GMM: 1D Mixture of Gaussians", font_size=32, color=PURPLE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(gmm1d_title))
        axes = Axes(x_range=[-4, 10], y_range=[0, 0.5], x_length=7, y_length=2.5, axis_config={"font_size": 20})
        axes.next_to(gmm1d_title, DOWN, buff=0.6)
        x = np.linspace(-4, 10, 400)
        # Three Gaussians
        mus = [0, 3, 6]
        sigmas = [1, 0.8, 1.2]
        pis = [0.3, 0.4, 0.3]
        gauss_curves = []
        for i, (mu, sigma, pi) in enumerate(zip(mus, sigmas, pis)):
            y = pi * norm.pdf(x, mu, sigma)
            curve = axes.plot_line_graph(x, y, add_vertex_dots=False, line_color=[YELLOW, BLUE, GREEN][i], stroke_width=4)
            gauss_curves.append(curve)
        # Mixture
        y_mix = sum(pi * norm.pdf(x, mu, sigma) for pi, mu, sigma in zip(pis, mus, sigmas))
        mix_curve = axes.plot_line_graph(x, y_mix, add_vertex_dots=False, line_color=RED, stroke_width=5)
        # Show all
        self.play(Create(axes))
        for curve in gauss_curves:
            self.play(Create(curve))
        self.wait(0.5)
        self.play(Create(mix_curve))
        self.wait(2)
        self.play(FadeOut(gmm1d_title), FadeOut(axes), *[FadeOut(curve) for curve in gauss_curves], FadeOut(mix_curve))

        # GMM 2D Visual
        gmm2d_title = Text("GMM: 2D Gaussian Clusters", font_size=32, color=PURPLE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(gmm2d_title))
        axes2 = Axes(x_range=[-2, 8], y_range=[-2, 8], x_length=5, y_length=5, axis_config={"font_size": 20})
        axes2.next_to(gmm2d_title, DOWN, buff=0.6)
        # Generate 2D data
        np.random.seed(0)
        points = np.vstack([
            np.random.multivariate_normal([1, 2], [[0.7, 0.2],[0.2, 0.5]], 60),
            np.random.multivariate_normal([5, 5], [[0.9, -0.4],[-0.4, 0.7]], 60),
            np.random.multivariate_normal([3, 6], [[0.6, 0.1],[0.1, 0.6]], 40)
        ])
        colors = [YELLOW]*60 + [BLUE]*60 + [GREEN]*40
        dots = VGroup(*[Dot(axes2.c2p(x, y), color=col, radius=0.08) for (x, y), col in zip(points, colors)])
        self.play(Create(axes2), FadeIn(dots))
        # Draw ellipses for GMM components
        ellipse1 = Ellipse(width=2.2, height=1.3, color=YELLOW).move_to(axes2.c2p(1, 2))
        ellipse2 = Ellipse(width=2.6, height=1.6, color=BLUE).move_to(axes2.c2p(5, 5)).rotate(-0.4)
        ellipse3 = Ellipse(width=1.6, height=1.1, color=GREEN).move_to(axes2.c2p(3, 6)).rotate(0.2)
        ellipses = [ellipse1, ellipse2, ellipse3]
        for ell in ellipses:
            self.play(Create(ell), run_time=0.5)
        self.wait(2)
        self.play(FadeOut(gmm2d_title), FadeOut(axes2), FadeOut(dots), *[FadeOut(ell) for ell in ellipses])

        # Central Tendency
        ct_title = Text("Central Tendency in GMM", font_size=32, color=ORANGE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(ct_title))
        ct_text = Text(
            "Central tendency: where data is centered\nMean, Median, Mode", font_size=28
        ).next_to(ct_title, DOWN, buff=0.2)
        self.play(FadeIn(ct_text))
        self.wait(1.3)
        self.play(FadeOut(ct_text))

        # Show means on 1D GMM
        axes_ct = Axes(x_range=[-4, 10], y_range=[0, 0.5], x_length=7, y_length=2.5, axis_config={"font_size": 20})
        axes_ct.next_to(ct_title, DOWN, buff=0.6)
        self.play(Create(axes_ct))
        for i, mu in enumerate(mus):
            mean_dot = Dot(axes_ct.c2p(mu, 0.36), color=[YELLOW, BLUE, GREEN][i], radius=0.13)
            mean_label = Text(f"μ{i+1}", font_size=22, color=[YELLOW, BLUE, GREEN][i]).next_to(mean_dot, UP, buff=0.1)
            self.play(FadeIn(mean_dot), FadeIn(mean_label))
        self.wait(1.3)
        self.play(FadeOut(axes_ct), *[FadeOut(mob) for mob in self.mobjects if isinstance(mob, Dot) or isinstance(mob, Text)])

        # Why it matters
        why_title = Text("Why Central Tendency Matters in GMM", font_size=30, color=WHITE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(why_title))
        why_text = Text(
            "GMM can model multiple centers (means)\nfor multimodal data — more flexible than a single average!",
            font_size=26
        ).next_to(why_title, DOWN, buff=0.2)
        self.play(FadeIn(why_text))
        self.wait(2)
        self.play(FadeOut(why_title), FadeOut(why_text))

        # Applications
        apps_title = Text("Applications of GMM", font_size=30, color=GREEN).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(apps_title))
        apps = BulletedList(
            "Image segmentation",
            "Speaker recognition",
            "Anomaly detection",
            "Clustering financial data",
            "Pattern recognition",
            font_size=25
        ).next_to(apps_title, DOWN, buff=0.2)
        self.play(FadeIn(apps))
        self.wait(2)
        self.play(FadeOut(apps_title), FadeOut(apps))

        # Limitations
        lim_title = Text("Limitations of GMM", font_size=30, color=RED).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(lim_title))
        lims = BulletedList(
            "Sensitive to initialization",
            "May converge to local minima",
            "Assumes Gaussian distribution",
            "Choosing k (clusters) can be tricky",
            font_size=25
        ).next_to(lim_title, DOWN, buff=0.2)
        self.play(FadeIn(lims))
        self.wait(2)
        self.play(FadeOut(lim_title), FadeOut(lims))

        # Wrap Up
        wrap = VGroup(
            Text("GMM = Mixture of Gaussians", font_size=28, color=YELLOW),
            Text("Soft clustering (probabilities)", font_size=28, color=BLUE),
            Text("Multiple centers (means)", font_size=28, color=GREEN),
            Text("Flexible & powerful for real-world data!", font_size=28, color=PURPLE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(UP, buff=0.8)
        self.play(FadeIn(wrap))
        self.wait(2.5)
        self.play(FadeOut(wrap), FadeOut(title))
        self.wait(0.5)
