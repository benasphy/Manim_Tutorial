from manim import *

class TestScene(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"color": BLUE},
        )
        
        # Add a simple dot
        dot = Dot(axes.c2p(2, 3), color=YELLOW)
        
        # Add some text
        text = Text("Test Scene", font_size=24).to_edge(UP)
        
        # Animate
        self.play(Create(axes))
        self.play(FadeIn(dot))
        self.play(Write(text))
        self.wait(2)
