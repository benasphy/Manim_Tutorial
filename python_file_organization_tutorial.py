from manim import *

class FileOrganizationTutorial(Scene):
    def construct(self):
        # Scene 1 — What is File Organization?
        title = Text("📂 File Organization in Python", font_size=42, color=BLUE)
        definition = Text("Reading, writing, and managing files", font_size=28, color=WHITE)
        
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.play(Write(definition.next_to(title, DOWN, buff=0.5)))
        
        # Key points
        points = VGroup(
            Text("• Store data permanently", font_size=24, color=YELLOW),
            Text("• Used for configs, logs, data", font_size=24, color=YELLOW),
            Text("• Like digital notebooks", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(definition, DOWN, buff=1)
        
        self.play(LaggedStart(*[FadeIn(point, shift=RIGHT) for point in points], lag_ratio=0.2))
        self.wait(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 2 — File Modes
        title2 = Text("🔓 File Modes", font_size=42, color=BLUE)
        self.play(Write(title2))
        self.play(title2.animate.to_edge(UP))
        
        # File modes
        modes = VGroup(
            Text('"r" → Read (default)', font="Monospace", font_size=24, color=WHITE),
            Text('"w" → Write (overwrites)', font="Monospace", font_size=24, color=WHITE),
            Text('"a" → Append (adds to end)', font="Monospace", font_size=24, color=WHITE),
            Text('"b" → Binary mode', font="Monospace", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title2, DOWN, buff=1)
        
        self.play(LaggedStart(*[FadeIn(mode, shift=RIGHT) for mode in modes], lag_ratio=0.2))
        self.wait(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 3 — Code Example
        title3 = Text("📝 Example: Writing to a File", font_size=42, color=BLUE)
        self.play(Write(title3))
        self.play(title3.animate.to_edge(UP))
        
        # Code with proper indentation
        code_lines = [
            "# Open file in write mode\n",
            "file = open(\"example.txt\", \"w\")",
            "file.write(\"Hello, Python!\")",
            "file.close()"
        ]
        
        code_group = VGroup(*[
            Text(line, font="Monospace", font_size=22,
                color=GRAY if i == 0 else WHITE)
            for i, line in enumerate(code_lines)
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title3, DOWN, buff=1)
        
        self.play(LaggedStart(*[FadeIn(line, shift=RIGHT) for line in code_group], lag_ratio=0.2))
        
        # Under the hood explanation
        explanation = VGroup(
            Text("Under the Hood:", font_size=28, color=YELLOW).to_edge(DOWN).shift(UP*0.5)
        )
        
        # Add explanation points one by one
        point1 = Text("1. open() connects to OS file system", font_size=22, color=WHITE)
        point1.next_to(explanation[0], DOWN, aligned_edge=LEFT)
        explanation.add(point1)
        
        point2 = Text("2. close() ensures data is saved", font_size=22, color=WHITE)
        point2.next_to(point1, DOWN, aligned_edge=LEFT)
        explanation.add(point2)
        
        # Animate explanation
        self.play(Write(explanation[0]))
        self.play(Write(explanation[1]))
        self.play(Write(explanation[2]))
        self.wait(2)
