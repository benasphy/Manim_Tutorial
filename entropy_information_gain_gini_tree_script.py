from manim import *

class EntropyInfoGainGiniTreeScript(Scene):
    def construct(self):
        # Title
        title = Text("Entropy, Information Gain & Gini Impurity", font_size=44)
        self.play(FadeIn(title))
        self.wait(0.7)
        self.play(title.animate.to_edge(UP))

        # Show full decision tree image (stylized tree)
        tree_title = Text("Decision Tree Example", font_size=32, color=BLUE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(tree_title))
        self.wait(1.2)
        self.play(FadeOut(tree_title))
        # Draw tree root and branches
        root_circle = Circle(radius=0.6, color=WHITE).move_to([0, 1.5, 0])
        root_label = Text("8 Yes\n4 No", font_size=28).move_to(root_circle.get_center())
        root = VGroup(root_circle, root_label)
        self.play(FadeIn(root))
        self.wait(0.7)

        # Root node entropy explanation
        entropy_title = Text("Root Node: Entropy", font_size=30, color=YELLOW).next_to(root, DOWN, buff=0.2)
        self.play(FadeIn(entropy_title))
        entropy_formula = MathTex(r"\text{Entropy}(S) = -p_1 \log_2(p_1) - p_2 \log_2(p_2)", font_size=32).next_to(entropy_title, DOWN, buff=0.2)
        self.play(FadeIn(entropy_formula))
        p_yes = MathTex(r"p_{yes} = \frac{8}{12} = 0.67", font_size=28).next_to(entropy_formula, DOWN, buff=0.15)
        p_no = MathTex(r"p_{no} = \frac{4}{12} = 0.33", font_size=28).next_to(p_yes, DOWN, buff=0.1)
        self.play(FadeIn(p_yes), FadeIn(p_no))
        entropy_calc = MathTex(r"\text{Entropy}_{root} = -0.67 \log_2(0.67) - 0.33 \log_2(0.33) \approx 0.918", font_size=30).next_to(p_no, DOWN, buff=0.15)
        self.play(FadeIn(entropy_calc))
        self.wait(2)
        self.play(FadeOut(entropy_title), FadeOut(entropy_formula), FadeOut(p_yes), FadeOut(p_no), FadeOut(entropy_calc))

        # Split branches
        split_text = Text("Split by Feature 1", font_size=30, color=GREEN).next_to(root, DOWN, buff=0.2)
        self.play(FadeIn(split_text))
        # Left branch (circle with label inside)
        left_circle = Circle(radius=0.5, color=WHITE).move_to([-2.5, -0.2, 0])
        left_label = Text("5 Yes\n2 No", font_size=24).move_to(left_circle.get_center())
        left_branch = VGroup(left_circle, left_label)
        # Right branch (circle with label inside)
        right_circle = Circle(radius=0.5, color=WHITE).move_to([2.5, -0.2, 0])
        right_label = Text("3 Yes\n2 No", font_size=24).move_to(right_circle.get_center())
        right_branch = VGroup(right_circle, right_label)
        left_arrow = Arrow(root_circle.get_bottom(), left_circle.get_top(), buff=0.1)
        right_arrow = Arrow(root_circle.get_bottom(), right_circle.get_top(), buff=0.1)
        self.play(GrowArrow(left_arrow), GrowArrow(right_arrow), FadeIn(left_branch), FadeIn(right_branch))
        self.wait(0.7)
        self.play(FadeOut(split_text))

        # Left branch entropy
        left_entropy_title = Text("Left Branch Entropy", font_size=28, color=YELLOW).next_to(left_branch, DOWN, buff=0.15)
        left_entropy = MathTex(r"\text{Entropy}_{left} = -\frac{5}{7} \log_2(\frac{5}{7}) - \frac{2}{7} \log_2(\frac{2}{7}) \approx 0.863", font_size=26).next_to(left_entropy_title, DOWN, buff=0.1)
        self.play(FadeIn(left_entropy_title), FadeIn(left_entropy))
        self.wait(1.5)
        self.play(FadeOut(left_entropy_title), FadeOut(left_entropy))

        # Right branch entropy
        right_entropy_title = Text("Right Branch Entropy", font_size=28, color=YELLOW).next_to(right_branch, DOWN, buff=0.15)
        right_entropy = MathTex(r"\text{Entropy}_{right} = -\frac{3}{5} \log_2(\frac{3}{5}) - \frac{2}{5} \log_2(\frac{2}{5}) \approx 0.971", font_size=26).next_to(right_entropy_title, DOWN, buff=0.1)
        self.play(FadeIn(right_entropy_title), FadeIn(right_entropy))
        self.wait(1.5)
        self.play(FadeOut(right_entropy_title), FadeOut(right_entropy))

        # Information Gain
        # Information Gain and Gini Impurity further below the root circle, near the bottom
        ig_y = -2.3
        ig_title = Text("Information Gain", font_size=30, color=PURPLE).move_to([0, ig_y, 0])
        ig_formula = MathTex(r"\text{IG} = \text{Entropy}_{parent} - (\frac{n_{left}}{n} \cdot \text{Entropy}_{left} + \frac{n_{right}}{n} \cdot \text{Entropy}_{right})", font_size=26).next_to(ig_title, DOWN, buff=0.1)
        ig_calc = MathTex(r"= 0.918 - (\frac{7}{12} \cdot 0.863 + \frac{5}{12} \cdot 0.971) \approx 0.045", font_size=26).next_to(ig_formula, DOWN, buff=0.1)
        self.play(FadeIn(ig_title), FadeIn(ig_formula), FadeIn(ig_calc))
        self.wait(2)
        self.play(FadeOut(ig_title), FadeOut(ig_formula), FadeOut(ig_calc))

        # Move Gini Impurity and closing summary near the bottom (but not too low)
        gini_y = -2.3
        gini_title = Text("Gini Impurity at Root", font_size=30, color=ORANGE).move_to([0, gini_y, 0])
        gini_formula = MathTex(r"\text{Gini}(S) = 1 - (0.67)^2 - (0.33)^2 \approx 0.445", font_size=28).next_to(gini_title, DOWN, buff=0.1)
        self.play(FadeIn(gini_title), FadeIn(gini_formula))
        self.wait(2)
        self.play(FadeOut(gini_title), FadeOut(gini_formula))

        # Make closing text start from the top, left-aligned
        closing = VGroup(
            Text("Entropy measures disorder.", font_size=30, color=YELLOW),
            Text("Information Gain: how much better the split is.", font_size=28),
            Text("Gini: another impurity measure.", font_size=28),
            Text("These metrics help build better trees!", font_size=28, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        closing.to_edge(UP, buff=0.8)
        closing.to_edge(LEFT, buff=0.8)
        # Remove decision tree and display closing text
        self.play(FadeOut(title), FadeOut(root), FadeOut(left_branch), FadeOut(right_branch), FadeOut(left_arrow), FadeOut(right_arrow))
        self.wait(0.3)
        self.play(FadeIn(closing))
        self.wait(2.5)
        self.play(FadeOut(closing))
        self.wait(0.5)
