from manim import *

class ExplainAIScene(Scene):
    def construct(self):
        # Title
        title = Text("What is AI?", font_size=60, color=YELLOW)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Human brain: use a circle with wavy lines
        brain_circle = Circle(radius=1, color=BLUE_E, fill_opacity=0.2)
        brain_waves = VGroup(
            Arc(radius=0.9, start_angle=0, angle=PI/2, color=BLUE_E),
            Arc(radius=0.8, start_angle=PI/2, angle=PI/2, color=BLUE_E),
            Arc(radius=0.7, start_angle=PI, angle=PI/2, color=BLUE_E),
            Arc(radius=0.6, start_angle=3*PI/2, angle=PI/2, color=BLUE_E),
        )
        brain_group = VGroup(brain_circle, brain_waves)
        brain_label = Text("Human Brain", font_size=32).next_to(brain_group, DOWN)
        brain_group = VGroup(brain_group, brain_label).to_edge(LEFT)

        # Computer: use a rectangle and a small square for the screen and base
        computer_screen = Rectangle(width=1.6, height=1, color=GREEN_E, fill_opacity=0.2)
        computer_base = Rectangle(width=1, height=0.2, color=GREEN_E, fill_opacity=0.4).next_to(computer_screen, DOWN, buff=0.05)
        computer_group = VGroup(computer_screen, computer_base)
        computer_label = Text("Computer", font_size=32).next_to(computer_group, DOWN)
        computer_group = VGroup(computer_group, computer_label).to_edge(RIGHT)

        # Show both
        self.play(FadeIn(brain_group), FadeIn(computer_group))
        self.wait(1)

        # Arrow and text: AI connects them
        arrow = Arrow(brain_group[0].get_right(), computer_group[0].get_left(), buff=0.3, color=WHITE)
        ai_text = Text("AI", font_size=40, color=YELLOW).next_to(arrow, UP)
        self.play(GrowArrow(arrow), FadeIn(ai_text))
        self.wait(1)

        # Explanation text
        explain = Text(
            "AI = Computers that can learn,\nreason, and solve problems\nlike humans!",
            font_size=34,
        ).next_to(title, DOWN, buff=1.5)
        self.play(Write(explain))
        self.wait(2)

        # Example: Cat vs Dog (using shapes and text)
        self.play(FadeOut(explain))
        # Cat: orange circle with ears
        cat_face = Circle(radius=0.5, color=ORANGE, fill_opacity=0.4)
        cat_ear1 = Triangle().scale(0.2).set_color(ORANGE).move_to(cat_face.get_top() + LEFT*0.2)
        cat_ear2 = Triangle().scale(0.2).set_color(ORANGE).move_to(cat_face.get_top() + RIGHT*0.2)
        cat_group = VGroup(cat_face, cat_ear1, cat_ear2)
        cat_label = Text("Cat", font_size=28).next_to(cat_group, DOWN, buff=0.1)
        cat_group = VGroup(cat_group, cat_label)
        cat_group.next_to(brain_group, DOWN, buff=1.1).shift(RIGHT*1.5 + UP*0.8)
        # Dog: grey rectangle with ears
        dog_face = RoundedRectangle(width=1, height=0.7, corner_radius=0.25, color=GREY, fill_opacity=0.4)
        dog_ear1 = Rectangle(width=0.2, height=0.3, color=GREY, fill_opacity=0.7).move_to(dog_face.get_top() + LEFT*0.35 + UP*0.15)
        dog_ear2 = Rectangle(width=0.2, height=0.3, color=GREY, fill_opacity=0.7).move_to(dog_face.get_top() + RIGHT*0.35 + UP*0.15)
        dog_group = VGroup(dog_face, dog_ear1, dog_ear2)
        dog_label = Text("Dog", font_size=28).next_to(dog_group, DOWN, buff=0.1)
        dog_group = VGroup(dog_group, dog_label)
        dog_group.next_to(computer_group, DOWN, buff=1.1).shift(LEFT*1.5 + UP*0.8)
        example_text = Text("AI can tell a cat from a dog!", font_size=34).next_to(title, DOWN, buff=1.5)
        self.play(FadeIn(cat_group), FadeIn(dog_group), Write(example_text))
        self.wait(2)

        # Arrows from cat/dog to computer
        cat_arrow = Arrow(cat_group[0].get_top(), computer_group[0].get_bottom(), buff=0.2, color=ORANGE)
        dog_arrow = Arrow(dog_group[0].get_top(), computer_group[0].get_bottom(), buff=0.2, color=GREY)
        self.play(GrowArrow(cat_arrow), GrowArrow(dog_arrow))
        self.wait(1)

        # Summary
        self.play(FadeOut(cat_group), FadeOut(dog_group), FadeOut(cat_arrow), FadeOut(dog_arrow), FadeOut(example_text))
        summary = Text(
            "AI = Computer Intelligence\nthat helps us in daily life!",
            font_size=38,
            color=YELLOW
        ).move_to(ORIGIN)
        self.play(Write(summary))
        self.wait(2)

        # End
        self.play(FadeOut(summary), FadeOut(brain_group), FadeOut(computer_group), FadeOut(arrow), FadeOut(ai_text), FadeOut(title))
        thanks = Text("Thanks for Watching!", font_size=44, color=BLUE_E)
        self.play(Write(thanks))
        self.wait(2)
