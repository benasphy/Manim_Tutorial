from manim import *

class EnsembleLearningExplained(Scene):
    def construct(self):
        # Scene 1: Opening Hook – Wisdom of the Crowd
        title = Text("Ensemble Learning: The Wisdom of the Crowd", font_size=44, color=BLUE)
        self.play(FadeIn(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        hook = Text("Imagine a quiz show...\nAsk the audience, average their answers,\nand you get closer to the truth!", font_size=32, color=WHITE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(hook))
        self.wait(2)
        self.play(FadeOut(hook))
        crowd = VGroup(*[Dot(LEFT*2 + DOWN*0.5 + i*RIGHT*0.6, color=GREY) for i in range(8)])
        answers = [0.7, 0.5, 0.8, 0.6, 0.5, 0.9, 0.4, 0.6]
        dots = VGroup(*[Dot(LEFT*2 + DOWN*1.2 + i*RIGHT*0.6, color=YELLOW).scale(answers[i]) for i in range(8)])
        avg_arrow = Arrow(LEFT*0.5 + DOWN*1.4, RIGHT*2 + DOWN*1.4, color=YELLOW)
        avg_label = Text("Average = Better!", font_size=28, color=YELLOW).next_to(avg_arrow, DOWN)
        self.play(FadeIn(crowd), FadeIn(dots))
        self.play(Create(avg_arrow), FadeIn(avg_label))
        self.wait(1.5)
        self.play(FadeOut(crowd), FadeOut(dots), FadeOut(avg_arrow), FadeOut(avg_label))

        # Scene 2: What is Ensemble Learning?
        sec2 = Text("What is Ensemble Learning?", font_size=38, color=YELLOW).next_to(title, DOWN, buff=0.4)
        expl2 = Text("Combine multiple weak learners\nto form a strong learner!\nLike democracy in ML.", font_size=30).next_to(sec2, DOWN, buff=0.2)
        types = BulletedList(
            "Bagging",
            "Boosting",
            "Stacking",
            font_size=30
        ).next_to(expl2, DOWN, buff=0.2)
        self.play(FadeIn(sec2), FadeIn(expl2), FadeIn(types))
        self.wait(2.5)
        self.play(FadeOut(sec2), FadeOut(expl2), FadeOut(types))

        # Scene 3: Bagging
        bag_title = Text("Bagging (Bootstrap Aggregating)", font_size=36, color=GREEN).next_to(title, DOWN, buff=0.4)
        bag_desc = Text("Train many models on bootstrapped samples\nAggregate their predictions.", font_size=28).next_to(bag_title, DOWN, buff=0.2)
        bag_steps = BulletedList(
            "Sample data with replacement",
            "Train a model on each sample",
            "Aggregate predictions (vote/avg)",
            font_size=26
        ).next_to(bag_desc, DOWN, buff=0.2)
        self.play(FadeIn(bag_title), FadeIn(bag_desc), FadeIn(bag_steps))
        self.wait(2.5)
        self.play(FadeOut(bag_title), FadeOut(bag_desc), FadeOut(bag_steps))
        # Bagging visual
        data_rect = Rectangle(width=2, height=1, color=WHITE).shift(LEFT*4)
        data_label = Text("Full Data", font_size=22).move_to(data_rect)
        bags = VGroup(*[Rectangle(width=1.2, height=0.6, color=GREY).shift(LEFT*1.5+i*UP*0.8) for i in range(-1,2)])
        bag_labels = VGroup(*[Text(f"Sample {i+1}", font_size=18).move_to(bags[i]) for i in range(3)])
        models = VGroup(*[Rectangle(width=0.7, height=0.7, color=GREEN).shift(RIGHT*0.5+i*RIGHT*1.2) for i in range(3)])
        model_labels = VGroup(*[Text(f"Model {i+1}", font_size=18).move_to(models[i]) for i in range(3)])
        agg = Circle(radius=0.45, color=YELLOW).shift(RIGHT*5)  # moved further right for no overlap
        agg_label = Text("Vote/Average", font_size=20).next_to(agg, DOWN, buff=0.15)
        self.play(FadeIn(data_rect), FadeIn(data_label))
        self.play(*[FadeIn(bags[i]) for i in range(3)], *[FadeIn(bag_labels[i]) for i in range(3)])
        self.play(*[FadeIn(models[i]) for i in range(3)], *[FadeIn(model_labels[i]) for i in range(3)])
        self.play(FadeIn(agg), FadeIn(agg_label))
        # Draw arrows (precise connections)
        arrows1 = VGroup(*[Arrow(data_rect.get_right(), bags[i].get_left(), buff=0.07, color=WHITE, stroke_width=4).set_z_index(1) for i in range(3)])
        arrows2 = VGroup(*[Arrow(bags[i].get_right(), models[i].get_left(), buff=0.07, color=WHITE, stroke_width=4).set_z_index(1) for i in range(3)])
        arrows3 = VGroup(*[Arrow(models[i].get_right(), agg.get_left(), buff=0.07, color=WHITE, stroke_width=4).set_z_index(1) for i in range(3)])
        # Animate arrows
        for arrow in arrows1:
            self.play(Create(arrow), run_time=0.25)
        for arrow in arrows2:
            self.play(Create(arrow), run_time=0.25)
        for arrow in arrows3:
            self.play(Create(arrow), run_time=0.25)
        self.wait(1.2)
        # Fade out all arrows and visuals
        self.play(FadeOut(data_rect), FadeOut(data_label), FadeOut(bags), FadeOut(bag_labels),
                  FadeOut(models), FadeOut(model_labels), FadeOut(agg), FadeOut(agg_label),
                  *[FadeOut(arrow) for arrow in arrows1],
                  *[FadeOut(arrow) for arrow in arrows2],
                  *[FadeOut(arrow) for arrow in arrows3])
        # Bagging why
        why_bag = Text("Bagging reduces variance!\nRandom Forest is the classic example.", font_size=28, color=GREEN).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(why_bag))
        self.wait(1.7)
        self.play(FadeOut(why_bag))

        # Scene 4: Boosting
        boost_title = Text("Boosting", font_size=36, color=ORANGE).next_to(title, DOWN, buff=0.4)
        boost_desc = Text("Train models sequentially,\neach focuses on previous errors.", font_size=28).next_to(boost_title, DOWN, buff=0.2)
        boost_steps = BulletedList(
            "Start with weak model",
            "Focus next on previous errors",
            "Combine with weighted voting",
            font_size=26
        ).next_to(boost_desc, DOWN, buff=0.2)
        self.play(FadeIn(boost_title), FadeIn(boost_desc), FadeIn(boost_steps))
        self.wait(2.5)
        self.play(FadeOut(boost_title), FadeOut(boost_desc), FadeOut(boost_steps))
        # Boosting visual
        b_data = Rectangle(width=2, height=1, color=WHITE).shift(LEFT*4)
        b_label = Text("Full Data", font_size=22).move_to(b_data)
        weak1 = Rectangle(width=0.8, height=0.8, color=ORANGE).shift(LEFT*2)
        weak2 = Rectangle(width=0.8, height=0.8, color=ORANGE).shift(LEFT*0.5)
        weak3 = Rectangle(width=0.8, height=0.8, color=ORANGE).shift(RIGHT*1)
        comb = Circle(radius=0.45, color=YELLOW).shift(RIGHT*3)
        comb_label = Text("Weighted Vote", font_size=20).move_to(comb)
        self.play(FadeIn(b_data), FadeIn(b_label))
        self.play(FadeIn(weak1))
        arrow_b1 = Arrow(b_data.get_right(), weak1.get_left(), buff=0.07, color=WHITE)
        self.play(Create(arrow_b1))
        self.play(FadeIn(weak2))
        arrow_b2 = Arrow(weak1.get_right(), weak2.get_left(), buff=0.07, color=WHITE)
        self.play(Create(arrow_b2))
        self.play(FadeIn(weak3))
        arrow_b3 = Arrow(weak2.get_right(), weak3.get_left(), buff=0.07, color=WHITE)
        self.play(Create(arrow_b3))
        self.play(FadeIn(comb), FadeIn(comb_label))
        arrow_b4 = Arrow(weak3.get_right(), comb.get_left(), buff=0.07, color=WHITE)
        self.play(Create(arrow_b4))
        self.wait(1.5)
        self.play(FadeOut(b_data), FadeOut(b_label), FadeOut(weak1), FadeOut(weak2), FadeOut(weak3), FadeOut(comb), FadeOut(comb_label), FadeOut(arrow_b1), FadeOut(arrow_b2), FadeOut(arrow_b3), FadeOut(arrow_b4))
        why_boost = Text("Boosting reduces bias!\nAdaBoost, XGBoost, LightGBM...", font_size=28, color=ORANGE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(why_boost))
        self.wait(1.7)
        self.play(FadeOut(why_boost))

        # Scene 5: Stacking
        stack_title = Text("Stacking", font_size=36, color=PURPLE).next_to(title, DOWN, buff=0.4)
        stack_desc = Text("Combine different models\nusing a meta-model.", font_size=28).next_to(stack_title, DOWN, buff=0.2)
        stack_steps = BulletedList(
            "Train diverse models (tree, SVM, NN)",
            "Meta-model learns to blend them",
            font_size=26
        ).next_to(stack_desc, DOWN, buff=0.2)
        self.play(FadeIn(stack_title), FadeIn(stack_desc), FadeIn(stack_steps))
        self.wait(2.5)
        self.play(FadeOut(stack_title), FadeOut(stack_desc), FadeOut(stack_steps))
        # Stacking visual
        s_data = Rectangle(width=2, height=1, color=WHITE).shift(LEFT*4)
        s_label = Text("Full Data", font_size=22).move_to(s_data)
        base1 = Rectangle(width=0.8, height=0.8, color=GREEN).shift(LEFT*2+UP*0.7)
        base2 = Rectangle(width=0.8, height=0.8, color=ORANGE).shift(LEFT*2+DOWN*0.7)
        base3 = Rectangle(width=0.8, height=0.8, color=BLUE).shift(LEFT*2)
        meta = Rectangle(width=1.3, height=0.8, color=PURPLE).shift(RIGHT*1)
        meta_label = Text("Meta-Model", font_size=20).move_to(meta)
        self.play(FadeIn(s_data), FadeIn(s_label))
        self.play(FadeIn(base1), FadeIn(base2), FadeIn(base3))
        arrow_s1 = Arrow(s_data.get_right(), base1.get_left(), buff=0.07, color=WHITE)
        arrow_s2 = Arrow(s_data.get_right(), base2.get_left(), buff=0.07, color=WHITE)
        arrow_s3 = Arrow(s_data.get_right(), base3.get_left(), buff=0.07, color=WHITE)
        self.play(Create(arrow_s1), Create(arrow_s2), Create(arrow_s3))
        self.play(FadeIn(meta), FadeIn(meta_label))
        arrow_s4 = Arrow(base1.get_right(), meta.get_left(), buff=0.07, color=WHITE)
        arrow_s5 = Arrow(base2.get_right(), meta.get_left(), buff=0.07, color=WHITE)
        arrow_s6 = Arrow(base3.get_right(), meta.get_left(), buff=0.07, color=WHITE)
        self.play(Create(arrow_s4), Create(arrow_s5), Create(arrow_s6))
        self.wait(1.5)
        self.play(FadeOut(s_data), FadeOut(s_label), FadeOut(base1), FadeOut(base2), FadeOut(base3), FadeOut(meta), FadeOut(meta_label), FadeOut(arrow_s1), FadeOut(arrow_s2), FadeOut(arrow_s3), FadeOut(arrow_s4), FadeOut(arrow_s5), FadeOut(arrow_s6))
        why_stack = Text("Stacking = model diversity!\nMeta-model learns best blend.", font_size=28, color=PURPLE).next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(why_stack))
        self.wait(1.7)
        self.play(FadeOut(why_stack))

        # Scene 6: Visual Comparison Table
        sec6 = Text("Bagging vs Boosting vs Stacking", font_size=34, color=YELLOW).next_to(title, DOWN, buff=0.4)
        table_data = [
            ["Technique", "Learners", "Training", "Goal", "Example"],
            ["Bagging", "Same type", "Parallel", "Reduce variance", "RandomForest"],
            ["Boosting", "Same type", "Sequential", "Reduce bias", "XGBoost"],
            ["Stacking", "Different types", "Parallel+Meta", "Mix strengths", "Any combo"]
        ]
        table = Table(table_data, include_outer_lines=True, element_to_mobject_config={"font_size": 22})
        table.scale(0.92).next_to(sec6, DOWN, buff=0.3)
        self.play(FadeIn(sec6), FadeIn(table))
        self.wait(2.5)
        self.play(FadeOut(sec6), FadeOut(table))

        # Scene 7: Advantages & Disadvantages
        sec7 = Text("Advantages & Disadvantages", font_size=34, color=BLUE).next_to(title, DOWN, buff=0.4)
        adv = BulletedList(
            "Improved performance and generalization",
            "Reduces bias (Boosting) or variance (Bagging)",
            "Often top in Kaggle competitions",
            font_size=24
        ).next_to(sec7, DOWN, buff=0.2)
        disadv = BulletedList(
            "Slower to train (esp. Boosting/Stacking)",
            "Can overfit if not tuned",
            "Less interpretable than single models",
            font_size=24
        ).next_to(adv, DOWN, buff=0.3)
        self.play(FadeIn(sec7), FadeIn(adv), FadeIn(disadv))
        self.wait(2.5)
        self.play(FadeOut(sec7), FadeOut(adv), FadeOut(disadv))

        # Scene 8: Summary
        summary = VGroup(
            Text("Bagging: Train many in parallel, combine.", font_size=28, color=GREEN),
            Text("Boosting: Train sequentially, correct mistakes.", font_size=28, color=ORANGE),
            Text("Stacking: Blend different models with meta-model.", font_size=28, color=PURPLE),
            Text("Ensemble = secret sauce for top ML!", font_size=28, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(summary))
        self.wait(3)
        self.play(FadeOut(summary), FadeOut(title))
