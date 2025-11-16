from manim import *

class PythonKeywordsTutorial(Scene):
    def construct(self):
        # Scene 1 — What are Keywords?
        title = Text("🔑 Python Keywords", font_size=42, color=BLUE)
        definition = Text("Reserved words with special meanings in Python", 
                         font_size=28, color=WHITE)
        
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.play(Write(definition.next_to(title, DOWN, buff=0.5)))
        
        # Key points
        points = VGroup(
            Text("• Control program flow and structure", font_size=24, color=YELLOW),
            Text("• Cannot be used as variable/function names", font_size=24, color=YELLOW),
            Text("• Examples: if, else, True, False, while, class, def", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(definition, DOWN, buff=1)
        
        self.play(LaggedStart(*[FadeIn(point, shift=RIGHT) for point in points], lag_ratio=0.2))
        self.wait(1)
        
        # Clean up
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 2 — Examples
        title2 = Text("📝 Examples of Python Keywords", font_size=42, color=BLUE)
        self.play(Write(title2))
        self.play(title2.animate.to_edge(UP))
        
        # Code example 1 - Valid usage
        code1_lines = [
            "# Example 1: Using keywords correctly\n",
            "if True:",
            "    print(\"This is valid!\")"
        ]
        
        code1_group = VGroup(*[
            Text(line, font="Monospace", font_size=22, color=WHITE) 
            for line in code1_lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title2, DOWN, buff=0.8)
        
        # Code example 2 - Invalid usage
        code2_lines = [
            "\n# Example 2: Invalid usage\n",
            "def = 5   # ❌ SyntaxError: invalid syntax"
        ]
        
        code2_group = VGroup(*[
            Text(line, font="Monospace", font_size=22, color=RED if i > 0 else WHITE) 
            for i, line in enumerate(code2_lines)
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(code1_group, DOWN, buff=0.8)
        
        # Animate code examples
        self.play(LaggedStart(
            *[FadeIn(line, shift=RIGHT) for line in code1_group],
            lag_ratio=0.2
        ))
        self.wait(0.5)
        
        self.play(LaggedStart(
            *[FadeIn(line, shift=RIGHT) for line in code2_group],
            lag_ratio=0.2
        ))
        self.wait(1)
        
        # Clean up
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 3 — Under the Hood
        title3 = Text("⚙️ Under the Hood: Python's Keyword System", font_size=42, color=BLUE)
        self.play(Write(title3))
        self.play(title3.animate.to_edge(UP))
        
        # Explanation
        explanation = VGroup(
            Text("Python maintains a list of reserved keywords", font_size=26, color=WHITE),
            Text("These words have special meaning in the language", font_size=26, color=WHITE),
            Text("Trying to use them as variable names causes a SyntaxError", font_size=26, color=RED)
        ).arrange(DOWN, buff=0.5).next_to(title3, DOWN, buff=1)
        
        self.play(LaggedStart(
            *[FadeIn(line, shift=UP) for line in explanation],
            lag_ratio=0.3
        ))
        
        # Show how to list all keywords
        code_lines = [
            "# View all Python keywords\n",
            "import keyword\n",
            "print(keyword.kwlist)"
        ]
        
        code_group = VGroup(*[
            Text(line, font="Monospace", font_size=22, color=YELLOW if i > 0 else WHITE)
            for i, line in enumerate(code_lines)
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(explanation, DOWN, buff=1)
        
        self.play(Write(code_group))
        self.wait(1)
        
        # Final note
        final_note = Text("Remember: Keywords are like the grammar rules of Python!", 
                         font_size=28, color=GREEN).next_to(code_group, DOWN, buff=1)
        self.play(Write(final_note))
        self.wait(2)
