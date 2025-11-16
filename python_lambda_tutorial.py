from manim import *

class PythonLambdaTutorial(Scene):
    def construct(self):
        # Scene 1 — What is a Lambda Function?
        title = Text("1️⃣ What is a Lambda Function?", font_size=42, color=BLUE)
        definition = Text(
            "A small, anonymous function in Python\n"
            "(no name unless you assign one)",
            font_size=28,
            color=WHITE,
            line_spacing=1.2
        )
        
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.play(Write(definition.next_to(title, DOWN, buff=0.5)))
        
        # Lambda vs def comparison
        lambda_code = Text("# Lambda function\nadd = lambda x: x + 2", 
                         font="Monospace", font_size=24, color=GREEN)
        
        def_code = Text("# Regular function\ndef add(x):\n    return x + 2", 
                       font="Monospace", font_size=24, color=YELLOW)
        
        # Create code examples first
        code_group = VGroup(
            lambda_code,
            Text("vs", font_size=32, color=WHITE),
            def_code
        ).arrange(DOWN, buff=0.7).next_to(definition, DOWN, buff=0.7)
        
        # Animate lambda code first
        self.play(Write(code_group[0]))
        self.wait(0.3)
        # Then 'vs' in the middle
        self.play(Write(code_group[1]))
        self.wait(0.3)
        # Then def code last
        self.play(Write(code_group[2]))
        self.wait(1)
        
        # Clean up for next scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=0.8
        )
        
        # Scene 2 — Under the Hood
        title2 = Text("2️⃣ How Lambda Functions Work", font_size=40, color=BLUE)
        self.play(Write(title2))
        self.play(title2.animate.to_edge(UP))
        
        # Lambda creation code
        code = Text('add = lambda x: x + 2',
                   font="Monospace", font_size=28, color=GREEN)
        self.play(Write(code))
        self.wait(0.5)
        
        # Clear screen for memory diagram
        self.play(
            FadeOut(code),
            title2.animate.scale(0.8).to_corner(UL, buff=0.5)
        )
        
        # Function object in memory
        func_box = RoundedRectangle(width=3, height=1.5, corner_radius=0.1, color=GREEN)
        func_box.set_fill(BLACK, opacity=0.8)
        func_type = Text("function", font_size=24, color=GREEN).next_to(func_box, UP, buff=0.1)
        
        # Function details
        func_details = VGroup(
            Text("λ x: x + 2", font="Monospace", font_size=24, color=GREEN),
            Text("<function at 0x...>", font="Monospace", font_size=18, color=GRAY)
        ).arrange(DOWN, buff=0.2).move_to(func_box)
        
        # Variable reference
        var_circle = Circle(radius=0.5, color=BLUE, fill_opacity=0.2)
        var_text = Text("add", font_size=24, color=BLUE).move_to(var_circle)
        var_group = VGroup(var_circle, var_text).to_edge(LEFT).shift(UP)
        
        # Arrow from variable to function
        arrow = Arrow(
            var_circle.get_right(),
            func_box.get_left(),
            buff=0.2,
            color=WHITE
        )
        
        # Animate
        self.play(Create(func_box), Write(func_type))
        self.play(Write(func_details))
        self.play(Create(var_group))
        self.play(Create(arrow))
        
        # Show function call
        call_code = Text("add(3)  # Returns 5", font="Monospace", font_size=28, color=YELLOW)
        call_code.next_to(func_box, DOWN, buff=1)
        
        # Animate function call
        self.play(Write(call_code))
        self.wait(0.5)
        
        # Show return value
        result = Text("5", font_size=32, color=GREEN)
        result.next_to(call_code, DOWN, buff=0.5)
        
        # Animate return arrow
        call_arrow = Arrow(
            func_box.get_bottom(),
            call_code.get_top(),
            color=YELLOW,
            buff=0.2
        )
        
        self.play(
            Create(call_arrow),
            run_time=0.8
        )
        self.play(Write(result))
        
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
