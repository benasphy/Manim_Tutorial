from manim import *
import numpy as np

class EDUERAIntro(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#0f0f1a"
        
        # --- Section 1: Logo Reveal ---
        logo = Text("EDUERA", font_size=100, font="Arial", gradient=(BLUE, BLUE_C))
        tagline = Text("Machine Learning Mastery", font_size=36, color=WHITE)
        tagline.next_to(logo, DOWN, buff=0.5)
        
        # Animate logo and tagline
        self.play(Write(logo), run_time=1.5)
        self.play(FadeIn(tagline, shift=UP*0.3), run_time=1)
        self.wait(1)
        
        # Move logo to top
        self.play(
            logo.animate.scale(0.6).to_edge(UP, buff=0.3),
            FadeOut(tagline)
        )
        
        # --- Section 2: Linear Regression ---
        lr_title = Text("Linear Regression", font_size=40, color=GREEN)
        lr_title.next_to(logo, DOWN, buff=0.8)
        
        # Create axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 15, 1],
            axis_config={"color": WHITE},
            tips=False
        ).scale(0.8).shift(DOWN*0.5)
        
        # Generate and plot random data points
        np.random.seed(42)
        x_vals = np.linspace(1, 9, 12)
        y_vals = 1.2 * x_vals + 2 + np.random.normal(0, 0.8, len(x_vals))
        dots = VGroup(*[Dot(axes.c2p(x, y), color=YELLOW) for x, y in zip(x_vals, y_vals)])
        
        # Best fit line
        line = axes.plot(lambda x: 1.2 * x + 2, color=GREEN)
        
        # Show linear regression
        self.play(Write(lr_title))
        self.wait(0.5)
        self.play(Create(axes), run_time=1)
        self.play(LaggedStart(*[GrowFromCenter(dot) for dot in dots], lag_ratio=0.1))
        self.wait(0.5)
        self.play(Create(line), run_time=1.5)
        
        # Equation
        eq = MathTex(r"y = b_0 + b_1x", color=GREEN).next_to(axes, DOWN, buff=0.5)
        self.play(Write(eq))
        self.wait(1)
        
        # --- Section 3: Neural Network ---
        nn_title = Text("Neural Networks", font_size=40, color=PURPLE)
        nn_title.move_to(lr_title)
        
        # Simple neural network
        def create_neuron(pos, color=WHITE):
            return Circle(radius=0.2, color=color, fill_opacity=0.7).move_to(pos)
        
        # Create layers
        input_layer = VGroup(*[create_neuron([-4, i, 0], BLUE) for i in np.linspace(1.5, -1.5, 4)])
        hidden_layer = VGroup(*[create_neuron([0, i, 0], GREEN) for i in np.linspace(2, -2, 6)])
        output_layer = VGroup(*[create_neuron([4, i, 0], RED) for i in np.linspace(1, -1, 2)])
        
        # Create connections
        connections = VGroup()
        for in_node in input_layer:
            for out_node in hidden_layer:
                connections.add(Line(
                    in_node.get_center(), 
                    out_node.get_center(),
                    stroke_width=1,
                    color=WHITE,
                    stroke_opacity=0.3
                ))
        
        for in_node in hidden_layer:
            for out_node in output_layer:
                connections.add(Line(
                    in_node.get_center(), 
                    out_node.get_center(),
                    stroke_width=1,
                    color=WHITE,
                    stroke_opacity=0.3
                ))
        
        # Animate transition to neural network
        self.play(
            FadeOut(axes), 
            FadeOut(dots), 
            FadeOut(line),
            FadeOut(eq),
            ReplacementTransform(lr_title, nn_title)
        )
        
        # Animate neural network
        self.play(Create(connections), run_time=2)
        self.play(LaggedStart(
            *[GrowFromCenter(neuron) for neuron in input_layer],
            *[GrowFromCenter(neuron) for neuron in hidden_layer],
            *[GrowFromCenter(neuron) for neuron in output_layer],
            lag_ratio=0.1
        ))
        
        # Pulsing effect
        self.play(
            *[Flash(neuron, color=YELLOW, flash_radius=0.3) for neuron in hidden_layer],
            run_time=2
        )
        
        # --- Section 4: Course Announcement ---
        self.play(
            FadeOut(connections),
            FadeOut(input_layer),
            FadeOut(hidden_layer),
            FadeOut(output_layer),
            FadeOut(nn_title)
        )
        
        # Final message
        course_text = Text("Machine Learning Course", font_size=48, gradient=(PURPLE, PINK))
        by_benjamin = Text("by Benjamin", font_size=36, color=WHITE)
        final_logo = logo.copy().scale(1.5).center()
        
        group = VGroup(course_text, by_benjamin).arrange(DOWN, buff=0.5).next_to(final_logo, DOWN, buff=0.8)
        
        self.play(
            FadeIn(final_logo, shift=UP*0.5),
            FadeIn(group, shift=UP*0.5)
        )
        
        # Add subscribe button
        subscribe = Text("Subscribe", font_size=32, color=YELLOW)
        button = SurroundingRectangle(subscribe, color=YELLOW, corner_radius=0.2, fill_opacity=0.2)
        button_group = VGroup(button, subscribe).next_to(by_benjamin, DOWN, buff=1)
        
        self.play(
            GrowFromCenter(button_group),
            run_time=1
        )
        
        # Pulsing effect on subscribe
        self.play(
            button_group.animate.scale(1.1),
            rate_func=there_and_back,
            run_time=1.5
        )
        
        self.wait(2)
        
        # Final zoom on logo
        self.play(
            FadeOut(group),
            FadeOut(button_group),
            final_logo.animate.scale(1.5)
        )
        
        self.wait(1)
