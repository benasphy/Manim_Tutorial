from manim import *
import numpy as np

# Simple color palette
BLUE = '#58C4DD'
YELLOW = '#FFFF00'
GREEN = '#83C167'

class LinearRegressionScene(Scene):
    def construct(self):
        # 1. Set up simple axes
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[100, 400, 50],
            axis_config={"color": BLUE},
            tips=False,
        )
        
        # Add axis labels
        x_label = Text("Size (1000 sqft)", font_size=24).next_to(axes.x_axis, DOWN)
        y_label = Text("Price ($1000s)", font_size=24).next_to(axes.y_axis, LEFT).rotate(90*DEGREES)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        # 2. Dataset from the image
        x_vals = np.array([1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0])
        y_vals = np.array([150, 200, 250, 175, 300, 225, 275, 250, 300, 350])
        
        # 3. Plot points one by one
        dots = VGroup()
        for x, y in zip(x_vals, y_vals):
            dot = Dot(axes.c2p(x, y), color=YELLOW)
            self.play(FadeIn(dot, scale=0.5), run_time=0.3)
            dots.add(dot)
        
        self.wait(0.5)
        
        # 4. Calculate and show best fit line (using numpy directly)
        A = np.vstack([x_vals, np.ones(len(x_vals))]).T
        slope, intercept = np.linalg.lstsq(A, y_vals, rcond=None)[0]
        
        # Create equation text
        equation = Text(
            f"y = {slope:.1f}x + {intercept:.1f}",
            font_size=24,
            color=GREEN
        ).to_edge(UP)
        
        # Create best fit line
        line_start = axes.c2p(0, intercept)
        line_end = axes.c2p(6.5, slope * 6.5 + intercept)
        best_fit_line = Line(line_start, line_end, color=GREEN, stroke_width=3)
        
        self.play(Write(equation))
        self.play(Create(best_fit_line), run_time=1.5)
        
        # 5. Make a prediction for size 4.5
        predict_size = 4.5
        predicted_price = slope * predict_size + intercept
        pred_point = axes.c2p(predict_size, predicted_price)
        pred_dot = Dot(pred_point, color=GREEN, radius=0.08)
        
        # Add prediction text
        prediction_text = Text(
            f"Predicted price for {predict_size}k sqft: ${predicted_price:,.0f},000",
            font_size=20,
            color=GREEN
        ).to_edge(DOWN)
        
        self.play(FadeIn(pred_dot, scale=2))
        self.play(Write(prediction_text))
        
        self.wait(3)

# To render this scene, run:
# manim -pql linear_regression_scene.py LinearRegressionScene
