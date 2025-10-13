from manim import *
import numpy as np

class DBSCANHDBSCANClusteringExplanation(Scene):
    def construct(self):
        # Title
        title = Text("DBSCAN & HDBSCAN – Density-Based Clustering", font_size=38)
        self.play(FadeIn(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # 1. What is DBSCAN?
        sec1 = Text("1. What is DBSCAN?", font_size=34, color=YELLOW).next_to(title, DOWN, buff=0.5)
        desc1 = Text("Groups closely packed points, marks low-density as noise.\nNo need to pick K, finds any shape!", font_size=28).next_to(sec1, DOWN, buff=0.2)
        self.play(FadeIn(sec1), FadeIn(desc1))
        self.wait(2)
        self.play(FadeOut(sec1), FadeOut(desc1))

        # 2. Intuition (marbles map)
        sec2 = Text("2. Intuition Behind DBSCAN", font_size=34, color=BLUE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(sec2))
        axes = Axes(x_range=[0, 10], y_range=[0, 8], x_length=6, y_length=4, axis_config={"font_size": 20})
        axes.next_to(sec2, DOWN, buff=0.6)
        np.random.seed(42)
        points = np.vstack([
            np.random.normal([3, 6], 0.5, (18, 2)),
            np.random.normal([7, 2], 0.7, (18, 2)),
            np.random.normal([6, 6], 0.3, (9, 2)),
            np.random.normal([1.5, 2], 0.4, (7, 2)),
            np.random.normal([8, 7], 0.2, (4, 2))
        ])
        dots = VGroup(*[Dot(axes.c2p(x, y), color=WHITE, radius=0.09) for x, y in points])
        self.play(Create(axes), FadeIn(dots))
        self.wait(1.2)
        self.play(FadeOut(sec2))

        # 3. Core, Border, Noise
        sec3 = Text("3. DBSCAN: Core, Border, Noise", font_size=32, color=PURPLE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(sec3))
        # Example: highlight core, border, noise
        core = [0, 1, 2, 3, 10, 19, 22, 28]
        border = [4, 11, 12, 20, 24, 27]
        noise = [5, 7, 29, 30, 32]
        for i in core:
            dots[i].set_color(GREEN)
        for i in border:
            dots[i].set_color(YELLOW)
        for i in noise:
            dots[i].set_color(RED)
        legend = VGroup(
            Dot(color=GREEN), Text("Core", font_size=22, color=GREEN),
            Dot(color=YELLOW), Text("Border", font_size=22, color=YELLOW),
            Dot(color=RED), Text("Noise", font_size=22, color=RED)
        ).arrange(RIGHT, buff=0.3).next_to(axes, DOWN, buff=0.2)
        self.play(FadeIn(legend))
        self.wait(2)
        self.play(FadeOut(sec3), FadeOut(legend), FadeOut(axes), FadeOut(dots))

        # 4. DBSCAN Steps
        sec4 = Text("4. How DBSCAN Works", font_size=32, color=BLUE).next_to(title, DOWN, buff=0.5)
        steps = BulletedList(
            "Pick random unvisited point",
            "If >= MinPts in epsilon: new cluster",
            "Expand cluster by neighbors",
            "Else: mark as noise",
            "Repeat until all visited",
            font_size=22
        ).next_to(sec4, DOWN, buff=0.2)
        self.play(FadeIn(sec4), FadeIn(steps))
        self.wait(2.2)
        self.play(FadeOut(sec4), FadeOut(steps))

        # 5. DBSCAN Pros/Cons
        sec5 = Text("5. DBSCAN: Pros & Cons", font_size=32, color=ORANGE).next_to(title, DOWN, buff=0.5)
        pros = BulletedList(
            "Finds any shape",
            "Detects noise/outliers",
            "No need to pick K",
            font_size=22
        ).next_to(sec5, DOWN, buff=0.2)
        cons = BulletedList(
            "Choosing epsilon, MinPts is tricky",
            "Struggles with varying density",
            font_size=22
        ).next_to(pros, DOWN, buff=0.3)
        self.play(FadeIn(sec5), FadeIn(pros), FadeIn(cons))
        self.wait(2.2)
        self.play(FadeOut(sec5), FadeOut(pros), FadeOut(cons))

        # 6. What is HDBSCAN?
        sec6 = Text("6. What is HDBSCAN?", font_size=34, color=YELLOW).next_to(title, DOWN, buff=0.5)
        desc6 = Text("Smarter, hierarchical DBSCAN. Handles varying densities. No need for ε!", font_size=28).next_to(sec6, DOWN, buff=0.2)
        self.play(FadeIn(sec6), FadeIn(desc6))
        self.wait(2)
        self.play(FadeOut(sec6), FadeOut(desc6))

        # 7. HDBSCAN Intuition
        sec7 = Text("7. Intuition Behind HDBSCAN", font_size=32, color=BLUE).next_to(title, DOWN, buff=0.5)
        steps7 = BulletedList(
            "Measure local density",
            "Build Minimum Spanning Tree (MST)",
            "Build cluster hierarchy (dendrogram)",
            "Select stable clusters",
            font_size=22
        ).next_to(sec7, DOWN, buff=0.2)
        self.play(FadeIn(sec7), FadeIn(steps7))
        self.wait(2.2)
        self.play(FadeOut(sec7), FadeOut(steps7))

        # 8. Key Math (mutual reachability)
        sec8 = Text("8. HDBSCAN: Key Math", font_size=32, color=PURPLE).next_to(title, DOWN, buff=0.5)
        formula = MathTex(r"d_{mreach}(i, j) = \max\{\text{core}_k(i), \text{core}_k(j), d(i, j)\}", font_size=34).next_to(sec8, DOWN, buff=0.3)
        self.play(FadeIn(sec8), FadeIn(formula))
        self.wait(2)
        self.play(FadeOut(sec8), FadeOut(formula))

        # 9. HDBSCAN Steps
        sec9 = Text("9. How HDBSCAN Works", font_size=32, color=YELLOW).next_to(title, DOWN, buff=0.5)
        steps9 = BulletedList(
            "Compute core distances",
            "Build mutual reachability graph",
            "Construct MST",
            "Build dendrogram",
            "Condense and select best clusters",
            font_size=22
        ).next_to(sec9, DOWN, buff=0.2)
        self.play(FadeIn(sec9), FadeIn(steps9))
        self.wait(2.2)
        self.play(FadeOut(sec9), FadeOut(steps9))

        # 10. DBSCAN vs HDBSCAN Table
        sec10 = Text("10. DBSCAN vs HDBSCAN", font_size=32, color=GREEN).next_to(title, DOWN, buff=0.5)
        table_data = [
            ["Feature", "DBSCAN", "HDBSCAN"],
            ["Density", "Single ε", "Varying (adaptive)"],
            ["ε required?", "Yes", "No"],
            ["Finds noise?", "Yes", "Yes"],
            ["Output", "Flat", "Flat + hierarchy"],
            ["Speed", "Faster", "Slower, more accurate"],
            ["Use case", "Uniform clusters", "Complex, real-world"]
        ]
        table = Table(table_data, include_outer_lines=True, element_to_mobject_config={"font_size": 22})
        table.scale(0.9).next_to(sec10, DOWN, buff=0.3)
        self.play(FadeIn(sec10), FadeIn(table))
        self.wait(2.2)
        self.play(FadeOut(sec10), FadeOut(table))

        # 11. Real World Example: GPS Data
        sec11 = Text("11. Real-World Example: GPS Data", font_size=32, color=ORANGE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(sec11))
        axes2 = Axes(x_range=[0, 10], y_range=[0, 8], x_length=6, y_length=4, axis_config={"font_size": 20})
        axes2.next_to(sec11, DOWN, buff=0.6)
        # Simulate GPS data with tight and loose clusters
        np.random.seed(7)
        tight = np.random.normal([2, 6], 0.3, (15, 2))
        loose = np.random.normal([7, 2], 1.0, (15, 2))
        noise = np.random.uniform([0,0], [10,8], (6,2))
        allpts = np.vstack([tight, loose, noise])
        # DBSCAN coloring: can't separate loose cluster well
        dbscan_colors = [YELLOW]*15 + [BLUE]*15 + [RED]*6
        dbscan_dots = VGroup(*[Dot(axes2.c2p(x, y), color=col, radius=0.11) for (x, y), col in zip(allpts, dbscan_colors)])
        self.play(Create(axes2), FadeIn(dbscan_dots))
        db_label = Text("DBSCAN: struggles with varying density", font_size=24, color=YELLOW).next_to(axes2, DOWN, buff=0.2)
        self.play(FadeIn(db_label))
        self.wait(1.5)
        self.play(FadeOut(dbscan_dots), FadeOut(db_label))
        # HDBSCAN coloring: can adapt
        hdbscan_colors = [GREEN]*15 + [PURPLE]*15 + [RED]*6
        hdbscan_dots = VGroup(*[Dot(axes2.c2p(x, y), color=col, radius=0.11) for (x, y), col in zip(allpts, hdbscan_colors)])
        self.play(FadeIn(hdbscan_dots))
        hdb_label = Text("HDBSCAN: adapts to both densities", font_size=24, color=GREEN).next_to(axes2, DOWN, buff=0.2)
        self.play(FadeIn(hdb_label))
        self.wait(1.5)
        self.play(FadeOut(hdbscan_dots), FadeOut(hdb_label), FadeOut(axes2), FadeOut(sec11))

        # 12. Advantages HDBSCAN
        sec12 = Text("12. Advantages of HDBSCAN", font_size=30, color=GREEN).next_to(title, DOWN, buff=0.5)
        adv = BulletedList(
            "No need to guess epsilon",
            "Handles varying densities",
            "Detects noise",
            "Produces hierarchy and flat clusters",
            font_size=22
        ).next_to(sec12, DOWN, buff=0.2)
        self.play(FadeIn(sec12), FadeIn(adv))
        self.wait(2.2)
        self.play(FadeOut(sec12), FadeOut(adv))

        # 13. Disadvantages
        sec13 = Text("13. Disadvantages", font_size=30, color=RED).next_to(title, DOWN, buff=0.5)
        disadv = BulletedList(
            "Slightly more computationally intensive",
            "Harder to explain than DBSCAN",
            font_size=22
        ).next_to(sec13, DOWN, buff=0.2)
        self.play(FadeIn(sec13), FadeIn(disadv))
        self.wait(2.2)
        self.play(FadeOut(sec13), FadeOut(disadv))

        # Conclusion
        final = VGroup(
            Text("DBSCAN: Quick, finds any shape (uniform density)", font_size=26, color=YELLOW),
            Text("HDBSCAN: Smarter, adapts to real-world data!", font_size=26, color=GREEN),
            Text("Choose based on your data's complexity.", font_size=26, color=BLUE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(ORIGIN)
        self.play(FadeIn(final))
        self.wait(2.5)
        self.play(FadeOut(final), FadeOut(title))
        self.wait(0.5)
