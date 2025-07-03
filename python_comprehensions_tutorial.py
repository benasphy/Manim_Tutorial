from manim import *

class PythonComprehensionsTutorial(Scene):
    def construct(self):
        # Scene 1.1 - Introduction
        title = Text("List & Dictionary Comprehensions", font_size=42, color=BLUE)
        self.play(Write(title))
        
        points = VGroup(
            Text("• Create collections in one line", font_size=24, color=YELLOW),
            Text("• More readable than loops", font_size=24, color=YELLOW),
            Text("• Faster execution", font_size=24, color=YELLOW)
        ).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=1)
        
        self.play(LaggedStart(*[Write(p) for p in points], lag_ratio=0.3))
        self.wait(2)
        self.clear()
        
        # Scene 1.2 - List Comprehension
        title2 = Text("List Comprehension", font_size=40, color=GREEN)
        title2.to_edge(UP)
        
        format_code = Text(
            "[expression for item in iterable if condition]",
            font="Monospace",
            font_size=24,
            color=GREEN
        ).next_to(title2, DOWN, buff=1)
        
        self.play(Write(title2), Write(format_code))
        
        # Example
        example = Text("squares = [x**2 for x in range(5)]", 
                      font="Monospace", font_size=24, color=YELLOW)
        output = Text("→ [0, 1, 4, 9, 16]", font_size=24, color=GREEN)
        example_group = VGroup(example, output).arrange(RIGHT, buff=0.5).next_to(format_code, DOWN, buff=1)
        
        self.play(Write(example_group))
        self.wait(2)
        self.clear()
        
        # Scene 1.3 - Dictionary Comprehension
        title3 = Text("Dictionary Comprehension", font_size=40, color=ORANGE)
        title3.to_edge(UP)
        
        dict_format = Text(
            "{key: value for item in iterable if condition}",
            font="Monospace",
            font_size=24,
            color=ORANGE
        ).next_to(title3, DOWN, buff=1)
        
        self.play(Write(title3), Write(dict_format))
        
        # Example
        dict_example = Text("squares = {x: x**2 for x in range(5)}", 
                           font="Monospace", font_size=24, color=YELLOW)
        dict_output = Text("→ {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}", 
                          font_size=24, color=GREEN)
        dict_group = VGroup(dict_example, dict_output).arrange(RIGHT, buff=0.5)
        dict_group.next_to(dict_format, DOWN, buff=1)
        
        self.play(Write(dict_group))
        self.wait(2)
        
        # Scene 2 - Under the Hood
        self.clear()
        title4 = Text("Under the Hood", font_size=42, color=BLUE)
        self.play(Write(title4))
        
        # List comprehension vs loop
        loop_code = '''# Traditional loop
squares = []
for x in range(5):
    squares.append(x ** 2)'''
        
        comp_code = '''# List comprehension
squares = [x**2 for x in range(5)]'''
        
        loop_text = Text(loop_code, font="Monospace", font_size=18, color=GRAY)
        comp_text = Text(comp_code, font="Monospace", font_size=18, color=GREEN)
        
        comparison = VGroup(loop_text, comp_text).arrange(RIGHT, buff=1).scale(0.8)
        comparison.next_to(title4, DOWN, buff=1)
        
        self.play(Write(comparison))
        
        self.wait(2)
        self.clear()
        
        # Scene 3 - Memory Layout Introduction
        title5 = Text("Memory Layout", font_size=42, color=BLUE)
        subtitle = Text("How Python stores list and dictionary comprehensions", 
                      font_size=24, color=WHITE, line_spacing=1.2)
        subtitle.next_to(title5, DOWN, buff=0.7)
        
        self.play(Write(title5))
        self.play(Write(subtitle))
        self.wait(1)
        
        # Explanation of memory layout
        explanation = VGroup(
            Text("• List comprehensions create a new list object", font_size=22, color=WHITE),
            Text("• Dictionary comprehensions create a new dict object", font_size=22, color=WHITE),
            Text("• Both are stored differently in memory", font_size=22, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(subtitle, DOWN, buff=1)
        
        self.play(Write(explanation))
        self.wait(2)
        self.clear()
        
        # Scene 4 - Memory Visualization
        title6 = Text("Memory Visualization", font_size=40, color=BLUE)
        title6.to_edge(UP)
        self.play(Write(title6))
        
        # List comprehension visualization
        list_title = Text("List Comprehension", font_size=26, color=GREEN)
        list_title.next_to(title6, DOWN, buff=1).to_edge(LEFT, buff=1)
        
        list_cells = VGroup()
        for i in range(5):
            cell = VGroup(
                Rectangle(width=1.2, height=0.8, fill_color=GREEN, 
                         fill_opacity=0.2, stroke_width=1, stroke_color=GREEN),
                Text(f"{i**2}", font_size=18)
            )
            list_cells.add(cell)
        
        list_cells.arrange(RIGHT, buff=0.1).next_to(list_title, DOWN, buff=0.7)
        
        # Dictionary comprehension visualization
        dict_title = Text("Dictionary Comprehension", font_size=26, color=ORANGE)
        dict_title.next_to(list_cells, DOWN, buff=1.5).to_edge(LEFT, buff=1)
        
        dict_cells = VGroup()
        for i in range(5):
            cell = VGroup(
                Rectangle(width=1.8, height=0.8, fill_color=ORANGE, 
                         fill_opacity=0.2, stroke_width=1, stroke_color=ORANGE),
                Text(f"{i}: {i**2}", font_size=16)
            )
            dict_cells.add(cell)
        
        dict_cells.arrange(RIGHT, buff=0.1).next_to(dict_title, DOWN, buff=0.7)
        
        # Animate all elements with proper timing
        self.play(Write(list_title))
        self.play(LaggedStart(*[Create(c) for c in list_cells], lag_ratio=0.15))
        self.wait(0.5)
        
        self.play(Write(dict_title))
        self.play(LaggedStart(*[Create(c) for c in dict_cells], lag_ratio=0.15))
        
        # Performance note
        note = Text("Key Points:", font_size=22, color=YELLOW, weight=BOLD)
        points = VGroup(
            Text("• New objects created in memory", font_size=20, color=YELLOW),
            Text("• More efficient than loops", font_size=20, color=YELLOW),
            Text("• Faster execution for simple ops", font_size=20, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        note_group = VGroup(note, points).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        note_group.to_edge(RIGHT, buff=1.5).shift(UP*0.5)
        
        self.play(Write(note))
        self.play(Write(points))
        self.wait(2)
