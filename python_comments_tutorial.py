from manim import *

class PythonCommentsTutorial(Scene):
    def construct(self):
        # Scene 1: Introduction to Comments
        self.intro_scene()
        
        # Clear the screen
        self.clear()
        
        # Scene 2: Why Comments are Important
        self.importance_scene()
        
        # Clear the screen
        self.clear()
        
        # Scene 3: How Python Handles Comments
        self.under_the_hood_scene()
    
    def intro_scene(self):
        # Title
        title = Text("💬 Python Comments", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Definition
        definition = Text(
            "Comments are notes in your code that Python ignores.",
            font_size=28,
            color=WHITE
        )
        self.play(Write(definition))
        self.wait(2)
        
        # Show example code with comments
        code = '''# This is a single-line comment

def greet(name):
    """
    This is a docstring (multi-line comment).
    It explains what the function does.
    
    Args:
        name (str): The name to greet
    """
    print(f"Hello, {name}!")

# This is another single-line comment
'''
        # Display code as simple text
        code_mobject = Text(
            code,
            font="Monospace",
            font_size=20,
            line_spacing=0.8,
            color=WHITE
        ).to_edge(LEFT, buff=1)
        
        # Add a background for better visibility
        code_bg = Rectangle(
            width=code_mobject.width * 1.1,
            height=code_mobject.height * 1.2,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=1
        ).move_to(code_mobject)
        
        self.play(ReplacementTransform(definition, code_mobject))
        self.wait(3)
        
        # Analogy
        analogy = Text(
            "Think of comments as sticky notes in a book -\n"
            "they help you understand but don't change the story.",
            font_size=24,
            color=YELLOW
        ).to_edge(DOWN)
        
        self.play(Write(analogy))
        self.wait(3)
    
    def importance_scene(self):
        # Title
        title = Text("🔍 Why Are Comments Important?", font_size=42, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Benefits
        benefits = VGroup(
            Text("1. Improve Code Readability", color=BLUE),
            Text("2. Help with Debugging", color=GREEN),
            Text("3. Document Functionality", color=YELLOW),
            Text("4. Team Collaboration", color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).scale(0.8)
        
        self.play(Write(benefits[0]))
        self.wait(1)
        self.play(Write(benefits[1]))
        self.wait(1)
        self.play(Write(benefits[2]))
        self.wait(1)
        self.play(Write(benefits[3]))
        self.wait(2)
        
        # Example: Bad vs Good Comments
        self.play(FadeOut(benefits))
        
        bad_code = """# Bad Example:
x = 10  # set x to 10
y = x * 2  # multiply x by 2
print(y)  # print y"""
        
        good_code = """# Good Example:
# Calculate total price with tax
TAX_RATE = 0.08  # 8% sales tax
subtotal = 100.0  # Price before tax
total = subtotal * (1 + TAX_RATE)  # Add tax to subtotal
print(f"Total: ${total:.2f}")  # Display formatted total"""
        
        # Display bad code example
        bad_code_mob = Text(
            bad_code,
            font="Monospace",
            font_size=18,
            line_spacing=0.8,
            color=WHITE
        ).to_edge(LEFT, buff=1)
        
        # Add background for bad code
        bad_bg = Rectangle(
            width=bad_code_mob.width * 1.1,
            height=bad_code_mob.height * 1.2,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=RED,
            stroke_width=1
        ).move_to(bad_code_mob)
        
        # Display good code example
        good_code_mob = Text(
            good_code,
            font="Monospace",
            font_size=18,
            line_spacing=0.8,
            color=WHITE
        ).to_edge(RIGHT, buff=1)
        
        # Add background for good code
        good_bg = Rectangle(
            width=good_code_mob.width * 1.1,
            height=good_code_mob.height * 1.2,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=GREEN,
            stroke_width=1
        ).move_to(good_code_mob)
        
        bad_label = Text("Less Helpful", color=RED).next_to(bad_code_mob, UP)
        good_label = Text("More Helpful", color=GREEN).next_to(good_code_mob, UP)
        
        self.play(Write(bad_label), Write(good_label))
        self.play(Write(bad_code_mob), Write(good_code_mob))
        self.wait(4)
    
    def under_the_hood_scene(self):
        # Title
        title = Text("🔧 How Python Handles Comments", font_size=42, color=ORANGE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Explanation
        explanation = Text(
            "Python's interpreter completely ignores comments during execution.",
            font_size=28,
            color=WHITE
        )
        self.play(Write(explanation))
        self.wait(2)
        
        # Show compilation process
        process = VGroup(
            Text("1. Source Code", color=YELLOW),
            Arrow(start=UP, end=DOWN, color=WHITE),
            Text("2. Parser (removes comments)", color=YELLOW),
            Arrow(start=UP, end=DOWN, color=WHITE),
            Text("3. Bytecode (no comments)", color=YELLOW)
        ).arrange(DOWN, buff=0.3).scale(0.8)
        
        self.play(ReplacementTransform(explanation, process))
        self.wait(3)
        
        # Docstrings are special
        docstring_note = Text(
            "Docstrings are stored as part of the function/class/module\n"
            "and can be accessed using the .__doc__ attribute or help()",
            font_size=24,
            color=GREEN
        ).to_edge(DOWN)
        
        self.play(Write(docstring_note))
        
        # Example of docstring access
        example_code = '''def example():
    """This is a docstring"""
    pass

# Access the docstring
print(example.__doc__)  # Output: This is a docstring
help(example)  # Shows the docstring'''
        
        # Display docstring example
        example_mob = Text(
            example_code,
            font="Monospace",
            font_size=18,
            line_spacing=0.8,
            color=WHITE
        ).next_to(process, DOWN, buff=1)
        
        # Add a background for the example code
        example_bg = Rectangle(
            width=example_mob.width * 1.1,
            height=example_mob.height * 1.2,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=YELLOW,
            stroke_width=1
        ).move_to(example_mob)
        
        self.play(Write(example_mob))
        self.wait(4)
        
        # Final note
        final_note = Text(
            "Remember: Good comments explain why, not what!",
            font_size=30,
            color=YELLOW
        ).to_edge(DOWN)
        
        self.play(Write(final_note))
        self.wait(3)

# To run the animation:
# manim -pql python_comments_tutorial.py PythonCommentsTutorial
