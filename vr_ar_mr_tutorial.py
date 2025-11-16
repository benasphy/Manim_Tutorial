from manim import *

class VRARMRTutorial(Scene):
    def construct(self):
        # Scene: Key Differences
        self.scene_key_differences()
        self.clear()

        # Scene: Where Are These Used?
        self.scene_use_cases()
        self.clear()

        # Scene: Challenges
        self.scene_challenges()
        self.clear()

    def scene_key_differences(self):
        title = Text("VR • AR • MR — Key Differences", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("VR: fully digital world — you leave reality", font_size=28, color=WHITE),
            Text("AR: real world + digital objects (overlay)", font_size=28, color=WHITE),
            Text("MR: real world + digital objects that interact", font_size=28, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        # Side-by-side visual: VR headset → game world, AR phone → overlay, MR glasses → hologram interacts with table
        vr = self._badge("VR", self._icon_vr_headset(), BLUE_E)
        ar = self._badge("AR", self._icon_phone_overlay(), TEAL_E)
        mr = self._badge("MR", self._icon_mr_glasses(), PURPLE_E)
        row = VGroup(vr, ar, mr).arrange(RIGHT, buff=0.8).next_to(bullets, DOWN, buff=0.8)
        self.play(FadeIn(row, shift=UP))

        # Small scene elements for each
        vr_world = self._icon_game_world().next_to(vr, DOWN, buff=0.4)
        ar_overlay = self._icon_overlay_cube().next_to(ar, DOWN, buff=0.4)
        mr_scene = self._icon_mr_table().next_to(mr, DOWN, buff=0.4)
        self.play(FadeIn(vr_world, shift=UP), FadeIn(ar_overlay, shift=UP), FadeIn(mr_scene, shift=UP))
        self.wait(1.5)

    def scene_use_cases(self):
        title = Text("Where Are These Used?", font_size=48, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("Entertainment & Gaming: VR games, AR filters, MR experiences", font_size=26, color=WHITE),
            Text("Education & Training: virtual classes, AR textbooks, MR sims", font_size=26, color=WHITE),
            Text("Shopping & Business: AR try-ons, MR product design", font_size=26, color=WHITE),
            Text("Healthcare: VR therapy, AR surgery guidance, MR training", font_size=26, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        # Collage: VR gaming, AR shopping, MR surgery demo
        vr_game = self._badge("VR Gaming", self._icon_gamepad(), BLUE_E)
        ar_shop = self._badge("AR Shopping", self._icon_tshirt_overlay(), TEAL_E)
        mr_surgery = self._badge("MR Surgery", self._icon_heart_holo(), PURPLE_E)
        collage = VGroup(vr_game, ar_shop, mr_surgery).arrange(RIGHT, buff=0.8).next_to(bullets, DOWN, buff=0.8)
        self.play(FadeIn(collage, shift=UP))
        self.wait(1.5)

    def scene_challenges(self):
        title = Text("Challenges", font_size=48, color=MAROON_E)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("Cost: headsets/MR devices can be expensive", font_size=26, color=WHITE),
            Text("Comfort: motion sickness in VR", font_size=26, color=WHITE),
            Text("Privacy: AR apps use camera/location", font_size=26, color=WHITE),
            Text("Content: not enough high-quality apps (yet)", font_size=26, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        icons = VGroup(
            self._badge("Cost", self._icon_money(), GRAY),
            self._badge("Comfort", self._icon_face_dizzy(), YELLOW_E),
            self._badge("Privacy", self._icon_lock(), TEAL_E),
            self._badge("Content", self._icon_box_apps(), BLUE_E)
        ).arrange(RIGHT, buff=0.6).next_to(bullets, DOWN, buff=0.8)
        self.play(FadeIn(icons, shift=UP))
        self.wait(2)

    # Helpers
    def _badge(self, label: str, icon: Mobject, color=BLUE):
        chip = RoundedRectangle(width=3.2, height=1.2, corner_radius=0.15, color=color, fill_color=BLACK, fill_opacity=0.85)
        icon_group = icon.copy().scale(0.6).next_to(chip.get_left(), RIGHT, buff=0.3)
        text = Text(label, font_size=24, color=color).next_to(icon_group, RIGHT, buff=0.4)
        return VGroup(chip, icon_group, text)

    # Icon primitives
    def _icon_vr_headset(self) -> VGroup:
        band = RoundedRectangle(width=0.9, height=0.25, corner_radius=0.12, color=WHITE)
        lenses = VGroup(Rectangle(width=0.25, height=0.18, color=WHITE), Rectangle(width=0.25, height=0.18, color=WHITE)).arrange(RIGHT, buff=0.08)
        lenses.move_to(band.get_center())
        return VGroup(band, lenses)

    def _icon_phone_overlay(self) -> VGroup:
        phone = RoundedRectangle(width=0.5, height=0.9, corner_radius=0.1, color=WHITE)
        overlay = Square(0.2, color=WHITE).set_fill(WHITE, opacity=0.2).move_to(phone.get_center())
        return VGroup(phone, overlay)

    def _icon_mr_glasses(self) -> VGroup:
        frame = VGroup(Arc(radius=0.22, start_angle=0, angle=PI, color=WHITE), Arc(radius=0.22, start_angle=0, angle=PI, color=WHITE)).arrange(RIGHT, buff=0.2)
        bridge = Line(LEFT*0.1, RIGHT*0.1, color=WHITE)
        return VGroup(frame, bridge)

    def _icon_game_world(self) -> VGroup:
        hill = ArcBetweenPoints(LEFT*0.5, RIGHT*0.5, angle=PI/2, color=WHITE)
        flag = VGroup(Line(ORIGIN, UP*0.25, color=WHITE), Triangle(color=WHITE).scale(0.12).next_to(ORIGIN, RIGHT, buff=0).shift(UP*0.25))
        flag.shift(UP*0.1+RIGHT*0.2)
        return VGroup(hill, flag)

    def _icon_overlay_cube(self) -> VGroup:
        sq = Square(0.3, color=WHITE)
        axes = VGroup(Line(ORIGIN, RIGHT*0.2, color=WHITE), Line(ORIGIN, UP*0.2, color=WHITE))
        return VGroup(sq, axes)

    def _icon_mr_table(self) -> VGroup:
        table = VGroup(Rectangle(width=0.9, height=0.1, color=WHITE), Line(ORIGIN, DOWN*0.3, color=WHITE).shift(LEFT*0.3), Line(ORIGIN, DOWN*0.3, color=WHITE).shift(RIGHT*0.3))
        holo = VGroup(Square(0.25, color=WHITE), Line(ORIGIN, DOWN*0.15, color=WHITE)).shift(UP*0.2)
        return VGroup(table, holo)

    def _icon_gamepad(self) -> VGroup:
        body = RoundedRectangle(width=0.8, height=0.35, corner_radius=0.15, color=WHITE)
        btns = VGroup(Dot(radius=0.04, color=WHITE).shift(LEFT*0.2), Dot(radius=0.04, color=WHITE).shift(RIGHT*0.2))
        return VGroup(body, btns)

    def _icon_tshirt_overlay(self) -> VGroup:
        shirt = VGroup(Rectangle(width=0.5, height=0.3, color=WHITE), Line(LEFT*0.25, RIGHT*0.25, color=WHITE).shift(UP*0.15))
        overlay = Square(0.18, color=WHITE).set_fill(WHITE, opacity=0.2).next_to(shirt, UP, buff=0.05)
        return VGroup(shirt, overlay)

    def _icon_heart_holo(self) -> VGroup:
        heart = VGroup(Arc(radius=0.12, start_angle=PI, angle=PI, color=WHITE).shift(LEFT*0.08), Arc(radius=0.12, start_angle=0, angle=PI, color=WHITE).shift(RIGHT*0.08), Polygon(LEFT*0.16, RIGHT*0.16, DOWN*0.2, color=WHITE))
        cross = VGroup(Line(LEFT*0.12, RIGHT*0.12, color=WHITE), Line(UP*0.12, DOWN*0.12, color=WHITE))
        return VGroup(heart, cross)

    def _icon_money(self) -> VGroup:
        bill = RoundedRectangle(width=0.6, height=0.3, corner_radius=0.06, color=WHITE)
        circle = Circle(radius=0.06, color=WHITE).move_to(bill.get_center())
        return VGroup(bill, circle)

    def _icon_face_dizzy(self) -> VGroup:
        face = Circle(radius=0.18, color=WHITE)
        eyes = VGroup(Line(LEFT*0.05+UP*0.05, RIGHT*0.05+DOWN*0.05, color=WHITE), Line(LEFT*0.05+DOWN*0.05, RIGHT*0.05+UP*0.05, color=WHITE))
        mouth = ArcBetweenPoints(LEFT*0.08, RIGHT*0.08, angle=-PI/4, color=WHITE)
        return VGroup(face, eyes, mouth)

    def _icon_lock(self) -> VGroup:
        lock = VGroup(
            RoundedRectangle(width=0.7, height=0.7, corner_radius=0.12, color=WHITE),
            ArcBetweenPoints(LEFT*0.25, RIGHT*0.25, angle=PI/1.2, color=WHITE).shift(UP*0.5),
            Dot(radius=0.05, color=WHITE)
        )
        return lock

    def _icon_box_apps(self) -> VGroup:
        grid = VGroup(*[Square(0.14, color=WHITE) for _ in range(6)]).arrange_in_grid(rows=2, cols=3, buff=0.06)
        return grid
