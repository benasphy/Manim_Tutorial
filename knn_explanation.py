from manim import *
import numpy as np

class KNNExplanation(Scene):
    def construct(self):
        # Title
        title = Text("K-Nearest Neighbors (KNN)", font_size=46, color=BLUE)
        self.play(FadeIn(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # 1. What is KNN and When to Use It
        sec1 = Text("What is KNN? When to Use It", font_size=36, color=YELLOW).next_to(title, DOWN, buff=0.5)
        desc1 = Text("Simple, interpretable algorithm for classification/regression.\nClassifies by majority among K nearest neighbors.", font_size=28).next_to(sec1, DOWN, buff=0.2)
        bullets = BulletedList(
            "Use when you want simplicity",
            "Data is not too large",
            "Predictions based on similarity",
            font_size=26
        ).next_to(desc1, DOWN, buff=0.2)
        self.play(FadeIn(sec1), FadeIn(desc1), FadeIn(bullets))
        self.wait(2.2)
        self.play(FadeOut(sec1), FadeOut(desc1), FadeOut(bullets))

        # 2. How KNN Works (with visual)
        sec2 = Text("How KNN Works", font_size=36, color=GREEN).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(sec2))
        axes = Axes(x_range=[0, 10], y_range=[0, 10], x_length=5.5, y_length=5.5, axis_config={"font_size": 20})
        axes.next_to(sec2, DOWN, buff=0.5)
        np.random.seed(1)
        apples = np.random.normal([3, 7], 0.7, (8, 2))
        pears = np.random.normal([7, 3], 0.7, (8, 2))
        test_pt = np.array([5.2, 5.2])
        apple_dots = VGroup(*[Dot(axes.c2p(x, y), color=RED, radius=0.16) for x, y in apples])
        pear_dots = VGroup(*[Dot(axes.c2p(x, y), color=GREEN, radius=0.16) for x, y in pears])
        test_dot = Dot(axes.c2p(*test_pt), color=YELLOW, radius=0.20)
        self.play(Create(axes), FadeIn(apple_dots), FadeIn(pear_dots), FadeIn(test_dot))
        # Draw lines to K=3 nearest
        all_pts = np.vstack([apples, pears])
        all_labels = ["Apple"]*8 + ["Pear"]*8
        dists = np.linalg.norm(all_pts - test_pt, axis=1)
        idx = np.argsort(dists)[:3]
        neighbor_lines = VGroup(*[Line(test_dot.get_center(), axes.c2p(*all_pts[i]), color=WHITE, stroke_width=3) for i in idx])
        self.play(*[Create(line) for line in neighbor_lines])
        # Show neighbor labels
        neighbor_labels = VGroup(*[Text(all_labels[i], font_size=28, color=RED if all_labels[i]=="Apple" else GREEN).next_to(axes.c2p(*all_pts[i]), DOWN) for i in idx])
        self.play(*[FadeIn(lbl) for lbl in neighbor_labels])
        maj_vote = Text("Majority vote: Apple!", font_size=32, color=RED).next_to(test_dot, RIGHT, buff=0.7)
        self.play(FadeIn(maj_vote))
        self.wait(2.5)
        self.play(FadeOut(sec2), FadeOut(axes), FadeOut(apple_dots), FadeOut(pear_dots), FadeOut(test_dot), FadeOut(neighbor_lines), FadeOut(neighbor_labels), FadeOut(maj_vote))

        # 3. How to Choose K
        sec3 = Text("Choosing the Best K", font_size=36, color=PURPLE).next_to(title, DOWN, buff=0.5)
        desc3 = Text("Balance bias and variance:\nSmall K: overfit, Large K: underfit", font_size=28).next_to(sec3, DOWN, buff=0.2)
        self.play(FadeIn(sec3), FadeIn(desc3))
        # Elbow method chart
        chart_axes = Axes(x_range=[1, 20, 1], y_range=[0, 0.5, 0.1], x_length=6, y_length=3.5, axis_config={"font_size": 20})
        chart_axes.next_to(desc3, DOWN, buff=0.5)
        k_vals = np.arange(1, 21)
        # Quadratic U-shape: error highest at K=1, drops to minimum at K=6, rises gently after
        val_error = 0.12 + 0.18 * ((k_vals - 6) / 8) ** 2
        elbow_k = 6
        elbow_dot = Dot(chart_axes.c2p(elbow_k, val_error[elbow_k - 1]), color=YELLOW, radius=0.18)
        elbow_curve = chart_axes.plot_line_graph(x_values=k_vals, y_values=val_error, add_vertex_dots=False, line_color=BLUE, stroke_width=4)
        elbow_label = Text("Elbow point (best K)", font_size=28, color=YELLOW).next_to(elbow_dot, RIGHT, buff=0.2)
        self.play(Create(chart_axes), Create(elbow_curve))
        self.play(FadeIn(elbow_dot), FadeIn(elbow_label))
        self.wait(2.5)
        self.play(FadeOut(sec3), FadeOut(desc3), FadeOut(chart_axes), FadeOut(elbow_curve), FadeOut(elbow_dot), FadeOut(elbow_label))

        # 4. Distance Metrics
        sec4 = Text("Distance Metrics in KNN", font_size=36, color=BLUE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(sec4))
        # Distance metric equations
        metric_eqs = VGroup(
            MathTex(r"d_{\text{euclid}}(p, q) = \sqrt{\sum_i (p_i - q_i)^2}", font_size=32, color=WHITE),
            MathTex(r"d_{\text{manhattan}}(p, q) = \sum_i |p_i - q_i|", font_size=32, color=WHITE),
            MathTex(r"d_{\text{minkowski}}(p, q) = (\sum_i |p_i - q_i|^p)^{1/p}", font_size=32, color=WHITE),
            MathTex(r"d_{\text{chebyshev}}(p, q) = \max_i |p_i - q_i|", font_size=32, color=WHITE),
            MathTex(r"d_{\text{cosine}}(A, B) = 1 - \frac{A \cdot B}{\|A\|\|B\|}", font_size=32, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.32).next_to(sec4, DOWN, buff=0.3)
        metric_names = VGroup(
            Text("Euclidean (L2)", font_size=28, color=WHITE),
            Text("Manhattan (L1)", font_size=28, color=WHITE),
            Text("Minkowski (p-tunable)", font_size=28, color=WHITE),
            Text("Chebyshev (max diff)", font_size=28, color=WHITE),
            Text("Cosine (angle)", font_size=28, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.38).next_to(metric_eqs, RIGHT, buff=1.1)
        self.play(FadeIn(metric_eqs), FadeIn(metric_names))
        self.wait(3)
        self.play(FadeOut(sec4), FadeOut(metric_eqs), FadeOut(metric_names))

        # 5. Distance metric visual demo (Euclidean vs Manhattan)
        sec5 = Text("Visualizing Distance Metrics", font_size=36, color=GREEN).next_to(title, DOWN, buff=0.5)
        axes2 = Axes(x_range=[0, 6], y_range=[0, 6], x_length=4.5, y_length=4.5, axis_config={"font_size": 18})
        axes2.next_to(sec5, DOWN, buff=0.6)
        p = np.array([1, 1])
        q = np.array([5, 4])
        dot_p = Dot(axes2.c2p(*p), color=YELLOW, radius=0.18)
        dot_q = Dot(axes2.c2p(*q), color=RED, radius=0.18)
        euclid = Line(axes2.c2p(*p), axes2.c2p(*q), color=BLUE, stroke_width=6)
        manhattan = VGroup(
            Line(axes2.c2p(*p), axes2.c2p(q[0], p[1]), color=ORANGE, stroke_width=6),
            Line(axes2.c2p(q[0], p[1]), axes2.c2p(*q), color=ORANGE, stroke_width=6),
        )
        self.play(FadeIn(sec5), Create(axes2), FadeIn(dot_p), FadeIn(dot_q))
        self.play(Create(euclid))
        euclid_label = Text("Euclidean distance", font_size=28, color=BLUE).next_to(euclid, UP)
        self.play(FadeIn(euclid_label))
        self.wait(1.2)
        self.play(FadeOut(euclid_label), FadeOut(euclid))
        self.play(Create(manhattan))
        manhattan_label = Text("Manhattan distance", font_size=28, color=ORANGE).next_to(manhattan, DOWN)
        self.play(FadeIn(manhattan_label))
        self.wait(1.5)
        self.play(FadeOut(manhattan_label), FadeOut(manhattan), FadeOut(sec5), FadeOut(axes2), FadeOut(dot_p), FadeOut(dot_q))

        # 6. Summary Table of Metrics
        sec6 = Text("Summary: Distance Metrics", font_size=36, color=YELLOW).next_to(title, DOWN, buff=0.5)
        table_data = [
            ["Metric", "Sensitive to Magnitude?", "Handles Sparse Data?", "Best Use Case"],
            ["Euclidean", "Yes", "No", "Spatial/geometric data"],
            ["Manhattan", "Less", "Yes", "Tabular/city-block problems"],
            ["Minkowski", "Depends on p", "Yes", "Tunable general use"],
            ["Chebyshev", "No", "No", "Strict thresholding"],
            ["Cosine", "No", "Yes", "Text/NLP problems"]
        ]
        table = Table(table_data, include_outer_lines=True, element_to_mobject_config={"font_size": 24})
        table.scale(0.95).next_to(sec6, DOWN, buff=0.3)
        self.play(FadeIn(sec6), FadeIn(table))
        self.wait(3)
        self.play(FadeOut(sec6), FadeOut(table))

        # 7. Final Tips
        tips = BulletedList(
            "Normalize data for Euclidean/Manhattan",
            "Use cross-validation for K and metric",
            "Cosine for high-dim, Euclidean/Manhattan for low-dim",
            font_size=28
        ).next_to(title, DOWN, buff=0.8)
        self.play(FadeIn(tips))
        self.wait(2.5)
        self.play(FadeOut(tips), FadeOut(title))
