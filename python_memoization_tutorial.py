from manim import *
from functools import lru_cache

class MemoizationTutorial(Scene):
    def construct(self):
        # Scene 1: Title and What is Memoization
        title = Text("📚 Python Memoization", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        definition = VGroup(
            Text("Memoization is an optimization technique where:", font_size=28),
            Text("• Function results are cached", font_size=24, color=YELLOW),
            Text("• Same inputs return cached results", font_size=24, color=YELLOW),
            Text("• Avoids redundant calculations", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=1)
        
        self.play(Write(definition[0]))
        self.play(Write(definition[1:]))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 2: Fibonacci Example
        title2 = Text("🐌 Fibonacci Without Memoization", font_size=42, color=BLUE)
        self.play(Write(title2))
        self.play(title2.animate.to_edge(UP))
        
        code1 = """def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

# Very slow for n > 30
print(fib(35))"""
        
        # Display code as text with monospace font
        code_mobj = Text(
            code1,
            font="Monospace",
            font_size=20,
            line_spacing=0.8,
            color=WHITE,
            background_stroke_width=0
        ).to_edge(LEFT, buff=0.5)
        
        self.play(Write(code_mobj))
        self.wait(2)
        
        # Show recursive calls
        calls = VGroup(
            Text("fib(5) calls:", font_size=24, color=YELLOW),
            Text("fib(4) + fib(3)", font_size=20, color=WHITE),
            Text("fib(3) + fib(2) + fib(2) + fib(1)", font_size=20, color=GRAY),
            Text("...and so on (exponential growth!)", font_size=20, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(DOWN)
        
        self.play(Write(calls))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 3: With Memoization
        title3 = Text("⚡ Fibonacci With Memoization", font_size=42, color=BLUE)
        self.play(Write(title3))
        self.play(title3.animate.to_edge(UP))
        
        code2 = """from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

# Now super fast!
print(fib(100))  # 354224848179261915075"""
        
        # Display second code block as text with monospace font
        code_mobj2 = Text(
            code2,
            font="Monospace",
            font_size=20,
            line_spacing=0.8,
            color=WHITE,
            background_stroke_width=0
        ).to_edge(LEFT, buff=0.5)
        
        self.play(Write(code_mobj2))
        self.wait(2)
        
        # Show cache visualization
        cache = VGroup(
            Text("Cache after fib(5):", font_size=24, color=YELLOW),
            Text("{2: 1, 3: 2, 4: 3, 5: 5}", font="Monospace", font_size=20, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(DOWN)
        
        self.play(Write(cache))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 4: When to Use Memoization
        title4 = Text("🎯 When to Use Memoization", font_size=42, color=BLUE)
        self.play(Write(title4))
        self.play(title4.animate.to_edge(UP))
        
        # Key points about when to use memoization
        use_when = VGroup(
            Text("✅ Use Memoization When:", font_size=32, color=GREEN),
            Text("• Function is pure (same input → same output)", font_size=24, color=WHITE),
            Text("• Function has repeated recursive calls with same inputs", font_size=24, color=WHITE),
            Text("• Function is computationally expensive", font_size=24, color=WHITE),
            Text("• Function has a limited input range", font_size=24, color=WHITE),
            
            Text("\n❌ Avoid When:", font_size=32, color=RED),
            Text("• Function has side effects", font_size=24, color=WHITE),
            Text("• Too many unique inputs (cache bloat)", font_size=24, color=WHITE),
            Text("• Function is already fast enough", font_size=24, color=WHITE),
            Text("• Memory usage is a concern", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.9).next_to(title4, DOWN, buff=0.8)
        
        # Animate the points in groups
        self.play(Write(use_when[0]))  # Title
        self.wait(0.5)
        self.play(Write(use_when[1:5]))  # When to use
        self.wait(1.5)
        self.play(Write(use_when[5]))   # Avoid title
        self.wait(0.5)
        self.play(Write(use_when[6:]))  # When to avoid
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        use_cases = VGroup(
            Text("Good for:", font_size=32, color=GREEN),
            Text("• Pure functions (same input → same output)", font_size=24),
            Text("• Expensive calculations", font_size=24),
            Text("• Recursive functions with overlapping subproblems", font_size=24),
            
            Text("\nAvoid when:", font_size=32, color=RED),
            Text("• Function has side effects", font_size=24),
            Text("• Too many unique inputs (cache bloat)", font_size=24),
            Text("• For simple, fast functions", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.9).next_to(title4, DOWN, buff=1)
        
        self.play(Write(use_cases[0:4]))
        self.wait(1)
        self.play(Write(use_cases[4:]))
        self.wait(3)
        
        # Final slide
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        final = VGroup(
            Text("🎉 Key Takeaways", font_size=48, color=YELLOW),
            Text("• Memoization caches function results", font_size=32, color=WHITE),
            Text("• Use @lru_cache for easy implementation", font_size=32, color=WHITE),
            Text("• Great for recursive/expensive functions", font_size=32, color=WHITE),
            Text("• Not for functions with side effects", font_size=32, color=WHITE)
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(final[0]))
        self.play(LaggedStart(*[Write(p) for p in final[1:]], lag_ratio=0.3))
        self.wait(3)
