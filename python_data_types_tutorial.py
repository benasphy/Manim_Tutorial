from manim import *

class DataTypesTutorial(Scene):
    def construct(self):
        # Scene 1 — What are Data Types?
        title = Text("1️⃣ What are Data Types?", font_size=48, color=BLUE)
        subtitle = Text("Python's way to categorize different kinds of data", font_size=28, color=WHITE)
        
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.play(Write(subtitle.next_to(title, DOWN, buff=0.3)))
        
        # Toolbox analogy
        tools = VGroup(
            Text("🔨 int (numbers)", font_size=32, color=YELLOW),
            Text("🔧 str (text)", font_size=32, color=BLUE),
            Text("🎨 list (collections)", font_size=32, color=GREEN),
            Text("🔧 dict (pairs)", font_size=32, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).shift(LEFT*2)
        
        self.play(FadeIn(tools, shift=RIGHT, lag_ratio=0.2))
        self.wait(1)
        
        # Clean up
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 2 — Under the Hood
        title2 = Text("2️⃣ Under the Hood", font_size=48, color=BLUE)
        code = Text("age = 25", font="Monospace", font_size=36, color=YELLOW)
        
        self.play(Write(title2))
        self.play(title2.animate.to_edge(UP))
        self.play(Write(code.next_to(title2, DOWN, buff=0.7)))
        
        # Memory diagram
        int_box = RoundedRectangle(width=2, height=1.2, corner_radius=0.1, color=YELLOW)
        int_box.set_fill(BLACK, opacity=0.8)
        int_value = Text("25", font_size=36, color=YELLOW).move_to(int_box)
        int_type = Text("int", font_size=24, color=YELLOW).next_to(int_box, UP, buff=0.1)
        
        # Variable reference
        var_circle = Circle(radius=0.5, color=BLUE, fill_opacity=0.2)
        var_text = Text("age", font_size=24, color=BLUE).move_to(var_circle)
        var_group = VGroup(var_circle, var_text).to_edge(LEFT).shift(UP)
        
        # Arrow
        arrow = Arrow(var_circle.get_right(), int_box.get_left(), buff=0.2, color=WHITE)
        
        # Animate
        self.play(Create(int_box), Write(int_value), Write(int_type))
        self.play(Create(var_group))
        self.play(Create(arrow))
        
        # Type info
        type_label = Text("Type: int", font_size=24, color=YELLOW).next_to(int_box, RIGHT, buff=0.5)
        self.play(Write(type_label))
        
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
