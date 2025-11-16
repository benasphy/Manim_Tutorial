from manim import *

class PythonListsTutorial(Scene):
    def construct(self):
        # Scene 1 — What is a List?
        title = Text("1️⃣ What is a List in Python?", font_size=42, color=BLUE)
        definition = Text("An ordered, mutable collection of items\nthat can store different data types",
                        font_size=28, color=WHITE, line_spacing=1.2)
        
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.play(Write(definition.next_to(title, DOWN, buff=0.5)))
        
        # Shopping list analogy
        shopping_list = VGroup(
            Rectangle(width=3, height=4, color=YELLOW, fill_opacity=0.1),
            Text("🛒 Shopping List", font_size=28, color=YELLOW).to_edge(UP * 1.5 + LEFT * 3),
            Text("1. Apples", font_size=24).to_edge(UP * 0.5 + LEFT * 3.5, buff=0.5),
            Text("2. Milk", font_size=24).to_edge(UP * 0.0 + LEFT * 3.5, buff=0.5),
            Text("3. Bread", font_size=24).to_edge(UP * -0.5 + LEFT * 3.5, buff=0.5),
        )
        
        # Python list equivalent
        code = '''# Python List
items = [
    "Apples",
    "Milk",
    "Bread"
]'''
        code_mob = Text(code, font="Monospace", font_size=24, color=GREEN)
        code_mob.next_to(shopping_list, RIGHT, buff=1)
        
        # Just show the definition first
        self.wait(1.5)
        
        # Clean up for next scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=0.8
        )
        
        # Scene 2 — Under the Hood
        title2 = Text("2️⃣ How Lists Work Internally", font_size=40, color=BLUE)
        self.play(Write(title2))
        self.play(title2.animate.to_edge(UP))
        
        # List creation code
        code = Text('fruits = ["apple", "banana", "cherry"]',
                   font="Monospace", font_size=28, color=YELLOW)
        self.play(Write(code))
        self.wait(1)
        
        # Clear screen for memory diagram
        self.play(
            FadeOut(code),
            title2.animate.scale(0.8).to_corner(UL, buff=0.5)
        )
        
        # Memory diagram
        list_box = RoundedRectangle(width=2, height=3, corner_radius=0.1, color=YELLOW)
        list_box.set_fill(BLACK, opacity=0.8)
        list_type = Text("list", font_size=24, color=YELLOW).next_to(list_box, UP, buff=0.1)
        
        # List elements
        fruits = ["apple", "banana", "cherry"]
        colors = ["#FF6B6B", "#FFD93D", "#6BCB77"]
        elements = []
        
        for i, (fruit, color) in enumerate(zip(fruits, colors)):
            elem = RoundedRectangle(width=1.8, height=0.7, corner_radius=0.1, color=color)
            elem.set_fill(BLACK, opacity=0.8)
            text = Text(fruit, font_size=20, color=color).move_to(elem)
            idx = Text(f"{i}", font_size=16, color=WHITE).next_to(elem, LEFT, buff=0.1)
            elements.append(VGroup(elem, text, idx))
        
        # Position elements
        list_box.shift(RIGHT * 3)
        list_type.next_to(list_box, UP, buff=0.1)
        elem_group = VGroup(*elements).arrange(DOWN, buff=0.15).move_to(list_box)
        
        # Variable reference
        var_circle = Circle(radius=0.5, color=BLUE, fill_opacity=0.2)
        var_text = Text("fruits", font_size=24, color=BLUE).move_to(var_circle)
        var_group = VGroup(var_circle, var_text).to_edge(LEFT).shift(UP)
        
        # Arrow from variable to list
        arrow = Arrow(var_circle.get_right(), list_box.get_left(), buff=0.2, color=WHITE)
        
        # Animate
        self.play(Create(list_box), Write(list_type))
        self.play(Create(var_group))
        self.play(Create(arrow))
        
        # Animate elements appearing
        for elem in elements:
            self.play(FadeIn(elem, shift=RIGHT))
            self.wait(0.2)
        
        self.wait(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
