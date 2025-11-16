from manim import *

class SoftwareLicensesTutorial(Scene):
    def construct(self):
        # Scene 1: What is Open Source Software?
        self.scene_open_source()
        self.clear()

        # Scene 2: What is Proprietary Software?
        self.scene_proprietary()
        self.clear()

        # Scene 3: Key Differences
        self.scene_comparison()
        self.clear()

    def scene_open_source(self):
        title = Text("Open Source Software", font_size=50, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        definition = VGroup(
            Text("Source code is open and available for anyone to:", font_size=26, color=WHITE),
            Text("• View • Modify • Share", font_size=26, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=0.8)
        self.play(Write(definition))

        # Examples
        examples = VGroup(
            Text("Examples:", font_size=24, color=WHITE, weight=BOLD),
            Text("• Linux (OS)\n• Firefox (Browser)\n• Python (Language)", 
                font_size=22, color=WHITE, line_spacing=1.2)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(definition, DOWN, buff=0.8)
        self.play(Write(examples))

        # Visual: People collaborating
        people = VGroup(*[self._icon_person() for _ in range(3)]).arrange(RIGHT, buff=0.6)
        code = self._icon_code().scale(0.8)
        
        # Animate code being passed
        group = VGroup(people, code).arrange(DOWN, buff=0.8).next_to(examples, DOWN, buff=0.8)
        self.play(FadeIn(people), FadeIn(code))
        
        # Animate code being passed around
        for i in range(3):
            self.play(code.animate.next_to(people[i], DOWN, buff=0.2), run_time=0.7)
            self.play(Rotate(code, angle=0.2), run_time=0.3)
        
        analogy = Text("Like sharing a recipe—everyone can use and improve it", font_size=24, color=TEAL)
        analogy.next_to(group, DOWN, buff=0.6)
        self.play(Write(analogy))
        self.wait(1.5)

    def scene_proprietary(self):
        title = Text("Proprietary Software", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        definition = VGroup(
            Text("Owned by a company - source code is hidden:", font_size=26, color=WHITE),
            Text("• Can use it\n• Can't see how it works\n• Can't modify it", 
                font_size=24, color=WHITE, line_spacing=1.2)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=0.8)
        self.play(Write(definition))

        # Examples
        examples = VGroup(
            Text("Examples:", font_size=24, color=WHITE, weight=BOLD),
            Text("• Windows (Microsoft)\n• macOS (Apple)\n• Microsoft Office", 
                font_size=22, color=WHITE, line_spacing=1.2)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(definition, DOWN, buff=0.8)
        self.play(Write(examples))

        # Visual: Locked box
        box = RoundedRectangle(width=2.5, height=2.0, corner_radius=0.15, color=RED)
        lock = self._icon_lock().scale(1.5)
        software = Text("Software", font_size=24, color=WHITE).next_to(box, DOWN, buff=0.3)
        
        group = VGroup(box, lock, software).next_to(examples, DOWN, buff=1.0)
        self.play(Create(box), FadeIn(lock), Write(software))
        
        # Shake animation for locked state
        self.play(
            box.animate.shift(LEFT*0.1),
            lock.animate.shift(LEFT*0.1),
            rate_func=there_and_back,
            run_time=0.5
        )
        
        analogy = Text("Like buying a cake—you can eat it but not see the recipe", font_size=24, color=TEAL)
        analogy.next_to(group, DOWN, buff=0.6)
        self.play(Write(analogy))
        self.wait(1.5)

    def scene_comparison(self):
        title = Text("Open Source vs Proprietary", font_size=50, color=PURPLE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Split screen comparison
        divider = Line(UP*4, DOWN*4, color=WHITE)
        self.play(Create(divider))

        # Open Source side
        os_title = Text("Open Source", font_size=32, color=GREEN).to_edge(UP).shift(LEFT*2.5)
        os_points = VGroup(
            Text("✓ Free to use", font_size=24, color=WHITE, t2c={"✓": GREEN}),
            Text("✓ Customizable", font_size=24, color=WHITE, t2c={"✓": GREEN}),
            Text("✓ Community-driven", font_size=24, color=WHITE, t2c={"✓": GREEN}),
            Text("• May need technical skills", font_size=20, color=GRAY)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(os_title, DOWN, buff=0.6).shift(LEFT*0.5)

        # Proprietary side
        ps_title = Text("Proprietary", font_size=32, color=BLUE).to_edge(UP).shift(RIGHT*2.5)
        ps_points = VGroup(
            Text("✓ Polished & user-friendly", font_size=24, color=WHITE, t2c={"✓": BLUE}),
            Text("✓ Professional support", font_size=24, color=WHITE, t2c={"✓": BLUE}),
            Text("✓ Integrated ecosystem", font_size=24, color=WHITE, t2c={"✓": BLUE}),
            Text("• Less flexible/customizable", font_size=20, color=GRAY)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(ps_title, DOWN, buff=0.6).shift(LEFT*0.5)

        # Animate titles and points
        self.play(Write(os_title), Write(ps_title))
        self.play(Write(os_points), Write(ps_points))

        # Visuals
        community = VGroup(
            self._icon_person(),
            self._icon_person().shift(RIGHT*0.8 + UP*0.2),
            self._icon_person().shift(LEFT*0.8 + UP*0.2)
        ).scale(0.7).next_to(os_points, DOWN, buff=0.8)
        
        company = self._icon_building().scale(1.2).next_to(ps_points, DOWN, buff=0.8)
        
        self.play(FadeIn(community), FadeIn(company))
        
        # Connection lines
        connections = VGroup(
            Arrow(community.get_bottom() + DOWN*0.5, company.get_bottom() + DOWN*0.5, 
                  color=YELLOW, buff=0.2, stroke_width=3),
            Text("Choose based on needs and skills", font_size=24, color=YELLOW)
                .next_to(divider, DOWN, buff=1.0)
        )
        
        self.play(Create(connections[0]), Write(connections[1]))
        self.wait(2)

    # Helper methods for creating UI elements
    def _icon_person(self):
        head = Circle(radius=0.3, color=WHITE, fill_opacity=1)
        body = Line(ORIGIN, DOWN*0.6, color=WHITE)
        arms = Line(LEFT*0.3, RIGHT*0.3, color=WHITE).shift(DOWN*0.2)
        legs = VGroup(
            Line(ORIGIN, LEFT*0.2+DOWN*0.3, color=WHITE).shift(DOWN*0.6),
            Line(ORIGIN, RIGHT*0.2+DOWN*0.3, color=WHITE).shift(DOWN*0.6)
        )
        return VGroup(head, body, arms, legs)

    def _icon_code(self):
        lines = VGroup(
            Text("def hello():", font_size=16, font="Monospace"),
            Text("    print(\"Hello, world!\")", font_size=16, font="Monospace").next_to(ORIGIN, DOWN, aligned_edge=LEFT, buff=0.2)
        )
        return lines

    def _icon_lock(self):
        body = RoundedRectangle(width=0.6, height=0.8, corner_radius=0.1, color=WHITE)
        shackle = Arc(radius=0.3, start_angle=0, angle=PI, color=WHITE).next_to(body, UP, buff=0)
        return VGroup(shackle, body)

    def _icon_building(self):
        base = Rectangle(width=1.5, height=1.0, color=WHITE)
        roof = Polygon(LEFT*0.9, UP*0.5, RIGHT*0.9, color=WHITE).next_to(base, UP, buff=0)
        windows = VGroup(*[
            Square(0.2, color=WHITE, fill_opacity=0.5, fill_color=YELLOW).shift(LEFT*0.4 + UP*0.2 + RIGHT*(i*0.4) + DOWN*0.2)
            for i in range(3)
        ])
        door = Rectangle(width=0.3, height=0.5, color=WHITE, fill_opacity=0.5, fill_color=GRAY).next_to(base, DOWN, buff=0)
        return VGroup(roof, base, windows, door)
