from manim import *

class FunctionsTutorial(Scene):
    def construct(self):
        # Scene 1: Title and Introduction
        title = Text("✨ Python Functions", font_size=48, color=BLUE)
        subtitle = Text("Reusable Blocks of Code", font_size=32, color=YELLOW)
        
        self.play(Write(title))
        self.play(Write(subtitle.next_to(title, DOWN, buff=0.5)))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 2: What is a Function?
        title1 = Text("1️⃣ What is a Function?", font_size=42, color=BLUE)
        self.play(Write(title1))
        self.play(title1.animate.to_edge(UP))
        
        definition = VGroup(
            Text("A function is a reusable block of code that performs a specific task.", font_size=28, color=WHITE),
            Text("• Like a mini-program inside your program", font_size=24, color=YELLOW),
            Text("• Takes inputs (parameters), processes them, and returns results", font_size=24, color=YELLOW),
            Text("• Can be called multiple times with different inputs", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title1, DOWN, buff=1)
        
        self.play(Write(definition[0]))
        self.wait(0.5)
        self.play(Write(definition[1:]))
        self.wait(2)
        
        # Clear for next scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 2: Coffee Machine Analogy
        analogy_title = Text("☕ Coffee Machine Analogy", font_size=36, color=BLUE)
        self.play(Write(analogy_title))
        self.play(analogy_title.animate.to_edge(UP))
        
        # Create a simple coffee machine using built-in shapes
        base = RoundedRectangle(height=2, width=3, color=WHITE, fill_color=BLACK, fill_opacity=1)
        top = Rectangle(height=0.8, width=2, color=WHITE, fill_color=BLACK, fill_opacity=1).next_to(base, UP, buff=0)
        spout = Rectangle(height=0.3, width=0.8, color=WHITE, fill_color=BLACK, fill_opacity=1)\
               .next_to(base, RIGHT, buff=0).shift(LEFT*0.2 + UP*0.2)
        button = Circle(radius=0.2, color=GREEN, fill_color=GREEN, fill_opacity=1)\
                .next_to(top, UP, buff=0.1).shift(LEFT*0.5)
        
        coffee_machine = VGroup(base, top, spout, button).scale(0.8).shift(UP*0.5)
        coffee_machine_label = Text("Coffee Machine", font_size=24).next_to(coffee_machine, DOWN)
        
        # Inputs and outputs
        input_group = VGroup(
            Text("Inputs:", font_size=24, color=YELLOW),
            Text("• Water", font_size=20, color=WHITE),
            Text("• Coffee powder", font_size=20, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT, buff=2).shift(UP*0.5)
        
        output_group = VGroup(
            Text("Output:", font_size=24, color=YELLOW),
            Text("• Coffee", font_size=20, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT, buff=2).shift(UP*0.5)
        
        # Create arrows
        arrow1 = Arrow(input_group.get_right(), coffee_machine.get_left(), buff=0.5)
        arrow2 = Arrow(coffee_machine.get_right(), output_group.get_left(), buff=0.5)
        
        # Animate the coffee machine
        self.play(
            FadeIn(coffee_machine, shift=UP),
            Write(coffee_machine_label)
        )
        
        # Animate inputs and arrows
        self.play(
            Write(input_group),
            Create(arrow1)
        )
        
        # Show processing (button press)
        button_highlight = button.copy().set_color(YELLOW).scale(1.2)
        self.play(Transform(button, button_highlight), run_time=0.5)
        self.wait(0.3)
        
        # Show output
        self.play(
            Write(output_group),
            Create(arrow2)
        )
        
        # Clear for next scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 3: Function Example
        title3 = Text("📝 Function Example", font_size=36, color=BLUE)
        self.play(Write(title3))
        self.play(title3.animate.to_edge(UP))
        
        # Function example
        code = '''def make_coffee(water, coffee_powder):
    # Process inputs
    coffee = f"Hot coffee made with {water}ml water and {coffee_powder}g coffee"
    return coffee

# Call the function
my_coffee = make_coffee(250, 15)
print(my_coffee)'''.split('\n')
        
        code_mob = VGroup(*[Text(line, font="Monospace", font_size=20, color=WHITE) 
                          for line in code])
        code_mob.arrange(DOWN, aligned_edge=LEFT)
        code_rect = SurroundingRectangle(code_mob, color=BLUE, buff=0.3, fill_color=BLACK, fill_opacity=1)
        code_group = VGroup(code_rect, code_mob).scale(0.8).to_edge(DOWN, buff=0.5)
        
        self.play(Write(code_group))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 3: Under the Hood
        title2 = Text("🔧 What's Happening Under the Hood?", font_size=36, color=BLUE)
        self.play(Write(title2))
        self.play(title2.animate.to_edge(UP))
        
        # Function definition explanation
        definition = VGroup(
            Text("When you define a function:", font_size=28, color=YELLOW),
            Text("1. Python stores the function's code in memory", font_size=24, color=WHITE),
            Text("2. Creates a reference to the function's name", font_size=24, color=WHITE),
            Text("3. No code is executed yet!", font_size=24, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title2, DOWN, buff=1)
        
        self.play(Write(definition[0]))
        self.play(Write(definition[1:]))
        self.wait(2)
        
        # Function call explanation
        call_title = Text("When you call a function:", font_size=28, color=YELLOW)
        call_steps = VGroup(
            Text("1. Python creates a stack frame (temporary workspace)", font_size=22, color=WHITE),
            Text("2. Assigns argument values to parameters", font_size=22, color=WHITE),
            Text("3. Executes the function's code", font_size=22, color=WHITE),
            Text("4. Returns the result (if any)", font_size=22, color=WHITE),
            Text("5. Cleans up the stack frame", font_size=22, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(definition, DOWN, buff=0.8)
        
        self.play(Write(call_title))
        self.wait(0.5)
        self.play(Write(call_steps[0]))
        self.wait(0.3)
        self.play(Write(call_steps[1]))
        self.wait(0.3)
        self.play(Write(call_steps[2]))
        self.wait(0.3)
        self.play(Write(call_steps[3]))
        self.wait(0.3)
        self.play(Write(call_steps[4]))
        self.wait(2)
        
        # Office Desk Analogy
        analogy_title = Text("🏢 Office Desk Analogy", font_size=32, color=GREEN).to_edge(UP).shift(DOWN*0.5)
        self.play(ReplacementTransform(title2, analogy_title))
        
        # Clear previous content
        self.play(
            FadeOut(definition),
            FadeOut(call_title),
            FadeOut(call_steps)
        )
        
        # Create office desk visualization
        desk = RoundedRectangle(width=8, height=4, color=WHITE, fill_color=BLACK, fill_opacity=1)
        desk_label = Text("Function Workspace", font_size=24).next_to(desk, DOWN)
        
        # Initial state: Clean desk
        clean_desk = VGroup(
            Text("1. Clean Desk (Function Defined)", font_size=22, color=YELLOW),
            Text("• Function code is stored in memory", font_size=20, color=WHITE),
            Text("• Ready to be used, but no work being done yet", font_size=20, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(desk, DOWN, buff=1.5)
        
        self.play(Create(desk), Write(desk_label))
        self.play(Write(clean_desk))
        self.wait(2)
        
        # Function call: Setup
        self.play(FadeOut(clean_desk))
        
        call_setup = VGroup(
            Text("2. Function Call: Setup", font_size=22, color=YELLOW),
            Text("• Parameters get their values (water=250, coffee_powder=15)", font_size=20, color=WHITE),
            Text("• Local variables are created", font_size=20, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(desk, DOWN, buff=1.5)
        
        # Add parameters to desk
        param1 = Text("water = 250", font="Monospace", font_size=18, color=YELLOW)
        param2 = Text("coffee_powder = 15", font="Monospace", font_size=18, color=YELLOW)
        params = VGroup(param1, param2).arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(desk)
        
        self.play(Write(call_setup))
        self.play(FadeIn(params, shift=UP))
        self.wait(2)
        
        # Function execution
        self.play(FadeOut(call_setup))
        
        execution = VGroup(
            Text("3. Execution", font_size=22, color=YELLOW),
            Text("• Code runs line by line", font_size=20, color=WHITE),
            Text("• Creates local variables (coffee)", font_size=20, color=WHITE),
            Text("• Returns the result", font_size=20, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(desk, DOWN, buff=1.5)
        
        # Show code execution
        code_line1 = Text("coffee = f'Hot coffee...'", font="Monospace", font_size=18, color=GREEN)
        return_line = Text("return coffee", font="Monospace", font_size=18, color=GREEN)
        result = Text("result = 'Hot coffee made with 250ml water and 15g coffee'", 
                     font="Monospace", font_size=16, color=YELLOW)
        
        code_line1.next_to(params, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        return_line.next_to(code_line1, DOWN, buff=0.3, aligned_edge=LEFT)
        result.next_to(desk, DOWN, buff=0.5)
        
        self.play(Write(execution))
        self.wait(0.5)
        self.play(Write(code_line1))
        self.wait(0.5)
        self.play(Write(return_line))
        self.wait(0.5)
        self.play(Write(result))
        self.wait(2)
        
        # Cleanup
        self.play(FadeOut(execution))
        
        cleanup = VGroup(
            Text("4. Cleanup", font_size=22, color=YELLOW),
            Text("• Return value is passed back to the caller", font_size=20, color=WHITE),
            Text("• Local variables are removed", font_size=20, color=WHITE),
            Text("• Desk is cleared for the next function call", font_size=20, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(desk, DOWN, buff=1.5)
        
        self.play(Write(cleanup))
        self.wait(1)
        
        # Animate cleanup
        self.play(
            FadeOut(params),
            FadeOut(code_line1),
            FadeOut(return_line),
            result.animate.scale(1.2).set_color(GREEN).to_edge(UP, buff=2)
        )
        
        # Final message
        final = Text("This happens every time you call a function!", font_size=28, color=YELLOW)
        self.play(Write(final.next_to(cleanup, DOWN, buff=1)))
        self.wait(3)
        
        # Clean up
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Final slide
        final_title = Text("🎉 Key Takeaways", font_size=48, color=YELLOW)
        takeaways = VGroup(
            Text("• Functions are reusable blocks of code that perform specific tasks", font_size=28, color=WHITE),
            Text("• They take inputs, process them, and return results", font_size=28, color=WHITE),
            Text("• Under the hood, Python manages function calls using a call stack", font_size=28, color=WHITE),
            Text("• Each function call gets its own workspace (stack frame)", font_size=28, color=WHITE),
            Text("• Understanding this helps debug and write better functions!", font_size=28, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        self.play(Write(final_title))
        self.play(LaggedStart(*[Write(takeaway) for takeaway in takeaways], lag_ratio=0.3))
        self.wait(3)
