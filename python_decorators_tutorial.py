from manim import *

class DecoratorsTutorial(Scene):
    def construct(self):
        # Scene 1 — What are Decorators?
        title = Text("✨ Python Decorators", font_size=42, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Definition
        definition = Text("A function that modifies another function's behavior", 
                         font_size=28, color=WHITE)
        self.play(Write(definition.next_to(title, DOWN, buff=0.8)))
        
        # Gift wrapper analogy
        analogy = VGroup(
            Text("Like a gift wrapper 🎁:", font_size=32, color=YELLOW),
            Text("• Original function = The gift", font_size=28, color=WHITE),
            Text("• Decorator = Wrapper that adds something extra", font_size=28, color=WHITE),
            Text("• Original function remains unchanged", font_size=28, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(definition, DOWN, buff=1)
        
        self.play(Write(analogy[0]))
        self.play(LaggedStart(*[Write(p) for p in analogy[1:]], lag_ratio=0.3))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 2 - Why Use Decorators?
        title2 = Text("💡 Why Use Decorators?", font_size=42, color=BLUE)
        self.play(Write(title2))
        self.play(title2.animate.to_edge(UP))
        
        # Benefits
        benefits = VGroup(
            Text("Key Benefits:", font_size=36, color=YELLOW),
            Text("1. Code Reusability", font_size=28, color=GREEN),
            Text("   Write once, apply to many functions", font_size=24, color=WHITE),
            Text("2. Separation of Concerns", font_size=28, color=GREEN),
            Text("   Keep cross-cutting concerns separate", font_size=24, color=WHITE),
            Text("3. Cleaner Code", font_size=28, color=GREEN),
            Text("   Eliminate repetitive code", font_size=24, color=WHITE),
            Text("4. Readability", font_size=28, color=GREEN),
            Text("   Clear intent with @decorator syntax", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.9)
        
        self.play(Write(benefits[0]))
        self.wait(0.5)
        self.play(Write(benefits[1:3]))
        self.wait(0.5)
        self.play(Write(benefits[3:5]))
        self.wait(0.5)
        self.play(Write(benefits[5:]))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 2 — Problem Example
        title2 = Text("❌ The Problem: Code Repetition", font_size=42, color=RED)
        self.play(Write(title2))
        self.play(title2.animate.to_edge(UP))
        
        # Bad code example
        bad_code = """# Repeating the same logic
def greet():
    return "Hello, World!"

def greet_uppercase():
    result = greet()
    return result.upper()

def welcome():
    return "Welcome!"

def welcome_uppercase():
    result = welcome()
    return result.upper()"""
        
        code_mobj = Text(bad_code, font="Monospace", font_size=20, color=WHITE)
        code_mobj.next_to(title2, DOWN, buff=0.8)
        
        self.play(Write(code_mobj))
        
        # Highlight the repetition
        highlight1 = SurroundingRectangle(
            VGroup(*code_mobj[bad_code.find('def greet_uppercase'):bad_code.find('return result.upper()') + 20]),
            color=RED, buff=0.1
        )
        highlight2 = SurroundingRectangle(
            VGroup(*code_mobj[bad_code.find('def welcome_uppercase'):]),
            color=RED, buff=0.1
        )
        
        self.play(Create(highlight1))
        self.wait(0.5)
        self.play(ReplacementTransform(highlight1, highlight2))
        self.wait(0.5)
        self.play(FadeOut(highlight2))
        
        problem = Text("Problem: Duplicate code for the same transformation!", 
                      font_size=24, color=YELLOW).to_edge(DOWN, buff=1)
        self.play(Write(problem))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 3 — Decorator Solution
        title3 = Text("✨ Decorator Solution", font_size=42, color=GREEN)
        self.play(Write(title3))
        self.play(title3.animate.to_edge(UP))
        
        # Decorator code
        decorator_code = """# The decorator function
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

# Using the decorator
@uppercase_decorator
def greet():
    return "Hello, World!"

@uppercase_decorator
def welcome():
    return "Welcome!"

print(greet())   # Output: HELLO, WORLD!
print(welcome()) # Output: WELCOME!"""
        
        code_mobj = Text(decorator_code, font="Monospace", font_size=20, color=WHITE)
        code_mobj.next_to(title3, DOWN, buff=0.8)
        
        self.play(Write(code_mobj))
        
        # Highlight decorator definition
        decorator_def = SurroundingRectangle(
            VGroup(*code_mobj[decorator_code.find('def uppercase'):decorator_code.find('return wrapper') + 15]),
            color=BLUE, buff=0.1
        )
        
        # Highlight decorator usage
        decorator_use1 = SurroundingRectangle(
            VGroup(*code_mobj[decorator_code.find('@uppercase'):decorator_code.find('def greet')]),
            color=GREEN, buff=0.1
        )
        
        decorator_use2 = SurroundingRectangle(
            VGroup(*code_mobj[decorator_code.rfind('@uppercase'):decorator_code.rfind('def welcome')]),
            color=GREEN, buff=0.1
        )
        
        self.play(Create(decorator_def))
        self.wait(1)
        self.play(ReplacementTransform(decorator_def, decorator_use1))
        self.wait(0.5)
        self.play(ReplacementTransform(decorator_use1, decorator_use2))
        self.wait(0.5)
        self.play(FadeOut(decorator_use2))
        
        self.wait(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 5 - What's Happening Under the Hood
        title5 = Text("🔍 What's Happening Under the Hood", font_size=42, color=BLUE)
        self.play(Write(title5))
        self.play(title5.animate.to_edge(UP))
        
        # Under the hood explanation
        explanation = VGroup(
            Text("The @decorator syntax is just syntactic sugar for:", font_size=28, color=YELLOW),
            Text("greet = uppercase_decorator(greet)", font="Monospace", font_size=28, color=BLUE_C),
            Text("\nWhat happens when you call greet():", font_size=28, color=YELLOW).shift(UP*0.5),
            Text("1. Python executes uppercase_decorator(greet)", font_size=24, color=WHITE),
            Text("2. Returns the wrapper function (not executed yet)", font_size=24, color=WHITE),
            Text("3. When you call greet(), you're actually calling wrapper()", font_size=24, color=WHITE),
            Text("4. wrapper() calls the original function and adds behavior", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.9)
        
        self.play(Write(explanation[0]))
        self.wait(0.5)
        self.play(Write(explanation[1]))
        self.wait(1)
        self.play(Write(explanation[2:]))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 4 — Practical Example
        title4 = Text("🔧 Real-world Example: Timing Function", font_size=42, color=BLUE)
        self.play(Write(title4))
        self.play(title4.animate.to_edge(UP))
        
        # Timing decorator example
        timing_code = """import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Usage
result = slow_function(1_000_000)"""
        
        code_mobj = Text(timing_code, font="Monospace", font_size=18, color=WHITE)
        code_mobj.next_to(title4, DOWN, buff=0.8)
        
        self.play(Write(code_mobj))
        
        self.wait(1)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 7 - Common Use Cases
        title7 = Text("🔧 Common Decorator Use Cases", font_size=42, color=BLUE)
        self.play(Write(title7))
        self.play(title7.animate.to_edge(UP))
        
        # Common use cases with explanations
        use_cases = VGroup(
            Text("1. @timer", font_size=32, color=YELLOW),
            Text("   Measure function execution time", font_size=24, color=WHITE),
            Text("   Great for performance testing", font_size=20, color=GRAY),
            
            Text("\n2. @login_required", font_size=32, color=YELLOW),
            Text("   Protect routes in web frameworks", font_size=24, color=WHITE),
            Text("   Redirects to login if not authenticated", font_size=20, color=GRAY),
            
            Text("\n3. @memoize", font_size=32, color=YELLOW),
            Text("   Cache function results", font_size=24, color=WHITE),
            Text("   Improves performance for expensive computations", font_size=20, color=GRAY),
            
            Text("\n4. @validate_input", font_size=32, color=YELLOW),
            Text("   Check function arguments", font_size=24, color=WHITE),
            Text("   Ensures data integrity", font_size=20, color=GRAY)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).scale(0.9).to_edge(LEFT, buff=1)
        
        self.play(LaggedStart(*[Write(uc) for uc in use_cases], lag_ratio=0.2))
        self.wait(3)
        
        # Final slide
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        final = VGroup(
            Text("Key Takeaways", font_size=42, color=BLUE),
            Text("• Decorators modify function behavior", font_size=32, color=WHITE),
            Text("• Use @decorator syntax for cleaner code", font_size=32, color=WHITE),
            Text("• Great for cross-cutting concerns", font_size=32, color=WHITE),
            Text("• Built-in decorators: @classmethod, @staticmethod, @property", 
                font_size=28, color=YELLOW)
        ).arrange(DOWN, buff=0.6, aligned_edge=LEFT).scale(0.9)
        
        self.play(Write(final[0]))
        self.play(LaggedStart(*[Write(p) for p in final[1:]], lag_ratio=0.3))
        self.wait(3)
