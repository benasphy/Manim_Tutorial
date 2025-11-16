from manim import *

class GeneratorsTutorial(Scene):
    def construct(self):
        # Scene 1 — What Are Generators?
        title = Text("⚡ Python Generators", font_size=42, color=BLUE)
        definition = Text("Produce values one at a time instead of all at once", 
                         font_size=28, color=WHITE)
        
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.play(Write(definition.next_to(title, DOWN, buff=0.5)))
        
        # Water tap analogy
        tap_analogy = Text("Like a water tap: get values when needed, not all at once",
                         font_size=24, color=YELLOW).to_edge(DOWN)
        
        # Memory efficiency note
        memory_note = Text("• Memory-efficient for large datasets\n• Useful for infinite sequences",
                         font_size=26, color=GREEN).next_to(definition, DOWN, buff=1)
        
        self.play(Write(tap_analogy))
        self.play(Write(memory_note))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 2 — Generator Example
        title2 = Text("🔧 Generator Example", font_size=42, color=BLUE)
        self.play(Write(title2))
        self.play(title2.animate.to_edge(UP))
        
        # Code example
        code = """# A simple generator that yields numbers
def number_generator():
    for i in range(1, 6):
        yield i  # Pauses here, returns i

# Using the generator
for num in number_generator():
    print(num)  # Prints 1, 2, 3, 4, 5"""
        
        code_mobj = Text(code, font="Monospace", font_size=22, color=WHITE)
        code_mobj.next_to(title2, DOWN, buff=0.8)
        
        # Highlight the yield keyword
        yield_line = code_mobj[code.find('yield'):code.find('yield')+5]
        highlight = SurroundingRectangle(yield_line, color=YELLOW, buff=0.1)
        
        self.play(Write(code_mobj))
        self.play(Create(highlight))
        self.wait(1)
        
        # Expected output
        output = Text("Output:", font_size=24, color=GREEN).to_edge(LEFT).shift(UP*0.5)
        numbers = Text("1\n2\n3\n4\n5", font="Monospace", font_size=24, color=WHITE)
        numbers.next_to(output, RIGHT, buff=0.5)
        
        output_group = VGroup(output, numbers).to_edge(DOWN, buff=1)
        self.play(Write(output_group))
        
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 3 — Under the Hood (Part 1)
        title3 = Text("🔍 Under the Hood: How Generators Work", font_size=42, color=BLUE)
        self.play(Write(title3))
        self.play(title3.animate.to_edge(UP))
        
        # Bookmark analogy
        analogy = Text("Like a bookmark in a book:", font_size=32, color=YELLOW)
        points = VGroup(
            Text("• Function runs until yield", font_size=26, color=WHITE),
            Text("• Pauses and returns the value", font_size=26, color=WHITE),
            Text("• Remembers its state (variables, position)", font_size=26, color=WHITE),
            Text("• Resumes from where it left off", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        analogy_group = VGroup(analogy, points).arrange(DOWN, buff=0.5).next_to(title3, DOWN, buff=1)
        
        self.play(Write(analogy))
        self.play(LaggedStart(*[FadeIn(point, shift=RIGHT) for point in points], lag_ratio=0.3))
        self.wait(2)
        
        # Clear for next scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 4 — Memory Comparison
        title4 = Text("💾 Memory Comparison", font_size=42, color=BLUE)
        self.play(Write(title4))
        self.play(title4.animate.to_edge(UP))
        
        # Memory comparison
        comparison = VGroup(
            Text("List vs Generator", font_size=32, color=YELLOW),
            Text("List: [1, 2, 3, 4, 5]", font="Monospace", font_size=28, color=RED),
            Text("• Stores all values in memory", font_size=24, color=RED),
            Text("• Faster access to elements", font_size=24, color=RED),
            Text("Generator: (1) (2) (3) (4) (5)", font="Monospace", font_size=28, color=GREEN),
            Text("• Generates values on-the-fly", font_size=24, color=GREEN),
            Text("• Memory efficient for large data", font_size=24, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title4, DOWN, buff=1)
        
        self.play(Write(comparison[0]))
        self.play(Write(comparison[1:4]))
        self.wait(1)
        self.play(Write(comparison[4:]))
        self.wait(2)
        
        # Final note
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        final_note = Text("Generators are perfect for:", font_size=32, color=YELLOW).to_edge(UP)
        use_cases = VGroup(
            Text("• Processing large files", font_size=28, color=WHITE),
            Text("• Working with infinite sequences", font_size=28, color=WHITE),
            Text("• Memory-efficient data processing", font_size=28, color=WHITE),
            Text("• Pipelining data processing", font_size=28, color=WHITE),
            Text("• Working with data streams", font_size=28, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(final_note, DOWN, buff=1)
        
        self.play(Write(final_note))
        self.play(LaggedStart(*[Write(uc) for uc in use_cases], lag_ratio=0.3))
        self.wait(3)
