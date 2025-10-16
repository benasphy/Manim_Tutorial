from manim import *

class EnsembleMethodsExplanation(Scene):
    def construct(self):
        # Title
        title = Text("Ensemble Learning: Bagging, Boosting & Stacking", font_size=44, color=BLUE)
        self.play(FadeIn(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # What is Ensemble Learning?
        sec1 = Text("What is Ensemble Learning?", font_size=36, color=YELLOW).next_to(title, DOWN, buff=0.5)
        desc1 = Text("Combine multiple models to get better performance\nthan any single model alone!", font_size=28).next_to(sec1, DOWN, buff=0.2)
        self.play(FadeIn(sec1), FadeIn(desc1))
        self.wait(2)
        self.play(FadeOut(sec1), FadeOut(desc1))

        # Bagging
        sec2 = Text("Bagging (Bootstrap Aggregating)", font_size=34, color=GREEN).next_to(title, DOWN, buff=0.5)
        bagging_bl = BulletedList(
            "Train many models independently",
            "Each sees a random sample (with replacement)",
            "Aggregate predictions (vote/average)",
            "Reduces variance, helps with overfitting",
            "Famous: Random Forest",
            font_size=24
        ).next_to(sec2, DOWN, buff=0.2)
        self.play(FadeIn(sec2), FadeIn(bagging_bl))
        self.wait(2.2)
        # Bagging visual: dataset -> samples -> models -> voting
        data_rect = Rectangle(width=1.6, height=0.7, color=WHITE).shift(LEFT*4+UP*0.5)
        data_label = Text("Full Data", font_size=22).move_to(data_rect)
        bags = VGroup(*[Rectangle(width=1.3, height=0.5, color=GREY).shift(LEFT*2.5+i*UP*0.7) for i in range(-1,2)])
        bag_labels = VGroup(*[Text(f"Sample {i+1}", font_size=18).move_to(bags[i]) for i in range(3)])
        trees = VGroup(*[Rectangle(width=0.6, height=0.6, color=GREEN).shift(RIGHT*0.5+i*RIGHT*1.1) for i in range(3)])
        tree_labels = VGroup(*[Text(f"Model {i+1}", font_size=18).move_to(trees[i]) for i in range(3)])
        vote_circle = Circle(radius=0.4, color=YELLOW).shift(RIGHT*3)
        vote_label = Text("Vote/Average", font_size=18).move_to(vote_circle)
        self.play(FadeIn(data_rect), FadeIn(data_label))
        self.wait(0.5)
        self.play(*[FadeIn(bags[i]) for i in range(3)], *[FadeIn(bag_labels[i]) for i in range(3)])
        self.wait(0.4)
        self.play(*[FadeIn(trees[i]) for i in range(3)], *[FadeIn(tree_labels[i]) for i in range(3)])
        self.wait(0.4)
        self.play(FadeIn(vote_circle), FadeIn(vote_label))
        # Arrows
        self.play(*[Create(Arrow(data_rect.get_right(), bags[i].get_left(), buff=0.07, color=WHITE)) for i in range(3)])
        self.play(*[Create(Arrow(bags[i].get_right(), trees[i].get_left(), buff=0.07, color=WHITE)) for i in range(3)])
        self.play(*[Create(Arrow(trees[i].get_right(), vote_circle.get_left(), buff=0.07, color=WHITE)) for i in range(3)])
        self.wait(1.4)
        self.play(FadeOut(sec2), FadeOut(bagging_bl), FadeOut(data_rect), FadeOut(data_label), FadeOut(bags), FadeOut(bag_labels), FadeOut(trees), FadeOut(tree_labels), FadeOut(vote_circle), FadeOut(vote_label))

        # Boosting
        sec3 = Text("Boosting", font_size=34, color=ORANGE).next_to(title, DOWN, buff=0.5)
        boosting_bl = BulletedList(
            "Train models sequentially",
            "Each new model focuses on previous errors",
            "Combine weak learners into strong one",
            "Reduces bias, can overfit if not regularized",
            "Famous: AdaBoost, Gradient Boosting",
            font_size=24
        ).next_to(sec3, DOWN, buff=0.2)
        self.play(FadeIn(sec3), FadeIn(boosting_bl))
        self.wait(2.2)
        # Boosting visual: data -> model1 -> model2 -> model3 -> combine
        b_data = Rectangle(width=1.6, height=0.7, color=WHITE).shift(LEFT*4+UP*0.5)
        b_label = Text("Full Data", font_size=22).move_to(b_data)
        weak1 = Rectangle(width=0.7, height=0.7, color=ORANGE).shift(LEFT*2+UP*0.5)
        weak2 = Rectangle(width=0.7, height=0.7, color=ORANGE).shift(LEFT*0.5+UP*0.5)
        weak3 = Rectangle(width=0.7, height=0.7, color=ORANGE).shift(RIGHT*1+UP*0.5)
        comb = Circle(radius=0.4, color=YELLOW).shift(RIGHT*3)
        comb_label = Text("Combine", font_size=18).move_to(comb)
        self.play(FadeIn(b_data), FadeIn(b_label))
        self.wait(0.5)
        self.play(FadeIn(weak1))
        self.play(Create(Arrow(b_data.get_right(), weak1.get_left(), buff=0.07, color=WHITE)))
        self.wait(0.3)
        self.play(FadeIn(weak2))
        self.play(Create(Arrow(weak1.get_right(), weak2.get_left(), buff=0.07, color=WHITE)))
        self.wait(0.3)
        self.play(FadeIn(weak3))
        self.play(Create(Arrow(weak2.get_right(), weak3.get_left(), buff=0.07, color=WHITE)))
        self.wait(0.3)
        self.play(FadeIn(comb), FadeIn(comb_label))
        self.play(Create(Arrow(weak3.get_right(), comb.get_left(), buff=0.07, color=WHITE)))
        self.wait(1.4)
        self.play(FadeOut(sec3), FadeOut(boosting_bl), FadeOut(b_data), FadeOut(b_label), FadeOut(weak1), FadeOut(weak2), FadeOut(weak3), FadeOut(comb), FadeOut(comb_label))

        # Stacking
        sec4 = Text("Stacking", font_size=34, color=PURPLE).next_to(title, DOWN, buff=0.5)
        stacking_bl = BulletedList(
            "Train different types of models",
            "Combine their predictions using a meta-model",
            "Meta-model learns how to best blend base models",
            "Can capture complex patterns",
            "Famous: Stacked Generalization",
            font_size=24
        ).next_to(sec4, DOWN, buff=0.2)
        self.play(FadeIn(sec4), FadeIn(stacking_bl))
        self.wait(2.2)
        # Stacking visual: data -> multiple models (tree, svm, nn) -> meta-model
        s_data = Rectangle(width=1.6, height=0.7, color=WHITE).shift(LEFT*4+UP*0.5)
        s_label = Text("Full Data", font_size=22).move_to(s_data)
        base1 = Rectangle(width=0.7, height=0.7, color=GREEN).shift(LEFT*2+UP*1.2)
        base2 = Rectangle(width=0.7, height=0.7, color=ORANGE).shift(LEFT*2+DOWN*0.2)
        base3 = Rectangle(width=0.7, height=0.7, color=BLUE).shift(LEFT*2+DOWN*1.5)
        meta = Rectangle(width=1.2, height=0.7, color=PURPLE).shift(RIGHT*1+DOWN*0.2)
        meta_label = Text("Meta-Model", font_size=20).move_to(meta)
        self.play(FadeIn(s_data), FadeIn(s_label))
        self.wait(0.5)
        self.play(FadeIn(base1), FadeIn(base2), FadeIn(base3))
        self.play(Create(Arrow(s_data.get_right(), base1.get_left(), buff=0.07, color=WHITE)),
                  Create(Arrow(s_data.get_right(), base2.get_left(), buff=0.07, color=WHITE)),
                  Create(Arrow(s_data.get_right(), base3.get_left(), buff=0.07, color=WHITE)))
        self.wait(0.4)
        self.play(FadeIn(meta), FadeIn(meta_label))
        self.play(Create(Arrow(base1.get_right(), meta.get_left(), buff=0.07, color=WHITE)),
                  Create(Arrow(base2.get_right(), meta.get_left(), buff=0.07, color=WHITE)),
                  Create(Arrow(base3.get_right(), meta.get_left(), buff=0.07, color=WHITE)))
        self.wait(1.4)
        self.play(FadeOut(sec4), FadeOut(stacking_bl), FadeOut(s_data), FadeOut(s_label), FadeOut(base1), FadeOut(base2), FadeOut(base3), FadeOut(meta), FadeOut(meta_label))

        # Comparison Table
        sec5 = Text("Bagging vs Boosting vs Stacking", font_size=32, color=YELLOW).next_to(title, DOWN, buff=0.5)
        table_data = [
            ["Method", "How", "Goal", "Famous Example"],
            ["Bagging", "Parallel, random samples", "Reduce variance", "Random Forest"],
            ["Boosting", "Sequential, focus errors", "Reduce bias", "AdaBoost, XGBoost"],
            ["Stacking", "Different models, meta", "Blend strengths", "Stacked Gen."]
        ]
        table = Table(table_data, include_outer_lines=True, element_to_mobject_config={"font_size": 22})
        table.scale(0.9).next_to(sec5, DOWN, buff=0.3)
        self.play(FadeIn(sec5), FadeIn(table))
        self.wait(2.5)
        self.play(FadeOut(sec5), FadeOut(table))

        # Summary
        summary = BulletedList(
            "Bagging: Many models, vote/average, less variance",
            "Boosting: Sequential, focus errors, less bias",
            "Stacking: Combine different models, meta-learner",
            font_size=26
        ).next_to(title, DOWN, buff=0.7)
        self.play(FadeIn(summary))
        self.wait(2.5)
        self.play(FadeOut(summary), FadeOut(title))
