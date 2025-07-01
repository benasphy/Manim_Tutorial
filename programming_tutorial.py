from manim import *

class ProgrammingTutorial(Scene):
    def construct(self):
        # Scene 1: What is Programming?
        self.scene_what_is_programming()
        self.clear()

        # Scene 2: Why Programming Matters
        self.scene_why_matters()
        self.clear()

        # Scene 3: Programming Languages
        self.scene_programming_languages()
        self.clear()

        # Scene 4: How Languages Differ
        self.scene_language_differences()
        self.clear()

        # Scene 5: Why You Should Care
        self.scene_why_learn()
        self.clear()

        # Scene 6: Quick Recap
        self.scene_recap()
        self.clear()

    def scene_what_is_programming(self):
        title = Text("What is Programming?", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        narration = VGroup(
            Text("Writing instructions that tell a computer what to do", font_size=26, color=WHITE),
            Text("Like giving a chef a recipe step by step", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.8)
        self.play(Write(narration))

        # Chef vs Computer comparison
        chef_side = self._badge("Chef", self._icon_chef(), TEAL_E)
        code_side = self._badge("Computer", self._icon_computer(), PURPLE_E)
        row = VGroup(chef_side, code_side).arrange(RIGHT, buff=1.5).next_to(narration, DOWN, buff=0.8)
        self.play(FadeIn(row, shift=UP))

        # Recipe steps appearing
        recipe = VGroup(
            Text("1. Mix flour and eggs", font_size=20, color=WHITE),
            Text("2. Add sugar and milk", font_size=20, color=WHITE),
            Text("3. Bake at 180°C", font_size=20, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(chef_side, DOWN, buff=0.6)
        
        code = VGroup(
            Text("def make_pancakes():", font_size=20, color=WHITE),
            Text("    mix(flour, eggs)", font_size=20, color=WHITE),
            Text("    add(sugar, milk)", font_size=20, color=WHITE),
            Text("    bake(temp=180)", font_size=20, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(code_side, DOWN, buff=0.6)

        self.play(Write(recipe), Write(code))
        self.wait(1.5)

    def scene_why_matters(self):
        title = Text("Why Programming Matters", font_size=48, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        narration = Text("It's behind almost everything in our modern world", font_size=26, color=WHITE).next_to(title, DOWN, buff=0.8)
        self.play(Write(narration))

        # Tech montage
        apps = self._badge("Apps", self._icon_phone(), BLUE_E)
        web = self._badge("Websites", self._icon_globe(), TEAL_E)
        iot = self._badge("IoT Devices", self._icon_iot(), YELLOW_E)
        row = VGroup(apps, web, iot).arrange(RIGHT, buff=0.8).next_to(narration, DOWN, buff=0.8)
        self.play(FadeIn(row, shift=UP))

        # Animated code brackets around the montage
        brace_top = ArcBetweenPoints(row.get_corner(UL) + UP*0.3, row.get_corner(UR) + UP*0.3, angle=-PI/2, color=WHITE)
        brace_bottom = ArcBetweenPoints(row.get_corner(DL) + DOWN*0.3, row.get_corner(DR) + DOWN*0.3, angle=PI/2, color=WHITE)
        self.play(Create(brace_top), Create(brace_bottom))
        
        tag = Text("All powered by code", font_size=24, color=YELLOW).next_to(brace_bottom, DOWN, buff=0.3)
        self.play(Write(tag))
        self.wait(1.5)

    def scene_programming_languages(self):
        title = Text("Programming Languages", font_size=48, color=TEAL_E)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        narration = VGroup(
            Text("Computers only understand binary (0s and 1s)", font_size=26, color=WHITE),
            Text("Programming languages bridge human thought and machine execution", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.8)
        self.play(Write(narration))

        # Human to machine flow
        human = self._badge("Human", self._icon_person(), BLUE_E)
        code = self._badge("Code", self._icon_code(), PURPLE_E)
        binary = self._badge("Machine Code", self._icon_binary(), GREEN_E)
        computer = self._badge("Computer", self._icon_server(), YELLOW_E)
        flow = VGroup(human, code, binary, computer).arrange(RIGHT, buff=0.6).next_to(narration, DOWN, buff=0.8)
        self.play(FadeIn(flow, shift=UP))

        # Arrows showing compilation/execution
        arrows = VGroup(
            Arrow(human.get_right(), code.get_left(), buff=0.2, color=WHITE),
            Arrow(code.get_right(), binary.get_left(), buff=0.2, color=WHITE),
            Arrow(binary.get_right(), computer.get_left(), buff=0.2, color=WHITE)
        )
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.2))
        self.wait(1.5)

    def scene_language_differences(self):
        title = Text("Programming Languages Differ", font_size=48, color=PURPLE_E)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Language cards
        python = self._language_card("Python", "Easy, flexible, great for beginners", BLUE_E)
        java = self._language_card("Java", "Stable, secure, runs everywhere", RED_E)
        c = self._language_card("C", "Fast, powerful, close to hardware", TEAL_E)
        js = self._language_card("JavaScript", "Interactive web pages", YELLOW_E)
        
        grid = VGroup(
            VGroup(python, java).arrange(RIGHT, buff=0.6),
            VGroup(c, js).arrange(RIGHT, buff=0.6)
        ).arrange(DOWN, buff=0.6).next_to(title, DOWN, buff=0.8)
        self.play(LaggedStart(*[FadeIn(card, shift=UP) for card in [python, java, c, js]], lag_ratio=0.15))

        # Language analogy
        analogy = Text("Like human languages—each fits certain situations better", font_size=24, color=YELLOW).next_to(grid, DOWN, buff=0.6)
        self.play(Write(analogy))
        self.wait(1.5)

    def scene_why_learn(self):
        title = Text("Why Learn Programming?", font_size=50, color=GOLD_E)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        benefits = VGroup(
            Text("• Problem-solving skills", font_size=26, color=WHITE),
            Text("• Logical thinking", font_size=26, color=WHITE),
            Text("• Creativity & innovation", font_size=26, color=WHITE),
            Text("• Understand the digital world", font_size=26, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.8)
        self.play(Write(benefits))

        # Journey visualization
        kid = self._icon_person().scale(0.6)
        dev = self._icon_person().scale(0.8)
        startup = self._icon_rocket().scale(0.8)
        journey = VGroup(kid, Arrow(RIGHT, LEFT), dev, Arrow(RIGHT, LEFT), startup).arrange(RIGHT, buff=0.4).next_to(benefits, DOWN, buff=0.8)
        self.play(Create(journey[1::2]))  # Arrows first
        self.play(FadeIn(kid, shift=RIGHT), FadeIn(dev, shift=UP), FadeIn(startup, shift=LEFT))
        
        labels = VGroup(
            Text("Start learning", font_size=20, color=WHITE).next_to(kid, DOWN, buff=0.2),
            Text("Become a developer", font_size=20, color=WHITE).next_to(dev, DOWN, buff=0.2),
            Text("Create something new", font_size=20, color=YELLOW).next_to(startup, DOWN, buff=0.2)
        )
        self.play(Write(labels))
        self.wait(1.5)

    def scene_recap(self):
        title = Text("Quick Recap", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        recap = VGroup(
            Text("Programming = giving instructions to computers", font_size=26, color=WHITE),
            Text("Powers nearly all modern technology", font_size=26, color=WHITE),
            Text("Many languages, each with different strengths", font_size=26, color=WHITE),
            Text("A valuable skill for the digital age", font_size=26, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(title, DOWN, buff=0.8)
        self.play(Write(recap))

        # Superpower badge
        badge = VGroup(
            Circle(radius=0.8, color=GOLD, stroke_width=8),
            Star(n=5, color=GOLD, fill_opacity=1).scale(0.5),
            Text("Digital\nSuperpower", font_size=24, color=BLACK).scale(0.9)
        ).arrange(DOWN, buff=0.2).next_to(recap, DOWN, buff=0.8)
        self.play(DrawBorderThenFill(badge[0]), FadeIn(badge[1:], shift=UP))
        self.wait(2)

    # --- Helpers ---
    def _badge(self, label: str, icon: Mobject, color=BLUE):
        chip = RoundedRectangle(width=3.0, height=1.2, corner_radius=0.15, color=color, fill_color=BLACK, fill_opacity=0.85)
        icon_group = icon.copy().scale(0.6).next_to(chip.get_left(), RIGHT, buff=0.3)
        text = Text(label, font_size=24, color=color).next_to(icon_group, RIGHT, buff=0.4)
        return VGroup(chip, icon_group, text)

    def _language_card(self, name: str, desc: str, color) -> VGroup:
        card = RoundedRectangle(width=4.0, height=2.0, corner_radius=0.12, color=color)
        title = Text(name, font_size=28, color=color).to_edge(UP, buff=0.3)
        desc_text = Text(desc, font_size=20, color=WHITE, line_spacing=1.2).scale(0.8).next_to(title, DOWN, buff=0.3)
        return VGroup(card, title, desc_text)

    def _icon_chef(self) -> VGroup:
        head = Circle(radius=0.2, color=WHITE)
        hat = Polygon(LEFT*0.3, RIGHT*0.3, RIGHT*0.2+UP*0.4, LEFT*0.2+UP*0.4, color=WHITE).next_to(head, UP, buff=-0.1)
        body = VGroup(
            Line(ORIGIN, DOWN*0.4, color=WHITE),
            Line(LEFT*0.2, RIGHT*0.2, color=WHITE).shift(DOWN*0.1),
            Line(LEFT*0.15, RIGHT*0.15, color=WHITE).shift(DOWN*0.2)
        ).next_to(head, DOWN, buff=0)
        return VGroup(hat, head, body)

    def _icon_computer(self) -> VGroup:
        screen = RoundedRectangle(width=0.8, height=0.5, corner_radius=0.06, color=WHITE)
        base = Rectangle(width=0.3, height=0.05, color=WHITE).next_to(screen, DOWN, buff=0)
        return VGroup(screen, base)

    def _icon_phone(self) -> VGroup:
        body = RoundedRectangle(width=0.4, height=0.7, corner_radius=0.08, color=WHITE)
        screen = RoundedRectangle(width=0.35, height=0.6, corner_radius=0.04, color=BLUE_E, fill_opacity=1).move_to(body.get_center())
        return VGroup(body, screen)

    def _icon_globe(self) -> VGroup:
        circle = Circle(radius=0.4, color=WHITE)
        grid = VGroup(
            Line(LEFT*0.4, RIGHT*0.4, color=WHITE),
            Line(UP*0.4, DOWN*0.4, color=WHITE),
            Arc(radius=0.4, start_angle=-PI/2, angle=PI, color=WHITE),
            Arc(radius=0.4, start_angle=PI/2, angle=PI, color=WHITE)
        )
        return VGroup(circle, grid)

    def _icon_iot(self) -> VGroup:
        base = RoundedRectangle(width=0.7, height=0.4, corner_radius=0.08, color=WHITE)
        wave = Arc(radius=0.3, start_angle=0, angle=PI, color=WHITE).next_to(base, UP, buff=0.1)
        return VGroup(base, wave)

    def _icon_person(self) -> VGroup:
        head = Circle(radius=0.15, color=WHITE)
        body = Line(ORIGIN, DOWN*0.4, color=WHITE)
        arms = VGroup(Line(LEFT*0.2, RIGHT*0.2, color=WHITE).shift(DOWN*0.1))
        legs = VGroup(Line(LEFT*0.1, RIGHT*0.1, color=WHITE).shift(DOWN*0.4))
        return VGroup(head, body, arms, legs)

    def _icon_code(self) -> VGroup:
        lines = VGroup(
            Text("def hello():", font_size=16, color=WHITE, font="Monospace"),
            Text("    print(\"Hi!\")", font_size=16, color=WHITE, font="Monospace").next_to(ORIGIN, DOWN, aligned_edge=LEFT, buff=0.2)
        )
        return lines

    def _icon_binary(self) -> VGroup:
        bits = VGroup(*[Text(bit, font_size=20, color=WHITE) for bit in ["0","1","0","1","1","0"]]).arrange(RIGHT, buff=0.1)
        return bits

    def _icon_server(self) -> VGroup:
        base = RoundedRectangle(width=0.6, height=0.4, corner_radius=0.06, color=WHITE)
        lights = VGroup(*[Dot(radius=0.03, color=GREEN).shift(RIGHT*(i*0.15-0.2) + DOWN*0.1) for i in range(3)])
        return VGroup(base, lights)

    def _icon_rocket(self) -> VGroup:
        body = VGroup(
            Rectangle(width=0.4, height=0.8, color=WHITE),
            Polygon(LEFT*0.2, RIGHT*0.2, UP*0.4, color=WHITE).shift(UP*0.4),
            Polygon(LEFT*0.2, RIGHT*0.2, DOWN*0.2, color=RED).shift(DOWN*0.4)
        )
        flames = VGroup(
            Line(ORIGIN, DOWN*0.3, color=YELLOW).shift(DOWN*0.4+LEFT*0.05),
            Line(ORIGIN, DOWN*0.4, color=YELLOW).shift(DOWN*0.4+LEFT*0.0),
            Line(ORIGIN, DOWN*0.3, color=YELLOW).shift(DOWN*0.4+RIGHT*0.05)
        )
        return VGroup(body, flames)
