from manim import *

class ExplainMachineLearningScene(Scene):
    def construct(self):
        # Title
        title = Text("What is Machine Learning?", font_size=56, color=YELLOW)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Arthur Samuel definition and fact
        as_def = Text(
            '“Machine Learning is the field of study that gives computers\nthe ability to learn without being explicitly programmed.”',
            font_size=32,
            color=WHITE,
            line_spacing=1.2
        )
        as_author = Text("- Arthur Samuel (1959)", font_size=28, color=BLUE_E).next_to(as_def, DOWN)
        as_fact = Text("Arthur Samuel coined the term 'machine learning' in 1959.", font_size=26, color=YELLOW).next_to(as_author, DOWN, buff=0.3)
        as_group = VGroup(as_def, as_author, as_fact).next_to(title, DOWN, buff=0.7)
        self.play(FadeIn(as_group))
        self.wait(3)
        self.play(FadeOut(as_group))

        # Tom Mitchell definition
        tm_def = Text(
            'Tom Mitchell (1997):\n“A computer program is said to learn from experience E,\nwith respect to some task T and performance measure P,\nif its performance at task T, as measured by P, improves with experience E.”',
            font_size=30,
            color=WHITE,
            line_spacing=1.2
        )
        tm_group = VGroup(tm_def).next_to(title, DOWN, buff=0.7)
        self.play(FadeIn(tm_group))
        self.wait(4)
        self.play(FadeOut(tm_group))

        # Visual: Computer + Data + Learning
        # Computer
        computer_screen = Rectangle(width=1.6, height=1, color=GREEN_E, fill_opacity=0.2)
        computer_base = Rectangle(width=1, height=0.2, color=GREEN_E, fill_opacity=0.4).next_to(computer_screen, DOWN, buff=0.05)
        computer_group = VGroup(computer_screen, computer_base).move_to(LEFT*2)
        computer_label = Text("Computer", font_size=28).next_to(computer_group, DOWN)
        computer_group = VGroup(computer_group, computer_label)

        # Data: stack of rectangles
        data_rects = VGroup(
            Rectangle(width=1.2, height=0.3, color=GREY, fill_opacity=0.3),
            Rectangle(width=1.2, height=0.3, color=GREY, fill_opacity=0.5).shift(DOWN*0.35),
            Rectangle(width=1.2, height=0.3, color=GREY, fill_opacity=0.7).shift(DOWN*0.7),
        ).move_to(RIGHT*2)
        data_label = Text("Data", font_size=28).next_to(data_rects, DOWN)
        data_group = VGroup(data_rects, data_label)

        # Show computer and data
        self.play(FadeIn(computer_group), FadeIn(data_group))
        self.wait(1)

        # Arrow from data to computer
        data_to_comp = Arrow(data_rects.get_left(), computer_screen.get_right(), buff=0.2, color=YELLOW)
        self.play(GrowArrow(data_to_comp))
        self.wait(1)

        # Learning process (gears between arrow)
        gear1 = Arc(radius=0.25, start_angle=0, angle=2*PI, color=BLUE).move_to(ORIGIN + UP*0.3)
        gear2 = Arc(radius=0.18, start_angle=0, angle=2*PI, color=BLUE).move_to(ORIGIN + DOWN*0.3)
        gears = VGroup(gear1, gear2)
        self.play(FadeIn(gears))
        self.wait(1)
        self.play(gears.animate.rotate(PI/2), run_time=1)
        self.wait(0.5)
        self.play(FadeOut(gears), FadeOut(data_to_comp))

        # Output: "Learning!"
        learning_text = Text("Learning!", font_size=38, color=YELLOW).move_to(ORIGIN)
        self.play(Write(learning_text))
        self.wait(1.5)
        self.play(FadeOut(learning_text))

        # Example: Spam filter
        email_icon = Rectangle(width=0.9, height=0.6, color=ORANGE, fill_opacity=0.3).move_to(LEFT*2 + DOWN*1.2)
        email_label = Text("Email", font_size=24).next_to(email_icon, DOWN, buff=0.1)
        spam_label = Text("Spam?", font_size=28, color=RED).move_to(RIGHT*2 + DOWN*1.2)
        self.play(FadeIn(email_icon), FadeIn(email_label), FadeIn(spam_label))
        self.wait(1)
        filter_arrow = Arrow(email_icon.get_right(), spam_label.get_left(), buff=0.2, color=YELLOW)
        self.play(GrowArrow(filter_arrow))
        self.wait(1)
        self.play(FadeOut(email_icon), FadeOut(email_label), FadeOut(spam_label), FadeOut(filter_arrow))

        # Summary
        summary = Text(
            "Machine Learning = Computers that learn from data!",
            font_size=36,
            color=YELLOW
        ).next_to(computer_group, DOWN, buff=1.5).shift(RIGHT*1.5)
        self.play(Write(summary))
        self.wait(2)
        self.play(FadeOut(summary), FadeOut(computer_group), FadeOut(data_group))

        thanks = Text("Thanks for Watching!", font_size=44, color=BLUE_E)
        self.play(Write(thanks))
        self.wait(2)
