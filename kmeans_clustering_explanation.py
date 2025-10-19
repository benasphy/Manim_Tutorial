from manim import *
import numpy as np

class KMeansClusteringExplanation(Scene):
    def construct(self):
        # Title
        title = Text("K-Means Clustering – Explained Simply", font_size=40)
        self.play(FadeIn(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # 1. What is K-Means?
        sec1 = Text("1. What is K-Means Clustering?", font_size=34, color=YELLOW).next_to(title, DOWN, buff=0.5)
        desc1 = Text("Unsupervised learning: group data into K clusters\nEach cluster has a centroid. Minimize distance to centroid.", font_size=28).next_to(sec1, DOWN, buff=0.2)
        self.play(FadeIn(sec1), FadeIn(desc1))
        self.wait(2)
        self.play(FadeOut(sec1), FadeOut(desc1))

        # 2. How does K-Means work? (step-by-step simulation)
        sec2 = Text("2. How Does K-Means Work?", font_size=34, color=BLUE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(sec2))
        # Simulate points
        np.random.seed(42)
        points = np.vstack([
            np.random.normal([2, 2], 0.4, (20, 2)),
            np.random.normal([5, 6], 0.5, (20, 2)),
            np.random.normal([8, 3], 0.6, (20, 2))
        ])
        axes = Axes(x_range=[0, 10], y_range=[0, 8], x_length=6, y_length=4, axis_config={"font_size": 20})
        axes.next_to(sec2, DOWN, buff=0.6)
        dots = VGroup(*[Dot(axes.c2p(x, y), color=WHITE, radius=0.09) for x, y in points])
        self.play(Create(axes), FadeIn(dots))
        self.wait(0.8)
        # Step 1: Choose K
        step1 = Text("Step 1: Choose K (e.g., K=3)", font_size=26, color=YELLOW).next_to(axes, UP, buff=0.2)
        self.play(FadeIn(step1))
        self.wait(1)
        self.play(FadeOut(step1))
        # Step 2: Initialize centroids
        init_idx = [0, 22, 40]
        centroids = [points[i] for i in init_idx]
        centroid_dots = VGroup(*[Dot(axes.c2p(*c), color=col, radius=0.15) for c, col in zip(centroids, [YELLOW, BLUE, GREEN])])
        self.play(FadeIn(centroid_dots))
        self.wait(1)
        step2 = Text("Step 2: Randomly initialize centroids", font_size=26, color=YELLOW).next_to(axes, UP, buff=0.2)
        self.play(FadeIn(step2))
        self.wait(1)
        self.play(FadeOut(step2))
        # Step 3: Assign points to nearest centroid
        step3 = Text("Step 3: Assign points to nearest centroid", font_size=26, color=YELLOW).next_to(axes, UP, buff=0.2)
        self.play(FadeIn(step3))
        # Assign colors
        assignments = np.argmin([np.linalg.norm(points - c, axis=1) for c in centroids], axis=0)
        cluster_colors = [YELLOW, BLUE, GREEN]
        for i, dot in enumerate(dots):
            self.play(dot.animate.set_color(cluster_colors[assignments[i]]), run_time=0.03)
        self.wait(1)
        self.play(FadeOut(step3))
        # Step 4: Recalculate centroids
        step4 = Text("Step 4: Recalculate centroids (mean of cluster)", font_size=26, color=YELLOW).next_to(axes, UP, buff=0.2)
        self.play(FadeIn(step4))
        new_centroids = [points[assignments == k].mean(axis=0) for k in range(3)]
        new_centroid_dots = VGroup(*[Dot(axes.c2p(*c), color=col, radius=0.18, fill_opacity=0.7) for c, col in zip(new_centroids, cluster_colors)])
        self.play(Transform(centroid_dots, new_centroid_dots))
        self.wait(1)
        self.play(FadeOut(step4))
        # Step 5: Repeat
        step5 = Text("Step 5: Repeat until convergence!", font_size=26, color=YELLOW).next_to(axes, UP, buff=0.2)
        self.play(FadeIn(step5))
        self.wait(1.2)
        self.play(FadeOut(step5))
        self.play(FadeOut(axes), FadeOut(dots), FadeOut(centroid_dots))
        self.play(FadeOut(sec2))

        # 3. Real-World Example
        sec3 = Text("3. Real-World Example: Customer Segmentation", font_size=32, color=GREEN).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(sec3))
        axes2 = Axes(x_range=[15, 70], y_range=[0, 110], x_length=6, y_length=4, axis_config={"font_size": 20}, x_axis_config={"numbers_to_include":[20,30,40,50,60]}, y_axis_config={"numbers_to_include":[20,40,60,80,100]})
        axes2.next_to(sec3, DOWN, buff=0.6)
        # Simulate example data
        np.random.seed(1)
        age = np.concatenate([np.random.normal(22, 3, 15), np.random.normal(40, 5, 15), np.random.normal(58, 4, 15)])
        score = np.concatenate([np.random.normal(30, 6, 15), np.random.normal(60, 8, 15), np.random.normal(90, 5, 15)])
        colors2 = [YELLOW]*15 + [BLUE]*15 + [GREEN]*15
        dots2 = VGroup(*[Dot(axes2.c2p(a, s), color=col, radius=0.1) for a, s, col in zip(age, score, colors2)])
        self.play(Create(axes2), FadeIn(dots2))
        self.wait(2)
        self.play(FadeOut(axes2), FadeOut(dots2), FadeOut(sec3))

        # 4. Cost Function (WCSS)
        sec4 = Text("4. The Cost Function: WCSS", font_size=32, color=ORANGE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(sec4))
        formula = MathTex(r"\text{WCSS} = \sum_{i=1}^K \sum_{x \in C_i} \|x - \mu_i\|^2", font_size=36).next_to(sec4, DOWN, buff=0.3)
        self.play(FadeIn(formula))
        self.wait(2)
        self.play(FadeOut(formula), FadeOut(sec4))

        # 5. Elbow Method
        sec5 = Text("5. Choosing K: The Elbow Method", font_size=32, color=PURPLE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(sec5))
        axes3 = Axes(x_range=[1, 8], y_range=[0, 600], x_length=5, y_length=3, axis_config={"font_size": 18})
        axes3.next_to(sec5, DOWN, buff=0.7)
        ks = np.arange(1, 8)
        wcss = [520, 330, 210, 180, 140, 120, 110]
        elbow_curve = axes3.plot_line_graph(ks, wcss, add_vertex_dots=True, line_color=YELLOW, stroke_width=4)
        self.play(Create(axes3), Create(elbow_curve))
        elbow_dot = Dot(axes3.c2p(3, 210), color=RED, radius=0.14)
        elbow_label = Text("Elbow (Best K)", font_size=22, color=RED).next_to(elbow_dot, DOWN+RIGHT, buff=0.12)
        self.play(FadeIn(elbow_dot), FadeIn(elbow_label))
        self.wait(2)
        self.play(FadeOut(axes3), FadeOut(elbow_curve), FadeOut(elbow_dot), FadeOut(elbow_label), FadeOut(sec5))

        # 6. Advantages
        sec6 = Text("6. Advantages of K-Means", font_size=30, color=GREEN).next_to(title, DOWN, buff=0.5)
        adv = BulletedList(
            "Simple to understand and implement",
            "Fast and scalable",
            "Works well for separated clusters",
            font_size=22
        ).next_to(sec6, DOWN, buff=0.2)
        self.play(FadeIn(sec6), FadeIn(adv))
        self.wait(2.2)
        self.play(FadeOut(sec6), FadeOut(adv))

        # 7. Disadvantages
        sec7 = Text("7. Disadvantages of K-Means", font_size=30, color=RED).next_to(title, DOWN, buff=0.5)
        disadv = BulletedList(
            "Need to choose K in advance",
            "Sensitive to initial centroids",
            "Assumes spherical, equal-size clusters",
            "Struggles with outliers/non-convex shapes",
            font_size=22
        ).next_to(sec7, DOWN, buff=0.2)
        self.play(FadeIn(sec7), FadeIn(disadv))
        self.wait(2.2)
        self.play(FadeOut(sec7), FadeOut(disadv))

        # Final Thought
        final = VGroup(
            Text("K-Means: Group identity for your data!", font_size=28, color=YELLOW),
            Text("Finds hidden patterns & segments.", font_size=28, color=BLUE),
            Text("Simple but powerful for ML & business.", font_size=28, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(ORIGIN)
        self.play(FadeIn(final))
        self.wait(2.5)
        self.play(FadeOut(final), FadeOut(title))
        self.wait(0.5)
