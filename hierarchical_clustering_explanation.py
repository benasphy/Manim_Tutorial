from manim import *
import numpy as np

class HierarchicalClusteringExplanation(Scene):
    def construct(self):
        # Title
        title = Text("Hierarchical Clustering – Explained Simply", font_size=40)
        self.play(FadeIn(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # 1. What is Hierarchical Clustering?
        sec1 = Text("1. What is Hierarchical Clustering?", font_size=34, color=YELLOW).next_to(title, DOWN, buff=0.5)
        desc1 = Text("Unsupervised learning.\nGroups data into clusters without preset number.\nBuilds a hierarchy (family tree) of clusters.", font_size=28).next_to(sec1, DOWN, buff=0.2)
        self.play(FadeIn(sec1), FadeIn(desc1))
        self.wait(2)
        self.play(FadeOut(sec1), FadeOut(desc1))

        # 2. Dendrogram
        sec2 = Text("2. Dendrogram: The Family Tree", font_size=34, color=BLUE).next_to(title, DOWN, buff=0.5)
        desc2 = Text("A dendrogram shows how clusters merge or split.\nHeight = dissimilarity.\nCut at any height for clusters!", font_size=28).next_to(sec2, DOWN, buff=0.2)
        self.play(FadeIn(sec2), FadeIn(desc2))
        self.wait(1.5)
        # Draw a dendrogram (stylized)
        axes = Axes(x_range=[0, 10], y_range=[0, 6], x_length=7, y_length=3, axis_config={"font_size": 18, "include_ticks": False, "include_tip": False})
        axes.next_to(desc2, DOWN, buff=0.6)
        # Leaves
        leaves_x = np.linspace(1, 9, 7)
        leaves_y = np.zeros(7)
        leaves = [axes.c2p(x, y) for x, y in zip(leaves_x, leaves_y)]
        leaf_dots = VGroup(*[Dot(p, color=WHITE, radius=0.08) for p in leaves])
        # Merge lines
        lines = VGroup()
        # First merge pairs
        for i in range(0, 7, 2):
            if i+1 < 7:
                midx = (leaves_x[i] + leaves_x[i+1])/2
                lines.add(Line(axes.c2p(leaves_x[i], 0), axes.c2p(midx, 1), color=GREY))
                lines.add(Line(axes.c2p(leaves_x[i+1], 0), axes.c2p(midx, 1), color=GREY))
        # Next merge
        lines.add(Line(axes.c2p((leaves_x[0]+leaves_x[1])/2, 1), axes.c2p(2, 2), color=GREY))
        lines.add(Line(axes.c2p((leaves_x[2]+leaves_x[3])/2, 1), axes.c2p(4, 2), color=GREY))
        lines.add(Line(axes.c2p((leaves_x[4]+leaves_x[5])/2, 1), axes.c2p(6, 2), color=GREY))
        # Merge those
        lines.add(Line(axes.c2p(2, 2), axes.c2p(3, 3), color=GREY))
        lines.add(Line(axes.c2p(4, 2), axes.c2p(3, 3), color=GREY))
        lines.add(Line(axes.c2p(6, 2), axes.c2p(5, 3), color=GREY))
        # Final merge
        lines.add(Line(axes.c2p(3, 3), axes.c2p(4, 4.5), color=GREY))
        lines.add(Line(axes.c2p(5, 3), axes.c2p(4, 4.5), color=GREY))
        # Add height label
        height_label = Text("Height (Dissimilarity)", font_size=20, color=GREY).next_to(axes.y_axis.get_top(), UP, buff=0.1)
        self.play(Create(axes), FadeIn(leaf_dots), *[Create(l) for l in lines], FadeIn(height_label))
        self.wait(2)
        self.play(FadeOut(sec2), FadeOut(desc2), FadeOut(axes), FadeOut(leaf_dots), *[FadeOut(l) for l in lines], FadeOut(height_label))

        # 3. Types of Hierarchical Clustering
        sec3 = Text("3. Types of Hierarchical Clustering", font_size=34, color=PURPLE).next_to(title, DOWN, buff=0.5)
        agglom = Text("Agglomerative (Bottom-Up):\nEach point starts alone, clusters merge.", font_size=26, color=YELLOW).next_to(sec3, DOWN, buff=0.2)
        divisive = Text("Divisive (Top-Down):\nAll points start together, clusters split.", font_size=26, color=BLUE).next_to(agglom, DOWN, buff=0.18)
        self.play(FadeIn(sec3), FadeIn(agglom), FadeIn(divisive))
        self.wait(1.2)
        # Agglomerative visual (bottom-up tree)
        agglom_points = [Dot(LEFT*2 + DOWN*1 + RIGHT*i, color=YELLOW, radius=0.14) for i in range(5)]
        agglom_vg = VGroup(*agglom_points).arrange(RIGHT, buff=0.7).next_to(divisive, DOWN, buff=0.6)
        self.play(FadeIn(agglom_vg))
        # Merge 1-2, 3-4
        l1 = Line(agglom_points[0].get_top(), agglom_points[1].get_top() + UP*0.5, color=YELLOW)
        l2 = Line(agglom_points[1].get_top(), agglom_points[1].get_top() + UP*0.5, color=YELLOW)
        l3 = Line(agglom_points[2].get_top(), agglom_points[3].get_top() + UP*0.5, color=YELLOW)
        l4 = Line(agglom_points[3].get_top(), agglom_points[3].get_top() + UP*0.5, color=YELLOW)
        self.play(Create(l1), Create(l2), Create(l3), Create(l4))
        merge1 = Dot((agglom_points[0].get_top() + agglom_points[1].get_top())/2 + UP*0.5, color=YELLOW, radius=0.11)
        merge2 = Dot((agglom_points[2].get_top() + agglom_points[3].get_top())/2 + UP*0.5, color=YELLOW, radius=0.11)
        self.play(FadeIn(merge1), FadeIn(merge2))
        # Merge those with center
        l5 = Line(merge1.get_top(), merge2.get_top() + UP*0.7, color=YELLOW)
        l6 = Line(merge2.get_top(), merge2.get_top() + UP*0.7, color=YELLOW)
        merge3 = Dot((merge1.get_top() + merge2.get_top())/2 + UP*0.7, color=YELLOW, radius=0.10)
        self.play(Create(l5), Create(l6), FadeIn(merge3))
        self.wait(0.8)
        self.play(FadeOut(agglom_vg), FadeOut(l1), FadeOut(l2), FadeOut(l3), FadeOut(l4), FadeOut(merge1), FadeOut(merge2), FadeOut(l5), FadeOut(l6), FadeOut(merge3))
        # Divisive visual (top-down tree)
        root = Dot(ORIGIN + DOWN*0.2, color=BLUE, radius=0.14)
        l7 = Line(root.get_bottom(), root.get_bottom() + DOWN*0.7, color=BLUE)
        split1 = [Dot(root.get_bottom() + DOWN*0.7 + LEFT*0.7, color=BLUE, radius=0.12), Dot(root.get_bottom() + DOWN*0.7 + RIGHT*0.7, color=BLUE, radius=0.12)]
        self.play(FadeIn(root), Create(l7), FadeIn(split1[0]), FadeIn(split1[1]))
        l8 = Line(split1[0].get_bottom(), split1[0].get_bottom() + DOWN*0.7, color=BLUE)
        l9 = Line(split1[1].get_bottom(), split1[1].get_bottom() + DOWN*0.7, color=BLUE)
        split2 = [Dot(split1[0].get_bottom() + DOWN*0.7 + LEFT*0.3, color=BLUE, radius=0.10), Dot(split1[0].get_bottom() + DOWN*0.7 + RIGHT*0.3, color=BLUE, radius=0.10),
                  Dot(split1[1].get_bottom() + DOWN*0.7 + LEFT*0.3, color=BLUE, radius=0.10), Dot(split1[1].get_bottom() + DOWN*0.7 + RIGHT*0.3, color=BLUE, radius=0.10)]
        self.play(Create(l8), Create(l9), *[FadeIn(dot) for dot in split2])
        self.wait(0.8)
        self.play(FadeOut(root), FadeOut(l7), FadeOut(split1[0]), FadeOut(split1[1]), FadeOut(l8), FadeOut(l9), *[FadeOut(dot) for dot in split2])
        self.wait(0.5)
        self.play(FadeOut(sec3), FadeOut(agglom), FadeOut(divisive))

        # 4. Silhouette Score (Loss Function)
        sec4 = Text("4. How Good Are Our Clusters?", font_size=34, color=GREEN).next_to(title, DOWN, buff=0.5)
        sil_title = Text("Silhouette Score", font_size=28, color=WHITE).next_to(sec4, DOWN, buff=0.18)
        sil_formula = MathTex(r"s = \frac{b - a}{\operatorname{max}(a, b)}", font_size=34).next_to(sil_title, DOWN, buff=0.18)
        sil_keys = BulletedList(
            "a: Cohesion (intra-cluster distance)",
            "b: Separation (nearest-cluster distance)",
            "s: +1 = well-clustered, 0 = boundary, -1 = wrong cluster",
            font_size=22
        ).next_to(sil_formula, DOWN, buff=0.2)
        self.play(FadeIn(sec4), FadeIn(sil_title), FadeIn(sil_formula))
        self.wait(1.2)
        self.play(FadeIn(sil_keys))
        self.wait(2.2)
        self.play(FadeOut(sec4), FadeOut(sil_title), FadeOut(sil_formula), FadeOut(sil_keys))

        # 5. Advantages & Disadvantages
        sec5 = Text("5. Advantages & Disadvantages", font_size=34, color=ORANGE).next_to(title, DOWN, buff=0.5)
        adv = BulletedList(
            "No need to specify number of clusters",
            "Dendrogram gives visual insight",
            "Works well for small/medium data",
            "Can capture nested/hierarchical structure",
            font_size=22
        ).next_to(sec5, DOWN, buff=0.2)
        disadv = BulletedList(
            "Computationally expensive for large data",
            "Merges/splits can't be undone",
            "Sensitive to noise and outliers",
            font_size=22
        ).next_to(adv, DOWN, buff=0.3)
        self.play(FadeIn(sec5), FadeIn(adv), FadeIn(disadv))
        self.wait(2.5)
        self.play(FadeOut(sec5), FadeOut(adv), FadeOut(disadv))

        # Final Thought
        final = VGroup(
            Text("Hierarchical clustering = family tree for data!", font_size=28, color=YELLOW),
            Text("Dendrogram shows structure visually.", font_size=28, color=BLUE),
            Text("No need to pick clusters in advance.", font_size=28, color=GREEN),
            Text("Try it when you want insight into your data!", font_size=28, color=PURPLE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(ORIGIN)
        self.play(FadeIn(final))
        self.wait(2.5)
        self.play(FadeOut(final), FadeOut(title))
        self.wait(0.5)
