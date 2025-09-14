from manim import *
import numpy as np

class ConfusionMatrixTutorial(Scene):
    def construct(self):
        # Scene 1: Title Screen
        self.scene_intro()
        self.clear()
        
        # Scene 2: Basic Explanation
        self.scene_basic_explanation()
        self.clear()
        
        # Scene 3: Draw 2x2 Table
        self.scene_draw_table()
        self.clear()
        
        # Scene 4: Fill in Cells
        self.scene_fill_cells()
        self.clear()
        
        # Scene 5: Malaria Test Example
        self.scene_malaria_example()
        self.clear()
        
        # Scene 6: Performance Metrics
        self.scene_performance_metrics()
        self.clear()
        
        # Scene 7: Outro
        self.scene_outro()
    
    def scene_intro(self):
        # Title
        title = Text("Confusion Matrix in Machine Learning", 
                    font_size=48, 
                    color=BLUE)
        
        # Subtitle
        subtitle = Text("Understanding Predictions vs Reality",
                      font_size=32,
                      color=WHITE)
        
        # Position subtitle below title
        subtitle.next_to(title, DOWN, buff=0.5)
        
        # Animate title and subtitle
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP*0.5), run_time=1)
        self.wait(1)
        
        # Add a simple icon (optional)
        matrix_icon = Square(side_length=2, color=YELLOW, fill_opacity=0.2)
        inner_lines = VGroup(
            Line(matrix_icon.get_corner(UL), matrix_icon.get_corner(DR), color=YELLOW),
            Line(matrix_icon.get_corner(UR), matrix_icon.get_corner(DL), color=YELLOW)
        )
        matrix_icon_group = VGroup(matrix_icon, inner_lines).next_to(subtitle, DOWN, buff=1)
        
        self.play(Create(matrix_icon), run_time=1)
        self.play(Create(inner_lines), run_time=1)
        
        self.wait(2)
    
    def scene_basic_explanation(self):
        # Title
        title = Text("What is a Confusion Matrix?", font_size=40, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Main explanation
        explanation = VGroup(
            Text("A Confusion Matrix is a 2x2 table that compares", font_size=28),
            Text("predicted labels vs actual labels in classification.", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=1)
        
        # Ethiopian analogy
        analogy_title = Text("Ethiopian Example:", font_size=32, color=YELLOW)
        analogy = VGroup(
            Text("Think of a malaria test at a local clinic:", font_size=26),
            Text("• The test can be positive (sick) or negative (healthy)", font_size=24, color=GREEN),
            Text("• But is the test always correct?", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(explanation, DOWN, buff=1)
        
        analogy_title.next_to(explanation, DOWN, buff=0.8)
        analogy.next_to(analogy_title, DOWN, buff=0.3, aligned_edge=LEFT)
        
        # Add a simple icon
        test_icon = VGroup(
            Circle(radius=0.8, color=GREEN, fill_opacity=0.2),
            Text("Test", font_size=24, color=WHITE)
        ).to_edge(RIGHT, buff=2)
        
        # Animate
        self.play(Write(explanation), run_time=1.5)
        self.play(Write(analogy_title), run_time=0.8)
        self.play(Write(analogy), run_time=1.5)
        self.play(Create(test_icon), run_time=1)
        
        self.wait(2)
    
    def scene_draw_table(self):
        # Title
        title = Text("The 2x2 Confusion Matrix", font_size=40, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create the table
        table = Table(
            [["", "Predicted Positive", "Predicted Negative"],
             ["Actual Positive", "", ""],
             ["Actual Negative", "", ""]],
            include_outer_lines=True
        ).scale(0.7)
        
        # Style the table
        table.get_entries((0, 1)).set_color(YELLOW)
        table.get_entries((0, 2)).set_color(YELLOW)
        table.get_entries((1, 0)).set_color(YELLOW)
        table.get_entries((2, 0)).set_color(YELLOW)
        
        # Add row and column labels
        actual_label = Text("Actual", font_size=24, color=YELLOW).next_to(table, LEFT, buff=0.5)
        predicted_label = Text("Predicted", font_size=24, color=YELLOW).next_to(table, UP, buff=0.5)
        
        # Animate table creation
        self.play(Create(table), run_time=1.5)
        self.play(Write(actual_label), Write(predicted_label), run_time=1)
        
        # Add arrows to explain rows/columns
        arrow1 = Arrow(
            start=table.get_cell((1, 1)).get_left() + LEFT*0.5,
            end=table.get_cell((3, 1)).get_left() + LEFT*0.5,
            buff=0.1,
            color=GREEN
        )
        
        arrow2 = Arrow(
            start=table.get_cell((1, 1)).get_top() + UP*0.5,
            end=table.get_cell((1, 3)).get_top() + UP*0.5,
            buff=0.1,
            color=GREEN
        )
        
        self.play(
            Create(arrow1),
            Create(arrow2),
            run_time=1
        )
        
        self.wait(2)
    
    def scene_fill_cells(self):
        # Title
        title = Text("Understanding the Cells", font_size=40, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create the table with values
        table = Table(
            [["", "Predicted Positive", "Predicted Negative"],
             ["Actual Positive", "True Positive (TP)", "False Negative (FN)"],
             ["Actual Negative", "False Positive (FP)", "True Negative (TN)"]],
            include_outer_lines=True
        ).scale(0.6)
        
        # Style the table
        table.get_entries((0, 1)).set_color(YELLOW)
        table.get_entries((0, 2)).set_color(YELLOW)
        table.get_entries((1, 0)).set_color(YELLOW)
        table.get_entries((2, 0)).set_color(YELLOW)
        
        # Color the cells
        table.get_cell((2, 1)).set_fill(GREEN, opacity=0.3)  # TP
        table.get_cell((2, 2)).set_fill(RED, opacity=0.3)     # FN
        table.get_cell((3, 1)).set_fill(ORANGE, opacity=0.3)  # FP
        table.get_cell((3, 2)).set_fill(GREEN, opacity=0.3)   # TN
        
        # Add explanations
        explanations = VGroup(
            Text("• TP: Predicted sick and actually sick", color=GREEN, font_size=24),
            Text("• FN: Predicted healthy but actually sick", color=RED, font_size=24),
            Text("• FP: Predicted sick but actually healthy", color=ORANGE, font_size=24),
            Text("• TN: Predicted healthy and actually healthy", color=GREEN, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(table, DOWN, buff=1)
        
        # Animate
        self.play(Create(table), run_time=1.5)
        self.wait(0.5)
        
        # Animate each explanation with its corresponding cell
        for i, exp in enumerate([(2,1), (2,2), (3,1), (3,2)]):
            cell = table.get_cell((exp[0], exp[1]))
            self.play(
                cell.animate.set_fill(opacity=0.8),
                Write(explanations[i]),
                run_time=1
            )
            self.wait(0.5)
        
        self.wait(2)
    
    def scene_malaria_example(self):
        # Title
        title = Text("Malaria Test Example", font_size=40, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create the table with values
        table = Table(
            [["", "Test Positive", "Test Negative"],
             ["Has Malaria", "TP: Correctly identified", "FN: Missed case"],
             ["No Malaria", "FP: False alarm", "TN: Correctly healthy"]],
            include_outer_lines=True
        ).scale(0.6)
        
        # Style the table
        table.get_entries((0, 1)).set_color(YELLOW)
        table.get_entries((0, 2)).set_color(YELLOW)
        table.get_entries((1, 0)).set_color(YELLOW)
        table.get_entries((2, 0)).set_color(YELLOW)
        
        # Color the cells
        table.get_cell((2, 1)).set_fill(GREEN, opacity=0.3)  # TP
        table.get_cell((2, 2)).set_fill(RED, opacity=0.3)     # FN
        table.get_cell((3, 1)).set_fill(ORANGE, opacity=0.3)  # FP
        table.get_cell((3, 2)).set_fill(GREEN, opacity=0.3)   # TN
        
        # Add a doctor character (simple stick figure)
        doctor = VGroup(
            Circle(radius=0.3, color=WHITE, fill_opacity=0.2),  # Head
            Line(ORIGIN, DOWN*0.5, color=WHITE).next_to(Circle().get_bottom(), DOWN, buff=0),  # Body
            Line(ORIGIN, LEFT*0.3, color=WHITE).next_to(Line(ORIGIN, DOWN*0.5).get_center(), LEFT, buff=0),  # Left arm
            Line(ORIGIN, RIGHT*0.3, color=WHITE).next_to(Line(ORIGIN, DOWN*0.5).get_center(), RIGHT, buff=0)  # Right arm
        ).scale(0.8).to_edge(LEFT, buff=2).shift(DOWN*0.5)
        
        # Add thought bubble
        thought_bubble = ThoughtBubble()
        thought_bubble.pin_to(doctor)
        thought_bubble.add_content(Text("Is this malaria?", font_size=20, color=WHITE))
        
        # Create doctor and table first
        self.play(Create(doctor), run_time=1)
        self.play(table.animate.scale(0.8).to_edge(RIGHT, buff=1), run_time=1)
        
        # Then add thought bubble
        self.play(Create(thought_bubble), run_time=1)
        
        # Highlight each cell with explanation
        cells = [
            (2, 1, "TP: Test says malaria and patient has it!", GREEN),
            (2, 2, "FN: Test missed the malaria case!", RED),
            (3, 1, "FP: False alarm! Test was wrong.", ORANGE),
            (3, 2, "TN: No malaria, and test agrees!", GREEN)
        ]
        
        for row, col, text, color in cells:
            cell = table.get_cell((row, col))
            highlight = cell.copy().set_fill(color, opacity=0.8)
            explanation = Text(text, font_size=20, color=color).next_to(table, DOWN, buff=0.5)
            
            self.play(
                FadeIn(highlight),
                Write(explanation),
                run_time=1
            )
            self.wait(0.5)
            self.play(
                FadeOut(highlight),
                FadeOut(explanation),
                run_time=0.5
            )
        
        self.wait(1)
    
    def scene_performance_metrics(self):
        # Title
        title = Text("Performance Metrics", font_size=40, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create formulas
        precision = MathTex(
            r"\text{Precision} = \frac{TP}{TP + FP} = \frac{\text{True Positives}}{\text{All Positive Predictions}}",
            font_size=32
        )
        
        recall = MathTex(
            r"\text{Recall} = \frac{TP}{TP + FN} = \frac{\text{True Positives}}{\text{All Actual Positives}}",
            font_size=32
        )
        
        accuracy = MathTex(
            r"\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN} = \frac{\text{Correct Predictions}}{\text{All Predictions}}",
            font_size=32
        )
        
        # Position formulas
        precision.next_to(title, DOWN, buff=1)
        recall.next_to(precision, DOWN, buff=0.5)
        accuracy.next_to(recall, DOWN, buff=0.5)
        
        # Add descriptions
        precision_desc = Text("How many selected items are relevant?", font_size=24, color=YELLOW).next_to(precision, RIGHT, buff=1)
        recall_desc = Text("How many relevant items are selected?", font_size=24, color=YELLOW).next_to(recall, RIGHT, buff=1)
        
        # Animate
        self.play(Write(precision), run_time=1.5)
        self.play(Write(precision_desc), run_time=1)
        self.wait(0.5)
        
        self.play(Write(recall), run_time=1.5)
        self.play(Write(recall_desc), run_time=1)
        self.wait(0.5)
        
        self.play(Write(accuracy), run_time=1.5)
        
        # Add example values
        example = Text("Example: TP=80, TN=15, FP=10, FN=5", font_size=24, color=GREEN).next_to(accuracy, DOWN, buff=1)
        self.play(Write(example), run_time=1)
        
        self.wait(2)
    
    def scene_outro(self):
        # Thank you message
        thanks = Text("Thank You!", font_size=48, color=BLUE)
        self.play(Write(thanks), run_time=1.5)
        self.play(thanks.animate.scale(1.2), run_time=0.5)
        self.play(thanks.animate.scale(1/1.2), run_time=0.5)
        
        # Summary
        summary = VGroup(
            Text("Key Takeaways:", font_size=32, color=YELLOW),
            Text("• Confusion Matrix shows prediction performance", font_size=24),
            Text("• TP, TN, FP, FN help understand model behavior", font_size=24),
            Text("• Precision, Recall, and Accuracy measure performance", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(thanks, DOWN, buff=1)
        
        self.play(LaggedStart(*[Write(line) for line in summary], lag_ratio=0.3), run_time=2)
        
        # Final message
        final_msg = Text("Subscribe for more ML concepts explained visually!", 
                        font_size=28, 
                        color=GREEN)
        final_msg.next_to(summary, DOWN, buff=1)
        
        self.play(Write(final_msg), run_time=1.5)
        self.wait(2)

# Helper class for thought bubble
class ThoughtBubble(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.width = 3
        self.height = 2
        
        # Create thought bubble shape
        bubble = Ellipse(
            width=self.width,
            height=self.height,
            fill_opacity=0.8,
            stroke_width=2,
            fill_color=BLACK,
            stroke_color=WHITE
        )
        
        # Add some small circles for the thought bubble tail
        tail1 = Dot(radius=0.1, color=WHITE, fill_opacity=0.8).move_to([-1, -0.5, 0])
        tail2 = Dot(radius=0.08, color=WHITE, fill_opacity=0.8).move_to([-1.3, -0.7, 0])
        tail3 = Dot(radius=0.06, color=WHITE, fill_opacity=0.8).move_to([-1.6, -0.9, 0])
        
        self.bubble = bubble
        self.add(bubble, tail1, tail2, tail3)
        self.content = None
    
    def add_content(self, content):
        self.content = content
        self.content.move_to(self.bubble.get_center())
        self.add(self.content)
        return self
    
    def pin_to(self, mobject):
        self.next_to(mobject, RIGHT, buff=0.5)
        return self
