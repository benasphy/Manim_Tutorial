from manim import *
import re

class RegexTutorial(Scene):
    def construct(self):
        self.scene1_intro()
        self.clear()
        self.scene2_under_the_hood()
    
    def create_code_snippet(self, code_str):
        # Create a styled code block using Text
        code = Text(code_str, font="Monospace", font_size=24, color=WHITE)
        code.background_rectangle = SurroundingRectangle(
            code, color=GREY, fill_color=BLACK, fill_opacity=1, buff=0.3
        )
        code_group = VGroup(code.background_rectangle, code)
        return code_group
    
    def scene1_intro(self):
        # Title and subtitle
        title = Text("Regular Expressions (Regex)", font_size=48, color=BLUE)
        subtitle = Text("Pattern matching in Python", font_size=32, color=YELLOW)
        subtitle.next_to(title, DOWN)
        self.play(Write(title), Write(subtitle))
        
        # Example code
        code = '''import re

text = "My name is Benjamin and my number is 12345"
pattern = r"\\d+"  # Matches digits

matches = re.findall(pattern, text)
print(matches)  # Output: ['12345']'''
        
        code_mobj = self.create_code_snippet(code).next_to(subtitle, DOWN, buff=1)
        self.play(FadeIn(code_mobj))
        
        # Highlight pattern and output
        # Find the pattern in the code text
        code_text = code_mobj[1]  # The Text object is the second element in the VGroup
        pattern_start = code_text.text.find(r'\d+')
        pattern_end = pattern_start + len(r'\d+')
        
        # Create a rectangle around the pattern
        pattern_box = SurroundingRectangle(
            code_text[pattern_start:pattern_end],
            color=YELLOW,
            buff=0.1
        )
        
        output = Text("Output: ['12345']", font="Monospace", color=GREEN)
        output.next_to(code_mobj, DOWN, buff=0.5)
        
        self.play(Create(pattern_box))
        self.play(Write(output))
        self.wait(2)
    
    def scene2_under_the_hood(self):
        title = Text("How Regex Works", font_size=48, color=BLUE)
        self.play(Write(title))
        
        # Pattern breakdown
        text = Text("12345", font="Monospace", font_size=36)
        pattern = Text(r"\d+", font="Monospace", font_size=36, color=YELLOW)
        group = VGroup(text, pattern).arrange(DOWN, buff=1).next_to(title, DOWN, buff=1)
        
        self.play(Write(group))
        
        # Explanation
        explanation = VGroup(
            Text(r"• \d  matches any digit (0-9)", font_size=28),
            Text(r"• +   means 'one or more' of the previous element", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(group, DOWN, buff=1)
        
        self.play(Write(explanation[0]))
        self.play(Write(explanation[1]))
        
        # Match visualization
        digits = [Text(d, font_size=36, color=GREEN) for d in "12345"]
        # Position digits in a horizontal line below the explanation
        for i, digit in enumerate(digits):
            digit.move_to(RIGHT * (i - 2) * 0.5 + DOWN * 2)
            digit.set_opacity(0)
            self.add(digit)
        
        # Animate matching
        for digit in digits:
            self.play(digit.animate.set_opacity(1), run_time=0.5)
        
        self.wait(2)

# Run with: manim -pql regex_tutorial.py RegexTutorial
