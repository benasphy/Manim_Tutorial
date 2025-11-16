from manim import *

class SystemVsApplicationSoftwareTutorial(Scene):
    def construct(self):
        # Scene 1: What is Software?
        self.scene_what_is_software()
        self.clear()

        # Scene 2: Two Main Types of Software
        self.scene_two_main_types()
        self.clear()

        # Scene 3: System Software
        self.scene_system_software()
        self.clear()

        # Scene 4: Application Software
        self.scene_application_software()
        self.clear()

        # Scene 5: Key Differences
        self.scene_key_differences()
        self.clear()

        # Scene 6: How They Work Together
        self.scene_how_they_work_together()
        self.clear()

        # Scene 7: Why This Matters
        self.scene_why_this_matters()
        self.clear()

        # Scene 8: Closing
        self.scene_closing()
        self.clear()

    def scene_what_is_software(self):
        title = Text("What is Software?", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("Software = instructions telling the computer what to do", font_size=28, color=WHITE),
            Text("Hardware = physical parts: CPU, RAM, screen, keyboard", font_size=28, color=WHITE),
            Text("Software brings the hardware to life", font_size=28, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))
        self.wait(2)

        # Simple visual: hardware vs software
        hardware = self._badge("Hardware", self._icon_hardware(), BLUE_E)
        software = self._badge("Software", self._icon_software(), GREEN_E)
        pair = VGroup(hardware, software).arrange(RIGHT, buff=1.0).next_to(bullets, DOWN, buff=0.8)
        self.play(FadeIn(pair, shift=UP))
        self.wait(1.5)

    def scene_two_main_types(self):
        title = Text("Two Main Types of Software", font_size=48, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        items = VGroup(
            self._badge("System Software", self._icon_system(), TEAL_E),
            self._badge("Application Software", self._icon_app(), MAROON_E)
        ).arrange(RIGHT, buff=1.2).next_to(title, DOWN, buff=1.0)

        self.play(FadeIn(items, shift=UP))
        self.wait(2)

    def scene_system_software(self):
        title = Text("System Software", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        definition = Text(
            "Foundation software that manages hardware and allows other programs to run",
            font_size=26, color=WHITE
        ).next_to(title, DOWN, buff=0.6)
        self.play(Write(definition))

        examples_title = Text("Examples:", font_size=26, color=YELLOW).next_to(definition, DOWN, buff=0.6)
        examples = VGroup(
            Text("Operating Systems: Windows, macOS, Linux, Android, iOS", font_size=24, color=WHITE),
            Text("Utility Programs: antivirus, disk cleanup, file managers", font_size=24, color=WHITE),
            Text("Device Drivers: printer, keyboard, graphics card drivers", font_size=24, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(examples_title, DOWN, buff=0.4)

        icons = VGroup(
            self._badge("OS", self._icon_system(), BLUE_E),
            self._badge("Utilities", self._icon_wrench(), TEAL_E),
            self._badge("Drivers", self._icon_plug(), PURPLE_E)
        ).arrange(RIGHT, buff=0.8).next_to(examples, DOWN, buff=0.8)

        self.play(Write(examples_title))
        self.play(Write(examples))
        self.play(FadeIn(icons, shift=UP))

        role = Text("Runs in the background — without it, nothing works", font_size=26, color=YELLOW)
        role.next_to(icons, DOWN, buff=0.6)
        self.play(Write(role))
        self.wait(2)

    def scene_application_software(self):
        title = Text("Application Software", font_size=48, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        definition = Text(
            "Programs you use directly to perform tasks and solve problems",
            font_size=26, color=WHITE
        ).next_to(title, DOWN, buff=0.6)
        self.play(Write(definition))

        examples_title = Text("Examples:", font_size=26, color=YELLOW).next_to(definition, DOWN, buff=0.6)
        examples = VGroup(
            Text("Productivity: Word, Excel, Google Docs", font_size=24, color=WHITE),
            Text("Entertainment: Spotify, Netflix, games", font_size=24, color=WHITE),
            Text("Communication: WhatsApp, Zoom, Gmail", font_size=24, color=WHITE),
            Text("Creative: Photoshop, Canva, iMovie", font_size=24, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(examples_title, DOWN, buff=0.4)

        icons = VGroup(
            self._badge("Docs", self._icon_doc(), TEAL_E),
            self._badge("Media", self._icon_media(), MAROON_E),
            self._badge("Chat", self._icon_chat(), YELLOW_E),
            self._badge("Design", self._icon_design(), PURPLE_E)
        ).arrange(RIGHT, buff=0.8).next_to(examples, DOWN, buff=0.8)

        self.play(Write(examples_title))
        self.play(Write(examples))
        self.play(FadeIn(icons, shift=UP))

        role = Text("Designed for the end user — you", font_size=26, color=YELLOW)
        role.next_to(icons, DOWN, buff=0.6)
        self.play(Write(role))
        self.wait(2)

    def scene_key_differences(self):
        title = Text("Key Differences", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Table-like comparison
        header = VGroup(
            Text("Feature", font_size=26, color=YELLOW),
            Text("System Software", font_size=26, color=YELLOW),
            Text("Application Software", font_size=26, color=YELLOW)
        ).arrange(RIGHT, buff=2.0).next_to(title, DOWN, buff=0.8)

        rows = [
            ("Purpose", "Manages hardware, runs the system", "Helps users perform tasks"),
            ("Runs", "In the background", "In the foreground"),
            ("Examples", "Windows, macOS, Linux, Drivers", "MS Word, Chrome, WhatsApp"),
            ("Users", "Mainly the computer itself", "Mainly the end user"),
            ("Dependency", "Needed for the computer to work", "Depends on system software"),
        ]

        table_rows = VGroup()
        for feature, sys_text, app_text in rows:
            row = VGroup(
                Text(feature, font_size=24, color=WHITE),
                Text(sys_text, font_size=24, color=WHITE),
                Text(app_text, font_size=24, color=WHITE)
            ).arrange(RIGHT, buff=1.0)
            table_rows.add(row)
        table_rows.arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(header, DOWN, buff=0.6)

        self.play(Write(header))
        self.play(Write(table_rows))

        punchline = Text(
            "Both are essential: without system software, apps can't run; without apps, the system feels empty",
            font_size=26, color=YELLOW
        ).next_to(table_rows, DOWN, buff=0.8)
        self.play(Write(punchline))
        self.wait(2)

    def scene_how_they_work_together(self):
        title = Text("How They Work Together", font_size=48, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        narrative = VGroup(
            Text("Phone example:", font_size=26, color=YELLOW),
            Text("Android (system software) runs the phone", font_size=24, color=WHITE),
            Text("YouTube (application software) runs on top of Android", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=0.8)
        self.play(Write(narrative))

        # Visual: Stack diagram
        stack = VGroup(
            RoundedRectangle(width=5.0, height=0.7, corner_radius=0.1, color=TEAL_E),
            RoundedRectangle(width=5.0, height=0.7, corner_radius=0.1, color=MAROON_E)
        ).arrange(DOWN, buff=0.15).next_to(narrative, DOWN, buff=0.8)
        labels = VGroup(
            Text("System Software (e.g., Android)", font_size=22, color=WHITE).move_to(stack[0]),
            Text("Application Software (e.g., YouTube)", font_size=22, color=WHITE).move_to(stack[1])
        )
        self.play(Create(stack))
        self.play(Write(labels))
        self.wait(1.5)

    def scene_why_this_matters(self):
        title = Text("Why This Matters", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("Knowing the difference explains updates:", font_size=26, color=YELLOW),
            Text("System update → security or hardware support", font_size=24, color=WHITE),
            Text("App update → new features or bug fixes", font_size=24, color=WHITE),
            Text("Both keep your device useful, secure, and fun", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))
        self.wait(2)

    def scene_closing(self):
        title = Text("Closing", font_size=44, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        closing = Text(
            "System software is the foundation; application software is built on top.\n"
            "Without system software, your device wouldn't start. Without apps, it wouldn't be useful.\n"
            "Together, they make technology powerful and personal.",
            font_size=26, color=WHITE, line_spacing=1.0
        ).next_to(title, DOWN, buff=0.8)
        self.play(Write(closing))
        self.wait(3)

    # --- Helpers (icons and badges built from primitives) ---
    def _badge(self, label: str, icon: Mobject, color=BLUE):
        chip = RoundedRectangle(width=3.2, height=1.2, corner_radius=0.15, color=color, fill_color=BLACK, fill_opacity=0.85)
        icon_group = icon.copy().scale(0.6).next_to(chip.get_left(), RIGHT, buff=0.3)
        text = Text(label, font_size=24, color=color).next_to(icon_group, RIGHT, buff=0.4)
        return VGroup(chip, icon_group, text)

    def _icon_hardware(self) -> VGroup:
        box = RoundedRectangle(width=1.8, height=1.1, corner_radius=0.1, color=WHITE)
        circle = Circle(radius=0.08, color=WHITE).next_to(box, DOWN, buff=0.05)
        return VGroup(box, circle)

    def _icon_software(self) -> VGroup:
        code = VGroup(Line(LEFT*0.3, ORIGIN, color=WHITE), Line(ORIGIN, RIGHT*0.3, color=WHITE))
        code.arrange(RIGHT, buff=0.05)
        sheet = RoundedRectangle(width=1.6, height=1.0, corner_radius=0.08, color=WHITE)
        return VGroup(sheet, code)

    def _icon_system(self) -> VGroup:
        gear = VGroup(Circle(radius=0.28, color=WHITE), *[Line(ORIGIN, RIGHT*0.22, color=WHITE).rotate(i*PI/4) for i in range(8)])
        return gear

    def _icon_app(self) -> VGroup:
        window = RoundedRectangle(width=1.6, height=1.0, corner_radius=0.08, color=WHITE)
        buttons = VGroup(*[Dot(radius=0.04, color=c) for c in (RED, YELLOW, GREEN)]).arrange(RIGHT, buff=0.06).next_to(window.get_top(), DOWN, buff=0.02)
        return VGroup(window, buttons)

    def _icon_wrench(self) -> VGroup:
        handle = Rectangle(width=0.1, height=0.5, color=WHITE)
        head = ArcBetweenPoints(LEFT*0.2, RIGHT*0.2, angle=PI/1.4, color=WHITE).shift(UP*0.25)
        return VGroup(handle, head)

    def _icon_plug(self) -> VGroup:
        prongs = VGroup(Rectangle(width=0.06, height=0.18, color=WHITE), Rectangle(width=0.06, height=0.18, color=WHITE)).arrange(RIGHT, buff=0.08)
        body = RoundedRectangle(width=0.3, height=0.2, corner_radius=0.05, color=WHITE).next_to(prongs, DOWN, buff=0.02)
        cable = Line(ORIGIN, RIGHT*0.5, color=WHITE).next_to(body, DOWN, buff=0.02)
        return VGroup(prongs, body, cable)

    def _icon_doc(self) -> VGroup:
        sheet = RoundedRectangle(width=0.9, height=1.2, corner_radius=0.08, color=WHITE)
        lines = VGroup(
            Line(LEFT*0.35, RIGHT*0.35, color=WHITE).shift(UP*0.25),
            Line(LEFT*0.35, RIGHT*0.35, color=WHITE),
            Line(LEFT*0.35, RIGHT*0.35, color=WHITE).shift(DOWN*0.25),
        )
        return VGroup(sheet, lines)

    def _icon_media(self) -> VGroup:
        play = Triangle(color=WHITE).scale(0.25).rotate(-PI/2)
        disc = Circle(radius=0.35, color=WHITE)
        return VGroup(disc, play)

    def _icon_chat(self) -> VGroup:
        bubble = RoundedRectangle(width=1.2, height=0.7, corner_radius=0.15, color=WHITE)
        tail = Polygon(ORIGIN, RIGHT*0.15, DOWN*0.15, color=WHITE).next_to(bubble, DOWN, buff=0)
        return VGroup(bubble, tail)

    def _icon_design(self) -> VGroup:
        frame = Square(0.8, color=WHITE)
        brush = VGroup(Line(ORIGIN, RIGHT*0.4, color=WHITE), ArcBetweenPoints(ORIGIN, RIGHT*0.2, angle=PI/2, color=WHITE).shift(RIGHT*0.4))
        return VGroup(frame, brush)
