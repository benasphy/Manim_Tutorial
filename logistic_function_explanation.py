from manim import *

class LogisticFunctionExplanation(Scene):
    def construct(self):
        # Title
        title = Text("Logistic (Sigmoid) Function", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Formula
        formula = MathTex(r"\sigma(x) = \\frac{1}{1 + e^{-x}}", font_size=48)
        formula.next_to(title, DOWN)
        self.play(Write(formula))
        self.wait(1)

        # Explanatory text
        explanation = Text(
            "The logistic (sigmoid) function squashes any real number to (0, 1).",
            font_size=28
        )
        explanation.next_to(formula, DOWN)
        self.play(Write(explanation))
        self.wait(1)

        # Axes for plotting
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-1, 1.5, 0.5],
            x_length=8,
            y_length=4,
            axis_config={"numbers_to_include": [-5, 0, 5, 1]},
            tips=False,
        )
        axes.to_edge(DOWN)

        # Linear function: y = x (clipped for display)
        linear_graph = axes.plot(lambda x: x/6, color=BLUE, x_range=[-6, 6])
        linear_label = axes.get_graph_label(linear_graph, label="y = x", x_val=4, direction=UR, color=BLUE)

        # Logistic (sigmoid) function
        sigmoid = lambda x: 1 / (1 + np.exp(-x))
        sigmoid_graph = axes.plot(sigmoid, color=YELLOW, x_range=[-6, 6])
        sigmoid_label = axes.get_graph_label(sigmoid_graph, label="y = \\sigma(x)", x_val=4, direction=UR, color=YELLOW)

        # Add axes and graphs
        self.play(Create(axes))
        self.wait(0.5)
        self.play(Create(linear_graph), Write(linear_label))
        self.wait(0.5)
        self.play(Create(sigmoid_graph), Write(sigmoid_label))
        self.wait(2)

        # Add a closing note
        note = Text(
            "Notice how the sigmoid squashes the linear output between 0 and 1!",
            font_size=28
        )
        note.next_to(axes, DOWN)
        self.play(Write(note))
        self.wait(2)
