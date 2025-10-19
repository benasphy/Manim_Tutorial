from manim import *

class ExplainTypesOfMLScene(Scene):
    def construct(self):
        # Title
        title = Text("Types of Machine Learning", font_size=56, color=YELLOW)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # List the types
        types = [
            ("Supervised Learning", BLUE_E),
            ("Unsupervised Learning", GREEN_E),
            ("Reinforcement Learning", ORANGE),
            ("Ensemble Learning", PURPLE)
        ]
        type_texts = [Text(t[0], font_size=38, color=t[1]) for t in types]
        types_group = VGroup(*type_texts).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(title, DOWN, buff=0.7)
        self.play(FadeIn(types_group))
        self.wait(2)
        self.play(FadeOut(types_group))

        # Supervised Learning
        sup_title = Text("Supervised Learning", font_size=44, color=BLUE_E).next_to(title, DOWN, buff=0.4)
        sup_def = Text("Learn from labeled data (input-output pairs)", font_size=32).next_to(sup_title, DOWN)
        sup_vis = VGroup(
            Square(0.7, color=BLUE_E, fill_opacity=0.2).shift(LEFT*2),
            Arrow(LEFT*1.3, RIGHT*1.3, buff=0.1, color=YELLOW),
            Square(0.7, color=GREEN_E, fill_opacity=0.2).shift(RIGHT*2)
        )
        sup_labels = VGroup(
            Text("Input\n(Data)", font_size=24).next_to(sup_vis[0], DOWN, buff=0.2),
            Text("Output\n(Label)", font_size=24).next_to(sup_vis[2], DOWN, buff=0.2)
        )
        sup_example = Text("E.g. Email Spam Detection", font_size=28, color=GREY).next_to(sup_vis, DOWN, buff=1)
        self.play(FadeIn(sup_title))
        self.wait(0.5)
        self.play(FadeIn(sup_def))
        self.wait(0.5)
        self.play(FadeIn(sup_vis), FadeIn(sup_labels))
        self.wait(0.5)
        self.play(Write(sup_example))
        self.wait(2)
        self.play(*[FadeOut(m) for m in [sup_title, sup_def, sup_vis, sup_labels, sup_example]])

        # Unsupervised Learning
        unsup_title = Text("Unsupervised Learning", font_size=44, color=GREEN_E).next_to(title, DOWN, buff=0.4)
        unsup_def = Text("Learn from unlabeled data (find patterns)", font_size=32).next_to(unsup_title, DOWN)
        # Visual: scattered dots grouped by color
        dots = VGroup(
            *[Dot(LEFT*2+UP*0.5+RIGHT*0.3*i, color=BLUE_E) for i in range(3)],
            *[Dot(RIGHT*2+DOWN*0.5+LEFT*0.3*i, color=GREEN_E) for i in range(3)],
            *[Dot(UP*1.5+RIGHT*0.5*i, color=ORANGE) for i in range(2)]
        )
        unsup_example = Text("E.g. Customer Segmentation", font_size=28, color=GREY).next_to(dots, DOWN, buff=1)
        self.play(FadeIn(unsup_title))
        self.wait(0.5)
        self.play(FadeIn(unsup_def))
        self.wait(0.5)
        self.play(FadeIn(dots))
        self.wait(0.5)
        self.play(Write(unsup_example))
        self.wait(2)
        self.play(*[FadeOut(m) for m in [unsup_title, unsup_def, dots, unsup_example]])

        # Reinforcement Learning
        rl_title = Text("Reinforcement Learning", font_size=44, color=ORANGE).next_to(title, DOWN, buff=0.4)
        rl_def = Text("Learn by trial and error (rewards & penalties)", font_size=32).next_to(rl_title, DOWN)
        # Visual: agent, environment, reward arrow
        agent = Circle(radius=0.5, color=ORANGE, fill_opacity=0.3).shift(LEFT*2)
        env = Square(1, color=BLUE_E, fill_opacity=0.2).shift(RIGHT*2)
        agent_label = Text("Agent", font_size=24).next_to(agent, DOWN)
        env_label = Text("Environment", font_size=24).next_to(env, DOWN)
        action_arrow = Arrow(agent.get_right(), env.get_left(), color=YELLOW)
        reward_arrow = Arrow(env.get_top(), agent.get_top(), color=GREEN_E).add_tip()
        reward_label = Text("Reward", font_size=22, color=GREEN_E).next_to(reward_arrow, UP, buff=0.2)
        rl_example = Text("E.g. Game Playing AI", font_size=28, color=GREY).next_to(env, DOWN, buff=1)
        self.play(FadeIn(rl_title))
        self.wait(0.5)
        self.play(FadeIn(rl_def))
        self.wait(0.5)
        self.play(FadeIn(agent), FadeIn(env), FadeIn(agent_label), FadeIn(env_label))
        self.play(GrowArrow(action_arrow))
        self.play(GrowArrow(reward_arrow), FadeIn(reward_label))
        self.wait(0.5)
        self.play(Write(rl_example))
        self.wait(2)
        self.play(*[FadeOut(m) for m in [rl_title, rl_def, agent, env, agent_label, env_label, action_arrow, reward_arrow, reward_label, rl_example]])

        # Ensemble Learning
        ens_title = Text("Ensemble Learning", font_size=44, color=PURPLE).next_to(title, DOWN, buff=0.4)
        ens_def = Text("Combine multiple models for better results", font_size=32).next_to(ens_title, DOWN)
        # Visual: three models (rectangles) -> one output
        model1 = Rectangle(width=0.7, height=0.5, color=PURPLE, fill_opacity=0.2).shift(LEFT*2+UP*0.5)
        model2 = Rectangle(width=0.7, height=0.5, color=PURPLE, fill_opacity=0.2).shift(ORIGIN)
        model3 = Rectangle(width=0.7, height=0.5, color=PURPLE, fill_opacity=0.2).shift(RIGHT*2+DOWN*0.5)
        output = Square(0.7, color=YELLOW, fill_opacity=0.2).shift(DOWN*1.5)
        arrows = VGroup(
            Arrow(model1.get_bottom(), output.get_left(), color=YELLOW),
            Arrow(model2.get_bottom(), output.get_bottom(), color=YELLOW),
            Arrow(model3.get_bottom(), output.get_right(), color=YELLOW)
        )
        ens_example = Text("E.g. Random Forest, Voting Classifier", font_size=28, color=GREY).next_to(output, DOWN, buff=1)
        self.play(FadeIn(ens_title))
        self.wait(0.5)
        self.play(FadeIn(ens_def))
        self.wait(0.5)
        self.play(FadeIn(model1), FadeIn(model2), FadeIn(model3), FadeIn(output))
        self.play(FadeIn(arrows))
        self.wait(0.5)
        self.play(Write(ens_example))
        self.wait(2)
        self.play(*[FadeOut(m) for m in [ens_title, ens_def, model1, model2, model3, output, arrows, ens_example]])

        # Summary
        summary = Text(
            "Supervised | Unsupervised | Reinforcement | Ensemble\nML adapts to many problems!",
            font_size=34,
            color=YELLOW
        ).move_to(DOWN*2.7)
        self.play(Write(summary))
        self.wait(2)
        self.play(FadeOut(summary), FadeOut(title))

        thanks = Text("Thanks for Watching!", font_size=44, color=BLUE_E)
        self.play(Write(thanks))
        self.wait(2)
