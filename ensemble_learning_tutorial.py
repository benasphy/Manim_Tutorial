from manim import *
import numpy as np
from manim.mobject.geometry.tips import ArrowTriangleFilledTip

class EnsembleLearningTutorial(Scene):
    def create_point_with_icon(self, icon, text, color=WHITE):
        return VGroup(
            Text(icon, font_size=28).set_color(color),
            Text(text, font_size=24).next_to(Text(icon), RIGHT, buff=0.3)
        )
        
    def create_step(self, num, text, color):
        return VGroup(
            Circle(radius=0.3, color=color, fill_opacity=0.2).scale(0.7),
            Text(num, font_size=20, color=color).scale(0.7),
            Text(text, font_size=24).next_to(Circle(radius=0.3), RIGHT, buff=0.3)
        )
        
    def create_dataset(self, n_points, color=BLUE):
        points = VGroup(*[Dot(radius=0.05, color=color) for _ in range(n_points)])
        points.arrange_in_grid(rows=5, cols=4, buff=0.3)
        box = SurroundingRectangle(points, buff=0.3, color=WHITE)
        return VGroup(points, box)
        
    def create_bootstrap_sample(self, dataset, color):
        points = dataset[0].copy()
        for p in points:
            p.set_color(color)
        box = SurroundingRectangle(points, buff=0.3, color=color)
        return VGroup(points, box)
        
    def create_decision_tree(self, depth=3):
        # Simple tree visualization
        root = Circle(radius=0.2, color=GREEN, fill_opacity=0.2)
        tree = VGroup(root)
        
        for i in range(1, depth):
            level = VGroup()
            for j in range(2**i):
                node = Circle(radius=0.15, color=GREEN, fill_opacity=0.2)
                node.shift(DOWN * i * 0.7 + RIGHT * (j - (2**i-1)/2) * 1.5)
                level.add(node)
            tree.add(level)
        
        return tree
    def construct(self):
        # Scene 1: Introduction
        self.scene1_intro()
        self.clear()
        
        # Scene 2: What is Ensemble Learning?
        self.scene2_what_is_ensemble()
        self.clear()
        
        # Scene 3: Bagging
        self.scene3a_bagging_concept()
        self.clear()
        self.scene3b_bagging_visual()
        self.clear()
        
        # Scene 4: Boosting
        self.scene4a_boosting_concept()
        self.clear()
        self.scene4b_student_analogy()
        self.clear()
        self.scene4c_boosting_math()
        self.clear()
        self.scene4d_boosting_visual()
        self.clear()
        
        # Scene 5: Stacking
        self.scene5a_stacking_concept()
        self.clear()
        self.scene5b_sports_analogy()
        self.clear()
        self.scene5c_stacking_visual()
        self.clear()
        
        # Scene 6: Comparison
        self.scene6_comparison()
        self.clear()
        
        # Scene 7: Outro
        self.scene7_outro()
    
    def scene1_intro(self):
        # Title and hook
        title = Text("Ensemble Learning", font_size=60, color=BLUE)
        subtitle = Text("Bagging, Boosting & Stacking Explained", font_size=32, color=YELLOW)
        subtitle.next_to(title, DOWN)
        
        # Key concept
        concept = VGroup(
            Text("Combining multiple models", font_size=36, color=GREEN),
            Text("to make better predictions", font_size=36, color=GREEN).next_to(Text("Combining multiple models"), DOWN, buff=0.3)
        ).next_to(subtitle, DOWN, buff=1)
        
        # Visual representation
        models = VGroup(
            *[Circle(radius=0.5, color=c, fill_opacity=0.2) 
              for c in [BLUE, GREEN, YELLOW, RED]]
        ).arrange(RIGHT, buff=0.5).next_to(concept, DOWN, buff=1)
        
        combined = Circle(radius=0.7, color=WHITE, fill_opacity=0.2).next_to(models, DOWN, buff=1)
        combined_label = Text("Combined Prediction", font_size=24).next_to(combined, DOWN, buff=0.3)
        
        # Connect models to combined prediction
        connections = VGroup(*[
            Line(
                model.get_bottom(),
                combined.get_top(),
                buff=0.1,
                stroke_width=2
            ) for model in models
        ])
        
        # Animate
        self.play(Write(title), Write(subtitle))
        self.wait(0.5)
        self.play(Write(concept))
        self.wait(1)
        
        # Show individual models
        for model in models:
            self.play(FadeIn(model, shift=UP*0.3))
            self.wait(0.2)
        
        # Show combination
        self.play(
            Create(connections, lag_ratio=0.2),
            run_time=1.5
        )
        self.play(
            FadeIn(combined, shift=UP*0.5),
            Write(combined_label)
        )
        self.wait(1)
        
        # Transition to next scene
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(concept),
            FadeOut(models),
            FadeOut(connections),
            FadeOut(combined),
            FadeOut(combined_label)
        )
    
    def scene2_what_is_ensemble(self):
        # Title
        title = Text("What is Ensemble Learning?", font_size=48, color=BLUE)
        title.to_edge(UP)
        
        # Definition
        definition = Text(
            "Combining multiple models to improve predictions",
            font_size=32
        )
        definition.next_to(title, DOWN, buff=1)
        
        # Key points
        key_points = VGroup(
            Text("• Reduces overfitting (variance)", font_size=28, color=GREEN),
            Text("• Reduces bias", font_size=28, color=GREEN),
            Text("• Improves generalization", font_size=28, color=GREEN)
        )
        key_points.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        key_points.next_to(definition, DOWN, buff=1)
        
        # Real-world examples
        examples = VGroup(
            Text("Real-world Examples:", font_size=28, color=YELLOW),
            Text("• Weather forecasting models", font_size=24),
            Text("• Medical diagnosis systems", font_size=24),
            Text("• Search engine rankings", font_size=24)
        )
        examples.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        examples.next_to(key_points, DOWN, buff=1)
        
        # Animate
        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(definition))
        self.wait(1)
        
        # Animate key points
        for point in key_points:
            self.play(Write(point))
            self.wait(0.3)
        
        # Show examples
        self.play(Write(examples[0]))
        self.wait(0.5)
        for example in examples[1:]:
            self.play(Write(example))
            self.wait(0.2)
        
        self.wait(2)
    
    def scene3a_bagging_concept(self):
        # Title
        title = Text("1. Bagging (Bootstrap Aggregating)", font_size=42, color=BLUE)
        title.to_edge(UP)
        
        # Definition with visual
        definition = VGroup(
            Text("Training multiple models in parallel on", font_size=28),
            Text("different bootstrap samples of the data", font_size=28)
        ).arrange(DOWN, center=False, aligned_edge=LEFT)
        definition.next_to(title, DOWN, buff=0.7)
        
        # Key concept: Bootstrap sampling
        bootstrap_title = Text("Bootstrap Sampling:", font_size=26, color=YELLOW).to_edge(LEFT, buff=1)
        bootstrap_points = VGroup(
            Text("• Random sampling with replacement", font_size=24),
            Text("• Creates multiple training sets", font_size=24),
            Text("• Each set has ~63.2% unique examples", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(bootstrap_title, DOWN, aligned_edge=LEFT, buff=0.5)
        
        # Visual example of bootstrap samples
        dataset = self.create_dataset(9, color=BLUE)
        dataset.scale(0.8).to_edge(RIGHT, buff=1).shift(UP*0.5)
        
        sample1 = self.create_bootstrap_sample(dataset, color=GREEN).scale(0.8).next_to(dataset, DOWN, buff=0.5)
        sample2 = self.create_bootstrap_sample(dataset, color=YELLOW).scale(0.8).next_to(sample1, DOWN, buff=0.5)
        
        # Show title and definition
        self.play(Write(title))
        self.play(Write(definition))
        self.wait(1)
        
        # Show bootstrap explanation
        self.play(Write(bootstrap_title))
        for point in bootstrap_points:
            self.play(Write(point), run_time=0.7)
            self.wait(0.2)
        
        # Show dataset and samples
        self.play(FadeIn(dataset))
        self.wait(0.5)
        
        # Animate sampling
        self.play(
            Transform(dataset.copy(), sample1, path_arc=PI/2),
            run_time=1.5
        )
        self.wait(0.5)
        
        self.play(
            Transform(dataset.copy(), sample2, path_arc=PI/2),
            run_time=1.5
        )
        self.wait(1)
        
        # Show how models are trained
        models_title = Text("Training Multiple Models:", font_size=26, color=YELLOW).next_to(bootstrap_points, DOWN, buff=1, aligned_edge=LEFT)
        models_points = VGroup(
            Text("• One model per bootstrap sample", font_size=24),
            Text("• Models trained independently", font_size=24),
            Text("• Can be parallelized", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(models_title, DOWN, aligned_edge=LEFT, buff=0.5)
        
        self.play(Write(models_title))
        for point in models_points:
            self.play(Write(point), run_time=0.7)
            self.wait(0.2)
        
        # Show model predictions
        prediction_title = Text("Combining Predictions:", font_size=26, color=YELLOW).next_to(models_points, DOWN, buff=1, aligned_edge=LEFT)
        prediction_points = VGroup(
            Text("• Classification: Majority voting", font_size=24),
            Text("• Regression: Average prediction", font_size=24),
            Text("• Reduces variance, prevents overfitting", font_size=24, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(prediction_title, DOWN, aligned_edge=LEFT, buff=0.5)
        
        self.play(Write(prediction_title))
        for point in prediction_points:
            self.play(Write(point), run_time=0.7)
            self.wait(0.2)
        
        self.wait(2)
        
    def scene3b_bagging_visual(self):
        # Title
        title = Text("Random Forest: A Bagging Example", font_size=42, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create dataset
        dataset = self.create_dataset(20)
        dataset.scale(0.8).to_edge(LEFT, buff=1)
        
        # Create 3 bootstrap samples
        samples = VGroup(*[self.create_bootstrap_sample(dataset, color=c).scale(0.8) 
                         for c in [GREEN, YELLOW, BLUE]])
        samples.arrange(RIGHT, buff=0.5).next_to(title, DOWN, buff=1)
        
        # Create decision trees
        trees = VGroup(*[self.create_decision_tree(depth=3).scale(0.7) for _ in range(3)])
        for tree, sample in zip(trees, samples):
            tree.next_to(sample, DOWN, buff=0.5)
        
        # Show dataset and sampling
        self.play(FadeIn(dataset))
        self.wait(0.5)
        
        # Animate sampling and model training
        for sample, tree in zip(samples, trees):
            # Show sampling
            self.play(
                Transform(dataset.copy(), sample),
                run_time=1
            )
            # Show model training
            self.play(
                FadeIn(tree, shift=UP*0.3),
                run_time=1
            )
            self.wait(0.3)
        
        # Show final prediction
        final_pred = Text("Final Prediction", font_size=28, color=YELLOW)
        final_pred.next_to(trees, DOWN, buff=1)
        
        # Create voting arrows
        vote_arrows = VGroup()
        for tree in trees:
            arrow = Arrow(
                tree.get_bottom(),
                final_pred.get_top(),
                buff=0.2,
                stroke_width=2,
                color=WHITE
            )
            vote_arrows.add(arrow)
        
        # Show voting
        self.play(
            Create(vote_arrows, lag_ratio=0.3),
            FadeIn(final_pred, shift=UP*0.5),
            run_time=2
        )
        
        # Add key points
        key_points = VGroup(
            Text("• Each tree sees different data", font_size=24),
            Text("• Decorrelates the trees", font_size=24),
            Text("• Final prediction by majority vote", font_size=24, color=GREEN)
        )
        key_points.arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT, buff=1)
        
        self.play(Write(key_points), run_time=2)
        self.wait(2)
    
    def scene4b_student_analogy(self):
        # Title
        title = Text("📚 Student Learning Analogy", font_size=42, color=BLUE)
        title.to_edge(UP)
        
        # Student learning process
        steps = VGroup(
            Text("1. Takes practice test", font_size=28, color=YELLOW),
            Text("2. Reviews mistakes", font_size=28, color=RED),
            Text("3. Focuses on weak areas", font_size=28, color=BLUE),
            Text("4. Improves for next test", font_size=28, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).to_edge(LEFT, buff=2)
        
        # Visual elements
        student = Text("👨‍🎓", font_size=100).to_edge(RIGHT, buff=2)
        
        # Show title and steps
        self.play(Write(title))
        self.wait(0.5)
        
        for step in steps:
            self.play(FadeIn(step, shift=RIGHT*0.5))
            self.wait(0.5)
        
        # Add student icon
        self.play(FadeIn(student, shift=LEFT*0.5))
        
        # Key takeaway
        takeaway = Text("Just like students learn from their mistakes,\nboosted models focus on hard examples",
                      font_size=28, color=YELLOW).next_to(steps, DOWN, buff=1)
        
        self.play(Write(takeaway))
        self.wait(2)
        
    def scene4a_boosting_concept(self):
        # Title
        title = Text("2. Boosting: Learning from Mistakes", font_size=42, color=BLUE)
        title.to_edge(UP)
        
        # Core concept
        concept = VGroup(
            Text("Sequentially train models where each new model", font_size=28),
            Text("focuses on the mistakes of previous models", font_size=28)
        ).arrange(DOWN, center=False, aligned_edge=LEFT)
        concept.next_to(title, DOWN, buff=0.7)
        
        # Key components
        components_title = Text("Key Components:", font_size=26, color=YELLOW).to_edge(LEFT, buff=1)
        components = VGroup(
            Text("1. Weak Learners (slightly better than random)", font_size=24),
            Text("2. Sequential Training (one after another)", font_size=24),
            Text("3. Error Weighting (focus on hard examples)", font_size=24),
            Text("4. Weighted Voting (stronger models have more say)", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(components_title, DOWN, aligned_edge=LEFT, buff=0.5)
        
        # Visual: Sequential learning
        models = VGroup(*[Circle(radius=0.4, color=c, fill_opacity=0.2) 
                         for c in [BLUE, GREEN, YELLOW, RED]])
        models.arrange(RIGHT, buff=0.5).to_edge(RIGHT, buff=1).shift(UP*0.5)
        
        arrows = VGroup()
        for i in range(3):
            arrow = Arrow(
                models[i].get_right(),
                models[i+1].get_left(),
                buff=0.1,
                stroke_width=2,
                color=WHITE
            )
            arrows.add(arrow)
        
        # Student analogy
        analogy_title = Text("📚 Student Analogy:", font_size=26, color=YELLOW).to_edge(LEFT, buff=1)
        analogy = VGroup(
            Text("• Student takes practice tests", font_size=22),
            Text("• Studies mistakes from previous tests", font_size=22),
            Text("• Focuses more on difficult problems", font_size=22),
            Text("• Gradually improves performance", font_size=22, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(analogy_title, DOWN, aligned_edge=LEFT, buff=0.5)
        
        # Show title and concept
        self.play(Write(title))
        self.play(Write(concept))
        self.wait(1)
        
        # Show key components
        self.play(Write(components_title))
        for comp in components:
            self.play(Write(comp), run_time=0.7)
            self.wait(0.1)
        
        # Show sequential models
        self.play(
            FadeIn(models[0], shift=UP*0.5),
            run_time=0.7
        )
        
        for i in range(3):
            self.play(
                FadeIn(models[i+1], shift=UP*0.5),
                Create(arrows[i]),
                run_time=0.7
            )
            self.wait(0.2)
        
        # Show student analogy
        self.play(
            FadeIn(analogy_title, shift=UP*0.5),
            FadeIn(analogy, shift=UP*0.5),
            run_time=1
        )
        
        # Math intuition
        math_title = Text("Mathematical Intuition:", font_size=26, color=YELLOW).to_edge(LEFT, buff=1)
        math_eq = MathTex(
            r"F_m(x) = F_{m-1}(x) + \eta h_m(x)",
            font_size=36
        ).next_to(math_title, DOWN, aligned_edge=LEFT, buff=0.5)
        
        math_explanation = VGroup(
            Text("• F_m: Current model", font_size=22),
            Text("• h_m: New weak learner", font_size=22),
            Text("• η: Learning rate", font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(math_eq, DOWN, aligned_edge=LEFT, buff=0.5)
        
        self.play(
            FadeIn(math_title, shift=UP*0.5),
            FadeIn(math_eq, shift=UP*0.5),
            run_time=1
        )
        
        for exp in math_explanation:
            self.play(Write(exp), run_time=0.5)
            self.wait(0.1)
        
        self.wait(2)
    
    def scene4c_boosting_math(self):
        # Title
        title = Text("Mathematical Intuition", font_size=42, color=BLUE)
        title.to_edge(UP)
        
        # Main equation
        math_eq = MathTex(
            r"F_m(x) = F_{m-1}(x) + \eta h_m(x)",
            font_size=48
        ).next_to(title, DOWN, buff=1)
        
        # Explanation
        explanation = VGroup(
            Text("• F_m: Current model's prediction", font_size=28),
            Text("• F_{m-1}: Previous model's prediction", font_size=28),
            Text("• h_m: New weak learner", font_size=28),
            Text("• η: Learning rate (controls contribution)", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(math_eq, DOWN, buff=1)
        
        # Visual representation
        models = VGroup(*[
            Rectangle(height=1, width=2, color=c, fill_opacity=0.2) 
            for c in [BLUE, GREEN, YELLOW, RED]
        ]).arrange(RIGHT, buff=0.3).next_to(explanation, DOWN, buff=1)
        
        plus = Text("+", font_size=36).next_to(models[0], RIGHT, buff=0.3)
        model_sum = Text("= Strong Model", font_size=36, color=GREEN).next_to(models[-1], RIGHT, buff=0.5)
        
        # Show content
        self.play(Write(title))
        self.wait(0.5)
        
        # Show equation
        self.play(Write(math_eq))
        self.wait(1)
        
        # Show explanation
        for item in explanation:
            self.play(Write(item))
            self.wait(0.3)
        
        # Show visual representation
        self.play(
            LaggedStart(*[FadeIn(model, shift=UP*0.5) for model in models], lag_ratio=0.3),
            run_time=1.5
        )
        
        self.play(
            Write(plus),
            Write(model_sum)
        )
        
        # Key takeaway
        takeaway = Text("Each new model corrects the errors of the previous ones",
                      font_size=28, color=YELLOW).next_to(models, DOWN, buff=1)
        
        self.play(Write(takeaway))
        self.wait(2)
    
    def scene4d_boosting_visual(self):
        # Title
        title = Text("Gradient Boosting: A Boosting Example", font_size=42, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create data points
        np.random.seed(42)
        x = np.linspace(-2, 2, 20)
        y = x**2 + np.random.normal(0, 0.2, len(x))
        
        # Create axes
        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-1, 5, 1],
            axis_config={"color": WHITE},
            tips=False
        )
        axes.scale(0.8).to_edge(LEFT, buff=1)
        
        # Create scatter plot
        dots = VGroup(*[Dot(axes.c2p(xi, yi), color=BLUE, radius=0.05) for xi, yi in zip(x, y)])
        
        # Initial prediction (mean)
        mean_y = np.mean(y)
        mean_line = axes.get_horizontal_line(axes.c2p(0, mean_y, 0), color=RED, stroke_width=3)
        
        # Show data and initial prediction
        self.play(
            Create(axes),
            Create(dots),
            run_time=1.5
        )
        
        self.play(
            Create(mean_line),
            run_time=1
        )
        
        # Show residuals
        residuals = VGroup()
        for xi, yi in zip(x, y):
            line = Line(
                axes.c2p(xi, mean_y, 0),
                axes.c2p(xi, yi, 0),
                color=YELLOW,
                stroke_width=2
            )
            residuals.add(line)
        
        self.play(
            Create(residuals),
            run_time=1.5
        )
        
        # Show next tree fitting residuals
        tree = self.create_decision_tree(depth=2).scale(0.7).to_edge(RIGHT, buff=1).shift(UP*0.5)
        tree_text = Text("Fit tree to residuals", font_size=24).next_to(tree, DOWN, buff=0.5)
        
        self.play(
            FadeIn(tree, shift=UP*0.5),
            Write(tree_text),
            run_time=1
        )
        
        # Show updated prediction
        new_pred = axes.plot(lambda x: 0.5*x**2 + mean_y, color=GREEN, stroke_width=3)
        
        self.play(
            Transform(mean_line, new_pred),
            FadeOut(residuals),
            run_time=1.5
        )
        
        # Key points
        key_points = VGroup(
            Text("• Models learn from previous errors", font_size=24),
            Text("• Each model focuses on hard examples", font_size=24),
            Text("• Combines weak learners into strong model", font_size=24, color=GREEN)
        )
        key_points.arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT, buff=1).shift(DOWN*1.5)
        
        self.play(Write(key_points), run_time=2)
        self.wait(2)
    
    def scene5a_stacking_concept(self):
        # Title
        title = Text("3. Stacking: Learning to Combine", font_size=42, color=BLUE)
        title.to_edge(UP)
        
        # Core concept
        concept = VGroup(
            Text("Training a meta-model to best combine", font_size=28),
            Text("the predictions of multiple base models", font_size=28)
        ).arrange(DOWN, center=False, aligned_edge=LEFT)
        concept.next_to(title, DOWN, buff=0.7)
        
        # Two-level architecture
        arch_title = Text("Two-Level Architecture:", font_size=26, color=YELLOW).to_edge(LEFT, buff=1)
        
        # Base models
        base_models = VGroup(
            Circle(radius=0.5, color=BLUE, fill_opacity=0.2),
            Circle(radius=0.5, color=GREEN, fill_opacity=0.2).shift(RIGHT*2),
            Circle(radius=0.5, color=YELLOW, fill_opacity=0.2).shift(RIGHT*4)
        )
        base_labels = VGroup(
            Text("Model 1", font_size=20).next_to(base_models[0], UP, buff=0.5),
            Text("Model 2", font_size=20).next_to(base_models[1], UP, buff=0.5),
            Text("Model 3", font_size=20).next_to(base_models[2], UP, buff=0.5)
        )
        
        # Meta-model
        meta_model = Circle(radius=0.6, color=RED, fill_opacity=0.2).shift(DOWN*2)
        meta_label = Text("Meta-Model", font_size=22).next_to(meta_model, DOWN, buff=0.5)
        
        # Arrows from base to meta
        arrows = VGroup()
        for model in base_models:
            arrow = Arrow(
                model.get_bottom(),
                meta_model.get_top(),
                buff=0.1,
                stroke_width=2,
                color=WHITE
            )
            arrows.add(arrow)
        
        # Stacking process
        process_title = Text("The Stacking Process:", font_size=26, color=YELLOW).to_edge(LEFT, buff=1).shift(DOWN*1.5)
        process = VGroup(
            Text("1. Split data into training and validation sets", font_size=22),
            Text("2. Train base models on training data", font_size=22),
            Text("3. Generate predictions on validation set", font_size=22),
            Text("4. Train meta-model on these predictions", font_size=22, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(process_title, DOWN, aligned_edge=LEFT, buff=0.5)
        
        # Show title and concept
        self.play(Write(title))
        self.play(Write(concept))
        self.wait(1)
        
        # Show architecture
        self.play(Write(arch_title))
        self.play(
            FadeIn(base_models, shift=UP*0.5),
            FadeIn(base_labels, shift=UP*0.5),
            run_time=1
        )
        
        # Show meta-model and connections
        self.play(
            FadeIn(meta_model, shift=UP*0.5),
            Write(meta_label),
            run_time=1
        )
        
        self.play(
            Create(arrows, lag_ratio=0.3),
            run_time=1.5
        )
        
        # Show stacking process
        self.play(
            FadeIn(process_title, shift=UP*0.5),
            FadeIn(process, shift=UP*0.5),
            run_time=1
        )
        
        self.wait(2)
    
    def scene5b_sports_analogy(self):
        # Title
        title = Text("🏈 Sports Analyst Analogy", font_size=42, color=BLUE)
        title.to_edge(UP)
        
        # Analogy explanation
        analogy = VGroup(
            Text("Think of Stacking like a sports team:", font_size=32, color=YELLOW),
            Text("1. Multiple experts (coaches) analyze the game", font_size=28),
            Text("2. Each has different insights and strategies", font_size=28),
            Text("3. The head coach (meta-model) combines their inputs", font_size=28),
            Text("4. Final game plan is stronger than any single opinion", font_size=28, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).scale(0.9).to_edge(LEFT, buff=1.5)
        
        # Visual elements
        coaches = VGroup(
            self.create_point_with_icon("👨‍💼", "Offensive Coach", BLUE),
            self.create_point_with_icon("👩‍💼", "Defensive Coach", GREEN),
            self.create_point_with_icon("👨‍💼", "Special Teams", YELLOW)
        ).arrange(DOWN, buff=0.8).to_edge(RIGHT, buff=2)
        
        head_coach = self.create_point_with_icon("👔", "Head Coach", RED).next_to(coaches, DOWN, buff=1.5)
        
        # Connect coaches to head coach
        connections = VGroup(*[
            Line(
                coach.get_bottom(),
                head_coach.get_top(),
                buff=0.1,
                stroke_width=2,
                color=WHITE
            ) for coach in coaches
        ])
        
        # Show title and analogy
        self.play(Write(title))
        self.wait(0.5)
        
        # Show analogy text
        self.play(Write(analogy[0]))
        self.wait(0.5)
        
        for point in analogy[1:]:
            self.play(Write(point))
            self.wait(0.3)
        
        # Show coaches
        self.play(
            LaggedStart(*[FadeIn(coach, shift=UP*0.5) for coach in coaches], lag_ratio=0.3),
            run_time=1.5
        )
        
        # Show head coach and connections
        self.play(
            FadeIn(head_coach, shift=UP*0.5),
            Create(connections, lag_ratio=0.2),
            run_time=1.5
        )
        
        # Key takeaway
        takeaway = Text("Just like a head coach combines expert opinions,\nStacking combines multiple models for better predictions",
                      font_size=28, color=YELLOW).next_to(analogy, DOWN, buff=1)
        
        self.play(Write(takeaway))
        self.wait(2)
    
    def scene5c_stacking_visual(self):
        # Title
        title = Text("Stacking in Action", font_size=42, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create base models with different algorithms
        models = VGroup(
            VGroup(
                Rectangle(height=1.5, width=2, color=BLUE, fill_opacity=0.2),
                Text("Decision\nTree", font_size=20, color=WHITE)
            ),
            VGroup(
                Rectangle(height=1.5, width=2, color=GREEN, fill_opacity=0.2),
                Text("SVM", font_size=20, color=WHITE)
            ),
            VGroup(
                Rectangle(height=1.5, width=2, color=YELLOW, fill_opacity=0.2),
                Text("Neural\nNetwork", font_size=20, color=WHITE)
            )
        )
        
        # Arrange models in a row
        models.arrange(RIGHT, buff=1).shift(UP*0.5)
        
        # Create meta-model
        meta_model = VGroup(
            Rectangle(height=1.5, width=2.5, color=RED, fill_opacity=0.2),
            Text("Meta-Model\n(Logistic Regression)", font_size=20, color=WHITE)
        ).shift(DOWN*2)
        
        # Create data flow
        train_data = VGroup(
            Rectangle(height=1, width=3, color=WHITE, fill_opacity=0.1),
            Text("Training Data", font_size=20)
        ).to_edge(LEFT, buff=1).shift(UP*2)
        
        val_data = VGroup(
            Rectangle(height=1, width=3, color=WHITE, fill_opacity=0.1),
            Text("Validation Data", font_size=20)
        ).to_edge(LEFT, buff=1).shift(UP*0.5)
        
        # Show data and models
        self.play(FadeIn(train_data), FadeIn(val_data))
        self.wait(0.5)
        
        # Animate base model training
        for i, model in enumerate(models):
            # Show model
            self.play(
                FadeIn(model, shift=UP*0.5),
                run_time=0.7
            )
            
            # Show data flow to model
            arrow1 = Arrow(
                train_data.get_right(),
                model.get_left(),
                buff=0.1,
                stroke_width=2,
                color=WHITE
            )
            
            self.play(
                Create(arrow1),
                run_time=0.7
            )
            
            # Show predictions
            preds = VGroup(
                Rectangle(height=0.8, width=2, color=model[0].get_color(), fill_opacity=0.2),
                Text(f"Preds {i+1}", font_size=16)
            ).next_to(model, DOWN, buff=0.5)
            
            arrow2 = Arrow(
                val_data.get_right(),
                model.get_left() + DOWN*0.5,
                buff=0.1,
                stroke_width=2,
                color=WHITE
            )
            
            self.play(
                Create(arrow2),
                FadeIn(preds, shift=UP*0.3),
                run_time=0.7
            )
            
            # Add to group for later use
            model.add(arrow1, arrow2, preds)
        
        # Show meta-features creation
        meta_features = VGroup(
            Rectangle(height=1, width=3, color=WHITE, fill_opacity=0.1),
            Text("Meta-Features\n(Predictions)", font_size=18)
        ).next_to(meta_model, UP, buff=1)
        
        # Connect predictions to meta-features
        for model in models:
            arrow = Arrow(
                model[3].get_bottom(),
                meta_features[0].get_top(),
                buff=0.1,
                stroke_width=2,
                color=WHITE
            )
            self.play(
                Create(arrow),
                run_time=0.7
            )
            model.add(arrow)
        
        # Show meta-model training
        self.play(
            FadeIn(meta_model, shift=UP*0.5),
            FadeIn(meta_features, shift=UP*0.5),
            run_time=1
        )
        
        # Show final prediction
        final_pred = VGroup(
            Rectangle(height=0.8, width=2, color=RED, fill_opacity=0.2),
            Text("Final\nPrediction", font_size=18, color=WHITE)
        ).next_to(meta_model, DOWN, buff=0.5)
        
        arrow_final = Arrow(
            meta_model[0].get_bottom(),
            final_pred[0].get_top(),
            buff=0.1,
            stroke_width=2,
            color=WHITE
        )
        
        self.play(
            Create(arrow_final),
            FadeIn(final_pred, shift=UP*0.3),
            run_time=0.7
        )
        
        # Key points
        key_points = VGroup(
            Text("• Combines different types of models", font_size=24),
            Text("• Learns optimal combination of predictions", font_size=24),
            Text("• Often wins machine learning competitions", font_size=24, color=GREEN)
        )
        key_points.arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT, buff=1).shift(UP*1)
        
        self.play(Write(key_points), run_time=2)
        self.wait(2)
    
    def scene6_comparison(self):
        # Title
        title = Text("Comparing Ensemble Methods", font_size=42, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create comparison table
        headers = ["", "Bagging", "Boosting", "Stacking"]
        rows = [
            ["Training", "Parallel", "Sequential", "Two-Phase"],
            ["Base Models", "Same type", "Same type", "Different types"],
            ["Focus", "Reduce variance", "Reduce bias", "Optimal combination"],
            ["Examples", "Random Forest", "XGBoost, AdaBoost", "Competition winners"],
            ["When to Use", "High variance", "High bias", "Best performance"]
        ]
        
        # Create table
        table = Table(
            rows,
            col_labels=[Text(h, font_size=24) for h in headers],
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT}
        ).scale(0.6).next_to(title, DOWN, buff=1)
        
        # Style table
        table.get_entries((0, 0)).set_color(YELLOW)
        table.get_entries((0, 1)).set_color(BLUE)
        table.get_entries((0, 2)).set_color(GREEN)
        table.get_entries((0, 3)).set_color(RED)
        
        # Add visual representations
        bagging_icon = VGroup(
            Circle(radius=0.4, color=BLUE, fill_opacity=0.2),
            Text("B", font_size=24, color=WHITE)
        ).to_edge(LEFT, buff=2).shift(UP*0.5)
        
        boosting_icon = VGroup(
            Arrow(LEFT*0.3, RIGHT*0.3, color=GREEN, stroke_width=4),
            Circle(radius=0.4, color=GREEN, fill_opacity=0.2).shift(RIGHT*0.8),
            Text("B", font_size=24, color=WHITE).shift(RIGHT*0.8)
        ).next_to(bagging_icon, RIGHT, buff=1.5)
        
        stacking_icon = VGroup(
            VGroup(
                Circle(radius=0.3, color=BLUE, fill_opacity=0.2),
                Text("1", font_size=16, color=WHITE)
            ),
            VGroup(
                Circle(radius=0.3, color=GREEN, fill_opacity=0.2).shift(RIGHT*0.7),
                Text("2", font_size=16, color=WHITE).shift(RIGHT*0.7)
            ),
            VGroup(
                Circle(radius=0.3, color=YELLOW, fill_opacity=0.2).shift(RIGHT*1.4),
                Text("3", font_size=16, color=WHITE).shift(RIGHT*1.4)
            ),
            Arrow(RIGHT*1.7, RIGHT*2.4, color=RED, stroke_width=4),
            VGroup(
                Circle(radius=0.4, color=RED, fill_opacity=0.2).shift(RIGHT*2.8),
                Text("M", font_size=20, color=WHITE).shift(RIGHT*2.8)
            )
        ).scale(0.8).next_to(boosting_icon, RIGHT, buff=1.5)
        
        # Show table and icons
        self.play(Create(table), run_time=1.5)
        self.wait(1)
        
        self.play(
            FadeIn(bagging_icon, shift=UP*0.5),
            FadeIn(boosting_icon, shift=UP*0.5),
            FadeIn(stacking_icon, shift=UP*0.5),
            run_time=1.5
        )
        
        # Key insights
        insights = VGroup(
            Text("Key Insights:", font_size=26, color=YELLOW).to_edge(LEFT, buff=1).shift(DOWN*2.5),
            Text("• Bagging: Best for high-variance models", font_size=22).next_to(Text("Key Insights:"), DOWN, aligned_edge=LEFT, buff=0.5),
            Text("• Boosting: Best for high-bias models", font_size=22).next_to(Text("• Bagging: Best for high-variance models"), DOWN, aligned_edge=LEFT, buff=0.3),
            Text("• Stacking: Best when different models capture different patterns", font_size=22).next_to(Text("• Boosting: Best for high-bias models"), DOWN, aligned_edge=LEFT, buff=0.3)
        )
        
        self.play(Write(insights), run_time=2)
        self.wait(2)
    
    def scene7_outro(self):
        # Title
        title = Text("Ensemble Learning: Key Takeaways", font_size=48, color=BLUE)
        title.to_edge(UP)
        
        # Key takeaways
        takeaways = VGroup(
            Text("1. Wisdom of Crowds", font_size=32, color=YELLOW).to_edge(LEFT, buff=2),
            Text("• Multiple models > Single model", font_size=24).next_to(Text("1. Wisdom of Crowds"), DOWN, aligned_edge=LEFT, buff=0.5),
            
            Text("2. Diversity Matters", font_size=32, color=YELLOW).next_to(Text("• Multiple models > Single model"), DOWN, aligned_edge=LEFT, buff=0.7),
            Text("• Different models capture different patterns", font_size=24).next_to(Text("2. Diversity Matters"), DOWN, aligned_edge=LEFT, buff=0.5),
            
            Text("3. Real-World Impact", font_size=32, color=YELLOW).next_to(Text("• Different models capture different patterns"), DOWN, aligned_edge=LEFT, buff=0.7),
            Text("• Used in competitions, industry, and research", font_size=24).next_to(Text("3. Real-World Impact"), DOWN, aligned_edge=LEFT, buff=0.5)
        )
        
        # Real-world applications
        apps = VGroup(
            Text("Applications:", font_size=28, color=GREEN).to_edge(RIGHT, buff=2).shift(UP*1),
            Text("• Netflix Prize winners", font_size=22).next_to(Text("Applications:"), DOWN, aligned_edge=LEFT, buff=0.5),
            Text("• Kaggle competitions", font_size=22).next_to(Text("• Netflix Prize winners"), DOWN, aligned_edge=LEFT, buff=0.3),
            Text("• Financial predictions", font_size=22).next_to(Text("• Kaggle competitions"), DOWN, aligned_edge=LEFT, buff=0.3),
            Text("• Medical diagnosis", font_size=22).next_to(Text("• Financial predictions"), DOWN, aligned_edge=LEFT, buff=0.3)
        )
        
        # Call to action
        cta = VGroup(
            Text("Ready to try it yourself?", font_size=32, color=YELLOW).shift(DOWN*1.5),
            Text("1. Start with Random Forest (easiest to use)", font_size=24).next_to(Text("Ready to try it yourself?"), DOWN, buff=0.7),
            Text("2. Experiment with XGBoost for tabular data", font_size=24).next_to(Text("1. Start with Random Forest (easiest to use)"), DOWN, aligned_edge=LEFT, buff=0.3),
            Text("3. Try stacking different models together", font_size=24).next_to(Text("2. Experiment with XGBoost for tabular data"), DOWN, aligned_edge=LEFT, buff=0.3)
        )
        
        # Final message
        final = Text("Thanks for learning about Ensemble Learning!", font_size=36, color=WHITE).shift(DOWN*3)
        
        # Animate
        self.play(Write(title))
        self.wait(0.5)
        
        # Show key takeaways
        self.play(Write(takeaways), run_time=2)
        self.wait(1)
        
        # Show applications
        self.play(Write(apps), run_time=1.5)
        self.wait(1)
        
        # Show call to action
        self.play(Write(cta), run_time=2)
        self.wait(1)
        
        # Final message
        self.play(Write(final), run_time=1.5)
        self.wait(3)

# Run with: manim -pql ensemble_learning_tutorial.py EnsembleLearningTutorial
