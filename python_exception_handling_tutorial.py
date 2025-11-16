from manim import *

class ExceptionHandlingTutorial(Scene):
    def construct(self):
        # Scene 1 — Introduction
        title = Text("🚨 Python Exception Handling", font_size=42, color=RED)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Main explanation
        explanation = Text("What happens when things go wrong?", font_size=32, color=WHITE)
        self.play(Write(explanation.next_to(title, DOWN, buff=0.8)))
        
        # Airbag analogy
        analogy = Text("Like airbags in a car:", font_size=28, color=YELLOW)
        points = VGroup(
            Text("• Unexpected things happen", font_size=24, color=WHITE),
            Text("• Instead of crashing badly", font_size=24, color=WHITE),
            Text("• We handle it gracefully", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        analogy_group = VGroup(analogy, points).arrange(DOWN, buff=0.5).next_to(explanation, DOWN, buff=1)
        self.play(Write(analogy_group))
        self.wait(2)
        
        # Common exceptions
        exceptions = VGroup(
            Text("Common exceptions:", font_size=28, color=YELLOW),
            Text("• ZeroDivisionError: 10 / 0", font="Monospace", font_size=24, color=WHITE),
            Text("• FileNotFoundError: open('missing.txt')", font="Monospace", font_size=24, color=WHITE),
            Text("• ValueError: int('abc')", font="Monospace", font_size=24, color=WHITE),
            Text("• IndexError: [1,2,3][10]", font="Monospace", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(analogy_group, DOWN, buff=1)
        
        self.play(Write(exceptions))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 2 — Basic Example
        title2 = Text("🔧 Basic Exception Handling", font_size=42, color=BLUE)
        self.play(Write(title2))
        self.play(title2.animate.to_edge(UP))
        
        # Code example
        code = """try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
except ZeroDivisionError:
    print("Can't divide by zero!")
except ValueError:
    print("Please enter a valid number!")"""
        
        code_mobj = Text(code, font="Monospace", font_size=22, color=WHITE)
        code_mobj.next_to(title2, DOWN, buff=0.8)
        
        # Highlight the try-except blocks
        try_block = SurroundingRectangle(
            VGroup(*code_mobj[code.find('try'):code.find('except')]), 
            color=GREEN, buff=0.1, corner_radius=0.1
        )
        except_blocks = VGroup(
            SurroundingRectangle(
                VGroup(*code_mobj[code.find('except Zero'):code.find('except Value')]), 
                color=RED, buff=0.1, corner_radius=0.1
            ),
            SurroundingRectangle(
                VGroup(*code_mobj[code.find('except Value'):]), 
                color=RED, buff=0.1, corner_radius=0.1
            )
        )
        
        self.play(Write(code_mobj))
        self.play(Create(try_block))
        self.wait(0.5)
        self.play(ReplacementTransform(try_block, except_blocks[0]))
        self.wait(0.5)
        self.play(ReplacementTransform(except_blocks[0], except_blocks[1]))
        self.wait(0.5)
        self.play(FadeOut(except_blocks[1]))
        
        # Example runs
        examples = VGroup(
            Text("Example runs:", font_size=28, color=YELLOW).to_edge(LEFT).shift(UP*0.5),
            Text("Input: 2\nOutput: 5.0", font="Monospace", font_size=22, color=GREEN),
            Text("Input: 0\nOutput: Can't divide by zero!", font="Monospace", font_size=22, color=RED),
            Text("Input: 'abc'\nOutput: Please enter a valid number!", font="Monospace", font_size=22, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(code_mobj, DOWN, buff=1)
        
        self.play(Write(examples[0]))
        self.play(Write(examples[1]))
        self.wait(0.5)
        self.play(Write(examples[2]))
        self.wait(0.5)
        self.play(Write(examples[3]))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 3 — Under the Hood
        title3 = Text("🔍 Under the Hood", font_size=42, color=BLUE)
        self.play(Write(title3))
        self.play(title3.animate.to_edge(UP))
        
        # Exception flow
        flow = VGroup(
            Text("What happens when an error occurs:", font_size=32, color=YELLOW),
            Text("1. Python creates an Exception object", font_size=26, color=WHITE),
            Text("2. It looks for an except block that matches", font_size=26, color=WHITE),
            Text("3. If found, runs that block and continues", font_size=26, color=GREEN),
            Text("4. If not, program crashes with traceback", font_size=26, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(title3, DOWN, buff=1)
        
        self.play(Write(flow[0:2]))
        self.wait(0.5)
        self.play(Write(flow[2:4]))
        self.wait(0.5)
        self.play(Write(flow[4]))
        
        # Best practices
        practices = VGroup(
            Text("\nBest Practices:", font_size=28, color=YELLOW),
            Text("• Be specific with exception types", font_size=24, color=WHITE),
            Text("• Don't use bare except:", font_size=24, color=WHITE),
            Text("• Include helpful error messages", font_size=24, color=WHITE),
            Text("• Clean up resources with finally:", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(DOWN, buff=1)
        
        self.play(Write(practices))
        self.wait(3)
        
        # Final slide
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        final = VGroup(
            Text("Key Takeaways", font_size=42, color=BLUE),
            Text("• Exceptions handle unexpected situations", font_size=32, color=WHITE),
            Text("• Use try/except to prevent crashes", font_size=32, color=WHITE),
            Text("• Be specific about which exceptions to catch", font_size=32, color=WHITE),
            Text("• Clean up resources in finally blocks", font_size=32, color=WHITE)
        ).arrange(DOWN, buff=0.6, aligned_edge=LEFT).scale(0.9)
        
        self.play(Write(final[0]))
        self.play(LaggedStart(*[Write(p) for p in final[1:]], lag_ratio=0.3))
        self.wait(3)
