from manim import *

class IoTTutorial(Scene):
    def construct(self):
        # Scene: How IoT Works
        self.scene_how_iot_works()
        self.clear()

        # Scene: Benefits of IoT
        self.scene_benefits()
        self.clear()

        # Scene: Challenges of IoT
        self.scene_challenges()
        self.clear()

        # Scene: Quick Recap
        self.scene_quick_recap()
        self.clear()

    def scene_how_iot_works(self):
        title = Text("How IoT Works", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("Sensors & Devices: collect data (temp, heart rate, location)", font_size=26, color=WHITE),
            Text("Internet Connection: Wi‑Fi, Bluetooth, or mobile networks", font_size=26, color=WHITE),
            Text("Cloud & Apps: store/analyze data, send instructions back", font_size=26, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        example = Text(
            "Example: Thermostat senses heat → sends to cloud → app tells it to cool",
            font_size=24, color=WHITE
        ).next_to(bullets, DOWN, buff=0.6)
        self.play(Write(example))

        # Flowchart: sensor → internet → cloud → action
        sensor = self._badge("Sensor", self._icon_sensor(), TEAL_E)
        net = self._badge("Internet", self._icon_wifi(), BLUE_E)
        cloud = self._badge("Cloud", self._icon_cloud(), PURPLE_E)
        action = self._badge("Action", self._icon_ac(), GREEN_E)
        chain = VGroup(sensor, net, cloud, action).arrange(RIGHT, buff=0.8).next_to(example, DOWN, buff=0.8)
        arrows = VGroup(*[Arrow(chain[i].get_right(), chain[i+1].get_left(), buff=0.2, color=WHITE) for i in range(3)])
        self.play(FadeIn(chain, shift=UP))
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15))
        self.wait(1.5)

    def scene_benefits(self):
        title = Text("Benefits of IoT", font_size=48, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("Convenience: control from anywhere", font_size=26, color=WHITE),
            Text("Efficiency: save time, energy, money", font_size=26, color=WHITE),
            Text("Safety & Health: better monitoring", font_size=26, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        # Visual: happy family controlling home devices from phone
        phone = self._badge("App", self._icon_phone(), YELLOW_E)
        devices = VGroup(self._badge("Lights", self._icon_bulb(), TEAL_E), self._badge("Thermostat", self._icon_ac(), BLUE_E), self._badge("Camera", self._icon_cam(), PURPLE_E)).arrange(RIGHT, buff=0.6)
        row = VGroup(phone, devices).arrange(DOWN, buff=0.6).next_to(bullets, DOWN, buff=0.8)
        self.play(FadeIn(row, shift=UP))
        self.wait(1.5)

    def scene_challenges(self):
        title = Text("Challenges of IoT", font_size=48, color=MAROON_E)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("Privacy risks: lots of personal data", font_size=26, color=WHITE),
            Text("Security issues: hackers target devices", font_size=26, color=WHITE),
            Text("Compatibility: not all devices align", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        # Visual: hacker vs smart home with shield
        hacker = self._badge("Intruder", self._icon_hacker(), GRAY)
        home = self._badge("Smart Home", self._icon_home(), TEAL_E)
        shield = self._icon_shield().scale(0.8).next_to(home, RIGHT, buff=0.2)
        row = VGroup(hacker, home, shield).arrange(RIGHT, buff=0.6).next_to(bullets, DOWN, buff=0.8)
        self.play(FadeIn(row, shift=UP))
        self.wait(1.5)

    def scene_quick_recap(self):
        title = Text("Quick Recap", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        items = VGroup(
            self._badge("Connects devices", self._icon_wifi(), TEAL_E),
            self._badge("Smart homes", self._icon_home(), GREEN_E),
            self._badge("Wearables", self._icon_watch(), YELLOW_E),
            self._badge("Cars", self._icon_car(), PURPLE_E),
            self._badge("Security matters", self._icon_shield(), MAROON_E)
        ).arrange(RIGHT, buff=0.6).next_to(title, DOWN, buff=0.8)
        self.play(FadeIn(items, shift=UP))
        self.wait(2)

    # Helpers
    def _badge(self, label: str, icon: Mobject, color=BLUE):
        chip = RoundedRectangle(width=3.2, height=1.2, corner_radius=0.15, color=color, fill_color=BLACK, fill_opacity=0.85)
        icon_group = icon.copy().scale(0.6).next_to(chip.get_left(), RIGHT, buff=0.3)
        text = Text(label, font_size=24, color=color).next_to(icon_group, RIGHT, buff=0.4)
        return VGroup(chip, icon_group, text)

    def _icon_sensor(self) -> VGroup:
        gauge = VGroup(Circle(radius=0.25, color=WHITE), Line(ORIGIN, UP*0.2, color=WHITE).rotate(-PI/6))
        return gauge

    def _icon_wifi(self) -> VGroup:
        base = Dot(radius=0.06, color=WHITE)
        a1 = ArcBetweenPoints(LEFT*0.3, RIGHT*0.3, angle=PI/2, color=WHITE).shift(UP*0.2)
        a2 = ArcBetweenPoints(LEFT*0.5, RIGHT*0.5, angle=PI/2, color=WHITE).shift(UP*0.4)
        return VGroup(base, a1, a2)

    def _icon_cloud(self) -> VGroup:
        puffs = VGroup(Circle(radius=0.25, color=WHITE), Circle(radius=0.3, color=WHITE), Circle(radius=0.22, color=WHITE))
        puffs.arrange(RIGHT, buff=-0.1)
        return puffs

    def _icon_ac(self) -> VGroup:
        fan = VGroup(Circle(radius=0.22, color=WHITE), *[Line(ORIGIN, UP*0.22, color=WHITE).rotate(i*PI/3) for i in range(6)])
        return fan

    def _icon_phone(self) -> VGroup:
        body = RoundedRectangle(width=0.6, height=1.2, corner_radius=0.12, color=WHITE)
        cam = Dot(radius=0.04, color=WHITE).next_to(body, UP, buff=-0.1)
        return VGroup(body, cam)

    def _icon_bulb(self) -> VGroup:
        bulb = VGroup(Circle(radius=0.22, color=WHITE), Rectangle(width=0.16, height=0.2, color=WHITE).next_to(ORIGIN, DOWN, buff=0))
        return bulb

    def _icon_cam(self) -> VGroup:
        body = RoundedRectangle(width=0.6, height=0.35, corner_radius=0.06, color=WHITE)
        lens = Circle(radius=0.08, color=WHITE).move_to(body.get_center())
        return VGroup(body, lens)

    def _icon_hacker(self) -> VGroup:
        hood = ArcBetweenPoints(LEFT*0.4, RIGHT*0.4, angle=PI/1.2, color=WHITE)
        face = Rectangle(width=0.4, height=0.2, color=WHITE).shift(DOWN*0.2)
        return VGroup(hood, face)

    def _icon_home(self) -> VGroup:
        roof = Polygon(LEFT*0.4+UP*0.2, ORIGIN+UP*0.6, RIGHT*0.4+UP*0.2, color=WHITE)
        base = Rectangle(width=0.8, height=0.4, color=WHITE)
        return VGroup(roof, base)

    def _icon_shield(self) -> VGroup:
        outer = ArcBetweenPoints(LEFT*0.6, RIGHT*0.6, angle=PI/1.4, color=WHITE)
        inner = Polygon(LEFT*0.6, RIGHT*0.6, DOWN*0.7, color=WHITE)
        return VGroup(outer, inner)

    def _icon_watch(self) -> VGroup:
        dial = Circle(radius=0.18, color=WHITE)
        band = VGroup(Rectangle(width=0.18, height=0.35, color=WHITE), Rectangle(width=0.18, height=0.35, color=WHITE)).arrange(DOWN, buff=0.1)
        band.move_to(dial.get_center())
        return VGroup(dial, band)

    def _icon_car(self) -> VGroup:
        body = RoundedRectangle(width=1.0, height=0.3, corner_radius=0.1, color=WHITE)
        wheels = VGroup(Circle(radius=0.1, color=WHITE).next_to(body, DOWN, buff=0), Circle(radius=0.1, color=WHITE).next_to(body, DOWN, buff=0).shift(RIGHT*0.5))
        return VGroup(body, wheels)
