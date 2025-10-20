from manim import *
import numpy as np

class FuzzyCMeansClusteringExplanation(Scene):
    def construct(self):
        # Title
        title = Text("Fuzzy C-Means Clustering – Soft Clustering in Action", font_size=38)
        self.play(FadeIn(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # 1. Hard vs Soft Clustering
        sec1 = Text("1. Hard vs Soft Clustering", font_size=34, color=YELLOW).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(sec1))
        # Hard clustering: Venn diagram style
        axes = Axes(x_range=[0, 8], y_range=[0, 6], x_length=5, y_length=3.5, axis_config={"font_size": 18})
        axes.next_to(sec1, DOWN, buff=0.6)
        hard_circle1 = Circle(radius=1, color=BLUE).move_to(axes.c2p(1.7, 3))
        hard_circle2 = Circle(radius=1, color=YELLOW).move_to(axes.c2p(6.7, 3))
        hard_points = [Dot(axes.c2p(1.7, 3.7), color=BLUE), Dot(axes.c2p(6.7, 2.3), color=YELLOW), Dot(axes.c2p(1.7, 2.3), color=BLUE), Dot(axes.c2p(6.7, 3.7), color=YELLOW)]
        hard_label = Text("Hard: Each point in one cluster", font_size=24).next_to(axes, DOWN, buff=0.2)
        self.play(Create(axes), Create(hard_circle1), Create(hard_circle2), *[FadeIn(p) for p in hard_points], FadeIn(hard_label))
        self.wait(1.5)
        self.play(FadeOut(hard_circle1), FadeOut(hard_circle2), *[FadeOut(p) for p in hard_points], FadeOut(hard_label))
        # Soft clustering: overlapping circles
        soft_circle1 = Circle(radius=1, color=BLUE, stroke_opacity=0.6).move_to(axes.c2p(2.8, 3))
        soft_circle2 = Circle(radius=1, color=YELLOW, stroke_opacity=0.6).move_to(axes.c2p(4.6, 3))
        soft_points = [Dot(axes.c2p(3.7, 3), color=WHITE), Dot(axes.c2p(2.8, 3.7), color=BLUE), Dot(axes.c2p(4.6, 2.3), color=YELLOW)]
        soft_label = Text("Soft: Each point has degrees of membership", font_size=24).next_to(axes, DOWN, buff=0.2)
        self.play(Create(soft_circle1), Create(soft_circle2), *[FadeIn(p) for p in soft_points], FadeIn(soft_label))
        self.wait(1.8)
        self.play(FadeOut(soft_circle1), FadeOut(soft_circle2), *[FadeOut(p) for p in soft_points], FadeOut(soft_label), FadeOut(axes), FadeOut(sec1))

        # 2. What is Fuzzy C-Means?
        sec2 = Text("2. What is Fuzzy C-Means?", font_size=34, color=BLUE).next_to(title, DOWN, buff=0.5)
        desc2 = Text("Soft clustering: Each point belongs to clusters with membership scores\nBased on fuzzy logic (partial truths)", font_size=28).next_to(sec2, DOWN, buff=0.2)
        self.play(FadeIn(sec2), FadeIn(desc2))
        self.wait(2)
        self.play(FadeOut(sec2), FadeOut(desc2))

        # 3. Key Notations and Math
        sec3 = Text("3. Key Notations and Math", font_size=34, color=PURPLE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(sec3))
        math1 = MathTex(r"\sum_{i=1}^{c} u_{ij} = 1 \,\, \forall j", font_size=32).next_to(sec3, DOWN, buff=0.2)
        math2 = MathTex(r"J = \sum_{j=1}^n \sum_{i=1}^c u_{ij}^m \|x_j - v_i\|^2", font_size=32).next_to(math1, DOWN, buff=0.18)
        math3 = MathTex(r"v_i = \frac{\sum_{j=1}^n u_{ij}^m x_j}{\sum_{j=1}^n u_{ij}^m}", font_size=32).next_to(math2, DOWN, buff=0.18)
        math4 = MathTex(r"u_{ij} = \frac{1}{\sum_{k=1}^c \left(\frac{\|x_j - v_i\|}{\|x_j - v_k\|}\right)^{\frac{2}{m-1}}}", font_size=32).next_to(math3, DOWN, buff=0.18)
        self.play(FadeIn(math1))
        self.wait(0.7)
        self.play(FadeIn(math2))
        self.wait(0.7)
        self.play(FadeIn(math3))
        self.wait(0.7)
        self.play(FadeIn(math4))
        self.wait(2)
        self.play(FadeOut(sec3), FadeOut(math1), FadeOut(math2), FadeOut(math3), FadeOut(math4))

        # 4. Algorithm Steps (simulation)
        sec4 = Text("4. Fuzzy C-Means Algorithm Steps", font_size=34, color=YELLOW).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(sec4))
        # Simulate points
        np.random.seed(0)
        pts = np.vstack([
            np.random.normal([2, 2], 0.4, (12, 2)),
            np.random.normal([5, 6], 0.5, (12, 2)),
            np.random.normal([8, 3], 0.6, (12, 2))
        ])
        axes2 = Axes(x_range=[0, 10], y_range=[0, 8], x_length=6, y_length=4, axis_config={"font_size": 20})
        axes2.next_to(sec4, DOWN, buff=0.6)
        dots2 = VGroup(*[Dot(axes2.c2p(x, y), color=WHITE, radius=0.09) for x, y in pts])
        self.play(Create(axes2), FadeIn(dots2))
        # Simulate soft memberships (for visualization)
        memberships = np.clip(np.random.dirichlet([2,2,2], len(pts)), 0.05, 0.95)
        centroids = np.array([[2,2],[5,6],[8,3]])
        for i, dot in enumerate(dots2):
            color = interpolate_color(YELLOW, BLUE, memberships[i,1])
            color = interpolate_color(color, GREEN, memberships[i,2])
            self.play(dot.animate.set_color(color), run_time=0.03)
        centroid_dots = VGroup(*[Dot(axes2.c2p(*c), color=col, radius=0.15) for c, col in zip(centroids, [YELLOW, BLUE, GREEN])])
        self.play(FadeIn(centroid_dots))
        self.wait(1.5)
        self.play(FadeOut(axes2), FadeOut(dots2), FadeOut(centroid_dots), FadeOut(sec4))

        # 5. Comparison Table
        sec5 = Text("5. Fuzzy C-Means vs K-Means", font_size=32, color=ORANGE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(sec5))
        table_data = [
            ["Feature", "K-Means", "Fuzzy C-Means"],
            ["Type", "Hard", "Soft"],
            ["Membership", "0 or 1", "0 to 1"],
            ["Best for", "Clear clusters", "Overlapping/uncertain"],
            ["Speed", "Faster", "Slower"],
            ["Output", "One cluster", "Degrees of membership"]
        ]
        table = Table(table_data, include_outer_lines=True, element_to_mobject_config={"font_size": 22})
        table.scale(0.9).next_to(sec5, DOWN, buff=0.3)
        self.play(FadeIn(table))
        self.wait(2.2)
        self.play(FadeOut(table), FadeOut(sec5))

        # 6. Example: Patient Risk Segmentation
        sec6 = Text("6. Example: Patient Risk Segmentation", font_size=32, color=GREEN).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(sec6))
        axes3 = Axes(x_range=[20, 80], y_range=[100, 300], x_length=6, y_length=4, axis_config={"font_size": 20})
        axes3.next_to(sec6, DOWN, buff=0.6)
        np.random.seed(1)
        age = np.concatenate([np.random.normal(25, 4, 12), np.random.normal(50, 6, 12), np.random.normal(70, 5, 12)])
        chol = np.concatenate([np.random.normal(160, 12, 12), np.random.normal(220, 18, 12), np.random.normal(270, 10, 12)])
        memberships2 = np.clip(np.random.dirichlet([3,2,1], len(age)), 0.05, 0.95)
        colors3 = [interpolate_color(GREEN, YELLOW, memberships2[i,1]) for i in range(len(age))]
        dots3 = VGroup(*[Dot(axes3.c2p(a, c), color=col, radius=0.1) for a, c, col in zip(age, chol, colors3)])
        self.play(Create(axes3), FadeIn(dots3))
        self.wait(2)
        self.play(FadeOut(axes3), FadeOut(dots3), FadeOut(sec6))

        # 7. Advantages
        sec7 = Text("7. Advantages of Fuzzy C-Means", font_size=30, color=YELLOW).next_to(title, DOWN, buff=0.5)
        adv = BulletedList(
            "Flexible for real-world problems",
            "Captures ambiguity in data",
            "Ideal for soft decision-making",
            font_size=22
        ).next_to(sec7, DOWN, buff=0.2)
        self.play(FadeIn(sec7), FadeIn(adv))
        self.wait(2.2)
        self.play(FadeOut(sec7), FadeOut(adv))

        # 8. Disadvantages
        sec8 = Text("8. Disadvantages", font_size=30, color=RED).next_to(title, DOWN, buff=0.5)
        disadv = BulletedList(
            "Slower than K-Means",
            "Sensitive to initial membership",
            "May get stuck in local minima",
            "Still assumes spherical clusters",
            font_size=22
        ).next_to(sec8, DOWN, buff=0.2)
        self.play(FadeIn(sec8), FadeIn(disadv))
        self.wait(2.2)
        self.play(FadeOut(sec8), FadeOut(disadv))

        # Summary
        final = VGroup(
            Text("Fuzzy C-Means: Flexible, soft clustering!", font_size=28, color=YELLOW),
            Text("Handles overlap and ambiguity.", font_size=28, color=BLUE),
            Text("Generalizes K-Means for real-world data.", font_size=28, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(ORIGIN)
        self.play(FadeIn(final))
        self.wait(2.5)
        self.play(FadeOut(final), FadeOut(title))
        self.wait(0.5)
