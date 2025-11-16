from manim import *

class RoboticsDrones3DPrintingTutorial(Scene):
    def construct(self):
        # Scene: How They Connect Together
        self.scene_connect_together()
        self.clear()

        # Scene: Benefits
        self.scene_benefits()
        self.clear()

        # Scene: Challenges
        self.scene_challenges()
        self.clear()

        # Scene: Quick Recap
        self.scene_quick_recap()
        self.clear()

    def scene_connect_together(self):
        title = Text("How They Connect Together", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("Robots built with 3D-printed parts", font_size=26, color=WHITE),
            Text("Drones scan land and send data to 3D printers", font_size=26, color=WHITE),
            Text("Medical robots using 3D-printed tools", font_size=26, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        # Visual: drone scanning → computer model → 3D printer builds structure
        drone = self._badge("Drone", self._icon_drone(), TEAL_E)
        model = self._badge("3D Model", self._icon_cad(), PURPLE_E)
        printer = self._badge("3D Printer", self._icon_printer3d(), GREEN_E)
        flow = VGroup(drone, model, printer).arrange(RIGHT, buff=0.8).next_to(bullets, DOWN, buff=0.8)
        arrows = VGroup(
            Arrow(drone.get_right(), model.get_left(), buff=0.2, color=WHITE),
            Arrow(model.get_right(), printer.get_left(), buff=0.2, color=WHITE)
        )
        self.play(FadeIn(flow, shift=UP))
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.2))
        self.wait(1.5)

    def scene_benefits(self):
        title = Text("Benefits", font_size=48, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("Faster production and delivery", font_size=26, color=WHITE),
            Text("Lower costs", font_size=26, color=WHITE),
            Text("Increased safety in dangerous jobs", font_size=26, color=WHITE),
            Text("Creative freedom to design anything", font_size=26, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        collage = VGroup(
            self._badge("Robotics", self._icon_robot_arm(), BLUE_E),
            self._badge("Drones", self._icon_drone(), TEAL_E),
            self._badge("3D Print", self._icon_printer3d(), PURPLE_E)
        ).arrange(RIGHT, buff=0.8).next_to(bullets, DOWN, buff=0.8)
        self.play(FadeIn(collage, shift=UP))
        self.wait(1.5)

    def scene_challenges(self):
        title = Text("Challenges", font_size=48, color=MAROON_E)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("High costs of advanced robots and drones", font_size=26, color=WHITE),
            Text("Privacy concerns with drone video", font_size=26, color=WHITE),
            Text("Limited materials and speed for 3D printing", font_size=26, color=WHITE),
            Text("Job replacement fears", font_size=26, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        icons = VGroup(
            self._badge("Cost", self._icon_money(), GRAY),
            self._badge("Privacy", self._icon_lock(), TEAL_E),
            self._badge("Materials", self._icon_cube(), BLUE_E),
            self._badge("Jobs", self._icon_people(), YELLOW_E)
        ).arrange(RIGHT, buff=0.6).next_to(bullets, DOWN, buff=0.8)
        self.play(FadeIn(icons, shift=UP))
        self.wait(1.5)

    def scene_quick_recap(self):
        title = Text("Quick Recap", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        items = VGroup(
            self._badge("Robotics", self._icon_robot_arm(), TEAL_E),
            self._badge("Drones", self._icon_drone(), GREEN_E),
            self._badge("3D Printing", self._icon_printer3d(), PURPLE_E),
            self._badge("Impact", self._icon_globe(), YELLOW_E)
        ).arrange(RIGHT, buff=0.7).next_to(title, DOWN, buff=0.8)
        self.play(FadeIn(items, shift=UP))

        summary = Text(
            "Robotics: automatic machines; Drones: flying robots; 3D Printing: make objects layer by layer.\n"
            "Together, they're transforming industries and daily life.",
            font_size=24, color=WHITE, line_spacing=1.0
        ).next_to(items, DOWN, buff=0.6)
        self.play(Write(summary))
        self.wait(2)

    # Helpers
    def _badge(self, label: str, icon: Mobject, color=BLUE):
        chip = RoundedRectangle(width=3.2, height=1.2, corner_radius=0.15, color=color, fill_color=BLACK, fill_opacity=0.85)
        icon_group = icon.copy().scale(0.6).next_to(chip.get_left(), RIGHT, buff=0.3)
        text = Text(label, font_size=24, color=color).next_to(icon_group, RIGHT, buff=0.4)
        return VGroup(chip, icon_group, text)

    def _icon_drone(self) -> VGroup:
        body = RoundedRectangle(width=0.7, height=0.25, corner_radius=0.1, color=WHITE)
        props = VGroup(*[Circle(radius=0.12, color=WHITE).shift(UP*0.25+LEFT*0.35), Circle(radius=0.12, color=WHITE).shift(UP*0.25+RIGHT*0.35), Circle(radius=0.12, color=WHITE).shift(DOWN*0.25+LEFT*0.35), Circle(radius=0.12, color=WHITE).shift(DOWN*0.25+RIGHT*0.35)])
        return VGroup(body, props)

    def _icon_cad(self) -> VGroup:
        cube = VGroup(Square(0.3, color=WHITE), Line(ORIGIN, RIGHT*0.2, color=WHITE), Line(ORIGIN, UP*0.2, color=WHITE))
        return cube

    def _icon_printer3d(self) -> VGroup:
        frame = RoundedRectangle(width=0.9, height=0.9, corner_radius=0.06, color=WHITE)
        nozzle = VGroup(Line(ORIGIN, DOWN*0.2, color=WHITE), Triangle(color=WHITE).scale(0.08).next_to(ORIGIN, DOWN, buff=0)).move_to(frame.get_top()).shift(DOWN*0.2)
        bed = Rectangle(width=0.6, height=0.06, color=WHITE).next_to(frame, DOWN, buff=0.15)
        return VGroup(frame, nozzle, bed)

    def _icon_robot_arm(self) -> VGroup:
        base = Rectangle(width=0.3, height=0.1, color=WHITE)
        arm1 = Line(ORIGIN, RIGHT*0.4, color=WHITE)
        arm2 = Line(ORIGIN, RIGHT*0.3, color=WHITE).shift(RIGHT*0.4)
        claw = VGroup(Line(ORIGIN, UP*0.12, color=WHITE), Line(ORIGIN, DOWN*0.12, color=WHITE)).shift(RIGHT*0.7)
        return VGroup(base, arm1, arm2, claw)

    def _icon_money(self) -> VGroup:
        bill = RoundedRectangle(width=0.6, height=0.3, corner_radius=0.06, color=WHITE)
        circle = Circle(radius=0.06, color=WHITE).move_to(bill.get_center())
        return VGroup(bill, circle)

    def _icon_lock(self) -> VGroup:
        lock = VGroup(
            RoundedRectangle(width=0.7, height=0.7, corner_radius=0.12, color=WHITE),
            ArcBetweenPoints(LEFT*0.25, RIGHT*0.25, angle=PI/1.2, color=WHITE).shift(UP*0.5),
            Dot(radius=0.05, color=WHITE)
        )
        return lock

    def _icon_cube(self) -> VGroup:
        sq = Square(0.25, color=WHITE)
        axes = VGroup(Line(ORIGIN, RIGHT*0.15, color=WHITE), Line(ORIGIN, UP*0.15, color=WHITE))
        return VGroup(sq, axes)

    def _icon_people(self) -> VGroup:
        head = Circle(radius=0.08, color=WHITE)
        body = Line(ORIGIN, DOWN*0.2, color=WHITE)
        return VGroup(head, body)

    def _icon_globe(self) -> VGroup:
        globe = Circle(radius=0.35, color=WHITE)
        lat = VGroup(Line(LEFT*0.3, RIGHT*0.3, color=WHITE).shift(UP*0.15), Line(LEFT*0.3, RIGHT*0.3, color=WHITE), Line(LEFT*0.3, RIGHT*0.3, color=WHITE).shift(DOWN*0.15))
        lon = VGroup(Arc(radius=0.35, start_angle=-PI/2, angle=PI, color=WHITE), Arc(radius=0.35, start_angle=PI/2, angle=PI, color=WHITE))
        return VGroup(globe, lat, lon)
