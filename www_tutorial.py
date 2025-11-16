from manim import *

class WorldWideWebTutorial(Scene):
    def construct(self):
        # Scene: What is the World Wide Web?
        self.scene_www_intro()
        self.clear()

        # Scene: Why This Matters
        self.scene_why_matters()
        self.clear()

        # Scene: Closing
        self.scene_closing()
        self.clear()

    def scene_www_intro(self):
        title = Text("The World Wide Web", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("The Web = huge collection of websites/pages on servers worldwide", font_size=28, color=WHITE),
            Text("Use browsers to view, search engines to find", font_size=28, color=WHITE),
            Text("The Web is just one part of the Internet", font_size=28, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        # Visuals: servers (books), browser, search engine
        servers = self._server_row()
        browser = self._badge("Browser", self._icon_browser(), TEAL_E)
        search = self._badge("Search Engine", self._icon_search(), YELLOW_E)
        visuals = VGroup(servers, VGroup(browser, search).arrange(RIGHT, buff=0.8)).arrange(DOWN, buff=0.8).next_to(bullets, DOWN, buff=0.8)
        self.play(FadeIn(visuals, shift=UP))
        self.wait(1.5)

        note = Text("Internet also includes email, messaging, file sharing, games, ...", font_size=24, color=WHITE)
        note.next_to(visuals, DOWN, buff=0.6)
        self.play(Write(note))
        self.wait(1)

    def scene_why_matters(self):
        title = Text("Why This Matters", font_size=48, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("Browsers let you see websites", font_size=28, color=WHITE),
            Text("Search engines help you find what you need", font_size=28, color=WHITE),
            Text("HTTPS keeps your information private", font_size=28, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        row = VGroup(
            self._badge("Browser", self._icon_browser(), BLUE_E),
            self._badge("Search Engine", self._icon_search(), TEAL_E),
            self._badge("HTTPS", self._icon_lock(), PURPLE_E)
        ).arrange(RIGHT, buff=0.8).next_to(bullets, DOWN, buff=0.8)
        self.play(FadeIn(row, shift=UP))
        self.wait(1.5)

    def scene_closing(self):
        title = Text("Closing", font_size=44, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        closing = Text(
            "The Web is a vast library of websites. Browsers let you read them,\n"
            "search engines help you find them, and HTTP/HTTPS are the rules that\n"
            "allow your device to talk to websites safely.",
            font_size=26, color=WHITE, line_spacing=1.0
        ).next_to(title, DOWN, buff=0.8)
        self.play(Write(closing))
        self.wait(3)

    # Helpers
    def _badge(self, label: str, icon: Mobject, color=BLUE):
        chip = RoundedRectangle(width=3.4, height=1.2, corner_radius=0.15, color=color, fill_color=BLACK, fill_opacity=0.85)
        icon_group = icon.copy().scale(0.55).next_to(chip.get_left(), RIGHT, buff=0.3)
        text = Text(label, font_size=24, color=color).next_to(icon_group, RIGHT, buff=0.4)
        return VGroup(chip, icon_group, text)

    def _server_row(self) -> VGroup:
        # Row of server racks to represent many websites/pages on servers
        racks = VGroup(*[self._icon_server() for _ in range(4)]).arrange(RIGHT, buff=0.5)
        label = Text("Servers hosting websites", font_size=22, color=WHITE).next_to(racks, DOWN, buff=0.2)
        return VGroup(racks, label)

    def _icon_server(self) -> VGroup:
        rack = VGroup(
            RoundedRectangle(width=0.8, height=1.2, corner_radius=0.06, color=WHITE),
            Line(LEFT*0.25, RIGHT*0.25, color=WHITE).shift(UP*0.25),
            Line(LEFT*0.25, RIGHT*0.25, color=WHITE),
            Line(LEFT*0.25, RIGHT*0.25, color=WHITE).shift(DOWN*0.25)
        )
        leds = VGroup(*[Dot(radius=0.03, color=GREEN).shift(DOWN*0.4 + RIGHT*(i*0.08 - 0.2)) for i in range(5)])
        return VGroup(rack, leds)

    def _icon_browser(self) -> VGroup:
        window = RoundedRectangle(width=1.6, height=1.0, corner_radius=0.08, color=WHITE)
        tab = Rectangle(width=0.6, height=0.15, color=WHITE).next_to(window, UP, buff=0)
        buttons = VGroup(*[Dot(radius=0.04, color=c) for c in (RED, YELLOW, GREEN)]).arrange(RIGHT, buff=0.06).next_to(window.get_top(), DOWN, buff=0.02)
        return VGroup(window, tab, buttons)

    def _icon_search(self) -> VGroup:
        circle = Circle(radius=0.2, color=WHITE)
        handle = Line(ORIGIN, RIGHT*0.25, color=WHITE).rotate(PI/4).next_to(circle, RIGHT, buff=0.02)
        return VGroup(circle, handle)

    def _icon_lock(self) -> VGroup:
        lock = VGroup(
            RoundedRectangle(width=0.7, height=0.7, corner_radius=0.12, color=WHITE),
            ArcBetweenPoints(LEFT*0.25, RIGHT*0.25, angle=PI/1.2, color=WHITE).shift(UP*0.5),
            Dot(radius=0.05, color=WHITE)
        )
        return lock
