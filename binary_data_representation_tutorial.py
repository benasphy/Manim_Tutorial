from manim import *
import numpy as np

class BinaryDataRepresentationTutorial(Scene):
    def construct(self):
        # Scene 1: What is Binary?
        self.binary_intro_scene()
        self.clear()

        # Scene 2: Bits and Bytes
        self.bits_bytes_scene()
        self.clear()

        # Scene 3: Representing Characters: ASCII
        self.ascii_scene()
        self.clear()

        # Scene 4: Beyond English: Unicode
        self.unicode_scene()
        self.clear()

        # Scene 5: Images, Sound, Video
        self.media_scene()
        self.clear()

        # Scene 6: Closing
        self.closing_scene()
        self.clear()

    def binary_intro_scene(self):
        title = Text("1. What is Binary?", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        lines = VGroup(
            Text("Computers don't understand letters or pictures directly.", font_size=28, color=WHITE),
            Text("They understand electricity: ON or OFF.", font_size=28, color=WHITE),
            Text("We represent ON as 1 and OFF as 0.", font_size=28, color=YELLOW),
            Text("Using only 0 and 1 is called binary.", font_size=28, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(title, DOWN, buff=0.8)

        for line in lines:
            self.play(Write(line))
            self.wait(0.2)

        # Visual: switches and 0/1
        switches = VGroup(
            self._switch(on=True),
            self._switch(on=False),
            self._switch(on=True),
            self._switch(on=False)
        ).arrange(RIGHT, buff=0.6).next_to(lines, DOWN, buff=0.8)
        labels = VGroup(*[Text(val, font_size=28, color=WHITE) for val in ["1", "0", "1", "0"]])
        labels.arrange(RIGHT, buff=0.6).next_to(switches, DOWN, buff=0.2)

        self.play(FadeIn(switches, shift=UP))
        self.play(Write(labels))

        # Analogy: Morse code
        analogy_title = Text("Analogy: Morse code for computers", font_size=28, color=YELLOW)
        analogy_title.next_to(labels, DOWN, buff=0.6)
        morse = VGroup(
            *[VGroup(Dot(radius=0.06, color=WHITE), Line(ORIGIN, RIGHT*0.3, color=WHITE).shift(RIGHT*0.2)).arrange(RIGHT, buff=0.15) for _ in range(3)]
        ).arrange(RIGHT, buff=0.5).next_to(analogy_title, DOWN, buff=0.3)

        self.play(Write(analogy_title))
        self.play(FadeIn(morse, shift=UP))
        self.wait(2)

    def bits_bytes_scene(self):
        title = Text("2. Bits and Bytes", font_size=48, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("Bit = smallest unit: 0 or 1", font_size=28, color=WHITE),
            Text("Byte = 8 bits (e.g., 01000001)", font_size=28, color=WHITE),
            Text("8 bits → 256 values (0 to 255)", font_size=28, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        # Visual: one bit and one byte
        bit_sq = Square(0.6, color=WHITE)
        bit_txt = Text("1", font_size=28, color=WHITE)
        bit_txt.move_to(bit_sq.get_center())
        one_bit = VGroup(bit_sq, bit_txt).next_to(bullets, DOWN, buff=0.6)
        byte_bits = VGroup(*[Square(0.5, color=WHITE) for _ in range(8)]).arrange(RIGHT, buff=0.1)
        byte_values = ["0","1","0","0","0","0","0","1"]
        byte_texts = VGroup(*[Text(v, font_size=22, color=WHITE) for v in byte_values]).arrange(RIGHT, buff=0.1)
        byte_group = VGroup(byte_bits, byte_texts).arrange(DOWN, buff=0.1).next_to(one_bit, DOWN, buff=0.6)

        # Necklace analogy (beads)
        beads = VGroup(*[Dot(radius=0.08, color=WHITE) for _ in range(8)]).arrange(RIGHT, buff=0.15)
        beads.next_to(byte_group, DOWN, buff=0.5)

        self.play(FadeIn(one_bit, shift=UP))
        self.play(FadeIn(byte_group, shift=UP))
        self.play(Create(beads))
        self.wait(2)

    def ascii_scene(self):
        title = Text("3. Representing Characters: ASCII", font_size=46, color=BLUE_E)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("Early computers needed numbers for letters.", font_size=28, color=WHITE),
            Text("ASCII assigns numbers to letters and symbols.", font_size=28, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        # Examples: A = 65 = 01000001, B = 66 = 01000010
        example = VGroup(
            Text("A = 65 → 01000001", font_size=28, color=YELLOW),
            Text("B = 66 → 01000010", font_size=28, color=YELLOW)
        ).arrange(DOWN, buff=0.3).next_to(bullets, DOWN, buff=0.6)

        self.play(Write(example))

        # Visual: HELLO to binary (simplified placeholders for brevity)
        hello = Text("HELLO", font_size=36, color=WHITE)
        arrow = Arrow(LEFT*2, RIGHT*2, color=WHITE)
        binary_placeholder = Text("01001000 01000101 01001100 01001100 01001111", font_size=24, color=WHITE)
        flow = VGroup(hello, arrow, binary_placeholder).arrange(RIGHT, buff=0.5).next_to(example, DOWN, buff=0.8)

        self.play(Write(hello))
        self.play(GrowArrow(arrow))
        self.play(Write(binary_placeholder))
        self.wait(2)

    def unicode_scene(self):
        title = Text("4. Beyond English: Unicode", font_size=46, color=TEAL_E)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("ASCII was limited (128 chars).", font_size=28, color=WHITE),
            Text("Unicode covers all languages and symbols.", font_size=28, color=WHITE),
            Text("UTF-8 is widely used today.", font_size=28, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        # Analogy: dictionaries
        analogy = VGroup(
            self._book_icon(label="ASCII", width=2.4),
            self._book_icon(label="Unicode", width=3.6)
        ).arrange(RIGHT, buff=1.0).next_to(bullets, DOWN, buff=0.8)

        self.play(FadeIn(analogy, shift=UP))

        # Example of diverse characters
        samples = Text("你好 ሰላም مرحبا 😊", font_size=36, color=WHITE)
        samples.next_to(analogy, DOWN, buff=0.6)
        self.play(Write(samples))
        self.wait(2)

    def media_scene(self):
        title = Text("5. Images, Sound, Video", font_size=46, color=PURPLE_E)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("Images: grids of pixels (numbers for colors)", font_size=28, color=WHITE),
            Text("Sound: numbers representing waves", font_size=28, color=WHITE),
            Text("Video: sequences of images + sound", font_size=28, color=WHITE),
            Text("At the deepest level: all 0s and 1s.", font_size=28, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        # Visuals row: image grid, waveform, film strip
        image_grid = self._pixel_grid(rows=5, cols=8, cell=0.22)
        waveform = self._waveform(width=4.0, height=1.2)
        film = self._film_strip(frames=5, width=4.5, height=1.4)

        visuals = VGroup(image_grid, waveform, film).arrange(RIGHT, buff=0.8).next_to(bullets, DOWN, buff=0.8)
        self.play(FadeIn(visuals, shift=UP))
        self.wait(2)

        punch = Text("Everything digital is just binary in different costumes.", font_size=28, color=YELLOW)
        punch.next_to(visuals, DOWN, buff=0.8)
        self.play(Write(punch))
        self.wait(2)

    def closing_scene(self):
        title = Text("6. Closing", font_size=44, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        closing = Text(
            "Computers only understand 0s and 1s — but with clever systems like\n"
            "ASCII and Unicode, they can represent any letter, image, sound, or\n"
            "video. And all of that data is brought to life by hardware (the body)\n"
            "and software (the mind).",
            font_size=26, color=WHITE, line_spacing=1.0
        ).next_to(title, DOWN, buff=0.8)
        self.play(Write(closing))
        self.wait(3)

    # Helper visuals
    def _switch(self, on: bool = True) -> VGroup:
        base = RoundedRectangle(width=1.2, height=0.6, corner_radius=0.3, color=WHITE)
        knob = Circle(radius=0.22, color=WHITE, fill_color=WHITE, fill_opacity=1.0)
        if on:
            base.set_fill(GREEN, opacity=0.6)
            knob.move_to(base.get_right()).shift(LEFT*0.25)
        else:
            base.set_fill(GRAY, opacity=0.6)
            knob.move_to(base.get_left()).shift(RIGHT*0.25)
        return VGroup(base, knob)

    def _book_icon(self, label: str, width: float = 3.0) -> VGroup:
        cover = RoundedRectangle(width=width, height=1.6, corner_radius=0.1, color=WHITE)
        spine = Rectangle(width=0.15, height=1.6, color=WHITE).next_to(cover, LEFT, buff=0)
        text = Text(label, font_size=22, color=WHITE).move_to(cover.get_center())
        return VGroup(cover, spine, text)

    def _pixel_grid(self, rows=6, cols=10, cell=0.2) -> VGroup:
        grid = VGroup()
        # Use a predefined palette to avoid reliance on Color()
        palette = [RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, PURPLE, PINK]
        for r in range(rows):
            for c in range(cols):
                fill_col = palette[(r * cols + c) % len(palette)]
                sq = Square(cell, color=WHITE)
                sq.set_fill(fill_col, opacity=0.9)
                sq.move_to(RIGHT * (c * cell) + DOWN * (r * cell))
                grid.add(sq)
        grid.center()
        grid.arrange_in_grid(rows=rows, cols=cols, buff=0.04)
        return grid

    def _waveform(self, width=4.0, height=1.0) -> VGroup:
        # Simple sampled waveform polyline
        samples = []
        N = 40
        for i in range(N+1):
            x = i / N
            y = 0.4 * np.sin(2*PI*2*x) * (1 - 0.3*np.cos(2*PI*x))
            samples.append(np.array([x*width - width/2, y*height, 0]))
        poly = VMobject(color=WHITE)
        poly.set_points_as_corners(samples)
        axis = Line(LEFT*width/2, RIGHT*width/2, color=GRAY_A)
        return VGroup(axis, poly)

    def _film_strip(self, frames=5, width=5.0, height=1.4) -> VGroup:
        strip = RoundedRectangle(width=width, height=height, corner_radius=0.05, color=WHITE)
        frame_width = (width - 0.6) / frames
        frame_rects = VGroup()
        for i in range(frames):
            fr = Rectangle(width=frame_width, height=height-0.4, color=WHITE)
            fr.move_to(LEFT*(width/2 - 0.3 - frame_width/2 - i*frame_width))
            frame_rects.add(fr)
        frame_rects.arrange(RIGHT, buff=0.0).move_to(strip.get_center())
        return VGroup(strip, frame_rects)
