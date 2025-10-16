from manim import *
import numpy as np

class DimensionalityReductionTutorial(ThreeDScene):
    def construct(self):
        # Part 1: Introduction (2 scenes)
        self.scene1_intro()
        self.clear()
        self.scene1a_intro_graph()
        self.clear()
        
        # Part 2: PCA Math (2 scenes)
        self.scene2_pca_math_part1()
        self.clear()
        self.scene2_pca_math_part2()
        self.clear()
        
        # Part 3: Visualization (1 scene)
        self.scene3_visualization()
        self.clear()
        
        # Part 4: Best Practices (1 scene)
        self.scene4_best_practices()
    
    def scene1_intro(self):
        # Title
        title = Text("Dimensionality Reduction", font_size=48, color=BLUE)
        subtitle = Text("Simplifying Complex Data", font_size=32, color=YELLOW)
        subtitle.next_to(title, DOWN)
        
        # Introduction text
        intro_text = Text("A technique to reduce the number of features in a dataset\nwhile preserving as much information as possible", 
                         font_size=28, line_spacing=1.5)
        intro_text.next_to(subtitle, DOWN, buff=1)
        
        # Show title and introduction
        self.play(Write(title), Write(subtitle))
        self.wait(0.5)
        self.play(Write(intro_text))
        self.wait(2)
        
        # Transition to next scene
        self.play(
            FadeOut(title, shift=UP),
            FadeOut(subtitle, shift=UP),
            FadeOut(intro_text, shift=UP)
        )
        
    def scene1a_intro_graph(self):
        # Create a more spread out 3D point cloud
        np.random.seed(42)
        n_points = 100
        
        # Create points in a 3D plane with some noise
        t = np.linspace(-2, 2, n_points)
        x = t + np.random.normal(0, 0.1, n_points)
        y = 0.5 * t + np.random.normal(0, 0.1, n_points)
        z = 0.3 * t + np.random.normal(0, 0.05, n_points)
        
        # Create 3D axes with proper aspect ratio
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            z_range=[-1.5, 1.5, 0.5],
            axis_config={"color": WHITE, "include_ticks": False},
        )
        
        # Create 3D point cloud with depth shading
        cloud_3d = VGroup(*[
            Dot3D(
                point=[x[i], y[i], z[i]],
                color=interpolate_color(BLUE_E, BLUE_A, (z[i] + 1.5)/3),
                radius=0.04,
                resolution=8
            )
            for i in range(n_points)
        ])
        
        # Create 2D projection (onto xy-plane)
        cloud_2d = VGroup(*[
            Dot(
                point=[x[i], y[i], 0],
                color=GREEN,
                radius=0.04
            )
            for i in range(n_points)
        ])
        
        # Add explanation text
        explanation = Text("3D Data with Clear Dimensional Structure", font_size=28)
        explanation.to_edge(UP)
        
        # Set initial camera orientation
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)
        
        # Show 3D data
        self.play(Write(explanation))
        self.play(
            Create(axes),
            LaggedStart(*[GrowFromCenter(dot) for dot in cloud_3d], lag_ratio=0.01),
            run_time=2
        )
        
        # Rotate camera to show 3D structure
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(2)
        self.stop_ambient_camera_rotation()
        
        # Show projection plane
        plane = Rectangle(
            width=6, height=4, color=GREEN, fill_opacity=0.1, stroke_width=1
        ).set_fill(GREEN, 0.1)
        
        # Update explanation text
        new_explanation = Text("Projecting 3D data onto 2D plane", font_size=28)
        new_explanation.to_edge(UP)
        
        self.play(
            FadeIn(plane),
            Transform(explanation, new_explanation)
        )
        
        # Animate projection to 2D
        self.play(
            Transform(cloud_3d, cloud_2d),
            FadeOut(plane),
            run_time=2
        )
        
        # Show final 2D view from top
        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=1.5)
        
        # Add final explanation
        final_text = Text("PCA finds the optimal 2D view that preserves maximum variance", 
                         font_size=24)
        final_text.next_to(cloud_2d, DOWN, buff=0.5)
        self.play(Write(final_text))
        self.wait(2)
    
    def scene2_pca_math_part1(self):
        title = Text("PCA: The Math Behind It (1/2)", font_size=42, color=BLUE)
        title.to_edge(UP)
        
        # Step 1: Center the data
        step1 = Text("1. Center the data:", font_size=32, color=YELLOW, weight=BOLD)
        step1.shift(UP * 0.5)
        formula1 = MathTex(r"X_{\text{centered}} = X - \bar{X}", font_size=36)
        formula1.next_to(step1, DOWN, buff=0.5)
        
        # Step 2: Covariance matrix
        step2 = Text("2. Calculate Covariance Matrix", font_size=32, color=YELLOW, weight=BOLD)
        step2.next_to(formula1, DOWN, buff=1)
        
        cov_formula1 = MathTex("\\text{Cov}(X) = \\frac{1}{n} X^T X", font_size=36)
        cov_formula1.next_to(step2, DOWN, buff=0.5)
        
        cov_formula2 = MathTex(r"\Sigma = \frac{1}{n-1} X^T X", font_size=36)
        cov_formula2.next_to(cov_formula1, DOWN, buff=0.3)
        
        # Show title and step 1
        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(step1))
        self.play(Write(formula1))
        self.wait(1)
        
        # Show step 2
        self.play(Write(step2))
        self.wait(0.5)
        self.play(Write(cov_formula1))
        self.wait(0.5)
        self.play(Write(cov_formula2))
        self.wait(2)
        
    def scene2_pca_math_part2(self):
        title = Text("PCA: The Math Behind It (2/2)", font_size=42, color=BLUE)
        title.to_edge(UP)
        
        # Step 3: Eigen decomposition
        step3 = Text("3. Find Eigenvectors & Eigenvalues", font_size=32, color=YELLOW, weight=BOLD)
        step3.shift(UP * 0.5)
        
        eigen_formula1 = MathTex("\\text{Cov}(X) \\cdot v = \\lambda \\cdot v", font_size=36)
        eigen_formula1.next_to(step3, DOWN, buff=0.5)
        
        eigen_formula2 = MathTex(r"\Sigma v_i = \lambda_i v_i", font_size=36)
        eigen_formula2.next_to(eigen_formula1, DOWN, buff=0.3)
        
        # Step 4: Project data
        step4 = Text("4. Project Data onto Principal Components", font_size=32, color=YELLOW, weight=BOLD)
        step4.next_to(eigen_formula2, DOWN, buff=1)
        
        proj_formula1 = MathTex("X_{\\text{new}} = X \\cdot W_k", font_size=36)
        proj_formula1.next_to(step4, DOWN, buff=0.5)
        
        proj_formula2 = MathTex(r"Z = X W_k^T", font_size=36)
        proj_formula2.next_to(proj_formula1, DOWN, buff=0.3)
        
        # Show title and step 3
        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(step3))
        self.play(Write(eigen_formula1))
        self.wait(0.5)
        self.play(Write(eigen_formula2))
        self.wait(1)
        
        # Show step 4
        self.play(Write(step4))
        self.wait(0.5)
        self.play(Write(proj_formula1))
        self.wait(0.5)
        self.play(Write(proj_formula2))
        self.wait(2)
    
    def scene3_visualization(self):
        title = Text("PCA Visualization", font_size=42, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create sample 2D data
        np.random.seed(42)
        x = np.random.normal(0, 1, 100)
        y = 0.7 * x + np.random.normal(0, 0.3, 100)
        
        # Create axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": WHITE},
            tips=False
        )
        
        # Plot data points
        data_centered = np.column_stack((x, y))
        dots = VGroup(*[
            Dot(point=[x, y, 0], color=BLUE, radius=0.06)
            for x, y in data_centered
        ])
        
        # Center the data
        x_mean, y_mean = np.mean(x), np.mean(y)
        x_centered = x - x_mean
        y_centered = y - y_mean
        
        # Calculate covariance matrix
        X = np.vstack((x_centered, y_centered))
        cov_matrix = np.cov(X)
        
        # Get eigenvectors and eigenvalues
        eig_vals, eig_vecs = np.linalg.eig(cov_matrix)
        
        # Sort by eigenvalue
        idx = eig_vals.argsort()[::-1]
        eig_vals = eig_vals[idx]
        eig_vecs = eig_vecs[:, idx]
        
        # Create PC vectors (scaled by sqrt of eigenvalue)
        pc1_start = np.array([0, 0, 0])
        pc1_end = np.array([*eig_vecs[:, 0], 0]) * np.sqrt(eig_vals[0]) * 2
        pc1 = Arrow(
            start=pc1_start,
            end=pc1_end,
            color=RED,
        )
        
        pc2_start = np.array([0, 0, 0])
        pc2_end = np.array([*eig_vecs[:, 1], 0]) * np.sqrt(eig_vals[1]) * 2
        pc2 = Arrow(
            start=pc2_start,
            end=pc2_end,
            color=GREEN,
        )
        
        # Show data and principal components
        self.play(
            FadeOut(title, shift=UP),
            Create(axes), 
            Create(dots), 
            run_time=1.5
        )
        self.wait(0.5)
        
        # Show mean
        mean_point = Dot(ORIGIN, color=YELLOW, radius=0.08)
        self.play(FadeIn(mean_point))
        self.wait(0.5)
        
        # Show principal components
        self.play(Create(pc1), Create(pc2))
        pc1_label = Text("PC1", font_size=24, color=RED).next_to(pc1.get_end(), RIGHT)
        pc2_label = Text("PC2", font_size=24, color=GREEN).next_to(pc2.get_end(), UP)
        self.play(Write(pc1_label), Write(pc2_label))
        self.wait(2)
        
        # Show projection onto PC1
        projected_points = VGroup(*[
            Dot([x_centered[i] * eig_vecs[0, 0], x_centered[i] * eig_vecs[1, 0], 0], 
                color=RED, radius=0.05, fill_opacity=0.5)
            for i in range(100)
        ])
        
        projection_lines = VGroup(*[
            DashedLine(
                dots[i].get_center(),
                projected_points[i].get_center(),
                color=YELLOW,
                stroke_width=1
            )
            for i in range(20)  # Only show some lines for clarity
        ])
        
        self.play(
            *[Create(line) for line in projection_lines],
            *[Create(point) for point in projected_points],
            run_time=2
        )
        
        # Add explanation
        explanation = Text("Projection onto first principal component", font_size=24, color=YELLOW)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)
    
    def scene4_best_practices(self):
        title = Text("PCA Best Practices", font_size=36, color=BLUE)
        title.to_edge(UP)
        
        # Create a list of best practices
        practices = VGroup(
            Text("1. Standardize your data", font_size=28, color=YELLOW, weight=BOLD),
            Text("• PCA is sensitive to feature scales", font_size=24, color=WHITE),
            
            Text("2. Choose components wisely", font_size=28, color=YELLOW, weight=BOLD),
            Text("• Use explained variance ratio", font_size=24, color=WHITE),
            Text("• Aim for 70-95% variance explained", font_size=24, color=WHITE),
            
            Text("3. Interpretability", font_size=28, color=YELLOW, weight=BOLD),
            Text("• Components are linear combinations of features", font_size=24, color=WHITE),
            Text("• May be harder to interpret than original features", font_size=24, color=WHITE),
            
            Text("4. When to use PCA", font_size=28, color=YELLOW, weight=BOLD),
            Text("• For dimensionality reduction before other ML models", font_size=24, color=WHITE),
            Text("• For visualization of high-dimensional data", font_size=24, color=WHITE),
            Text("• When features are highly correlated", font_size=24, color=WHITE)
        )
        
        # Arrange practices in a column
        practices.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        practices.next_to(title, DOWN, buff=0.5)
        practices.to_edge(LEFT, buff=1)
        
        # Show title and practices with animation
        self.play(Write(title))
        self.wait(0.5)
        
        # Animate practices in groups
        self.play(Write(practices[0:2]))
        self.wait(0.5)
        
        self.play(Write(practices[2:5]))
        self.wait(0.5)
        
        self.play(Write(practices[5:8]))
        self.wait(0.5)
        
        self.play(Write(practices[8:]))
        self.wait(2)
        self.wait(0.5)
        self.play(Write(practices[7:]))
        self.wait(2)
        
        # Final message
        final_msg = Text("Thank you for learning about PCA!", font_size=36, color=YELLOW)
        self.play(ReplacementTransform(VGroup(title, practices), final_msg))
        self.wait(2)

# Run with: manim -pql dimensionality_reduction_tutorial.py DimensionalityReductionTutorial
