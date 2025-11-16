from manim import *
import numpy as np

class SVMTutorial(Scene):
    def construct(self):
        # Scene 1: Introduction
        self.scene_intro()
        self.clear()
        
        # Scene 2: Types of SVM
        self.scene_svm_types()
        self.clear()
        
        # Scene 3: How SVM Works
        self.scene_how_svm_works()
        self.clear()
        
        # Scene 4: Math Behind SVM
        self.scene_math_behind()
        self.clear()
        
        # Scene 5: Soft Margin SVM
        self.scene_soft_margin()
        self.clear()
        
        # Scene 6: Kernels in SVM
        self.scene_kernels()
        self.clear()
        
        # Scene 7: Choosing the Right Kernel
        self.scene_choose_kernel()
        self.clear()
        
        # Scene 8: Conclusion
        self.scene_conclusion()
    
    def scene_intro(self):
        # Title
        title = Text("Support Vector Machines (SVM)", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Definition
        definition = Text(
            "A powerful supervised learning algorithm for classification and regression",
            font_size=28,
            color=WHITE
        )
        self.play(Write(definition))
        self.wait(1)
        self.play(FadeOut(definition))
        
        # Create sample data
        np.random.seed(0)
        class1 = np.random.randn(10, 2) + [2, 2]
        class2 = np.random.randn(10, 2) + [-2, -2]
        
        # Create scatter plot
        dots1 = VGroup(*[Dot(point=[x, y, 0], color=BLUE) for x, y in class1])
        dots2 = VGroup(*[Dot(point=[x, y, 0], color=RED) for x, y in class2])
        
        # Create axes
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            axis_config={"color": WHITE},
            tips=False
        )
        
        # Add everything to scene
        self.play(Create(axes), run_time=1)
        self.play(Create(dots1), Create(dots2), run_time=1.5)
        
        # Add separating line
        line = Line(start=[-5, -5, 0], end=[5, 5, 0], color=YELLOW)
        self.play(Create(line), run_time=1)
        
        # Add labels
        label1 = Text("Class 1", color=BLUE).next_to(dots1[0], UP)
        label2 = Text("Class -1", color=RED).next_to(dots2[0], DOWN)
        self.play(Write(label1), Write(label2))
        
        self.wait(2)
    
    def scene_svm_types(self):
        # Title
        title = Text("Types of SVM", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create two columns
        left_col = VGroup()
        right_col = VGroup()
        
        # Linear SVM
        linear_title = Text("Linear SVM", font_size=32, color=GREEN)
        linear_desc = Text("Uses a straight line\nto separate classes", font_size=24)
        linear = VGroup(linear_title, linear_desc).arrange(DOWN, buff=0.5)
        
        # Non-linear SVM
        nonlin_title = Text("Non-linear SVM", font_size=32, color=ORANGE)
        nonlin_desc = Text("Uses curves or circles\nto separate classes", font_size=24)
        nonlin = VGroup(nonlin_title, nonlin_desc).arrange(DOWN, buff=0.5)
        
        # Arrange in columns
        left_col.add(linear)
        right_col.add(nonlin)
        
        # Create a group for the grid
        grid = VGroup(left_col, right_col).arrange(RIGHT, buff=1.5)
        grid.next_to(title, DOWN, buff=1)
        
        # Add to scene
        self.play(Write(linear_title))
        self.play(Write(linear_desc))
        self.wait(0.5)
        
        self.play(Write(nonlin_title))
        self.play(Write(nonlin_desc))
        self.wait(1)
        
        # Add example visualizations
        self.play(grid.animate.scale(0.8).to_edge(UP, buff=1.5))
        
        # Linear example
        linear_plot = self._create_linear_example()
        linear_plot.next_to(linear, DOWN, buff=0.5)
        self.play(Create(linear_plot))
        
        # Non-linear example
        nonlin_plot = self._create_nonlinear_example()
        nonlin_plot.next_to(nonlin, DOWN, buff=0.5)
        self.play(Create(nonlin_plot))
        
        self.wait(2)
    
    def scene_how_svm_works(self):
        # Title
        title = Text("How SVM Works", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create sample data
        np.random.seed(1)
        class1 = np.random.randn(10, 2) * 0.5 + [1, 1]
        class2 = np.random.randn(10, 2) * 0.5 + [-1, -1]
        
        # Create scatter plot
        dots1 = VGroup(*[Dot(point=[x, y, 0], color=BLUE) for x, y in class1])
        dots2 = VGroup(*[Dot(point=[x, y, 0], color=RED) for x, y in class2])
        
        # Create axes
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={"color": WHITE},
            tips=False
        )
        
        # Add everything to scene
        self.play(Create(axes), run_time=1)
        self.play(Create(dots1), Create(dots2), run_time=1.5)
        
        # Add separating line (hyperplane)
        hyperplane = Line(start=[-3, -3, 0], end=[3, 3, 0], color=YELLOW)
        self.play(Create(hyperplane), run_time=1)
        
        # Add margins
        margin = 1.0
        margin1 = hyperplane.copy().shift(UP * margin / np.sqrt(2))
        margin2 = hyperplane.copy().shift(DOWN * margin / np.sqrt(2))
        
        margin1.set_color(GREEN)
        margin2.set_color(GREEN)
        
        self.play(Create(margin1), Create(margin2), run_time=1)
        
        # Highlight support vectors (points closest to the hyperplane)
        support_vectors = VGroup(dots1[3], dots2[2])
        self.play(
            *[dot.animate.set_color(YELLOW).scale(1.5) for dot in support_vectors],
            run_time=1.5
        )
        
        # Add labels
        sv_label = Text("Support Vectors", color=YELLOW).to_edge(DOWN)
        self.play(Write(sv_label))
        
        self.wait(2)
    
    def scene_math_behind(self):
        # Title
        title = Text("Math Behind SVM", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Hyperplane equation
        hyperplane_eq = MathTex(
            r"w \cdot x + b = 0",
            font_size=48,
            color=YELLOW
        )
        hyperplane_label = Text("Hyperplane equation:", font_size=32).next_to(hyperplane_eq, UP)
        
        # Margin formula
        margin_eq = MathTex(
            r"\text{Margin} = \frac{2}{\|w\|}",
            font_size=48,
            color=GREEN
        ).next_to(hyperplane_eq, DOWN, buff=1)
        
        # Optimization problem
        opt_problem = MathTex(
            r"\min_{w,b} \frac{1}{2} \|w\|^2",
            r"\text{s.t. } y_i(w \cdot x_i + b) \geq 1, \forall i",
            font_size=36,
            color=ORANGE
        ).arrange(DOWN, aligned_edge=LEFT).next_to(margin_eq, DOWN, buff=1)
        
        # Add to scene
        self.play(Write(hyperplane_label))
        self.play(Write(hyperplane_eq))
        self.wait(1)
        
        self.play(Write(margin_eq))
        self.wait(1)
        
        self.play(Write(opt_problem))
        self.wait(2)
    
    def scene_soft_margin(self):
        # Title
        title = Text("Soft Margin SVM", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create sample data with some overlap
        np.random.seed(2)
        class1 = np.random.randn(8, 2) * 0.5 + [1, 1]
        class2 = np.random.randn(8, 2) * 0.5 + [-1, -1]
        
        # Add some overlapping points
        overlap1 = np.random.randn(4, 2) * 0.3 + [0, 0]
        overlap2 = np.random.randn(4, 2) * 0.3 + [0, 0]
        
        class1 = np.vstack([class1, overlap1])
        class2 = np.vstack([class2, overlap2])
        
        # Create scatter plot
        dots1 = VGroup(*[Dot(point=[x, y, 0], color=BLUE) for x, y in class1])
        dots2 = VGroup(*[Dot(point=[x, y, 0], color=RED) for x, y in class2])
        
        # Create axes
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            axis_config={"color": WHITE},
            tips=False
        )
        
        # Add everything to scene
        self.play(Create(axes), run_time=1)
        self.play(Create(dots1), Create(dots2), run_time=1.5)
        
        # Add separating line (hyperplane)
        hyperplane = Line(start=[-3, -3, 0], end=[3, 3, 0], color=YELLOW)
        self.play(Create(hyperplane), run_time=1)
        
        # Add slack variables explanation
        slack_eq = MathTex(
            r"\min_{w,b,\xi} \frac{1}{2} \|w\|^2 + C\sum_{i=1}^n \xi_i \\
            \text{s.t. } y_i(w \cdot x_i + b) \geq 1 - \xi_i \\
            \xi_i \geq 0",
            font_size=32,
            color=GREEN
        ).to_edge(RIGHT)
        
        self.play(Write(slack_eq))
        
        # Show C parameter effect
        c_text = Text("C = 0.1", font_size=32, color=YELLOW).to_edge(LEFT).shift(UP*2)
        self.play(Write(c_text))
        
        # Animate different C values
        for c_val in [0.1, 1, 10, 100]:
            new_text = Text(f"C = {c_val}", font_size=32, color=YELLOW).to_edge(LEFT).shift(UP*2)
            self.play(Transform(c_text, new_text))
            self.wait(0.5)
        
        self.wait(2)
    
    def scene_kernels(self):
        # Title
        title = Text("Kernels in SVM", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Kernel types
        kernels = VGroup(
            self._create_kernel_card("Linear", r"K(x_i, x_j) = x_i \cdot x_j"),
            self._create_kernel_card("Polynomial", r"K(x_i, x_j) = (x_i \cdot x_j + c)^d"),
            self._create_kernel_card("RBF (Gaussian)", r"K(x_i, x_j) = \exp\left(-\frac{\|x_i - x_j\|^2}{2\sigma^2}\right)")
        ).arrange(RIGHT, buff=0.5).scale(0.9).next_to(title, DOWN, buff=1)
        
        # Add to scene
        self.play(LaggedStart(
            *[FadeIn(kernel, shift=UP) for kernel in kernels],
            lag_ratio=0.3
        ))
        
        # Show example data for each kernel
        self.play(kernels.animate.scale(0.8).to_edge(UP, buff=1.5))
        
        # Show example plots
        linear_plot = self._create_linear_plot()
        poly_plot = self._create_poly_plot()
        rbf_plot = self._create_rbf_plot()
        
        plots = VGroup(linear_plot, poly_plot, rbf_plot).arrange(RIGHT, buff=0.5)
        plots.next_to(kernels, DOWN, buff=0.5)
        
        self.play(Create(linear_plot))
        self.wait(0.5)
        self.play(Create(poly_plot))
        self.wait(0.5)
        self.play(Create(rbf_plot))
        
        self.wait(2)
    
    def scene_choose_kernel(self):
        # Title
        title = Text("Choosing the Right Kernel", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Decision chart
        decision_chart = VGroup(
            Text("Decision Chart", font_size=36, color=YELLOW),
            Text("Linear → Linearly separable data", font_size=24, color=WHITE, t2c={"Linear": GREEN}),
            Text("Polynomial → Feature interactions", font_size=24, color=WHITE, t2c={"Polynomial": ORANGE}),
            Text("RBF → Complex, non-linear data", font_size=24, color=WHITE, t2c={"RBF": BLUE}),
            Text("Default: Try RBF first, then others", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(title, DOWN, buff=1)
        
        self.play(Write(decision_chart[0]))
        self.wait(0.5)
        
        for item in decision_chart[1:]:
            self.play(Write(item))
            self.wait(0.3)
        
        self.wait(1)
        
        # Add tips
        tips = Text(
            "Tips:\n• Start with default parameters\n• Use cross-validation\n• Scale your features",
            font_size=24,
            color=GREEN
        ).next_to(decision_chart, DOWN, buff=1)
        
        self.play(Write(tips))
        self.wait(2)
    
    def scene_conclusion(self):
        # Title
        title = Text("Recap & Conclusion", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Key points
        points = VGroup(
            Text("• SVM finds the optimal separating hyperplane", color=YELLOW),
            Text("• Maximizes margin between classes", color=YELLOW),
            Text("• Uses support vectors (critical points)", color=YELLOW),
            Text("• Can handle non-linear data with kernels", color=YELLOW),
            Text("• Robust to overfitting with proper C", color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).scale(0.9).next_to(title, DOWN, buff=1)
        
        # Add points one by one
        for point in points:
            self.play(Write(point), run_time=0.7)
        
        self.wait(1)
        
        # Final message
        final_message = Text(
            "SVM is powerful because it focuses only on the critical data points — the support vectors!",
            font_size=28,
            color=GREEN,
            t2c={"support vectors": YELLOW}
        ).next_to(points, DOWN, buff=1)
        
        self.play(Write(final_message))
        self.wait(3)
    
    # Helper methods
    def _create_linear_example(self):
        # Create a simple linear separation example
        axes = Axes(x_range=[-2, 2], y_range=[-2, 2], axis_config={"color": WHITE}, tips=False)
        line = Line(start=[-2, -2, 0], end=[2, 2, 0], color=GREEN)
        return VGroup(axes, line)
    
    def _create_nonlinear_example(self):
        # Create a simple non-linear (circular) separation example
        axes = Axes(x_range=[-2, 2], y_range=[-2, 2], axis_config={"color": WHITE}, tips=False)
        circle = Circle(radius=1.5, color=ORANGE)
        return VGroup(axes, circle)
    
    def _create_kernel_card(self, name, formula):
        return VGroup(
            Text(name, font_size=28, color=YELLOW),
            MathTex(formula, font_size=24, color=WHITE)
        ).arrange(DOWN, buff=0.3)
    
    def _create_linear_plot(self):
        axes = Axes(x_range=[-2, 2], y_range=[-2, 2], axis_config={"color": WHITE}, tips=False)
        line = Line(start=[-2, -2, 0], end=[2, 2, 0], color=GREEN)
        return VGroup(axes, line)
    
    def _create_poly_plot(self):
        axes = Axes(x_range=[-2, 2], y_range=[-2, 2], axis_config={"color": WHITE}, tips=False)
        # Simple curve for polynomial kernel
        curve = ParametricFunction(
            lambda t: np.array([t, 0.5 * t**2 - 1, 0]),
            t_range=[-2, 2],
            color=ORANGE
        )
        return VGroup(axes, curve)
    
    def _create_rbf_plot(self):
        axes = Axes(x_range=[-2, 2], y_range=[-2, 2], axis_config={"color": WHITE}, tips=False)
        # Circle for RBF kernel
        circle = Circle(radius=1.2, color=BLUE)
        return VGroup(axes, circle)
