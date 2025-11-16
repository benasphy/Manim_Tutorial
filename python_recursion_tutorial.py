from manim import *

class RecursionTutorial(Scene):
    def construct(self):
        # Scene 1 — What is Recursion?
        title = Text("🔄 Recursion in Python", font_size=42, color=BLUE)
        definition = Text("A function that calls itself to solve a problem", 
                         font_size=28, color=WHITE)
        
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.play(Write(definition.next_to(title, DOWN, buff=0.5)))
        
        # Mirror analogy
        mirror_analogy = Text("Like standing between two mirrors — reflections repeat infinitely",
                            font_size=24, color=YELLOW).to_edge(DOWN)
        
        self.play(Write(mirror_analogy))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 2 — Anatomy of a Recursive Function
        title2 = Text("🧩 Anatomy of a Recursive Function", font_size=42, color=BLUE)
        self.play(Write(title2))
        self.play(title2.animate.to_edge(UP))
        
        # Create components one by one
        base_case_title = Text("1. Base Case", font_size=32, color=GREEN).to_edge(LEFT).shift(UP*0.5)
        base_case_desc = Text("• Condition where recursion stops", font_size=24, color=WHITE)
        base_case_desc.next_to(base_case_title, DOWN, aligned_edge=LEFT)
        
        recursive_case_title = Text("2. Recursive Case", font_size=32, color=GREEN).to_edge(LEFT)
        recursive_case_title.next_to(base_case_desc, DOWN, buff=0.5, aligned_edge=LEFT)
        
        recursive_case_desc = Text("• Function calls itself with smaller input", font_size=24, color=WHITE)
        recursive_case_desc.next_to(recursive_case_title, DOWN, aligned_edge=LEFT)
        
        warning = Text("⚠️ Without base case:", font_size=28, color=RED)
        warning.next_to(recursive_case_desc, DOWN, buff=0.5, aligned_edge=LEFT)
        
        error_msg = Text("RecursionError: maximum recursion depth exceeded", 
                        font="Monospace", font_size=20, color=RED)
        error_msg.next_to(warning, DOWN, aligned_edge=LEFT)
        
        # Group all components
        components = VGroup(
            base_case_title, base_case_desc,
            recursive_case_title, recursive_case_desc,
            warning, error_msg
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title2, DOWN, buff=0.8)
        
        self.play(LaggedStart(*[FadeIn(comp, shift=RIGHT) for comp in components], lag_ratio=0.3))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 3 — Factorial Example
        title3 = Text("🔢 Example: Factorial Function", font_size=42, color=BLUE)
        self.play(Write(title3))
        self.play(title3.animate.to_edge(UP))
        
        # Math formula
        formula = MathTex("n! = n \\times (n-1) \\times (n-2) \\times ... \\times 1",
                         font_size=36).next_to(title3, DOWN, buff=1)
        self.play(Write(formula))
        
        # Code example
        code = '''def factorial(n):
    # Base case
    if n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120'''
        
        code_mobj = Text(code, font="Monospace", font_size=22, color=WHITE)
        code_mobj.next_to(formula, DOWN, buff=0.8)
        self.play(Write(code_mobj))
        self.wait(2)
        
        # Clear for next slide
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # New slide for explanation
        title3_2 = Text("🔢 How Factorial Works", font_size=42, color=BLUE)
        self.play(Write(title3_2))
        self.play(title3_2.animate.to_edge(UP))
        
        # Call stack visualization with better spacing
        calls_title = Text("Function Call Stack:", font_size=28, color=YELLOW).to_edge(UP, buff=1.5)
        self.play(Write(calls_title))
        
        calls = VGroup(
            Text("factorial(5) calls factorial(4)", font_size=22, color=YELLOW),
            Text("factorial(4) calls factorial(3)", font_size=22, color=YELLOW),
            Text("factorial(3) calls factorial(2)", font_size=22, color=YELLOW),
            Text("factorial(2) calls factorial(1)", font_size=22, color=YELLOW),
            Text("factorial(1) → returns 1 (base case)", font_size=22, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(calls_title, DOWN, buff=0.8)
        
        self.play(LaggedStart(*[FadeIn(call, shift=RIGHT) for call in calls], lag_ratio=0.4))
        
        # Show the unwinding process
        result_text = Text("Then the stack unwinds:", font_size=26, color=WHITE)
        result_calcs = Text("2*1=2,  3*2=6,  4*6=24,  5*24=120", 
                           font_size=24, color=BLUE_C)
        
        result_group = VGroup(result_text, result_calcs).arrange(DOWN, buff=0.5)
        result_group.next_to(calls, DOWN, buff=1)
        
        self.play(Write(result_text))
        self.play(Write(result_calcs))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 4 — Under the Hood: Call Stack
        title4 = Text("🥞 Under the Hood: The Call Stack", font_size=42, color=BLUE)
        self.play(Write(title4))
        self.play(title4.animate.to_edge(UP))
        
        # Stack explanation
        explanation = VGroup(
            Text("1. Each function call is pushed onto the call stack", font_size=24, color=WHITE),
            Text("2. When base case is reached, stack unwinds", font_size=24, color=WHITE),
            Text("3. Results are computed and returned back up", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(title4, DOWN, buff=1)
        
        # Plate analogy
        plate_analogy = Text("Think of stacking plates: push when calling, pop when returning",
                           font_size=22, color=YELLOW).to_edge(DOWN)
        
        self.play(Write(explanation))
        self.play(Write(plate_analogy))
        
        # Visualize stack
        stack = VGroup()
        for i in range(5, 0, -1):
            plate = Rectangle(
                width=3, height=0.8,
                fill_color=BLUE_D, fill_opacity=0.8,
                stroke_width=2
            )
            text = Text(f"factorial({i})", font_size=20)
            plate.add(text)
            stack.add(plate)
        
        stack.arrange(UP, buff=0).next_to(explanation, DOWN, buff=1)
        
        # Animate stack building up
        self.play(LaggedStart(
            *[GrowFromEdge(plate, UP) for plate in stack],
            lag_ratio=0.3
        ))
        
        # Animate stack unwinding
        self.wait(1)
        results = [1, 2, 6, 24, 120]
        
        for i, plate in enumerate(reversed(stack)):
            result_text = Text(f"→ returns {results[i]}", font_size=20, color=GREEN)
            result_text.next_to(plate, RIGHT)
            self.play(
                ApplyMethod(plate.set_fill, RED, 0.8),
                Write(result_text)
            )
            self.wait(0.5)
        
        self.wait(2)
