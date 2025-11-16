from manim import *

class IfStatementsTutorial(Scene):
    def construct(self):
        # Scene 1: Introduction to If Statements
        self.intro_scene()
        
        # Clear the screen
        self.clear()
        
        # Scene 2: Under the Hood - How Python Evaluates Conditions
        self.under_the_hood_scene()
        
        # Clear the screen
        self.clear()
        
        # Scene 3: Best Practices
        self.best_practices_scene()
        
        # Final message
        self.show_final_message()
    
    def intro_scene(self):
        # Title
        title = Text("🔀 Python If Statements", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Main points
        points = VGroup(
            Text("• Programs need to make decisions", font_size=32, color=WHITE),
            Text("• if/elif/else control program flow", font_size=32, color=WHITE),
            Text("• Just like making choices in real life!", font_size=32, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(title, DOWN, buff=1)
        
        self.play(Write(points[0]))
        self.wait(0.5)
        self.play(Write(points[1:]))
        self.wait(1)
        
        # Real-life decision tree
        self.show_decision_tree()
    
    def show_decision_tree(self):
        # Create decision tree
        decision = Text("Going outside?", font_size=28, color=YELLOW)
        decision.to_edge(UP, buff=1.5)
        
        # Conditions and actions
        conditions = VGroup(
            Text("if raining:", color=BLUE, font="Monospace"),
            Text("    take_umbrella()", color=GREEN, font="Monospace"),
            Text("elif cloudy:", color=BLUE, font="Monospace"),
            Text("    take_jacket()", color=GREEN, font="Monospace"),
            Text("else:", color=BLUE, font="Monospace"),
            Text("    go_outside()", color=GREEN, font="Monospace")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(decision, DOWN, buff=1)
        
        # Add background for code
        code_bg = Rectangle(
            width=conditions.width * 1.2,
            height=conditions.height * 1.4,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=1
        ).move_to(conditions)
        
        # Show decision tree
        self.play(Write(decision))
        self.wait(0.5)
        self.play(Create(code_bg))
        
        # Animate conditions appearing one by one
        for i in range(0, len(conditions), 2):
            self.play(Write(conditions[i:i+2]))
            self.wait(0.5)
        
        self.wait(2)
    
    def under_the_hood_scene(self):
        # Title
        title = Text("🔍 How Python Evaluates Conditions", font_size=42, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Checklist analogy
        checklist = VGroup(
            Text("Python checks conditions like a checklist:", font_size=30, color=YELLOW),
            Text("1. Is the first condition True?", font_size=26, color=WHITE),
            Text("   ✓ If yes: Run this block and stop", font_size=24, color=GREEN),
            Text("   ✗ If no: Move to next condition", font_size=24, color=RED),
            Text("2. If no conditions match, run else (if it exists)", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=1)
        
        self.play(Write(checklist[0]))
        self.wait(0.5)
        self.play(Write(checklist[1:]))
        self.wait(2)
        
        # Visual example
        example_code = '''temperature = 25

if temperature > 30:
    print("It's hot!")
elif temperature > 20:
    print("It's pleasant!")
else:
    print("It's cold!")'''
        
        code_mob = Text(
            example_code,
            font="Monospace",
            font_size=20,
            line_spacing=0.8,
            color=WHITE
        )
        
        code_bg = Rectangle(
            width=code_mob.width * 1.2,
            height=code_mob.height * 1.3,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=YELLOW,
            stroke_width=1
        ).next_to(checklist, DOWN, buff=1)
        
        code_mob.move_to(code_bg)
        
        self.play(Create(code_bg), Write(code_mob))
        
        # Highlight the path Python takes
        temp_text = Text("temperature = 25", color=YELLOW, font_size=24)
        temp_text.next_to(code_bg, RIGHT, buff=1)
        arrow = Arrow(temp_text.get_left(), code_bg.get_right(), buff=0.1, color=YELLOW)
        
        self.play(
            Write(temp_text),
            GrowArrow(arrow)
        )
        
        # Show evaluation path
        path = VGroup(
            Text("25 > 30? False → Move to next", color=RED, font_size=20),
            Text("25 > 20? True! Run this block", color=GREEN, font_size=20),
            Text("Skip the rest", color=GRAY, font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(code_bg, DOWN, buff=1)
        
        self.play(Write(path[0]))
        self.wait(0.5)
        self.play(Write(path[1]))
        self.wait(0.3)
        self.play(Write(path[2]))
        self.wait(2)
    
    def best_practices_scene(self):
        # Title
        title = Text("🏆 Best Practices", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Best practices
        practices = VGroup(
            Text("✅ Keep conditions readable:", font_size=28, color=YELLOW),
            Text("   if (age >= 18) and (has_id):", font="Monospace", font_size=22, color=WHITE),
            Text("✅ Use elif instead of nested ifs:", font_size=28, color=YELLOW),
            Text("   if x > 10: ...\n   elif x > 5: ...", font="Monospace", font_size=22, color=WHITE),
            Text("✅ Only use else when needed:", font_size=28, color=YELLOW),
            Text("   if x > 0: ...\n   else: ...  # Only if you need a default", font="Monospace", font_size=22, color=WHITE),
            Text("❌ Don't repeat conditions:", font_size=28, color=YELLOW),
            Text("   if x > 0: ...\n   if x <= 0: ...  # Use else instead!", font="Monospace", font_size=22, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.9).next_to(title, DOWN, buff=1)
        
        # Add background for better visibility
        bg = Rectangle(
            width=practices.width * 1.2,
            height=practices.height * 1.3,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=BLUE,
            stroke_width=2
        ).move_to(practices)
        
        self.play(Create(bg))
        
        # Animate practices appearing in groups
        for i in range(0, len(practices), 2):
            self.play(Write(practices[i:i+2]))
            self.wait(0.5)
        
        self.wait(2)
    
    def show_final_message(self):
        final = Text("Now you understand Python if statements! 🎉", font_size=36, color=GREEN)
        self.play(Write(final))
        self.wait(2)
        
        # Add a call to action
        cta = Text("Try these in your Python console!", font_size=28, color=YELLOW)
        examples = Text(
            "x = 10\n"
            "if x > 5:\n"
            "    print(\"x is greater than 5\")\n"
            "elif x == 5:\n"
            "    print(\"x is 5\")\n"
            "else:\n"
            "    print(\"x is less than 5\")",
            font="Monospace",
            font_size=20,
            color=WHITE
        )
        
        group = VGroup(cta, examples).arrange(DOWN, buff=0.8)
        self.play(Transform(final, cta))
        self.wait(0.5)
        self.play(Write(examples))
        self.wait(3)
