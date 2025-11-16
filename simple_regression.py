from manim import *
import numpy as np

class SimpleRegression(Scene):
    def construct(self):
        # 1. Create axes with more detailed configuration
        # Create axes with simplified configuration
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 400, 50],
            x_length=9,
            y_length=6,
            axis_config={
                "color": BLUE,
                "include_numbers": True,
                "decimal_number_config": {"num_decimal_places": 0},
            },
            x_axis_config={
                "numbers_to_include": np.arange(0, 8, 1),  # Only show whole numbers
                "numbers_with_elongated_ticks": np.arange(0, 8, 1),
                "include_ticks": True,
                "include_tip": False,  # Remove arrow at the end
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 450, 50),
                "include_ticks": True,
                "include_tip": False,  # Remove arrow at the end
            },
        )
        
        # Add minor ticks manually
        minor_ticks = VGroup()
        for x in [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]:
            tick = Line(
                start=axes.c2p(x, -0.1),
                end=axes.c2p(x, 0.1),
                stroke_width=1,
                color=BLUE
            )
            minor_ticks.add(tick)
        
        # Add 0 at the origin
        origin_label = Text("0", font_size=24, color=BLUE).next_to(
            axes.c2p(0, 0), DOWN + LEFT, buff=0.1
        )
        
        # Manually add 0 at the origin
        origin_label = Text("0", font_size=24, color=BLUE).next_to(
            axes.c2p(0, 0), DOWN + LEFT, buff=0.1
        )
        
        # Add axis labels with better positioning
        x_label = Text("Size (1000 sqft)", font_size=24).next_to(axes.x_axis, DOWN, buff=0.5)
        y_label = Text("Price ($1000s)", font_size=24).next_to(axes.y_axis, LEFT, buff=0.5).rotate(90*DEGREES)
        
        # Add title
        title = Text("House Price Prediction", font_size=32).to_edge(UP)
        
        # 2. Dataset
        points = [
            (1.5, 150), (2.0, 200), (2.5, 250), (3.0, 175),
            (3.5, 300), (4.0, 225), (4.5, 275), (5.0, 250),
            (5.5, 300), (6.0, 350)
        ]
        
        # 3. Show axes and labels
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            Write(title),
            Write(origin_label),
            Create(minor_ticks)
        )
        self.wait(0.5)
        
        # Add points one by one
        dots = VGroup()
        for x, y in points:
            dot = Dot(axes.c2p(x, y), color=YELLOW, radius=0.06)
            dots.add(dot)
            self.play(FadeIn(dot, scale=0.5), run_time=0.2)
        
        self.wait(0.5)
        
        # 4. Calculate best fit line (from origin)
        x_vals = np.array([p[0] for p in points])
        y_vals = np.array([p[1] for p in points])
        
        # Force line through origin (y = mx)
        slope = np.sum(x_vals * y_vals) / np.sum(x_vals ** 2)
        
        # Create best fit line
        line = Line(
            axes.c2p(0, 0),
            axes.c2p(6.5, slope * 6.5),
            color=GREEN,
            stroke_width=4
        )
        
        # Add equation text
        equation = MathTex(
            f"y = {slope:.1f}x",
            color=GREEN,
            font_size=28
        ).to_edge(UP, buff=0.5)
        
        self.play(Create(line), Write(equation))
        self.wait(1)
        
        # 5. Add example prediction
        example_x = 4.5
        predicted_y = slope * example_x
        
        # Create prediction dot and lines
        pred_dot = Dot(axes.c2p(example_x, predicted_y), color=RED, radius=0.08)
        h_line = DashedLine(
            axes.c2p(0, predicted_y),
            axes.c2p(example_x, predicted_y),
            color=RED,
            stroke_width=2
        )
        v_line = DashedLine(
            axes.c2p(example_x, 0),
            axes.c2p(example_x, predicted_y),
            color=RED,
            stroke_width=2
        )
        
        # Add prediction text - positioned above x-axis, right-aligned
        prediction_text = Text(
            f"At {example_x}k sqft, predicted price: ${predicted_y:,.0f},000",
            font_size=20,
            color=RED
        ).next_to(axes.x_axis, DOWN, buff=0.2).align_to(axes, RIGHT).shift(LEFT*0.5)
        
        # Add example point and lines
        example_dot = Dot(axes.c2p(example_x, predicted_y), color=RED, radius=0.1)
        v_line = DashedLine(
            axes.c2p(example_x, 0),
            axes.c2p(example_x, predicted_y),
            color=RED,
            stroke_width=2
        )
        h_line = DashedLine(
            axes.c2p(0, predicted_y),
            axes.c2p(example_x, predicted_y),
            color=RED,
            stroke_width=2
        )
        
        # Ensure axis labels are visible and in correct z-order
        self.bring_to_back(axes, x_label, y_label, title)
        
        self.play(
            Create(v_line),
            Create(h_line),
            FadeIn(example_dot, scale=0.5),
            Write(prediction_text),
            FadeIn(pred_dot, scale=1.5),
            run_time=1.5
        )
        self.play(Write(prediction_text))
        
        # Add a title
        title = Text("House Price Prediction", font_size=32, color=WHITE).to_edge(UP)
        self.play(Transform(equation, title))
        
        self.wait(3)
