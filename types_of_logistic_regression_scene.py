from manim import *

class TypesOfLogisticRegression(Scene):
    def construct(self):
        # Title
        title = Text("Types of Logistic Regression", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Intro
        intro = Text(
            "Logistic Regression isn't just a one-size-fits-all model.\nThere are three main types, each for a different kind of prediction.",
            font_size=32
        )
        self.play(Write(intro))
        self.wait(2)
        self.play(FadeOut(intro))

        # 1. Binary Logistic Regression
        binary_title = Text("1. Binary Logistic Regression", font_size=36, color=YELLOW)
        binary_desc = Text(
            "Most common: Only two outcomes\n(yes/no, 1/0, true/false)", font_size=28
        ).next_to(binary_title, DOWN, buff=0.3)
        binary_examples = VGroup(
            Text("Will the customer churn? ✔️ or ❌", font_size=26),
            Text("Does the patient have diabetes? ✅ or ❎", font_size=26),
            Text("Will the loan be paid back? 💰 or 🚫", font_size=26)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(binary_desc, DOWN, buff=0.3)
        binary_outcome = Text(
            'Model: "There’s a 72% chance the answer is YES."', font_size=26, color=WHITE
        ).next_to(binary_examples, DOWN, buff=0.3)
        self.play(Write(binary_title))
        self.play(FadeIn(binary_desc))
        self.play(FadeIn(binary_examples))
        self.play(FadeIn(binary_outcome))
        self.wait(2)
        self.play(FadeOut(binary_title), FadeOut(binary_desc), FadeOut(binary_examples), FadeOut(binary_outcome))

        # 2. Multinomial Logistic Regression
        multi_title = Text("2. Multinomial Logistic Regression", font_size=36, color=GREEN)
        multi_desc = Text(
            "More than two outcomes, no order among them.", font_size=28
        ).next_to(multi_title, DOWN, buff=0.3)
        multi_examples = VGroup(
            Text("What type of product will a customer buy? 🧼 🧴 📦", font_size=26),
            Text("Which political party will someone vote for? 🟦 🟥 🟩", font_size=26),
            Text("What star rating will a customer give? ⭐️⭐️⭐️⭐️⭐️", font_size=26)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(multi_desc, DOWN, buff=0.3)
        multi_outcome = Text(
            "Model predicts probabilities for each category — picks the highest.", font_size=26
        ).next_to(multi_examples, DOWN, buff=0.3)
        self.play(Write(multi_title))
        self.play(FadeIn(multi_desc))
        self.play(FadeIn(multi_examples))
        self.play(FadeIn(multi_outcome))
        self.wait(2)
        self.play(FadeOut(multi_title), FadeOut(multi_desc), FadeOut(multi_examples), FadeOut(multi_outcome))

        # 3. Ordinal Logistic Regression
        ordinal_title = Text("3. Ordinal Logistic Regression", font_size=36, color=ORANGE)
        ordinal_desc = Text(
            "Outcomes have a natural order, but are still categories.", font_size=28
        ).next_to(ordinal_title, DOWN, buff=0.3)
        ordinal_examples = VGroup(
            Text("Level of customer satisfaction: 😠 😐 🙂 😄", font_size=26),
            Text("Severity of a disease: mild → moderate → severe", font_size=26),
            Text("Cancer stage: Stage I → II → III → IV", font_size=26)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(ordinal_desc, DOWN, buff=0.3)
        ordinal_outcome = Text(
            "Model predicts class and respects the ranking.", font_size=26
        ).next_to(ordinal_examples, DOWN, buff=0.3)
        self.play(Write(ordinal_title))
        self.play(FadeIn(ordinal_desc))
        self.play(FadeIn(ordinal_examples))
        self.play(FadeIn(ordinal_outcome))
        self.wait(2)
        self.play(FadeOut(ordinal_title), FadeOut(ordinal_desc), FadeOut(ordinal_examples), FadeOut(ordinal_outcome))

        # Recap
        recap = VGroup(
            Text("Recap:", font_size=34, color=BLUE),
            Text("✅ Binary: 2 outcomes — yes or no", font_size=28, color=YELLOW),
            Text("🎯 Multinomial: 3+ outcomes — no order", font_size=28, color=GREEN),
            Text("📈 Ordinal: 3+ outcomes — with a clear order", font_size=28, color=ORANGE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        recap.move_to(ORIGIN)
        self.play(FadeIn(recap))
        self.wait(2)
        outro = Text(
            "So next time you hear 'logistic regression',\nremember — it’s a family of models!",
            font_size=32, color=WHITE
        ).next_to(recap, DOWN, buff=0.7)
        self.play(Write(outro))
        self.wait(2)
        self.play(FadeOut(recap), FadeOut(outro), FadeOut(title))
