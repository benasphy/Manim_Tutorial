from manim import *

class RegexTutorial(Scene):
    def construct(self):
        # Scene 1 — What is Regex?
        title = Text("🔍 Regular Expressions (Regex)", font_size=42, color=BLUE)
        definition = Text("A powerful pattern-matching tool for text", font_size=28, color=WHITE)
        
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.play(Write(definition.next_to(title, DOWN, buff=0.5)))
        
        # Real-world examples
        examples = VGroup(
            Text("• Filtering emails by subject", font_size=24, color=YELLOW),
            Text("• Searching for text patterns", font_size=24, color=YELLOW),
            Text("• Validating phone numbers/emails", font_size=24, color=YELLOW),
            Text("• Extracting data from text", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(definition, DOWN, buff=1)
        
        self.play(LaggedStart(*[FadeIn(example, shift=RIGHT) for example in examples], lag_ratio=0.2))
        self.wait(1)
        
        # Clean up
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 2 — Simple Example
        title2 = Text("🔍 Simple Regex Example", font_size=42, color=BLUE)
        self.play(Write(title2))
        self.play(title2.animate.to_edge(UP))
        
        # Code example with exact format and better spacing
        code_lines = [
            "import re\n",
            "text = \"My name is Benjamin and my number is 12345\"\n",
            "pattern = r\"\\d+\"   # \\d+ means \"one or more digits\"\n\n",
            "match = re.findall(pattern, text)\n",
            "print(match)  # ['12345']"
        ]
        
        code_group = VGroup()
        for i, line in enumerate(code_lines):
            # Create text object for each line
            if line.strip() == "":
                code_group.add(Text(" ", font="Monospace", font_size=22))
            else:
                code_group.add(Text(line, font="Monospace", font_size=22, line_spacing=1.2))
        
        # Position the code block with more vertical space
        code_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title2, DOWN, buff=0.6)
        
        # Add output separately for better control
        output_text = Text("['12345']", font="Monospace", font_size=22, color=GREEN)
        output_text.next_to(code_group[-1], DOWN, aligned_edge=LEFT, buff=0.3)
        
        # Animate code line by line with output
        self.play(LaggedStart(
            *[FadeIn(line, shift=RIGHT) for line in code_group],
            lag_ratio=0.2
        ))
        self.play(Write(output_text))
        
        # Highlight the pattern in the code
        pattern_text = code_group[2][12:16]  # The "\d+" part
        pattern_box = SurroundingRectangle(pattern_text, color=YELLOW, buff=0.05)
        
        self.play(Create(pattern_box))
        self.wait(1)
        
        # Clean up
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 3 — How It Works
        title3 = Text("🧠 What's Happening Under the Hood", font_size=42, color=BLUE)
        self.play(Write(title3))
        self.play(title3.animate.to_edge(UP))
        
        # Text to search in with better spacing
        search_text = Text("My name is Benjamin and my number is 12345", 
                          font_size=26, color=WHITE)
        self.play(Write(search_text.next_to(title3, DOWN, buff=0.8)))
        
        # Pattern explanation
        pattern = Text(r"\d+", font="Monospace", font_size=36, color=YELLOW)
        pattern_label = Text("Pattern:", font_size=32, color=WHITE)
        pattern_group = VGroup(pattern_label, pattern).arrange(RIGHT, buff=0.5).next_to(search_text, DOWN, buff=1)
        
        self.play(Write(pattern_group))
        
        # Break down the pattern with better spacing
        breakdown = VGroup(
            Text(r"• \d   Matches any digit (0-9)", font_size=22, color=GREEN),
            Text(r"• +    Matches one or more of the", font_size=22, color=GREEN),
            Text(r"       previous element", font_size=22, color=GREEN),
            Text(r"• \\d+  Matches one or more digits", font_size=22, color=GREEN),
            Text(r"       (like 12345)", font_size=22, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(pattern_group, DOWN, buff=0.8)
        
        self.play(LaggedStart(*[FadeIn(item, shift=RIGHT) for item in breakdown], lag_ratio=0.3))
        self.wait(1)
        
        # Show matching animation
        match_text = search_text[-5:]
        match_box = SurroundingRectangle(match_text, color=GREEN, buff=0.1)
        
        self.play(Create(match_box))
        
        # Show the result with better spacing
        result = Text("Found: 12345", font_size=28, color=GREEN).next_to(breakdown, DOWN, buff=0.8)
        self.play(Write(result))
        self.wait(1)
        
        # Final explanation with better spacing
        final_text = Text("re.findall() scans the text and returns", 
                         font_size=26, color=YELLOW).next_to(result, DOWN, buff=0.8)
        final_text2 = Text("all matches as a list",
                         font_size=26, color=YELLOW).next_to(final_text, DOWN, buff=0.2)
        self.play(Write(VGroup(final_text, final_text2)))
        self.wait(2)
