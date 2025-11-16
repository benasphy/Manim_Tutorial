from manim import *

class MathOperationsTutorial(Scene):
    def construct(self):
        # Scene 1: Introduction to Math in Python
        self.intro_scene()
        
        # Clear the screen
        self.clear()
        
        # Scene 2: Under the Hood - Number Types
        self.number_types_scene()
        
        # Clear the screen
        self.clear()
        
        # Final message
        self.show_final_message()
    
    def intro_scene(self):
        # Title
        title = Text("🧮 Math Operations in Python", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Main points
        points = VGroup(
            Text("• Python is a powerful calculator", font_size=32, color=WHITE),
            Text("• Supports basic to advanced math operations", font_size=32, color=WHITE),
            Text("• Essential for data science, AI, and engineering", font_size=32, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(title, DOWN, buff=1)
        
        self.play(Write(points[0]))
        self.wait(0.5)
        self.play(Write(points[1:]))
        self.wait(1)
        
        # Digital notebook analogy
        notebook = VGroup(
            Rectangle(width=6, height=4, color=WHITE, fill_color=BLACK, fill_opacity=0.8),
            Text("Python Notebook", font_size=24, color=YELLOW).to_edge(UP, buff=0.2)
        )
        
        calculator = VGroup(
            Rectangle(width=3, height=2, color=BLUE, fill_color=BLACK, fill_opacity=0.8),
            Text("Calculator", font_size=16, color=WHITE).to_edge(UP, buff=0.1)
        )
        
        notebook.next_to(points, DOWN, buff=1)
        calculator.next_to(notebook, RIGHT, buff=1)
        
        self.play(Create(notebook), Create(calculator))
        
        # Draw connection
        arrow = Arrow(
            notebook.get_right(),
            calculator.get_left(),
            buff=0.2,
            color=YELLOW
        )
        
        analogy_text = Text(
            "Python combines the power of a notebook and calculator\n"
            "Write formulas → Get instant results",
            font_size=24,
            color=YELLOW
        ).next_to(VGroup(notebook, calculator), DOWN, buff=0.5)
        
        self.play(GrowArrow(arrow), Write(analogy_text))
        self.wait(3)
    
    def number_types_scene(self):
        # Title
        title = Text("🧠 Under the Hood: Python Numbers", font_size=42, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Number type explanations
        int_explanation = self.create_number_card(
            "Integer (int)",
            "Unlimited precision\nNo size limit like in C/Java",
            BLUE
        )
        
        float_explanation = self.create_number_card(
            "Float (float)",
            "IEEE 754 standard\nApproximate decimals",
            YELLOW
        )
        
        complex_explanation = self.create_number_card(
            "Complex (complex)",
            "Built-in support\nReal + Imaginary parts",
            PINK
        )
        
        # Arrange in a row
        explanations = VGroup(int_explanation, float_explanation, complex_explanation)
        explanations.arrange(RIGHT, buff=1).next_to(title, DOWN, buff=1)
        
        # Animate in sequence
        self.play(FadeIn(int_explanation, shift=UP))
        self.wait(0.5)
        self.play(FadeIn(float_explanation, shift=UP))
        self.wait(0.5)
        self.play(FadeIn(complex_explanation, shift=UP))
        self.wait(1)
        
        # Add container analogy
        analogy = VGroup(
            Text("Think of numbers like containers:", font_size=28, color=YELLOW),
            Text("• int = Expandable container (grows as needed)", font_size=24, color=WHITE),
            Text("• float = Measuring tape (limited precision)", font_size=24, color=WHITE),
            Text("• complex = Two-part container (real + imaginary)", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(explanations, DOWN, buff=1)
        
        self.play(Write(analogy[0]))
        self.play(Write(analogy[1:]))
        self.wait(2)
    
    def create_number_card(self, title, description, color):
        """Helper function to create a card for number type explanation"""
        card = VGroup(
            Rectangle(
                width=3.5,
                height=2.5,
                color=color,
                fill_color=BLACK,
                fill_opacity=0.8,
                stroke_width=2
            ),
            Text(title, font_size=24, color=color).to_edge(UP, buff=0.3),
            Text(description, font_size=18, color=WHITE, line_spacing=1.2)
            .scale(0.8)
            .next_to(Text("", font_size=24), DOWN, buff=0.5)
        )
        return card
    
    def show_final_message(self):
        final = Text("Now you understand Python math operations! 🎉", font_size=36, color=GREEN)
        self.play(Write(final))
        self.wait(2)
        self.play(FadeOut(final))
        
        # Add a call to action
        cta = Text("Try these in your Python console!", font_size=28, color=YELLOW)
        examples = Text(
            "3 + 4 * 2\n"
            "10 / 3\n"
            "2 ** 10\n"
            "3.14 * (5 ** 2)",
            font="Monospace",
            font_size=24,
            color=WHITE
        )
        
        group = VGroup(cta, examples).arrange(DOWN, buff=0.8)
        self.play(Write(cta))
        self.wait(0.5)
        self.play(Write(examples))
        self.wait(3)
