from manim import *

class EntropyInfoGainGiniGym(Scene):
    def construct(self):
        # Title
        title = Text("Decision Tree Splits: Entropy, Info Gain, Gini", font_size=44)
        self.play(FadeIn(title))
        self.wait(0.7)
        self.play(title.animate.to_edge(UP))

        # Scenario intro
        intro = Text("Should I go to the gym?", font_size=36, color=BLUE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(intro))
        self.wait(0.8)
        features = Text("Features: Motivation, Energy", font_size=30).next_to(intro, DOWN, buff=0.3)
        self.play(FadeIn(features))
        self.wait(1.2)

        # Example data table
        table_title = Text("Example Data", font_size=30, color=YELLOW).next_to(features, DOWN, buff=0.4)
        self.play(FadeIn(table_title))
        gym_data = [
            ["Motivation", "Energy", "Go to Gym?"],
            ["High", "High", "Yes"],
            ["High", "Low", "Yes"],
            ["Low", "High", "No"],
            ["Low", "Low", "No"],
            ["High", "High", "Yes"],
            ["Low", "High", "No"],
            ["High", "Low", "Yes"],
            ["Low", "Low", "No"]
        ]
        table = Table(gym_data, include_outer_lines=True, element_to_mobject_config={"font_size": 22})
        table.scale(0.9).next_to(table_title, DOWN, buff=0.3)
        self.play(FadeIn(table))
        self.wait(2)
        self.play(FadeOut(table_title), FadeOut(table))

        # Entropy explanation
        entropy_title = Text("Entropy (Impurity Measure)", font_size=32, color=PURPLE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(entropy_title))
        entropy_formula = MathTex(r"H(S) = -\sum p_i \log_2 p_i", font_size=36).next_to(entropy_title, DOWN, buff=0.3)
        self.play(FadeIn(entropy_formula))
        self.wait(0.8)
        entropy_explain = Text(
            "Entropy measures the disorder or impurity in the set.\nHigh entropy = mixed labels, Low entropy = pure.", font_size=26
        ).next_to(entropy_formula, DOWN, buff=0.25)
        self.play(FadeIn(entropy_explain))
        self.wait(1.6)
        self.play(FadeOut(entropy_title), FadeOut(entropy_formula), FadeOut(entropy_explain))

        # Information Gain explanation
        ig_title = Text("Information Gain", font_size=32, color=GREEN).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(ig_title))
        ig_formula = MathTex(r"IG(S, A) = H(S) - \sum_{v \in \text{values}(A)} \frac{|S_v|}{|S|} H(S_v)", font_size=34).next_to(ig_title, DOWN, buff=0.3)
        self.play(FadeIn(ig_formula))
        self.wait(0.8)
        ig_explain = Text(
            "Information Gain measures the reduction in entropy\nafter splitting on a feature. Higher is better!", font_size=26
        ).next_to(ig_formula, DOWN, buff=0.25)
        self.play(FadeIn(ig_explain))
        self.wait(1.6)
        self.play(FadeOut(ig_title), FadeOut(ig_formula), FadeOut(ig_explain))

        # Gini Impurity explanation
        gini_title = Text("Gini Impurity", font_size=32, color=ORANGE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(gini_title))
        gini_formula = MathTex(r"Gini(S) = 1 - \sum p_i^2", font_size=36).next_to(gini_title, DOWN, buff=0.3)
        self.play(FadeIn(gini_formula))
        self.wait(0.8)
        gini_explain = Text(
            "Gini Impurity also measures impurity.\n0 = pure, higher = more mixed.", font_size=26
        ).next_to(gini_formula, DOWN, buff=0.25)
        self.play(FadeIn(gini_explain))
        self.wait(1.6)
        self.play(FadeOut(gini_title), FadeOut(gini_formula), FadeOut(gini_explain))

        # Calculation Example for Motivation split
        calc_title = Text("Example: Splitting on Motivation", font_size=32, color=BLUE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(calc_title))
        # Show split
        split_text = Text("Split data into Motivation = High and Motivation = Low", font_size=28).next_to(calc_title, DOWN, buff=0.3)
        self.play(FadeIn(split_text))
        self.wait(0.7)
        # Counts
        high_group = Text("High: 4 Yes, 0 No", font_size=26, color=GREEN).next_to(split_text, DOWN, buff=0.2)
        low_group = Text("Low: 0 Yes, 4 No", font_size=26, color=RED).next_to(high_group, DOWN, buff=0.15)
        self.play(FadeIn(high_group), FadeIn(low_group))
        self.wait(0.8)
        # Entropy for each group
        high_entropy = MathTex(r"H_{high} = -1\log_2 1 = 0", font_size=30).next_to(low_group, DOWN, buff=0.2)
        low_entropy = MathTex(r"H_{low} = -1\log_2 1 = 0", font_size=30).next_to(high_entropy, DOWN, buff=0.15)
        self.play(FadeIn(high_entropy), FadeIn(low_entropy))
        self.wait(0.8)
        # Weighted avg entropy
        weighted = MathTex(r"H_{split} = 0", font_size=30).next_to(low_entropy, DOWN, buff=0.15)
        self.play(FadeIn(weighted))
        self.wait(0.8)
        # Info gain
        ig_calc = MathTex(r"IG = H_{root} - H_{split} = 1 - 0 = 1", font_size=30, color=GREEN).next_to(weighted, DOWN, buff=0.15)
        self.play(FadeIn(ig_calc))
        self.wait(1.5)
        self.play(FadeOut(calc_title), FadeOut(split_text), FadeOut(high_group), FadeOut(low_group),
                  FadeOut(high_entropy), FadeOut(low_entropy), FadeOut(weighted), FadeOut(ig_calc))

        # Calculation Example for Energy split
        calc_title2 = Text("Example: Splitting on Energy", font_size=32, color=BLUE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(calc_title2))
        split_text2 = Text("Split data into Energy = High and Energy = Low", font_size=28).next_to(calc_title2, DOWN, buff=0.3)
        self.play(FadeIn(split_text2))
        self.wait(0.7)
        # Counts
        high_group2 = Text("High: 2 Yes, 2 No", font_size=26, color=YELLOW).next_to(split_text2, DOWN, buff=0.2)
        low_group2 = Text("Low: 2 Yes, 2 No", font_size=26, color=YELLOW).next_to(high_group2, DOWN, buff=0.15)
        self.play(FadeIn(high_group2), FadeIn(low_group2))
        self.wait(0.8)
        # Entropy for each group
        high_entropy2 = MathTex(r"H_{high} = -0.5\log_2 0.5 - 0.5\log_2 0.5 = 1", font_size=30).next_to(low_group2, DOWN, buff=0.2)
        low_entropy2 = MathTex(r"H_{low} = -0.5\log_2 0.5 - 0.5\log_2 0.5 = 1", font_size=30).next_to(high_entropy2, DOWN, buff=0.15)
        self.play(FadeIn(high_entropy2), FadeIn(low_entropy2))
        self.wait(0.8)
        # Weighted avg entropy
        weighted2 = MathTex(r"H_{split} = 1", font_size=30).next_to(low_entropy2, DOWN, buff=0.15)
        self.play(FadeIn(weighted2))
        self.wait(0.8)
        # Info gain
        ig_calc2 = MathTex(r"IG = H_{root} - H_{split} = 1 - 1 = 0", font_size=30, color=RED).next_to(weighted2, DOWN, buff=0.15)
        self.play(FadeIn(ig_calc2))
        self.wait(1.5)
        self.play(FadeOut(calc_title2), FadeOut(split_text2), FadeOut(high_group2), FadeOut(low_group2),
                  FadeOut(high_entropy2), FadeOut(low_entropy2), FadeOut(weighted2), FadeOut(ig_calc2))

        # Summary
        summary = VGroup(
            Text("Entropy, Info Gain, Gini help choose the best split!", font_size=32, color=GREEN),
            Text("Entropy: impurity measure", font_size=28),
            Text("Info Gain: reduction in impurity", font_size=28),
            Text("Gini: alternative impurity measure", font_size=28),
            Text("Choose the split with highest Info Gain or lowest Gini!", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(title, DOWN, buff=0.7)
        self.play(FadeIn(summary))
        self.wait(2.5)
        self.play(FadeOut(summary), FadeOut(title))
        self.wait(0.5)
