from manim import *

class CybersecurityTutorial(Scene):
    def construct(self):
        # Scene 1: What is Cybersecurity?
        self.scene_what_is_cybersecurity()
        self.clear()

        # Scene 2: Encryption – The Secret Code
        self.scene_encryption()
        self.clear()

        # Scene 3: Why Cybersecurity Matters
        self.scene_why_matters()
        self.clear()

        # Scene 4: Quick Recap
        self.scene_quick_recap()
        self.clear()

    def scene_what_is_cybersecurity(self):
        title = Text("What is Cybersecurity?", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        narration = Text(
            "Cybersecurity protects computers, networks, and personal information\n"
            "from attacks, theft, or damage — keeping your data safe and private.",
            font_size=26, color=WHITE, line_spacing=1.0
        ).next_to(title, DOWN, buff=0.8)
        self.play(Write(narration))

        # Visual: Shield protecting a computer with data inside
        shield = self._icon_shield().scale(1.1)
        computer = self._icon_computer()
        data = VGroup(*[Square(0.12, color=WHITE).set_fill(BLUE, opacity=0.8) for _ in range(6)]).arrange(RIGHT, buff=0.08)
        data.arrange_in_grid(rows=2, cols=3, buff=0.08).move_to(computer.get_center())
        group = VGroup(computer, data, shield).arrange(RIGHT, buff=0.6).next_to(narration, DOWN, buff=0.8)
        self.play(FadeIn(group, shift=UP))
        self.wait(1.5)

    def scene_encryption(self):
        title = Text("Encryption – The Secret Code", font_size=48, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        narration = VGroup(
            Text("Encryption scrambles messages using a key.", font_size=26, color=WHITE),
            Text("Only someone with the right key can read it.", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.8)
        self.play(Write(narration))

        # Example: Hello -> gibberish
        plain = Text("Hello", font_size=28, color=WHITE)
        arrow = Arrow(LEFT*1.2, RIGHT*1.2, color=WHITE)
        cipher = Text("X1A4%$#", font_size=28, color=YELLOW)
        example = VGroup(plain, arrow, cipher).arrange(RIGHT, buff=0.4).next_to(narration, DOWN, buff=0.6)
        self.play(Write(example))

        https_note = Text("HTTPS = your data is encrypted in transit", font_size=24, color=YELLOW).next_to(example, DOWN, buff=0.6)
        lock = self._icon_lock().next_to(https_note, RIGHT, buff=0.4)
        self.play(Write(https_note), FadeIn(lock, shift=UP))
        self.wait(1.5)

    def scene_why_matters(self):
        title = Text("Why Cybersecurity Matters", font_size=48, color=TEAL_E)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        narration = Text(
            "Hackers try to steal data or control systems. Cybersecurity helps\n"
            "prevent identity theft, scams, and data leaks.",
            font_size=26, color=WHITE, line_spacing=1.0
        ).next_to(title, DOWN, buff=0.8)
        self.play(Write(narration))

        # Visual: headlines vs safe user
        headlines = VGroup(
            Text("Data Breach Exposes Millions", font_size=22, color=RED),
            Text("Ransomware Hits Hospitals", font_size=22, color=ORANGE),
            Text("Phishing Scams on the Rise", font_size=22, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        user_safe = VGroup(self._icon_computer(), Text("You", font_size=22, color=GREEN)).arrange(DOWN, buff=0.2)
        row = VGroup(headlines, user_safe).arrange(RIGHT, buff=1.2).next_to(narration, DOWN, buff=0.8)
        self.play(FadeIn(row, shift=UP))
        self.wait(1.5)

    def scene_quick_recap(self):
        title = Text("Quick Recap", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        items = VGroup(
            self._badge("Encryption", self._icon_keylock(), TEAL_E),
            self._badge("Firewall", self._icon_firewall(), MAROON_E),
            self._badge("VPN", self._icon_vpn(), PURPLE_E),
            self._badge("Passwords", self._icon_password(), YELLOW_E)
        ).arrange(RIGHT, buff=0.8).next_to(title, DOWN, buff=0.8)
        self.play(FadeIn(items, shift=UP))

        bullets = VGroup(
            Text("Encryption scrambles data", font_size=24, color=WHITE),
            Text("Firewalls block threats", font_size=24, color=WHITE),
            Text("VPNs create private tunnels", font_size=24, color=WHITE),
            Text("Strong passwords = strong keys", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(items, DOWN, buff=0.6)
        self.play(Write(bullets))
        self.wait(2)

    # Helpers
    def _badge(self, label: str, icon: Mobject, color=BLUE):
        chip = RoundedRectangle(width=3.2, height=1.2, corner_radius=0.15, color=color, fill_color=BLACK, fill_opacity=0.85)
        icon_group = icon.copy().scale(0.6).next_to(chip.get_left(), RIGHT, buff=0.3)
        text = Text(label, font_size=24, color=color).next_to(icon_group, RIGHT, buff=0.4)
        return VGroup(chip, icon_group, text)

    def _icon_shield(self) -> VGroup:
        outer = ArcBetweenPoints(LEFT*0.6, RIGHT*0.6, angle=PI/1.4, color=WHITE)
        inner = Polygon(LEFT*0.6, RIGHT*0.6, DOWN*0.7, color=WHITE)
        return VGroup(outer, inner)

    def _icon_computer(self) -> VGroup:
        screen = RoundedRectangle(width=1.6, height=1.0, corner_radius=0.08, color=WHITE)
        stand = VGroup(Rectangle(width=0.2, height=0.3, color=WHITE).next_to(screen, DOWN, buff=0.05), Rectangle(width=0.9, height=0.08, color=WHITE).next_to(screen, DOWN, buff=0.25))
        return VGroup(screen, stand)

    def _icon_lock(self) -> VGroup:
        lock = VGroup(
            RoundedRectangle(width=0.7, height=0.7, corner_radius=0.12, color=WHITE),
            ArcBetweenPoints(LEFT*0.25, RIGHT*0.25, angle=PI/1.2, color=WHITE).shift(UP*0.5),
            Dot(radius=0.05, color=WHITE)
        )
        return lock

    def _icon_keylock(self) -> VGroup:
        key = VGroup(Line(LEFT*0.25, RIGHT*0.25, color=WHITE), Circle(radius=0.08, color=WHITE).next_to(ORIGIN, LEFT, buff=0)).arrange(RIGHT, buff=0.05)
        lock = self._icon_lock().scale(0.7)
        return VGroup(key, lock)

    def _icon_firewall(self) -> VGroup:
        wall = VGroup(*[Rectangle(width=0.3, height=0.15, color=WHITE) for _ in range(9)]).arrange_in_grid(rows=3, cols=3, buff=0.04)
        flame = VGroup(
            ArcBetweenPoints(ORIGIN, UP*0.4, angle=PI/2, color=RED),
            ArcBetweenPoints(ORIGIN, UP*0.3, angle=PI/2, color=ORANGE).shift(RIGHT*0.1)
        )
        return VGroup(wall, flame)

    def _icon_vpn(self) -> VGroup:
        tunnel = VGroup(
            Circle(radius=0.22, color=WHITE),
            Circle(radius=0.32, color=WHITE),
            Circle(radius=0.42, color=WHITE)
        )
        shield = self._icon_shield().scale(0.6)
        return VGroup(tunnel, shield)

    def _icon_password(self) -> VGroup:
        box = RoundedRectangle(width=1.4, height=0.5, corner_radius=0.1, color=WHITE)
        stars = VGroup(*[Star(n=5, outer_radius=0.08, color=WHITE) for _ in range(5)]).arrange(RIGHT, buff=0.12)
        stars.move_to(box.get_center())
        return VGroup(box, stars)
