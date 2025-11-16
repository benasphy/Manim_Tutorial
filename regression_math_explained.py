from manim import *
import numpy as np

class LinearRegressionMath(Scene):
    def construct(self):
        # Main title
        main_title = Text("Understanding Linear Regression", font_size=36, color=BLUE)
        self.play(Write(main_title))
        self.wait(1)
        self.play(main_title.animate.to_edge(UP, buff=0.5))
        self.wait(0.5)
        
        # Part 1: Simple Linear Regression
        self.simple_linear_regression()
        
        # Part 2: Multiple Linear Regression
        self.clear_screen()
        self.multiple_linear_regression()
        
    def clear_screen(self):
        # Keep track of the last mobject (which is the section title)
        last_mobject = self.mobjects[-1] if self.mobjects else None
        
        # Fade out all mobjects except the last one (section title)
        mobs_to_fade = [mob for mob in self.mobjects if mob != last_mobject]
        if mobs_to_fade:
            self.play(*[FadeOut(mob) for mob in mobs_to_fade])
    
    def simple_linear_regression(self):
        # Section 1: Basic Equation and Explanation
        section_title = Text("1. Simple Linear Regression", font_size=28, color=YELLOW)
        section_title.next_to(self.mobjects[0], DOWN, buff=0.8)  # Positioned relative to main title
        self.play(Write(section_title))
        self.wait(0.5)
        
        # Equation
        eq1 = MathTex("y = \\beta_0 + \\beta_1 x + \\epsilon", color=GREEN)
        eq1.next_to(section_title, DOWN, buff=1.0)
        
        # Create and position the "Where:" text
        where_text = Text("Where:", font_size=24, color=WHITE).next_to(eq1, DOWN, buff=1.0).to_edge(LEFT)
        
        # Create all terms with proper relative positioning
        y_term = MathTex("y ", "\\text{ - Dependent variable (target)}", color=WHITE).scale(0.8)
        y_term.next_to(where_text, DOWN, buff=0.3).to_edge(LEFT)
            
        x_term = MathTex("x ", "\\text{ - Independent variable (feature)}", color=WHITE).scale(0.8)
        x_term.next_to(y_term, DOWN, buff=0.2).to_edge(LEFT)
            
        beta0_term = MathTex("\\beta_0 ", "\\text{ - y-intercept}", color=WHITE).scale(0.8)
        beta0_term.next_to(x_term, DOWN, buff=0.2).to_edge(LEFT)
            
        beta1_term = MathTex("\\beta_1 ", "\\text{ - Slope}", color=WHITE).scale(0.8)
        beta1_term.next_to(beta0_term, DOWN, buff=0.2).to_edge(LEFT)
            
        epsilon_term = MathTex("\\epsilon ", "\\text{ - Error term}", color=WHITE).scale(0.8)
        epsilon_term.next_to(beta1_term, DOWN, buff=0.2).to_edge(LEFT)
        
        # Group all terms together
        terms = VGroup(where_text, y_term, x_term, beta0_term, beta1_term, epsilon_term)
        
        self.play(Write(eq1))
        self.wait(1)
        self.play(Write(terms[0]))
        self.play(LaggedStart(*[Write(term) for term in terms[1:]], lag_ratio=0.2))
        self.wait(2)
        
        # Clear for next section
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Section 2: Vector and Matrix Forms
        section_title = Text("Simple Linear Regression", font_size=28, color=YELLOW).to_edge(UP)
        self.play(Write(section_title))
        self.wait(0.5)
        
        # Vector form
        vec_title = Text("Vector Form:", font_size=26, color=YELLOW).shift(UP * 1.5)
        vec_eq = MathTex(
            "\\mathbf{y} = \\mathbf{X}\\mathbf{\\beta} + \\mathbf{\\epsilon}",
            color=BLUE
        ).next_to(vec_title, DOWN)
        
        self.play(Write(vec_title))
        self.play(Write(vec_eq))
        self.wait(1.5)
        
        # Matrix form
        matrix_title = Text("Matrix Form:", font_size=26, color=YELLOW).next_to(vec_eq, DOWN, buff=1.0)
        matrix_eq = MathTex(
            "\\begin{bmatrix} y_1 \\\\ y_2 \\\\ \\vdots \\\\ y_m \\end{bmatrix} = "
            "\\begin{bmatrix} "
            "1 & x_1 \\\\ "
            "1 & x_2 \\\\ "
            "\\vdots & \\vdots \\\\ "
            "1 & x_m "
            "\\end{bmatrix} "
            "\\begin{bmatrix} \\beta_0 \\\\ \\beta_1 \\end{bmatrix} + "
            "\\begin{bmatrix} \\epsilon_1 \\\\ \\epsilon_2 \\\\ \\vdots \\\\ \\epsilon_m \\end{bmatrix}",
            color=WHITE
        ).scale(0.8).next_to(matrix_title, DOWN)
        
        self.play(Write(matrix_title))
        self.play(Write(matrix_eq))
        self.wait(2)
        
        # Clear for next section
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
    def multiple_linear_regression(self):
        # Section title
        section_title = Text("2. Multiple Linear Regression", font_size=32, color=YELLOW).to_edge(UP)
        if self.mobjects:
            self.play(Transform(self.mobjects[-1], section_title))
        else:
            self.play(Write(section_title))
        self.wait(0.5)
        
        # General form equation
        eq1 = MathTex(
            "y = \\beta_0 + \\beta_1 x_1 + \\beta_2 x_2 + \\dots + \\beta_n x_n + \\epsilon",
            color=GREEN
        ).shift(UP * 2)
        
        # Vectorized form
        eq2 = MathTex(
            "\\mathbf{y} = \\mathbf{X}\\mathbf{\\beta} + \\mathbf{\\epsilon}",
            color=BLUE
        ).next_to(eq1, DOWN * 1.5)
        
        # Matrix form
        matrix_eq = MathTex(
            "\\begin{bmatrix} y_1 \\\\ y_2 \\\\ \\vdots \\\\ y_m \\end{bmatrix} = "
            "\\begin{bmatrix} "
            "1 & x_{11} & x_{12} & \\dots & x_{1n} \\\\ "
            "1 & x_{21} & x_{22} & \\dots & x_{2n} \\\\ "
            "\\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\ "
            "1 & x_{m1} & x_{m2} & \\dots & x_{mn} "
            "\\end{bmatrix} "
            "\\begin{bmatrix} \\beta_0 \\\\ \\beta_1 \\\\ \\vdots \\\\ \\beta_n \\end{bmatrix} + "
            "\\begin{bmatrix} \\epsilon_1 \\\\ \\epsilon_2 \\\\ \\vdots \\\\ \\epsilon_m \\end{bmatrix}",
            color=WHITE
        ).scale(0.6).next_to(eq2, DOWN * 1.5)
        
        self.play(Write(eq1))
        self.wait(1)
        self.play(Write(eq2))
        self.wait(1)
        self.play(Write(matrix_eq))
        self.wait(2)
        
        # Clear for gradient descent section
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Add gradient descent explanation at the end
        self.gradient_descent_explanation()
    
    def gradient_descent_explanation(self):
        # Title for gradient descent section
        title = Text("Gradient Descent", font_size=36, color=BLUE).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Cost function explanation
        cost_title = Text("Cost Function (Mean Squared Error):", font_size=28, color=YELLOW).shift(UP * 1)
        cost_eq = MathTex(
            "J(\\theta) = \\frac{1}{2m} \\sum_{i=1}^{m} (h_\\theta(x^{(i)}) - y^{(i)})^2",
            color=GREEN
        ).next_to(cost_title, DOWN)
        
        self.play(Write(cost_title))
        self.play(Write(cost_eq))
        self.wait(2)
        
        # Gradient descent update rule
        gd_title = Text("Gradient Descent Update Rule:", font_size=28, color=YELLOW).shift(DOWN * 1)
        gd_eq = MathTex(
            "\\theta_j := \\theta_j - \\alpha \\frac{\\partial}{\\partial\\theta_j}J(\\theta)",
            color=GREEN
        ).next_to(gd_title, DOWN)
        
        self.play(Write(gd_title))
        self.play(Write(gd_eq))
        self.wait(2)
        
        # Learning rate note
        note = Text("α is the learning rate (step size)", font_size=24, color=YELLOW).shift(DOWN * 2.5)
        self.play(Write(note))
        self.wait(2)
