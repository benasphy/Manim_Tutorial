from manim import *
import numpy as np

class DecisionTreeExplanation(Scene):
    def construct(self):
        # Title
        title = Text("Decision Tree Explained", font_size=48)
        self.play(FadeIn(title))
        self.wait(0.7)
        self.play(title.animate.to_edge(UP))

        # What is a Decision Tree?
        what_is = Text("What is a Decision Tree?", font_size=36, color=BLUE)
        what_is_text = Text(
            "A Decision Tree is a flowchart-like structure\nused for classification and regression.\nIt splits data into branches based on feature questions.",
            font_size=28
        ).next_to(what_is, DOWN, buff=0.3)
        self.play(FadeIn(what_is.next_to(title, DOWN, buff=0.5)))
        self.play(FadeIn(what_is_text))
        self.wait(2)
        self.play(FadeOut(what_is), FadeOut(what_is_text))

        # Example Weather Data Table
        table_title = Text("Weather Data Example", font_size=32, color=YELLOW)
        self.play(FadeIn(table_title.next_to(title, DOWN, buff=0.5)))
        weather_data = [
            ["Outlook", "Temperature", "Humidity", "Wind", "Play"],
            ["Sunny", "Hot", "High", "Weak", "No"],
            ["Sunny", "Hot", "High", "Strong", "No"],
            ["Overcast", "Hot", "High", "Weak", "Yes"],
            ["Rain", "Mild", "High", "Weak", "Yes"],
            ["Rain", "Cool", "Normal", "Weak", "Yes"],
            ["Rain", "Cool", "Normal", "Strong", "No"],
            ["Overcast", "Cool", "Normal", "Strong", "Yes"],
            ["Sunny", "Mild", "High", "Weak", "No"],
            ["Sunny", "Cool", "Normal", "Weak", "Yes"],
            ["Rain", "Mild", "Normal", "Weak", "Yes"],
            ["Sunny", "Mild", "Normal", "Strong", "Yes"],
            ["Overcast", "Mild", "High", "Strong", "Yes"],
            ["Overcast", "Hot", "Normal", "Weak", "Yes"],
            ["Rain", "Mild", "High", "Strong", "No"]
        ]
        table = Table(weather_data, include_outer_lines=True, element_to_mobject_config={"font_size": 22})
        table.scale(0.8).next_to(table_title, DOWN, buff=0.4)
        self.play(FadeIn(table))
        self.wait(2.5)
        self.play(FadeOut(table_title), FadeOut(table))

        # Decision Tree Visualization (simplified)
        tree_title = Text("Decision Tree for Weather Data", font_size=32, color=GREEN)
        self.play(FadeIn(tree_title.next_to(title, DOWN, buff=0.5)))
        # Draw a simple tree manually for clarity
        root = Text("Outlook?", font_size=28, color=WHITE)
        sunny = Text("Sunny", font_size=26, color=YELLOW)
        overcast = Text("Overcast", font_size=26, color=GREY_B)
        rain = Text("Rain", font_size=26, color=BLUE)
        no_leaf = Text("No", font_size=26, color=RED)
        yes_leaf = Text("Yes", font_size=26, color=GREEN)

        # Layout positions
        root.move_to([0, 1.5, 0])
        sunny.move_to([-3, 0.5, 0])
        overcast.move_to([0, 0.5, 0])
        rain.move_to([3, 0.5, 0])
        no_leaf.move_to([-3, -0.5, 0])
        yes_leaf.move_to([0, -0.5, 0])
        # Separate Rain branch leaves vertically to avoid overlap
        no_leaf2 = Text("No", font_size=26, color=RED).move_to([2.2, -0.2, 0])
        yes_leaf2 = Text("Yes", font_size=26, color=GREEN).move_to([3.8, -1.2, 0])

        # Draw edges
        sunny_edge = Arrow(root.get_bottom(), sunny.get_top(), buff=0.1)
        overcast_edge = Arrow(root.get_bottom(), overcast.get_top(), buff=0.1)
        rain_edge = Arrow(root.get_bottom(), rain.get_top(), buff=0.1)
        sunny_no_edge = Arrow(sunny.get_bottom(), no_leaf.get_top(), buff=0.1)
        sunny_yes_edge = Arrow(sunny.get_bottom(), yes_leaf.get_top(), buff=0.1)
        # Adjust rain branch arrows to match new leaf positions
        rain_no_edge = Arrow(rain.get_bottom(), no_leaf2.get_top(), buff=0.1)
        rain_yes_edge = Arrow(rain.get_bottom(), yes_leaf2.get_top(), buff=0.1)

        # Animate tree
        self.play(FadeIn(root))
        self.play(GrowArrow(sunny_edge), FadeIn(sunny),
                  GrowArrow(overcast_edge), FadeIn(overcast),
                  GrowArrow(rain_edge), FadeIn(rain))
        self.wait(0.7)
        self.play(GrowArrow(sunny_no_edge), FadeIn(no_leaf),
                  GrowArrow(sunny_yes_edge), FadeIn(yes_leaf))
        self.wait(0.7)
        self.play(GrowArrow(rain_no_edge), FadeIn(no_leaf2),
                  GrowArrow(rain_yes_edge), FadeIn(yes_leaf2))
        self.wait(2.5)
        self.play(FadeOut(tree_title), FadeOut(root), FadeOut(sunny), FadeOut(overcast), FadeOut(rain),
                  FadeOut(no_leaf), FadeOut(yes_leaf), FadeOut(no_leaf2), FadeOut(yes_leaf2),
                  FadeOut(sunny_edge), FadeOut(overcast_edge), FadeOut(rain_edge),
                  FadeOut(sunny_no_edge), FadeOut(sunny_yes_edge), FadeOut(rain_no_edge), FadeOut(rain_yes_edge))

        # How does Decision Tree Algorithm work?
        algo_title = Text("How Does the Decision Tree Algorithm Work?", font_size=32, color=BLUE)
        self.play(FadeIn(algo_title.next_to(title, DOWN, buff=0.5)))
        steps = VGroup(
            Text("1. Start at the root node (entire dataset)", font_size=26),
            Text("2. Ask the best question (split on best feature)", font_size=26),
            Text("3. Branch out and divide data", font_size=26),
            Text("4. Repeat splitting at each branch", font_size=26),
            Text("5. Stop at leaf nodes (final prediction)", font_size=26)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(algo_title, DOWN, buff=0.3)
        self.play(FadeIn(steps))
        self.wait(4)
        self.play(FadeOut(algo_title), FadeOut(steps))

        # Summary
        summary = VGroup(
            Text("Decision Trees split data by asking questions!", font_size=32, color=GREEN),
            Text("Great for classification and regression", font_size=28),
            Text("Easy to interpret and visualize", font_size=28),
            Text("Example: Weather data → tree", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(title, DOWN, buff=0.7)
        self.play(FadeIn(summary))
        self.wait(2.5)
        self.play(FadeOut(summary), FadeOut(title))
        self.wait(0.5)
