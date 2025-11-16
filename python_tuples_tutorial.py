from manim import *

class PythonTuplesTutorial(Scene):
    def construct(self):
        # Scene 1 — What is a Tuple?
        title = Text("1️⃣ What is a Tuple in Python?", font_size=42, color=BLUE)
        definition = Text(
            "An ordered, immutable collection of items\nOnce created, cannot be changed",
            font_size=28,
            color=WHITE,
            line_spacing=1.2
        )
        
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.play(Write(definition.next_to(title, DOWN, buff=0.5)))
        
        # Show immutable nature with text lock
        lock_icon = Text("🔒", font_size=48, color=YELLOW).shift(DOWN*0.5)
        
        self.play(FadeIn(lock_icon, scale=0.5))
        self.wait(1)
        
        # Clean up for next scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=0.8
        )
        
        # Scene 2 — Under the Hood
        title2 = Text("2️⃣ How Tuples Work Internally", font_size=40, color=BLUE)
        self.play(Write(title2))
        self.play(title2.animate.to_edge(UP))
        
        # Tuple creation code
        code = Text('colors = ("red", "green", "blue")',
                   font="Monospace", font_size=28, color=YELLOW)
        self.play(Write(code))
        self.wait(1)
        
        # Clear screen for memory diagram
        self.play(
            FadeOut(code),
            title2.animate.scale(0.8).to_corner(UL, buff=0.5)
        )
        
        # Memory diagram
        # Tuple object (similar to list but with lock icon)
        tuple_box = RoundedRectangle(width=2, height=3, corner_radius=0.1, color=YELLOW)
        tuple_box.set_fill(BLACK, opacity=0.8)
        tuple_type = Text("tuple", font_size=24, color=YELLOW).next_to(tuple_box, UP, buff=0.1)
        
        # Lock symbol on the tuple
        lock = Text("🔒", font_size=24, color=RED).move_to(
            tuple_box.get_top() + DOWN*0.3 + RIGHT*0.7
        )
        
        # Tuple elements
        colors = ["red", "green", "blue"]
        color_hex = ["#FF6B6B", "#6BCB77", "#4D96FF"]
        elements = []
        
        for i, (color, hex_val) in enumerate(zip(colors, color_hex)):
            elem = RoundedRectangle(width=1.8, height=0.7, corner_radius=0.1, color=hex_val)
            elem.set_fill(BLACK, opacity=0.8)
            text = Text(f'"{color}"', font_size=18, color=hex_val).move_to(elem)
            idx = Text(f"{i}", font_size=16, color=WHITE).next_to(elem, LEFT, buff=0.1)
            elements.append(VGroup(elem, text, idx))
        
        # Position elements
        tuple_box.shift(RIGHT * 3)
        tuple_type.next_to(tuple_box, UP, buff=0.1)
        elem_group = VGroup(*elements).arrange(DOWN, buff=0.15).move_to(tuple_box)
        
        # Variable reference
        var_circle = Circle(radius=0.5, color=BLUE, fill_opacity=0.2)
        var_text = Text("colors", font_size=24, color=BLUE).move_to(var_circle)
        var_group = VGroup(var_circle, var_text).to_edge(LEFT).shift(UP)
        
        # Arrow from variable to tuple
        arrow = Arrow(var_circle.get_right(), tuple_box.get_left(), buff=0.2, color=WHITE)
        
        # Animate
        self.play(Create(tuple_box), Write(tuple_type), FadeIn(lock, scale=0.5))
        self.play(Create(var_group))
        self.play(Create(arrow))
        
        # Animate elements appearing
        for elem in elements:
            self.play(FadeIn(elem, shift=RIGHT))
            self.wait(0.2)
        
        # Show immutability note
        note = Text("IMMUTABLE: Cannot change after creation",
                   font_size=20, color=RED)
        note.next_to(tuple_box, DOWN, buff=0.5)
        self.play(Write(note))
        
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
