from manim import *

class DatabasesTutorial(Scene):
    def construct(self):
        # Scene 1: What is a Database?
        self.scene_what_is_database()
        self.clear()

        # Scene 2: Big Data (3 Vs)
        self.scene_big_data()
        self.clear()

    def scene_what_is_database(self):
        title = Text("What is a Database?", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        narration = VGroup(
            Text("An organized collection of data for easy access, management, and updates", font_size=26, color=WHITE),
            Text("Structured storage makes searching and organizing fast", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.8)
        self.play(Write(narration))

        # Visual: card catalog vs modern dashboard
        card_catalog = self._badge("Card Catalog", self._icon_drawers(), TEAL_E)
        dashboard = self._badge("DB Dashboard", self._icon_dashboard(), PURPLE_E)
        row = VGroup(card_catalog, dashboard).arrange(RIGHT, buff=1.2).next_to(narration, DOWN, buff=0.8)
        self.play(FadeIn(row, shift=UP))

        analogy = Text("Think of a database as a smart digital filing cabinet", font_size=24, color=YELLOW).next_to(row, DOWN, buff=0.6)
        self.play(Write(analogy))
        self.wait(1.5)

    def scene_big_data(self):
        title = Text("Big Data", font_size=50, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        narration = VGroup(
            Text("Data so large and complex that traditional DBs struggle", font_size=26, color=WHITE),
            Text("Sources: social media, video, transactions, GPS, sensors", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.8)
        self.play(Write(narration))

        # 3 Vs
        vs = VGroup(
            self._badge("Volume", self._icon_db_stack(), BLUE_E),
            self._badge("Velocity", self._icon_speed(), YELLOW_E),
            self._badge("Variety", self._icon_variety(), TEAL_E)
        ).arrange(RIGHT, buff=0.8).next_to(narration, DOWN, buff=0.6)
        self.play(FadeIn(vs, shift=UP))

        # Visual: wave of data (phones, sensors, cameras) -> servers -> cloud
        phone = self._badge("Phones", self._icon_phone(), GRAY)
        sensor = self._badge("Sensors", self._icon_sensor(), GRAY)
        camera = self._badge("Cameras", self._icon_cam(), GRAY)
        sources = VGroup(phone, sensor, camera).arrange(RIGHT, buff=0.6)

        servers = VGroup(*[self._icon_server() for _ in range(3)]).arrange(RIGHT, buff=0.4)
        cloud = self._badge("Cloud", self._icon_cloud(), PURPLE_E)

        flow = VGroup(sources, servers, cloud).arrange(DOWN, buff=0.8).next_to(vs, DOWN, buff=0.8)
        self.play(FadeIn(flow, shift=UP))

        arrows = VGroup(
            Arrow(sources.get_bottom(), servers.get_top(), buff=0.2, color=WHITE),
            Arrow(servers.get_bottom(), cloud.get_top(), buff=0.2, color=WHITE)
        )
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.2))

        tools = VGroup(
            self._badge("Hadoop", self._icon_elephant(), BLUE_E),
            self._badge("Spark", self._icon_star(), YELLOW_E),
            self._badge("GCP / AWS / Azure", self._icon_cloud(), TEAL_E)
        ).arrange(RIGHT, buff=0.8).next_to(flow, DOWN, buff=0.8)
        self.play(FadeIn(tools, shift=UP))
        self.wait(2)

    # --- Helpers ---
    def _badge(self, label: str, icon: Mobject, color=BLUE):
        chip = RoundedRectangle(width=3.4, height=1.2, corner_radius=0.15, color=color, fill_color=BLACK, fill_opacity=0.85)
        icon_group = icon.copy().scale(0.55).next_to(chip.get_left(), RIGHT, buff=0.3)
        text = Text(label, font_size=24, color=color).next_to(icon_group, RIGHT, buff=0.4)
        return VGroup(chip, icon_group, text)

    def _icon_drawers(self) -> VGroup:
        box = RoundedRectangle(width=1.2, height=1.0, corner_radius=0.06, color=WHITE)
        drawers = VGroup(
            Rectangle(width=1.0, height=0.28, color=WHITE).shift(UP*0.3),
            Rectangle(width=1.0, height=0.28, color=WHITE),
            Rectangle(width=1.0, height=0.28, color=WHITE).shift(DOWN*0.3)
        )
        handles = VGroup(*[Dot(radius=0.03, color=WHITE).move_to(d) for d in drawers])
        drawers.move_to(box.get_center())
        return VGroup(box, drawers, handles)

    def _icon_dashboard(self) -> VGroup:
        panel = RoundedRectangle(width=1.6, height=1.0, corner_radius=0.08, color=WHITE)
        chart = VGroup(Line(LEFT*0.5, RIGHT*0.5, color=WHITE).shift(DOWN*0.2), Line(LEFT*0.2, UP*0.2, color=WHITE)).move_to(panel.get_center())
        bars = VGroup(*[Rectangle(width=0.1, height=0.2 + i*0.08, color=WHITE) for i in range(4)]).arrange(RIGHT, buff=0.06).shift(DOWN*0.1)
        bars.move_to(panel.get_center()+DOWN*0.2)
        return VGroup(panel, chart, bars)

    def _icon_db_stack(self) -> VGroup:
        top = ArcBetweenPoints(LEFT*0.35, RIGHT*0.35, angle=PI/2, color=WHITE)
        mid = Rectangle(width=0.7, height=0.18, color=WHITE).next_to(top, DOWN, buff=0)
        base = ArcBetweenPoints(RIGHT*0.35, LEFT*0.35, angle=PI/2, color=WHITE).next_to(mid, DOWN, buff=0)
        stack = VGroup(top, mid, base)
        stack2 = stack.copy().shift(DOWN*0.25)
        stack3 = stack.copy().shift(DOWN*0.5)
        return VGroup(stack, stack2, stack3)

    def _icon_speed(self) -> VGroup:
        dial = Circle(radius=0.22, color=WHITE)
        needle = Line(ORIGIN, UP*0.2, color=WHITE).rotate(-PI/6)
        return VGroup(dial, needle)

    def _icon_variety(self) -> VGroup:
        a = Square(0.18, color=WHITE)
        b = Circle(radius=0.1, color=WHITE)
        c = Triangle(color=WHITE).scale(0.18)
        return VGroup(a, b, c).arrange(RIGHT, buff=0.12)

    def _icon_phone(self) -> VGroup:
        body = RoundedRectangle(width=0.5, height=0.9, corner_radius=0.1, color=WHITE)
        cam = Dot(radius=0.04, color=WHITE).next_to(body, UP, buff=-0.1)
        return VGroup(body, cam)

    def _icon_sensor(self) -> VGroup:
        gauge = VGroup(Circle(radius=0.22, color=WHITE), Line(ORIGIN, UP*0.18, color=WHITE).rotate(-PI/6))
        return gauge

    def _icon_cam(self) -> VGroup:
        body = RoundedRectangle(width=0.6, height=0.35, corner_radius=0.06, color=WHITE)
        lens = Circle(radius=0.08, color=WHITE).move_to(body.get_center())
        return VGroup(body, lens)

    def _icon_server(self) -> VGroup:
        rack = VGroup(
            RoundedRectangle(width=0.8, height=1.2, corner_radius=0.06, color=WHITE),
            Line(LEFT*0.25, RIGHT*0.25, color=WHITE).shift(UP*0.25),
            Line(LEFT*0.25, RIGHT*0.25, color=WHITE),
            Line(LEFT*0.25, RIGHT*0.25, color=WHITE).shift(DOWN*0.25)
        )
        leds = VGroup(*[Dot(radius=0.03, color=GREEN).shift(DOWN*0.4 + RIGHT*(i*0.08 - 0.2)) for i in range(5)])
        return VGroup(rack, leds)

    def _icon_cloud(self) -> VGroup:
        puffs = VGroup(Circle(radius=0.25, color=WHITE), Circle(radius=0.3, color=WHITE), Circle(radius=0.22, color=WHITE))
        puffs.arrange(RIGHT, buff=-0.1)
        return puffs

    def _icon_elephant(self) -> VGroup:
        # Abstract elephant silhouette for Hadoop
        body = Ellipse(width=0.5, height=0.3, color=WHITE)
        head = Circle(radius=0.12, color=WHITE).next_to(body, LEFT, buff=-0.05)
        trunk = Line(ORIGIN, DOWN*0.18, color=WHITE).next_to(head, DOWN, buff=0)
        ear = Circle(radius=0.06, color=WHITE).next_to(head, UP, buff=-0.05)
        return VGroup(body, head, trunk, ear)

    def _icon_star(self) -> VGroup:
        rays = VGroup(*[Line(ORIGIN, RIGHT*0.22, color=WHITE).rotate(i*PI/5) for i in range(10)])
        return rays
