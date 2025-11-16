from manim import *
import numpy as np

class SVMTutorialClean(Scene):
    def construct(self):
        # Scene 1: Introduction to SVM
        self.scene_intro()
        self.clear()
        
        # Scene 2: Types of SVM
        self.scene_types()
        self.clear()
        
        # Scene 3: How SVM Works
        self.scene_how_it_works()
        self.clear()
        
        # Scene 4: Math Behind SVM
        self.scene_math()
        self.clear()
        
        # Scene 5: Soft Margin SVM
        self.scene_soft_margin()
        self.clear()
        
        # Scene 6: Kernels
        self.scene_kernels()
        self.clear()
        
        # Scene 7: Choosing the Right Kernel
        self.scene_choose_kernel()
    
    def scene_intro(self):
        # Title
        title = Text("Support Vector Machines (SVM)", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Definition
        definition = VGroup(
            Text("A supervised learning algorithm for", font_size=32, color=WHITE),
            Text("classification and regression problems", font_size=32, color=WHITE)
        ).arrange(DOWN, buff=0.3).next_to(title, DOWN, buff=1)
        
        self.play(Write(definition))
        self.wait(1)
        
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
        
        # Add separating line
        line = Line(start=[-3, -3, 0], end=[3, 3, 0], color=YELLOW)
        self.play(Create(line), run_time=1)
        
        # Add labels
        label1 = Text("Class 1", color=BLUE).next_to(dots1[0], UP)
        label2 = Text("Class -1", color=RED).next_to(dots2[0], DOWN)
        self.play(Write(label1), Write(label2))
        
        self.wait(2)
    
    def scene_types(self):
        # Title
        title = Text("Types of SVM", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Linear SVM
        linear = VGroup(
            Text("Linear SVM", font_size=36, color=GREEN),
            Text("• Separates data with a straight line", font_size=28, color=WHITE),
            Text("• Works for linearly separable data", font_size=28, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(LEFT, buff=1)
        
        # Non-linear SVM
        non_linear = VGroup(
            Text("Non-linear SVM", font_size=36, color=ORANGE),
            Text("• Uses kernel trick for complex data", font_size=28, color=WHITE),
            Text("• Can handle non-linear boundaries", font_size=28, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(RIGHT, buff=1)
        
        self.play(Write(linear))
        self.wait(0.5)
        self.play(Write(non_linear))
        self.wait(1)
        
        # Add example visualizations below
        linear_plot = self._create_linear_plot()
        non_linear_plot = self._create_nonlinear_plot()
        
        self.play(
            linear.animate.shift(UP * 1.5).scale(0.8).to_edge(LEFT, buff=1),
            non_linear.animate.shift(UP * 1.5).scale(0.8).to_edge(RIGHT, buff=1)
        )
        
        linear_plot.next_to(linear, DOWN, buff=0.5)
        non_linear_plot.next_to(non_linear, DOWN, buff=0.5)
        
        self.play(Create(linear_plot), Create(non_linear_plot))
        self.wait(2)
    
    def scene_how_it_works(self):
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
        
        # Add hyperplane
        hyperplane = Line(start=[-3, -3, 0], end=[3, 3, 0], color=YELLOW)
        self.play(Create(hyperplane), run_time=1)
        
        # Add margins
        margin = 1.0
        margin1 = hyperplane.copy().shift(UP * margin / np.sqrt(2))
        margin2 = hyperplane.copy().shift(DOWN * margin / np.sqrt(2))
        margin1.set_color(GREEN)
        margin2.set_color(GREEN)
        
        self.play(Create(margin1), Create(margin2), run_time=1)
        
        # Highlight support vectors
        support_vectors = VGroup(dots1[3], dots2[2])
        self.play(
            *[dot.animate.set_color(YELLOW).scale(1.5) for dot in support_vectors],
            run_time=1.5
        )
        
        # Add labels
        sv_label = Text("Support Vectors", color=YELLOW).to_edge(DOWN)
        self.play(Write(sv_label))
        
        self.wait(2)
    
    def scene_math(self):
        # Title
        title = Text("Math Behind SVM", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Hyperplane equation
        hyperplane = MathTex(
            r"w \cdot x + b = 0",
            font_size=48,
            color=YELLOW
        ).shift(UP * 2)
        
        # Margin formula
        margin = MathTex(
            r"\text{Margin} = \frac{2}{\|w\|}",
            font_size=48,
            color=GREEN
        ).next_to(hyperplane, DOWN, buff=1)
        
        # Optimization problem
        optimization = VGroup(
            MathTex(r"\min_{w,b} \frac{1}{2} \|w\|^2", font_size=36, color=ORANGE),
            MathTex(r"\text{s.t. } y_i(w \cdot x_i + b) \geq 1, \forall i", font_size=36, color=ORANGE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(margin, DOWN, buff=1)
        
        self.play(Write(hyperplane))
        self.wait(1)
        self.play(Write(margin))
        self.wait(1)
        self.play(Write(optimization))
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
        
        # Add hyperplane with slack variables
        hyperplane = Line(start=[-3, -3, 0], end=[3, 3, 0], color=YELLOW)
        self.play(Create(hyperplane), run_time=1)
        
        # Add slack variables explanation
        slack_eq = VGroup(
            MathTex(r"\min_{w,b,\xi} \frac{1}{2} \|w\|^2 + C\sum_{i=1}^n \xi_i", font_size=32, color=GREEN),
            MathTex(r"\text{s.t. } y_i(w \cdot x_i + b) \geq 1 - \xi_i", font_size=32, color=GREEN),
            MathTex(r"\xi_i \geq 0", font_size=32, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(RIGHT, buff=1)
        
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
            self._create_kernel_card("RBF", r"K(x_i, x_j) = \exp\left(-\frac{\|x_i - x_j\|^2}{2\sigma^2}\right)")
        ).arrange(RIGHT, buff=0.5).scale(0.9).next_to(title, DOWN, buff=1)
        
        # Add to scene
        self.play(LaggedStart(
            *[FadeIn(kernel, shift=UP) for kernel in kernels],
            lag_ratio=0.3
        ))
        
        # Show example plots
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
            Text("• Linear → Linearly separable data", font_size=28, color=GREEN),
            Text("• Polynomial → Feature interactions", font_size=28, color=ORANGE),
            Text("• RBF → Complex, non-linear data", font_size=28, color=BLUE),
            Text("• Default: Try RBF first, then others", font_size=28, color=YELLOW)
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
        self.wait(3)
    
    def _create_linear_plot(self):
        axes = Axes(x_range=[-2, 2], y_range=[-2, 2], axis_config={"color": WHITE}, tips=False)
        line = Line(start=[-2, -2, 0], end=[2, 2, 0], color=GREEN)
        return VGroup(axes, line)
    
    def _create_nonlinear_plot(self):
        axes = Axes(x_range=[-2, 2], y_range=[-2, 2], axis_config={"color": WHITE}, tips=False)
        circle = Circle(radius=1.5, color=ORANGE)
        return VGroup(axes, circle)
    
    def _create_kernel_card(self, name, formula):
        return VGroup(
            Text(name, font_size=28, color=YELLOW),
            MathTex(formula, font_size=24, color=WHITE)
        ).arrange(DOWN, buff=0.3)
    
    def _create_poly_plot(self):
        axes = Axes(x_range=[-2, 2], y_range=[-2, 2], axis_config={"color": WHITE}, tips=False)
        curve = ParametricFunction(
            lambda t: np.array([t, 0.5 * t**2 - 1, 0]),
            t_range=[-2, 2],
            color=ORANGE
        )
        return VGroup(axes, curve)
    
    def _create_rbf_plot(self):
        axes = Axes(x_range=[-2, 2], y_range=[-2, 2], axis_config={"color": WHITE}, tips=False)
        circle = Circle(radius=1.2, color=BLUE)
        return VGroup(axes, circle)
