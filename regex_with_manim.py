from manim import (
    Scene, Title, VGroup, Text, Tex,
    FadeIn, LaggedStartMap, Write, Indicate, SurroundingRectangle, Create,
    DOWN, UP, RIGHT, LEFT,
    GREEN, YELLOW
)
import re


class RegexIntro(Scene):
    """Part 1 — a single scene that explains what Regex is.
    Keeps the text large and simple for a slide-like appearance.
    """

    def construct(self):
        title = Title("What is Regex?")

        bullets = VGroup(
            Text("Regex = Regular Expressions", font_size=36),
            Text("Pattern-matching tool for searching, extracting, and manipulating strings", font_size=28),
            Text("Used in real life: email filters, search, validation (phone/email)", font_size=28),
            Text("In Python: provided by the re module (import re)", font_size=28),
        ).arrange(direction=DOWN, aligned_edge=LEFT, buff=0.6)

        bullets.move_to(DOWN * 0.5)

        self.play(FadeIn(title, shift=UP))
        self.play(LaggedStartMap(FadeIn, bullets, shift=RIGHT, lag_ratio=0.15))
        self.wait(2)

        # Small code hint shown at the bottom
        code_string = (
            'import re\n\n'
            'text = "My name is Benjamin and my number is 12345"\n'
            r'pattern = r"\d+"  # \d+ means "one or more digits"' + '\n\n'
            'match = re.findall(pattern, text)\n'
            "print(match)  # ['12345']"
        )
        code_text = Text(code_string, font="Courier", font_size=20)
        code_text.to_edge(DOWN)
        self.play(FadeIn(code_text, shift=DOWN))
        self.wait(3)


class RegexExampleSlide1(Scene):
    """Part 2 — Slide 1: show the example string and pattern and animate finding the digits."""

    def construct(self):
        title = Title("Example: A Simple Search")

        text = Text('My name is Benjamin and my number is 12345', font_size=30)
        pattern = Tex(r"Pattern: $\d+$", font_size=36)

        text.move_to(UP * 0.8)
        pattern.next_to(text, DOWN, buff=0.7)

        # Highlight the digits in the text by creating a copy and coloring digits
        digits = "12345"
        # create a submobject for the digits by locating them via substring slicing
        # We'll construct a surrounding rectangle for the digits to emphasize them
        digits_mob = Text(digits, font_size=30, color=YELLOW)
        digits_mob.move_to(text.get_center() + RIGHT * 3.5 + DOWN * 0.05)

        self.play(FadeIn(title))
        self.play(Write(text), run_time=2)
        self.play(Write(pattern))
        self.wait(0.8)

        # Emphasize digits and show extraction result
        self.play(Indicate(digits_mob, scale_factor=1.2))
        result_box = SurroundingRectangle(digits_mob, color=GREEN, buff=0.25)
        extracted_text = Text("re.findall(r'\\d+', text) → ['12345']", font="Courier", font_size=24, color=GREEN)
        extracted_text.next_to(pattern, DOWN, buff=1.0)

        self.play(FadeIn(digits_mob), Create(result_box))
        self.wait(0.5)
        self.play(FadeIn(extracted_text))
        self.wait(3)


class RegexExampleSlide2(Scene):
    """Part 2 — Slide 2: short explanation of the tokens used (\d and +) and the concept of findall."""

    def construct(self):
        title = Title("What \'s Happening Under the Hood?")

        lines = VGroup(
            Tex(r"\\d \rightarrow digit (0--9)", font_size=36),
            Tex(r"+ \rightarrow one or more times", font_size=36),
            Tex(r"Together: \\d+ finds whole numbers", font_size=36),
            Tex(r"re.findall scans the entire text and returns matches as a list", font_size=30),
        ).arrange(direction=DOWN, aligned_edge=LEFT, buff=0.6)

        lines.move_to(DOWN * 0.2)

        self.play(FadeIn(title))
        self.play(LaggedStartMap(FadeIn, lines, shift=RIGHT, lag_ratio=0.15))
        self.wait(2)

        closing = Text("Think of regex as a filter lens: only matching parts are caught.", font_size=26)
        closing.next_to(lines, DOWN, buff=0.8)
        self.play(FadeIn(closing))
        self.wait(3)
