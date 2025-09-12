from manim import *

class ComputerComponentsTutorial(Scene):
    def construct(self):
        # Scene 1: Why These Components Matter
        self.components_scene()
        self.clear()

        # Scene 2: Closing / Teaser
        self.closing_scene()
        self.clear()

    def components_scene(self):
        # Title
        title = Text("🧩 Computer Components — Why They Matter", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        intro = Text(
            "Computers aren't magic — they're specialized parts working in harmony.",
            font_size=28, color=WHITE
        ).next_to(title, DOWN, buff=0.6)
        self.play(Write(intro))

        # Create component cards (icons + labels + short description)
        cpu = self.card("CPU", "The computer thinks", self._icon_cpu(), color=BLUE_E)
        ram = self.card("RAM", "Short-term memory", self._icon_ram(), color=GREEN_E)
        storage = self.card("Storage", "Long-term memory", self._icon_storage(), color=PURPLE_E)
        mobo = self.card("Motherboard", "Connects everything", self._icon_motherboard(), color=TEAL_E)
        gpu = self.card("GPU", "Paints the pictures", self._icon_gpu(), color=MAROON_E)
        input_dev = self.card("Input", "You → Computer", self._icon_input_devices(), color=YELLOW_E)
        output_dev = self.card("Output", "Computer → You", self._icon_output_devices(), color=ORANGE)

        grid_top = VGroup(cpu, ram, storage).arrange(RIGHT, buff=0.7)
        grid_mid = VGroup(mobo).arrange(RIGHT, buff=0.7)
        grid_bot = VGroup(gpu, input_dev, output_dev).arrange(RIGHT, buff=0.7)

        grid = VGroup(grid_top, grid_mid, grid_bot).arrange(DOWN, buff=0.8).next_to(intro, DOWN, buff=0.8)

        # Animate appearance
        self.play(FadeIn(grid_top, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(grid_mid, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(grid_bot, shift=UP))
        self.wait(0.8)

        # Draw connections (motherboard in center connects others)
        connections = VGroup(
            Arrow(mobo.get_top(), cpu.get_bottom(), buff=0.2, color=GRAY),
            Arrow(mobo.get_top(), ram.get_bottom(), buff=0.2, color=GRAY),
            Arrow(mobo.get_top(), storage.get_bottom(), buff=0.2, color=GRAY),
            Arrow(mobo.get_bottom(), gpu.get_top(), buff=0.2, color=GRAY),
            Arrow(mobo.get_bottom(), input_dev.get_top(), buff=0.2, color=GRAY),
            Arrow(mobo.get_bottom(), output_dev.get_top(), buff=0.2, color=GRAY),
        )
        self.play(LaggedStart(*[GrowArrow(a) for a in connections], lag_ratio=0.1, run_time=2))
        self.wait(1)

        # Narration bullets
        bullets = VGroup(
            Text("• CPU thinks.", font_size=26, color=WHITE),
            Text("• RAM remembers short-term.", font_size=26, color=WHITE),
            Text("• Storage remembers long-term.", font_size=26, color=WHITE),
            Text("• Motherboard connects everything.", font_size=26, color=WHITE),
            Text("• GPU paints the pictures.", font_size=26, color=WHITE),
            Text("• Input devices let you talk to the computer.", font_size=26, color=WHITE),
            Text("• Output devices let the computer talk back to you.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        bullets.next_to(grid, DOWN, buff=0.8)

        self.play(Write(bullets[0]))
        for i in range(1, len(bullets)):
            self.play(Write(bullets[i]))
            self.wait(0.1)
        self.wait(1.5)

        # Recognition line
        line = Text(
            "Once you know these building blocks, you can look at any device\n"
            "— laptop, gaming PC, smartphone — and recognize what's inside.",
            font_size=26, color=YELLOW, line_spacing=1.0
        ).next_to(bullets, DOWN, buff=0.8)
        self.play(Write(line))
        self.wait(2)

    def closing_scene(self):
        title = Text("Closing", font_size=44, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        closing = Text(
            "So next time you press a key, click your mouse, or open a game,\n"
            "you'll know exactly which part of the computer is at work.\n\n"
            "In the next lesson, we'll dive into how these parts communicate —\n"
            "and trust me, it's even more fascinating.",
            font_size=28, color=WHITE, line_spacing=1.05
        ).next_to(title, DOWN, buff=0.8)

        self.play(Write(closing))
        self.wait(3)

    # Helper: component card (icon + label + description)
    def card(self, label: str, desc: str, icon: Mobject, color=BLUE):
        box = RoundedRectangle(width=3.6, height=2.6, corner_radius=0.15, color=color, fill_color=BLACK, fill_opacity=0.85)
        title = Text(label, font_size=24, color=color).next_to(box.get_top(), DOWN, buff=0.05)
        description = Text(desc, font_size=20, color=WHITE).next_to(box.get_bottom(), UP, buff=0.6)
        icon_group = icon.copy().scale(0.9).move_to(box.get_center()).shift(UP*0.2)
        return VGroup(box, icon_group, title, description)

    # Icons built from primitives to avoid external assets
    def _icon_cpu(self) -> VGroup:
        chip = RoundedRectangle(width=1.6, height=1.6, corner_radius=0.12, color=WHITE)
        pins_top = VGroup(*[Line(UP*0.22, UP*0.42, color=WHITE) for _ in range(6)]).arrange(RIGHT, buff=0.16).next_to(chip, UP, buff=0.02)
        pins_bottom = pins_top.copy().next_to(chip, DOWN, buff=0.02)
        pins_left = VGroup(*[Line(LEFT*0.22, LEFT*0.42, color=WHITE) for _ in range(6)]).arrange(DOWN, buff=0.16).next_to(chip, LEFT, buff=0.02)
        pins_right = pins_left.copy().next_to(chip, RIGHT, buff=0.02)
        text = Text("CPU", font_size=20, color=WHITE).move_to(chip.get_center())
        return VGroup(chip, pins_top, pins_bottom, pins_left, pins_right, text)

    def _icon_ram(self) -> VGroup:
        module = RoundedRectangle(width=2.2, height=0.7, corner_radius=0.1, color=WHITE)
        chips = VGroup(*[RoundedRectangle(width=0.3, height=0.4, corner_radius=0.05, color=WHITE) for _ in range(4)])
        chips.arrange(RIGHT, buff=0.15).move_to(module.get_center())
        notches = VGroup(Line(DOWN*0.15, UP*0.15, color=WHITE).move_to(module.get_bottom()+UP*0.05))
        return VGroup(module, chips, notches)

    def _icon_storage(self) -> VGroup:
        base = RoundedRectangle(width=2.0, height=0.5, corner_radius=0.1, color=WHITE)
        mid = base.copy().shift(UP*0.35)
        top = base.copy().shift(UP*0.70)
        leds = VGroup(*[Dot(radius=0.03, color=GREEN).move_to(base.get_left()+RIGHT*(0.3+i*0.2)) for i in range(5)])
        return VGroup(base, mid, top, leds)

    def _icon_motherboard(self) -> VGroup:
        board = RoundedRectangle(width=2.4, height=1.6, corner_radius=0.1, color=WHITE)
        socket = Square(0.5, color=WHITE).move_to(board.get_center()+LEFT*0.5)
        slots = VGroup(
            Line(LEFT*0.4, RIGHT*0.4, color=WHITE).shift(UP*0.4),
            Line(LEFT*0.4, RIGHT*0.4, color=WHITE),
            Line(LEFT*0.4, RIGHT*0.4, color=WHITE).shift(DOWN*0.4),
        ).move_to(board.get_center()+RIGHT*0.5)
        traces = VGroup(*[Line(ORIGIN, RIGHT*0.4, color=GRAY_A).shift(UP*(i*0.15-0.3)) for i in range(5)])
        traces.move_to(board.get_center())
        return VGroup(board, socket, slots, traces)

    def _icon_gpu(self) -> VGroup:
        body = RoundedRectangle(width=2.0, height=1.0, corner_radius=0.1, color=WHITE)
        fan = VGroup(Circle(radius=0.25, color=WHITE), *[Line(ORIGIN, UP*0.3, color=WHITE).rotate(i*PI/3) for i in range(6)])
        fan.move_to(body.get_center())
        bracket = Rectangle(width=0.2, height=1.0, color=WHITE).next_to(body, LEFT, buff=0)
        return VGroup(body, fan, bracket)

    def _icon_input_devices(self) -> VGroup:
        keyboard = RoundedRectangle(width=1.6, height=0.5, corner_radius=0.08, color=WHITE)
        keys = VGroup(*[Square(0.12, color=WHITE) for _ in range(12)]).arrange(RIGHT, buff=0.04).move_to(keyboard.get_center())
        mouse = VGroup(RoundedRectangle(width=0.35, height=0.5, corner_radius=0.18, color=WHITE), Line(UP*0.08, DOWN*0.08, color=WHITE)).next_to(keyboard, RIGHT, buff=0.2)
        return VGroup(keyboard, keys, mouse)

    def _icon_output_devices(self) -> VGroup:
        monitor = RoundedRectangle(width=1.6, height=0.9, corner_radius=0.08, color=WHITE)
        stand = VGroup(Rectangle(width=0.12, height=0.22, color=WHITE).next_to(monitor, DOWN, buff=0.04),
                       Rectangle(width=0.5, height=0.06, color=WHITE).next_to(monitor, DOWN, buff=0.22))
        speaker = VGroup(Rectangle(width=0.25, height=0.5, color=WHITE), Circle(radius=0.07, color=WHITE)).next_to(monitor, RIGHT, buff=0.2)
        return VGroup(monitor, stand, speaker)
