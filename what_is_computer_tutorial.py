from manim import *

class WhatIsComputerTutorial(Scene):
    def construct(self):
        # Scene 1: What is a Computer? (Definition)
        self.definition_scene()
        self.clear()

        # Scene 2: Why is this important?
        self.why_important_scene()
        self.clear()

        # Final message
        self.final_message()

    def definition_scene(self):
        # Title
        title = Text("💻 What is a Computer?", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Narration lines
        narration = VGroup(
            Text("A computer is an electronic device that takes input,", font_size=28, color=WHITE),
            Text("processes it, stores it, and then produces output.", font_size=28, color=WHITE),
            Text("In simple words:", font_size=28, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=0.8)

        self.play(Write(narration[0]))
        self.play(Write(narration[1]))
        self.play(Write(narration[2]))
        self.wait(0.5)

        # Build IPO diagram: Input -> Process -> Storage -> Output
        input_box = self._labeled_box("Input", color=BLUE_D, icon=self._icon_keyboard())
        process_box = self._labeled_box("Process", color=GREEN_D, icon=self._icon_cpu())
        storage_box = self._labeled_box("Storage", color=PURPLE_D, icon=self._icon_storage())
        output_box = self._labeled_box("Output", color=YELLOW_D, icon=self._icon_monitor())

        chain = VGroup(input_box, process_box, storage_box, output_box).arrange(RIGHT, buff=0.8).next_to(narration, DOWN, buff=1)

        # Arrows
        arrows = VGroup(
            Arrow(input_box.get_right(), process_box.get_left(), buff=0.15, color=WHITE),
            Arrow(process_box.get_right(), storage_box.get_left(), buff=0.15, color=WHITE),
            Arrow(storage_box.get_right(), output_box.get_left(), buff=0.15, color=WHITE),
        )

        # Explanations under the chain
        explain = VGroup(
            Text("Input: The data you give it", font_size=24, color=WHITE),
            Text("Process: The brainwork it does", font_size=24, color=WHITE),
            Text("Storage: Where it remembers things", font_size=24, color=WHITE),
            Text("Output: The result you see", font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.8).next_to(chain, DOWN, buff=0.6)

        # Animate
        self.play(FadeIn(input_box, shift=UP))
        self.play(GrowArrow(arrows[0]), FadeIn(process_box, shift=UP))
        self.play(GrowArrow(arrows[1]), FadeIn(storage_box, shift=UP))
        self.play(GrowArrow(arrows[2]), FadeIn(output_box, shift=UP))
        self.wait(0.5)
        self.play(Write(explain))
        self.wait(2)

        # Principle line
        principle = Text("Every computer follows: Input → Process → Output", font_size=28, color=YELLOW)
        principle.next_to(explain, DOWN, buff=0.6)
        self.play(Write(principle))
        self.wait(2)

    def why_important_scene(self):
        # Title
        title = Text("🌍 Why is this Important?", font_size=48, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Paragraphs
        para1 = Text(
            "Understanding what a computer is and how it evolved helps us\n"
            "appreciate how far technology has come. The computer is not just a\n"
            "machine — it's the foundation of modern society.",
            font_size=26, color=WHITE, line_spacing=1.0
        ).next_to(title, DOWN, buff=0.8)

        domains = VGroup(
            self._domain_chip("Healthcare", BLUE),
            self._domain_chip("Education", YELLOW),
            self._domain_chip("Transportation", GREEN),
            self._domain_chip("Communication", PURPLE)
        ).arrange(RIGHT, buff=0.6).next_to(para1, DOWN, buff=0.6)

        para2 = Text(
            "And we're still in the middle of this journey: AI, quantum computing,\n"
            "and brain–computer interfaces will make the future even more revolutionary.",
            font_size=26, color=YELLOW, line_spacing=1.0
        ).next_to(domains, DOWN, buff=0.8)

        self.play(Write(para1))
        self.play(FadeIn(domains, shift=UP))
        self.play(Write(para2))
        self.wait(2)

        # Simple future icons row
        ai = self._labeled_box("AI", color=BLUE_E, icon=self._icon_brain())
        qc = self._labeled_box("Quantum", color=TEAL_E, icon=self._icon_atom())
        bci = self._labeled_box("BCI", color=MAROON_A, icon=self._icon_signal())
        future = VGroup(ai, qc, bci).arrange(RIGHT, buff=0.8).next_to(para2, DOWN, buff=0.8)

        self.play(FadeIn(future, shift=UP))
        self.wait(2)

    def final_message(self):
        final = Text("Computers power our world — and the future.", font_size=36, color=GREEN)
        self.play(Write(final))
        self.wait(2)
        self.play(FadeOut(final))

    # Helper shapes/icons built from basic primitives (no external SVGs)
    def _labeled_box(self, label: str, color=BLUE_D, icon: Mobject | None = None) -> VGroup:
        box = RoundedRectangle(width=3.2, height=2.0, corner_radius=0.2, color=color, fill_color=BLACK, fill_opacity=0.85)
        text = Text(label, font_size=26, color=color).next_to(box.get_bottom(), UP, buff=0.0)
        group = VGroup(box)
        if icon is not None:
            icon.scale(0.9).move_to(box.get_center()).shift(UP*0.2)
            group.add(icon)
        group.add(text)
        return group

    def _icon_keyboard(self) -> VGroup:
        body = RoundedRectangle(width=2.2, height=0.8, corner_radius=0.1, color=WHITE)
        keys = VGroup(*[
            RoundedRectangle(width=0.25, height=0.18, corner_radius=0.03, color=WHITE)
            for _ in range(10)
        ])
        keys.arrange(RIGHT, buff=0.05).move_to(body.get_center())
        return VGroup(body, keys)

    def _icon_cpu(self) -> VGroup:
        chip = RoundedRectangle(width=1.4, height=1.4, corner_radius=0.1, color=WHITE)
        pins_top = VGroup(*[Line(UP*0.2, UP*0.4, color=WHITE) for _ in range(6)]).arrange(RIGHT, buff=0.15).next_to(chip, UP, buff=0.02)
        pins_bottom = pins_top.copy().next_to(chip, DOWN, buff=0.02)
        pins_left = VGroup(*[Line(LEFT*0.2, LEFT*0.4, color=WHITE) for _ in range(6)]).arrange(DOWN, buff=0.15).next_to(chip, LEFT, buff=0.02)
        pins_right = pins_left.copy().next_to(chip, RIGHT, buff=0.02)
        text = Text("CPU", font_size=24, color=WHITE).move_to(chip.get_center())
        return VGroup(chip, pins_top, pins_bottom, pins_left, pins_right, text)

    def _icon_storage(self) -> VGroup:
        # Simple stacked drives icon
        base = RoundedRectangle(width=2.0, height=0.5, corner_radius=0.1, color=WHITE)
        mid = base.copy().shift(UP*0.35)
        top = base.copy().shift(UP*0.70)
        leds = VGroup(*[Dot(radius=0.03, color=GREEN).move_to(base.get_left()+RIGHT*(0.3+i*0.2)) for i in range(5)])
        return VGroup(base, mid, top, leds)

    def _icon_monitor(self) -> VGroup:
        screen = RoundedRectangle(width=2.2, height=1.3, corner_radius=0.08, color=WHITE)
        stand = VGroup(Rectangle(width=0.2, height=0.3, color=WHITE).next_to(screen, DOWN, buff=0.05),
                       Rectangle(width=0.8, height=0.08, color=WHITE).next_to(screen, DOWN, buff=0.25))
        return VGroup(screen, stand)

    def _domain_chip(self, label: str, color) -> VGroup:
        chip = RoundedRectangle(width=2.6, height=0.9, corner_radius=0.12, color=color, fill_color=BLACK, fill_opacity=0.85)
        text = Text(label, font_size=24, color=color).move_to(chip.get_center())
        return VGroup(chip, text)

    def _icon_brain(self) -> VGroup:
        # Abstract brain: two circles and paths
        left = Circle(radius=0.35, color=WHITE)
        right = Circle(radius=0.35, color=WHITE).next_to(left, RIGHT, buff=0.1)
        folds = VGroup(
            Arc(radius=0.25, start_angle=0, angle=PI, color=WHITE).move_to(left.get_center()+UP*0.05),
            Arc(radius=0.25, start_angle=0, angle=PI, color=WHITE).move_to(right.get_center()+DOWN*0.05)
        )
        return VGroup(left, right, folds).scale(0.9)

    def _icon_atom(self) -> VGroup:
        nucleus = Dot(radius=0.06, color=WHITE)
        orbit1 = Ellipse(width=0.9, height=0.4, color=WHITE)
        orbit2 = Ellipse(width=0.9, height=0.4, color=WHITE).rotate(PI/3)
        orbit3 = Ellipse(width=0.9, height=0.4, color=WHITE).rotate(-PI/3)
        return VGroup(nucleus, orbit1, orbit2, orbit3)

    def _icon_signal(self) -> VGroup:
        # Simple wireless signal icon
        base = Dot(radius=0.05, color=WHITE)
        arc1 = ArcBetweenPoints(LEFT*0.3, RIGHT*0.3, angle=PI/2, color=WHITE).shift(UP*0.15)
        arc2 = ArcBetweenPoints(LEFT*0.5, RIGHT*0.5, angle=PI/2, color=WHITE).shift(UP*0.35)
        arc3 = ArcBetweenPoints(LEFT*0.7, RIGHT*0.7, angle=PI/2, color=WHITE).shift(UP*0.6)
        return VGroup(base, arc1, arc2, arc3)
