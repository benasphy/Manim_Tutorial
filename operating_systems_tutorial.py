from manim import *

class OperatingSystemsTutorial(Scene):
    def construct(self):
        # Scene 1: Core Functions of an OS
        self.core_functions_scene()
        self.clear()

        # Scene 2: Why Different Operating Systems?
        self.why_different_scene()
        self.clear()

        # Scene 3: The Future of Operating Systems
        self.future_scene()
        self.clear()

        # Scene 4: Closing
        self.closing_scene()
        self.clear()

    def core_functions_scene(self):
        title = Text("1. Core Functions of an OS", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        intro = Text(
            "To understand why an OS matters, let's break down its main jobs.",
            font_size=28, color=WHITE
        ).next_to(title, DOWN, buff=0.6)
        self.play(Write(intro))

        # Create cards for each function
        resource = self.card("Resource Management", "CPU, RAM, storage, devices", self._icon_resource())
        file_mgmt = self.card("File Management", "Folders, directories, drives", self._icon_files())
        ui = self.card("User Interface", "Windows, icons, menus", self._icon_ui())
        device_mgmt = self.card("Device Management", "Keyboard, mouse, printer", self._icon_devices())
        security = self.card("Security", "Logins, permissions, protection", self._icon_security())

        grid_top = VGroup(resource, file_mgmt, ui).arrange(RIGHT, buff=0.7)
        grid_bot = VGroup(device_mgmt, security).arrange(RIGHT, buff=0.7)
        grid = VGroup(grid_top, grid_bot).arrange(DOWN, buff=0.8).next_to(intro, DOWN, buff=0.8)

        self.play(FadeIn(grid_top, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(grid_bot, shift=UP))
        self.wait(0.8)

        # Examples line
        examples = VGroup(
            Text("Example: Watching YouTube while downloading a file —", font_size=24, color=YELLOW),
            Text("the OS shares CPU, RAM, and network fairly.", font_size=24, color=WHITE)
        ).arrange(DOWN, buff=0.2).next_to(grid, DOWN, buff=0.6)
        self.play(Write(examples))

        punch = Text("The OS is the manager, organizer, and protector.", font_size=28, color=YELLOW)
        punch.next_to(examples, DOWN, buff=0.6)
        self.play(Write(punch))
        self.wait(2)

    def why_different_scene(self):
        title = Text("2. Why Different Operating Systems?", font_size=48, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        intro = Text("Each OS is designed with different goals.", font_size=28, color=WHITE)
        intro.next_to(title, DOWN, buff=0.6)
        self.play(Write(intro))

        # OS cards
        windows = self.badge("Windows", self._icon_window_logo(), BLUE_E)
        macos = self.badge("macOS", self._icon_apple_logo(), GRAY)
        linux = self.badge("Linux", self._icon_linux(), YELLOW_E)
        android = self.badge("Android", self._icon_android(), GREEN_E)
        ios = self.badge("iOS", self._icon_apple_logo(), WHITE)

        row1 = VGroup(windows, macos, linux).arrange(RIGHT, buff=0.8)
        row2 = VGroup(android, ios).arrange(RIGHT, buff=0.8)
        rows = VGroup(row1, row2).arrange(DOWN, buff=0.8).next_to(intro, DOWN, buff=0.6)

        self.play(FadeIn(row1, shift=UP))
        self.play(FadeIn(row2, shift=UP))

        bullets = VGroup(
            Text("Windows → Versatility and compatibility", font_size=26, color=WHITE),
            Text("macOS → Seamless design and creative tools", font_size=26, color=WHITE),
            Text("Linux → Freedom, security, server power", font_size=26, color=WHITE),
            Text("Android → Variety and global reach", font_size=26, color=WHITE),
            Text("iOS → Security and premium experience", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(rows, DOWN, buff=0.6)
        self.play(Write(bullets))

        analogy = Text("Analogy: Like cars — vans, sports cars, trucks — all vehicles, different needs.", font_size=26, color=YELLOW)
        analogy.next_to(bullets, DOWN, buff=0.6)
        self.play(Write(analogy))
        self.wait(2)

    def future_scene(self):
        title = Text("3. The Future of Operating Systems", font_size=48, color=TEAL_E)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("Cloud integration and cross-device experiences", font_size=26, color=WHITE),
            Text("AI-powered assistance and automation", font_size=26, color=WHITE),
            Text("Android apps on Windows, phone integration on macOS", font_size=26, color=WHITE),
            Text("The OS may become invisible — seamless across devices", font_size=26, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        # Visuals: cloud, AI brain, devices
        cloud = self._icon_cloud()
        brain = self._icon_brain()
        devices = self._devices_row()
        visuals = VGroup(cloud, brain, devices).arrange(RIGHT, buff=1.0).next_to(bullets, DOWN, buff=0.8)
        self.play(FadeIn(visuals, shift=UP))
        self.wait(2)

    def closing_scene(self):
        title = Text("4. Closing", font_size=44, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        closing = Text(
            "The operating system is the soul of your device: it manages hardware,\n"
            "organizes files, runs apps, and protects your system. Whether you're\n"
            "on Windows, macOS, Linux, Android, or iOS — you rely on it every day.",
            font_size=26, color=WHITE, line_spacing=1.0
        ).next_to(title, DOWN, buff=0.8)
        self.play(Write(closing))
        self.wait(3)

    # Helpers
    def card(self, label: str, desc: str, icon: Mobject, color=BLUE):
        box = RoundedRectangle(width=3.8, height=2.6, corner_radius=0.15, color=color, fill_color=BLACK, fill_opacity=0.85)
        title = Text(label, font_size=24, color=color).next_to(box.get_top(), DOWN, buff=0.05)
        description = Text(desc, font_size=20, color=WHITE).next_to(box.get_bottom(), UP, buff=0.6)
        icon_group = icon.copy().scale(0.9).move_to(box.get_center()).shift(UP*0.2)
        return VGroup(box, icon_group, title, description)

    def badge(self, label: str, icon: Mobject, color=BLUE):
        chip = RoundedRectangle(width=3.2, height=1.2, corner_radius=0.15, color=color, fill_color=BLACK, fill_opacity=0.85)
        icon_group = icon.copy().scale(0.6).next_to(chip.get_left(), RIGHT, buff=0.3)
        text = Text(label, font_size=24, color=color).next_to(icon_group, RIGHT, buff=0.4)
        return VGroup(chip, icon_group, text)

    # Icon primitives
    def _icon_resource(self) -> VGroup:
        cpu = self._icon_cpu()
        ram = self._icon_ram()
        disk = self._icon_disk()
        group = VGroup(cpu, ram, disk).arrange(RIGHT, buff=0.2)
        return group

    def _icon_files(self) -> VGroup:
        folder = VGroup(
            Rectangle(width=1.8, height=1.0, color=WHITE),
            Rectangle(width=0.8, height=0.3, color=WHITE).next_to(UP*0.5, DOWN, buff=0)
        )
        doc = VGroup(
            Rectangle(width=0.7, height=0.9, color=WHITE),
            Line(LEFT*0.25, RIGHT*0.25, color=WHITE).shift(UP*0.2),
            Line(LEFT*0.25, RIGHT*0.25, color=WHITE),
            Line(LEFT*0.25, RIGHT*0.25, color=WHITE).shift(DOWN*0.2)
        ).next_to(folder, RIGHT, buff=0.1)
        return VGroup(folder, doc)

    def _icon_ui(self) -> VGroup:
        window = RoundedRectangle(width=2.2, height=1.4, corner_radius=0.08, color=WHITE)
        buttons = VGroup(*[Dot(radius=0.05, color=c) for c in (RED, YELLOW, GREEN)]).arrange(RIGHT, buff=0.08).next_to(window.get_top(), DOWN, buff=0.02)
        return VGroup(window, buttons)

    def _icon_devices(self) -> VGroup:
        keyboard = RoundedRectangle(width=1.6, height=0.5, corner_radius=0.08, color=WHITE)
        keys = VGroup(*[Square(0.12, color=WHITE) for _ in range(12)]).arrange(RIGHT, buff=0.04).move_to(keyboard.get_center())
        mouse = VGroup(RoundedRectangle(width=0.35, height=0.5, corner_radius=0.18, color=WHITE), Line(UP*0.08, DOWN*0.08, color=WHITE)).next_to(keyboard, RIGHT, buff=0.2)
        return VGroup(keyboard, keys, mouse)

    def _icon_security(self) -> VGroup:
        lock = VGroup(
            RoundedRectangle(width=0.9, height=0.9, corner_radius=0.12, color=WHITE),
            ArcBetweenPoints(LEFT*0.3, RIGHT*0.3, angle=PI/1.2, color=WHITE).shift(UP*0.6),
            Dot(radius=0.06, color=WHITE)
        )
        return lock

    def _icon_cpu(self) -> VGroup:
        chip = RoundedRectangle(width=1.4, height=1.4, corner_radius=0.1, color=WHITE)
        pins_top = VGroup(*[Line(UP*0.2, UP*0.4, color=WHITE) for _ in range(6)]).arrange(RIGHT, buff=0.15).next_to(chip, UP, buff=0.02)
        pins_bottom = pins_top.copy().next_to(chip, DOWN, buff=0.02)
        pins_left = VGroup(*[Line(LEFT*0.2, LEFT*0.4, color=WHITE) for _ in range(6)]).arrange(DOWN, buff=0.15).next_to(chip, LEFT, buff=0.02)
        pins_right = pins_left.copy().next_to(chip, RIGHT, buff=0.02)
        text = Text("CPU", font_size=20, color=WHITE).move_to(chip.get_center())
        return VGroup(chip, pins_top, pins_bottom, pins_left, pins_right, text)

    def _icon_ram(self) -> VGroup:
        module = RoundedRectangle(width=2.2, height=0.7, corner_radius=0.1, color=WHITE)
        chips = VGroup(*[RoundedRectangle(width=0.3, height=0.4, corner_radius=0.05, color=WHITE) for _ in range(4)])
        chips.arrange(RIGHT, buff=0.15).move_to(module.get_center())
        return VGroup(module, chips)

    def _icon_disk(self) -> VGroup:
        base = RoundedRectangle(width=1.6, height=0.6, corner_radius=0.1, color=WHITE)
        led = Dot(radius=0.05, color=GREEN).next_to(base.get_left(), RIGHT, buff=0.2)
        return VGroup(base, led)

    def _icon_window_logo(self) -> VGroup:
        quad = VGroup(
            Square(0.3, color=WHITE), Square(0.3, color=WHITE),
            Square(0.3, color=WHITE), Square(0.3, color=WHITE)
        ).arrange_in_grid(rows=2, cols=2, buff=0.06)
        return quad

    def _icon_apple_logo(self) -> VGroup:
        # Abstract apple: circle + leaf
        body = Circle(radius=0.25, color=WHITE)
        leaf = Ellipse(width=0.2, height=0.1, color=WHITE).next_to(body, UP, buff=0)
        return VGroup(body, leaf)

    def _icon_linux(self) -> VGroup:
        # Simple penguin-like icon
        body = Ellipse(width=0.5, height=0.8, color=WHITE)
        belly = Ellipse(width=0.3, height=0.5, color=WHITE).set_fill(WHITE, opacity=0.6)
        eyes = VGroup(Dot(radius=0.03, color=WHITE).shift(UP*0.15+LEFT*0.06), Dot(radius=0.03, color=WHITE).shift(UP*0.15+RIGHT*0.06))
        return VGroup(body, belly, eyes)

    def _icon_android(self) -> VGroup:
        # Abstract Android robot: head with antennae + body with arms and legs
        head = RoundedRectangle(width=0.5, height=0.3, corner_radius=0.1, color=WHITE).shift(UP*0.25)
        antenna_left = Line(ORIGIN, UP*0.2, color=WHITE).rotate(-PI/6).next_to(head, UP, buff=0, aligned_edge=LEFT).shift(RIGHT*0.08)
        antenna_right = Line(ORIGIN, UP*0.2, color=WHITE).rotate(PI/6).next_to(head, UP, buff=0, aligned_edge=RIGHT).shift(LEFT*0.08)
        eye_l = Dot(radius=0.02, color=WHITE).move_to(head.get_center()+LEFT*0.12)
        eye_r = Dot(radius=0.02, color=WHITE).move_to(head.get_center()+RIGHT*0.12)
        body = RoundedRectangle(width=0.6, height=0.55, corner_radius=0.12, color=WHITE)
        arm_l = Rectangle(width=0.1, height=0.35, color=WHITE).next_to(body, LEFT, buff=0.05)
        arm_r = Rectangle(width=0.1, height=0.35, color=WHITE).next_to(body, RIGHT, buff=0.05)
        leg_l = Rectangle(width=0.12, height=0.18, color=WHITE).next_to(body, DOWN, buff=0.02).shift(LEFT*0.15)
        leg_r = Rectangle(width=0.12, height=0.18, color=WHITE).next_to(body, DOWN, buff=0.02).shift(RIGHT*0.15)
        robot = VGroup(body, arm_l, arm_r, leg_l, leg_r, head, antenna_left, antenna_right, eye_l, eye_r)
        robot.scale(0.9)
        return robot

    def _icon_cloud(self) -> VGroup:
        puffs = VGroup(Circle(radius=0.25, color=WHITE), Circle(radius=0.3, color=WHITE), Circle(radius=0.22, color=WHITE))
        puffs.arrange(RIGHT, buff=-0.1)
        return puffs

    def _icon_brain(self) -> VGroup:
        left = Circle(radius=0.35, color=WHITE)
        right = Circle(radius=0.35, color=WHITE).next_to(left, RIGHT, buff=0.1)
        folds = VGroup(
            Arc(radius=0.25, start_angle=0, angle=PI, color=WHITE).move_to(left.get_center()+UP*0.05),
            Arc(radius=0.25, start_angle=0, angle=PI, color=WHITE).move_to(right.get_center()+DOWN*0.05)
        )
        return VGroup(left, right, folds).scale(0.9)

    def _devices_row(self) -> VGroup:
        phone = RoundedRectangle(width=0.8, height=1.6, corner_radius=0.12, color=WHITE)
        tablet = RoundedRectangle(width=1.2, height=1.8, corner_radius=0.12, color=WHITE)
        laptop = RoundedRectangle(width=2.2, height=1.4, corner_radius=0.12, color=WHITE)
        return VGroup(phone, tablet, laptop).arrange(RIGHT, buff=0.6)
