from manim import *
import numpy as np

class LearningRateExplanation(Scene):
    def construct(self):
        # 1. Draw the cost function curve (a parabola)
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 18, 2],
            x_length=8,
            y_length=5,
            axis_config={"color": GREY},
        )
        curve = axes.plot(lambda x: (x-1)**2 + 2, color=BLUE, stroke_width=6)
        min_dot = Dot(axes.c2p(1, 2), color=YELLOW, radius=0.14)
        min_label = Text("Global Minimum", font_size=30, color=YELLOW).next_to(min_dot, DOWN)
        self.play(Create(axes), Create(curve))
        self.play(FadeIn(min_dot), Write(min_label))
        self.wait(1)

        # 2. Good learning rate
        good_label = Text("Good Learning Rate", font_size=36, color=GREEN).to_edge(UP)
        self.play(Write(good_label))
        start = -3.5
        point = Dot(axes.c2p(start, (start-1)**2 + 2), color=GREEN, radius=0.14)
        self.play(FadeIn(point))
        steps = [start]
        lr = 0.4
        for _ in range(7):
            grad = 2*(steps[-1] - 1)
            next_x = steps[-1] - lr * grad
            steps.append(next_x)
            next_y = (next_x-1)**2 + 2
            self.play(point.animate.move_to(axes.c2p(next_x, next_y)), run_time=0.6)
        self.wait(0.5)
        self.play(FadeOut(point), FadeOut(good_label))

        # 3. Overshoot
        over_label = Text("Too High: Overshoot", font_size=36, color=RED).to_edge(UP)
        self.play(Write(over_label))
        start = -3.5
        point = Dot(axes.c2p(start, (start-1)**2 + 2), color=RED, radius=0.14)
        self.play(FadeIn(point))
        steps = [start]
        lr = 1.2
        for _ in range(4):
            grad = 2*(steps[-1] - 1)
            next_x = steps[-1] - lr * grad
            steps.append(next_x)
            next_y = (next_x-1)**2 + 2
            self.play(point.animate.move_to(axes.c2p(next_x, next_y)), run_time=0.6)
        self.wait(0.5)
        self.play(FadeOut(point), FadeOut(over_label))

        # 4. Undershoot
        under_label = Text("Too Low: Undershoot", font_size=36, color=ORANGE).to_edge(UP)
        self.play(Write(under_label))
        start = -3.5
        point = Dot(axes.c2p(start, (start-1)**2 + 2), color=ORANGE, radius=0.14)
        self.play(FadeIn(point))
        steps = [start]
        lr = 0.08
        for _ in range(14):
            grad = 2*(steps[-1] - 1)
            next_x = steps[-1] - lr * grad
            steps.append(next_x)
            next_y = (next_x-1)**2 + 2
            self.play(point.animate.move_to(axes.c2p(next_x, next_y)), run_time=0.3)
        self.wait(1)
        self.play(FadeOut(point), FadeOut(under_label), FadeOut(min_dot), FadeOut(min_label), FadeOut(curve), FadeOut(axes))

        # 5. Final summary
        summary = Text("Learning rate controls the speed and stability\nof reaching the minimum!", font_size=38, color=BLUE).move_to(ORIGIN)
        self.play(Write(summary))
        self.wait(2)
        self.play(FadeOut(summary))

# To render this scene, run:
# manim -pql learning_rate_explanation.py LearningRateExplanation
