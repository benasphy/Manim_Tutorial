from manim import *

class ThreadingTutorial(Scene):
    def construct(self):
        # Scene 1: Title and Introduction
        title = Text("🧵 Python Threading", font_size=48, color=BLUE)
        subtitle = Text("Running Multiple Tasks Concurrently", font_size=32, color=YELLOW)
        
        self.play(Write(title))
        self.play(Write(subtitle.next_to(title, DOWN, buff=0.5)))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 2: What is Threading?
        title1 = Text("1️⃣ What is Threading?", font_size=42, color=BLUE)
        self.play(Write(title1))
        self.play(title1.animate.to_edge(UP))
        
        definition = VGroup(
            Text("Threading allows multiple tasks to run concurrently", font_size=28, color=WHITE),
            Text("within the same program.", font_size=28, color=WHITE),
            Text("• Like having multiple hands working on different tasks", font_size=24, color=YELLOW),
            Text("• All threads share the same memory space", font_size=24, color=YELLOW),
            Text("• Great for I/O-bound tasks (networking, file operations)", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title1, DOWN, buff=1)
        
        self.play(Write(definition[0:2]))
        self.wait(0.5)
        self.play(Write(definition[2:]))
        self.wait(2)
        
        # Clear for cooking analogy scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 2: Cooking Analogy
        analogy_title = Text("👨‍🍳 Cooking Analogy", font_size=36, color=GREEN)
        self.play(Write(analogy_title))
        self.play(analogy_title.animate.to_edge(UP))
        
        # Create cooking scene with built-in shapes
        # Chef (simplified as a circle with a face)
        head = Circle(radius=0.5, color=WHITE, fill_opacity=1)
        body = Rectangle(height=0.8, width=0.6, color=WHITE, fill_opacity=1).next_to(head, DOWN, buff=0)
        chef = VGroup(head, body).scale(1.2).to_edge(LEFT, buff=1.5)
        
        # Pan (simplified as a circle with a handle)
        pan_body = Circle(radius=0.4, color=WHITE, fill_opacity=1)
        pan_handle = Rectangle(height=0.1, width=0.6, color=WHITE, fill_opacity=1).next_to(pan_body, RIGHT, buff=0)
        pan = VGroup(pan_body, pan_handle).next_to(chef, RIGHT, buff=1)
        
        # Cutting board (simplified as a rectangle with wood texture)
        cutting_board = Rectangle(
            height=0.3, width=1.2, 
            color=WHITE, fill_opacity=1,
            stroke_width=2,
            stroke_color=WHITE
        ).next_to(chef, LEFT, buff=1)
        
        # Add wood grain texture
        wood_grain = VGroup(*[
            Line(
                cutting_board.get_left() + UP * 0.1 * i,
                cutting_board.get_right() + UP * 0.1 * i,
                stroke_width=1,
                color=WHITE,
                stroke_opacity=0.3
            ) for i in range(-1, 2)
        ])
        cutting_board = VGroup(cutting_board, wood_grain)
        
        self.play(
            FadeIn(chef, shift=LEFT),
            FadeIn(pan, shift=UP),
            FadeIn(cutting_board, shift=RIGHT)
        )
        
        # Animate tasks
        stir_arrow = Arrow(pan.get_top() + UP*0.5, pan.get_top(), buff=0.1, color=YELLOW)
        chop_arrow = Arrow(cutting_board.get_top() + UP*0.5, cutting_board.get_top(), buff=0.1, color=YELLOW)
        
        self.play(Write(Text("Stirring soup...", font_size=20).next_to(pan, DOWN)))
        self.play(Create(stir_arrow), run_time=0.5)
        self.wait(0.5)
        self.play(Write(Text("Chopping veggies...", font_size=20).next_to(cutting_board, DOWN)))
        self.play(Create(chop_arrow), run_time=0.5)
        
        # Show both tasks happening
        self.play(
            Rotate(pan, angle=0.3, about_point=pan.get_center(), run_time=1, rate_func=there_and_back),
            Rotate(cutting_board, angle=0.3, about_point=cutting_board.get_center(), run_time=1, rate_func=there_and_back)
        )
        
        self.wait(1)
        
        self.wait(2)
        
        # Clear for common uses scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 3: Common Use Cases
        uses_title = Text("🔧 Common Use Cases", font_size=36, color=YELLOW)
        self.play(Write(uses_title))
        self.play(uses_title.animate.to_edge(UP))
        
        # Common use cases
        uses = VGroup(
            Text("Threading is perfect for:", font_size=28, color=WHITE).next_to(uses_title, DOWN, buff=1),
            Text("• Downloading files while keeping UI responsive", font_size=24, color=YELLOW),
            Text("• Handling multiple client requests in servers", font_size=24, color=YELLOW),
            Text("• Background tasks (logging, monitoring, etc.)", font_size=24, color=YELLOW),
            Text("• Web scraping multiple pages simultaneously", font_size=24, color=YELLOW),
            Text("• Processing multiple network requests", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(uses_title, DOWN, buff=1.5)
        
        self.play(Write(uses[0]))
        self.wait(0.5)
        self.play(LaggedStart(*[Write(use) for use in uses[1:]], lag_ratio=0.3))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 3: Threads vs Processes
        title2 = Text("2️⃣ Threads vs Processes", font_size=42, color=BLUE)
        self.play(Write(title2))
        self.play(title2.animate.to_edge(UP))
        
        # Restaurant analogy
        analogy = VGroup(
            Text("🍽️ Restaurant Analogy", font_size=32, color=GREEN).next_to(title2, DOWN, buff=1),
            Text("Processes are like different restaurants", font_size=24, color=WHITE),
            Text("• Each has its own kitchen, tables, and staff", font_size=20, color=YELLOW),
            Text("• Completely independent from each other", font_size=20, color=YELLOW),
            Text("• Heavy to start/stop", font_size=20, color=YELLOW),
            
            Text("\nThreads are like tables in the same restaurant", font_size=24, color=WHITE).next_to(title2, DOWN, buff=3.5),
            Text("• Share the same kitchen and resources", font_size=20, color=YELLOW),
            Text("• Lighter weight, faster to start/stop", font_size=20, color=YELLOW),
            Text("• But need to coordinate (like sharing a waiter)", font_size=20, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.9)
        
        self.play(Write(analogy[0]))
        self.wait(0.5)
        self.play(Write(analogy[1:5]))
        self.wait(1)
        self.play(Write(analogy[5:]))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 4: Under the Hood (GIL)
        title3 = Text("🔧 What's Happening Under the Hood?", font_size=36, color=BLUE)
        self.play(Write(title3))
        self.play(title3.animate.to_edge(UP))
        
        # GIL Explanation
        gil_title = Text("Python's Global Interpreter Lock (GIL)", font_size=32, color=YELLOW)
        self.play(Write(gil_title.next_to(title3, DOWN, buff=1)))
        
        gil_explanation = VGroup(
            Text("• Only one thread can execute Python bytecode at a time", font_size=24, color=WHITE),
            Text("• Prevents multiple threads from modifying Python objects", font_size=24, color=WHITE),
            Text("• Makes Python thread-safe by default", font_size=24, color=GREEN),
            Text("• But can limit performance for CPU-bound tasks", font_size=24, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(gil_title, DOWN, buff=1)
        
        self.play(Write(gil_explanation[0]))
        self.wait(0.3)
        for item in gil_explanation[1:]:
            self.play(Write(item))
            self.wait(0.2)
        
        self.wait(1)
        
        # Clear for spoon analogy scene
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != title3])
        
        # New Scene: Spoon Analogy
        spoon_title = Text("🍴 Spoon Analogy for GIL", font_size=36, color=GREEN)
        self.play(ReplacementTransform(title3, spoon_title))
        self.play(spoon_title.animate.to_edge(UP))
        
        # Spoon Analogy
        spoon_analogy = VGroup(
            Text("Imagine a kitchen with one spoon (GIL):", font_size=28, color=WHITE).next_to(spoon_title, DOWN, buff=1),
            Text("• Only one person can use the spoon at a time", font_size=24, color=YELLOW),
            Text("• Others must wait their turn (synchronization)", font_size=24, color=YELLOW),
            Text("• But they can prepare food (I/O) while waiting", font_size=24, color=YELLOW),
            Text("• This is why threads are great for I/O-bound tasks!", font_size=24, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(spoon_title, DOWN, buff=1.5)
        
        # Create visual of people sharing a spoon
        try:
            spoon = SVGMobject("manim/assets/svg_images/spoon.svg", height=0.5, color=YELLOW).to_edge(RIGHT, buff=2)
            self.play(FadeIn(spoon))
        except:
            spoon = Line(ORIGIN, RIGHT*0.5, stroke_width=10, color=YELLOW).to_edge(RIGHT, buff=2)
            spoon = VGroup(
                spoon,
                Circle(radius=0.1, color=YELLOW, fill_opacity=1).next_to(spoon, LEFT, buff=0)
            )
            self.play(FadeIn(spoon))
        
        # Create people as circles with different colors
        people = VGroup(*[
            Circle(radius=0.3, color=color, fill_opacity=0.8).shift(LEFT*2 + UP*i*0.7) 
            for i, color in enumerate([BLUE, GREEN, RED])
        ])
        
        self.play(LaggedStart(*[FadeIn(p) for p in people], lag_ratio=0.3))
        self.wait(0.5)
        
        # Animate spoon being passed
        for i, person in enumerate(people):
            self.play(spoon.animate.next_to(person, RIGHT, buff=0.2).shift(UP*0.1), run_time=0.7)
            self.wait(0.3)
        
        self.wait(0.5)
        self.play(Write(spoon_analogy[0]))
        self.wait(0.5)
        self.play(LaggedStart(*[Write(item) for item in spoon_analogy[1:]], lag_ratio=0.3))
        self.wait(2)
        
        # Clear for when to use threads vs multiprocessing
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # New Scene: When to Use Threads vs Multiprocessing
        title_use = Text("🔄 When to Use Threads vs Multiprocessing", font_size=36, color=BLUE)
        self.play(Write(title_use))
        self.play(title_use.animate.to_edge(UP))
        
        # When to use threads vs multiprocessing
        when_to_use = VGroup(
            Text("✅ Use Threads When:", font_size=30, color=GREEN).to_edge(UP, buff=2),
            Text("• Tasks are I/O-bound (network, file operations, APIs)", font_size=24, color=YELLOW),
            Text("• You need to keep a UI responsive", font_size=24, color=YELLOW),
            Text("• Tasks involve waiting for external resources", font_size=24, color=YELLOW),
            
            Text("\n❌ Use Multiprocessing When:", font_size=30, color=RED).to_edge(UP, buff=5.5),
            Text("• Tasks are CPU-bound (math, data processing)", font_size=24, color=YELLOW),
            Text("• You need true parallel execution", font_size=24, color=YELLOW),
            Text("• Tasks are computation-intensive", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).scale(0.9)
        
        # Create a visual comparison using built-in shapes
        # Threads visualization (multiple lines for threading)
        thread_icon = VGroup(*[
            Line(UP*0.5, DOWN*0.5, color=GREEN, stroke_width=3).shift(LEFT*3 + RIGHT*i*0.3) 
            for i in range(3)
        ]).to_edge(LEFT, buff=2)
        
        # Processes visualization (separate containers)
        process_icon = VGroup(*[
            Circle(radius=0.5, color=RED, fill_opacity=0.2, stroke_width=2)
            .shift(RIGHT*2 + UP*(i-1)*0.6)
            for i in range(3)
        ]).to_edge(RIGHT, buff=2)
        
        # Add labels
        thread_label = Text("Threads", font_size=20, color=GREEN).next_to(thread_icon, DOWN)
        process_label = Text("Processes", font_size=20, color=RED).next_to(process_icon, DOWN)
        
        self.play(
            FadeIn(thread_icon),
            FadeIn(process_icon),
            Write(thread_label),
            Write(process_label)
        )
        
        # Animate the text appearing
        self.play(Write(when_to_use[0]))
        self.play(LaggedStart(*[Write(item) for item in when_to_use[1:4]], lag_ratio=0.3))
        self.wait(0.5)
        self.play(Write(when_to_use[4]))
        self.play(LaggedStart(*[Write(item) for item in when_to_use[5:]], lag_ratio=0.3))
        
        # Add connecting line with explanation
        vs_text = Text("vs", font_size=40, color=WHITE).move_to(ORIGIN)
        comparison = Text("Shared Memory  |  Separate Memory", font_size=20, color=YELLOW).next_to(vs_text, DOWN, buff=0.5)
        
        # Add arrows to show memory sharing
        thread_arrow = Arrow(
            thread_icon.get_right() + RIGHT*0.5,
            thread_icon.get_right() + RIGHT*1.5,
            color=GREEN,
            buff=0.1,
            max_tip_length_to_length_ratio=0.2
        )
        
        process_arrow = Arrow(
            process_icon.get_left() + LEFT*0.5,
            process_icon.get_left() + LEFT*1.5,
            color=RED,
            buff=0.1,
            max_tip_length_to_length_ratio=0.2
        )
        
        self.play(
            Write(vs_text),
            Write(comparison),
            GrowArrow(thread_arrow),
            GrowArrow(process_arrow)
        )
        
        self.wait(3)
        
        # Final slide
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        final = VGroup(
            Text("🎉 Key Takeaways", font_size=48, color=YELLOW),
            Text("• Threads let you run multiple tasks concurrently", font_size=28, color=WHITE),
            Text("• Great for I/O-bound tasks, not CPU-bound ones", font_size=28, color=WHITE),
            Text("• Threads share memory, processes don't", font_size=28, color=WHITE),
            Text("• Python's GIL means only one thread runs Python code at a time", font_size=28, color=WHITE),
            Text("• For CPU-heavy work, consider multiprocessing instead", font_size=28, color=YELLOW)
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(final[0]))
        self.play(LaggedStart(*[Write(takeaway) for takeaway in final[1:]], lag_ratio=0.3))
        self.wait(3)
