from manim import *

class PythonArgsKwargsTutorial(Scene):
    def construct(self):
        # Scene 1 - What are *args and **kwargs?
        title = Text("1️⃣ What Are *args and **kwargs?", font_size=38, color=BLUE)
        title.to_edge(UP)
        
        definition = Text(
            "Functions can take a variable number of arguments\n\n"
            "*args → captures extra positional arguments into a tuple\n"
            "**kwargs → captures extra keyword arguments into a dictionary",
            font_size=24,
            color=WHITE,
            line_spacing=1.2
        )
        definition.next_to(title, DOWN, buff=0.7)
        
        self.play(Write(title))
        self.play(Write(definition))
        self.wait(2)
        
        # Visual representation
        args_box = RoundedRectangle(width=3, height=1.5, corner_radius=0.1, 
                                 color=GREEN, fill_opacity=0.1)
        args_text = Text("*args: tuple", font_size=20, color=GREEN)
        args_group = VGroup(args_box, args_text).shift(LEFT * 3)
        
        kwargs_box = RoundedRectangle(width=3, height=1.5, corner_radius=0.1, 
                                   color=YELLOW, fill_opacity=0.1)
        kwargs_text = Text("**kwargs: dict", font_size=20, color=YELLOW)
        kwargs_group = VGroup(kwargs_box, kwargs_text).shift(RIGHT * 3)
        
        self.play(
            Create(args_group.next_to(definition, DOWN, buff=1).shift(LEFT * 3)),
            Create(kwargs_group.next_to(definition, DOWN, buff=1).shift(RIGHT * 3))
        )
        self.wait(1)
        
        # Clean up for next scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 2 - Why are they useful?
        title2 = Text("2️⃣ Why Are They Useful?", font_size=40, color=BLUE)
        title2.to_edge(UP)
        
        benefits = VGroup(
            Text("✓ Flexible Functions", font_size=26, color=GREEN),
            Text("• Accept any number of arguments", font_size=22, color=WHITE),
            Text("• No need to know argument count in advance", font_size=22, color=WHITE),
            
            Text("\n✓ Reusable Code", font_size=26, color=GREEN).shift(DOWN),
            Text("• Can be mixed with normal parameters", font_size=22, color=WHITE).shift(DOWN),
            Text("• Makes function interfaces more intuitive", font_size=22, color=WHITE).shift(DOWN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title2, DOWN, buff=0.7)
        
        self.play(Write(title2))
        self.play(LaggedStart(
            *[Write(benefit) for benefit in benefits],
            lag_ratio=0.3
        ))
        self.wait(2)
        
        # Clean up for next scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 3 - Example and Explanation
        title3 = Text("3️⃣ Example and Explanation", font_size=40, color=BLUE)
        title3.to_edge(UP)
        
        code = '''def greet_people(*args, **kwargs):
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

greet_people("Alice", "Bob", "Charlie", 
             age=25, city="New York")'''
        
        code_mob = Text(code, font="Monospace", font_size=20, color=YELLOW)
        code_mob.next_to(title3, DOWN, buff=0.7)
        
        output = Text(
            "Positional arguments (args): ('Alice', 'Bob', 'Charlie')\n"
            "Keyword arguments (kwargs): {'age': 25, 'city': 'New York'}",
            font="Monospace", font_size=16, color=GREEN
        )
        output.next_to(code_mob, DOWN, buff=0.7)
        
        self.play(Write(title3))
        self.play(Write(code_mob))
        self.wait(1)
        self.play(Write(output))
        self.wait(2)
        
        # Clean up for next scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 4 - Under the Hood
        title4 = Text("4️⃣ Under the Hood", font_size=40, color=BLUE)
        title4.to_edge(UP)
        
        # *args explanation
        args_title = Text("*args: Packed into a tuple", font_size=28, color=GREEN)
        args_title.next_to(title4, DOWN, buff=0.7)
        
        args_example = Text(
            '"Alice", "Bob", "Charlie"  →  args = ("Alice", "Bob", "Charlie")',
            font="Monospace", font_size=18, color=GREEN
        )
        args_example.next_to(args_title, DOWN, buff=0.5)
        
        # **kwargs explanation
        kwargs_title = Text("**kwargs: Packed into a dictionary", font_size=28, color=YELLOW)
        kwargs_title.next_to(args_example, DOWN, buff=1)
        
        kwargs_example = Text(
            'age=25, city="New York"  →  kwargs = {"age": 25, "city": "New York"}',
            font="Monospace", font_size=18, color=YELLOW
        )
        kwargs_example.next_to(kwargs_title, DOWN, buff=0.5)
        
        # Visual representation
        args_rect = SurroundingRectangle(args_example, color=GREEN, buff=0.2, fill_opacity=0.1)
        kwargs_rect = SurroundingRectangle(kwargs_example, color=YELLOW, buff=0.2, fill_opacity=0.1)
        
        self.play(Write(title4))
        self.play(Write(args_title))
        self.play(Write(args_example))
        self.play(Create(args_rect))
        self.wait(1)
        
        self.play(Write(kwargs_title))
        self.play(Write(kwargs_example))
        self.play(Create(kwargs_rect))
        self.wait(2)
        
        # Clean up
        self.play(*[FadeOut(mob) for mob in self.mobjects])
