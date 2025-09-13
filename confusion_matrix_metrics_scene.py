from manim import *

class ConfusionMatrixMetricsScene(Scene):
    def construct(self):
        # Title
        title = Text("Confusion Matrix Made Simple", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Opening Hook
        hook = Text(
            "You built a machine learning model.\nBut is it actually good?\nLet me explain using disease prediction!",
            font_size=32
        )
        self.play(Write(hook))
        self.wait(2)
        self.play(FadeOut(hook))

        # What is a confusion matrix?
        cm_title = Text("What is a Confusion Matrix?", font_size=38, color=YELLOW)
        self.play(Write(cm_title))
        self.wait(1)
        self.play(cm_title.animate.next_to(title, DOWN, buff=0.2))

        # Create the confusion matrix with all labels included
        cm_table = Table(
            [
                ["", "Predicted No", "Predicted Yes"],
                ["Actual No", "TN", "FP"],
                ["Actual Yes", "FN", "TP"]
            ],
            include_outer_lines=True,
            element_to_mobject_config={"font_size": 32},
            line_config={"stroke_width": 2}
        ).scale(0.9).next_to(cm_title, DOWN, buff=0.6)
        
        # Color the TN, FP, FN, TP labels
        cell_colors = {"TP": GREEN, "TN": BLUE, "FP": RED, "FN": ORANGE}
        for key, color in cell_colors.items():
            row, col = (1, 1) if key == "TN" else (1, 2) if key == "FP" else (2, 1) if key == "FN" else (2, 2)
            cell = cm_table.get_cell((row, col))
            # Find the text object in the cell and set its color
            for mob in cell:
                if isinstance(mob, Text) and mob.text == key:
                    mob.set_color(color)
        
        # Add the table to the scene
        self.play(Create(cm_table))
        self.wait(1)
        
        # Store references to the cell coordinates for highlighting
        cell_coords = {
            "TN": (1, 1),  # Actual No, Predicted No
            "FP": (1, 2),  # Actual No, Predicted Yes
            "FN": (2, 1),  # Actual Yes, Predicted No
            "TP": (2, 2)   # Actual Yes, Predicted Yes
        }
        
        # Cell coordinates (row, col) in the table
        cell_coords = {
            "TN": (1, 1),  # Actual No, Predicted No
            "FP": (1, 2),  # Actual No, Predicted Yes
            "FN": (2, 1),  # Actual Yes, Predicted No
            "TP": (2, 2)   # Actual Yes, Predicted Yes
        }
        cell_descs = {
            "TP": "TP: Correctly predicted Yes (actually Yes)",
            "TN": "TN: Correctly predicted No (actually No)",
            "FP": "FP: Predicted Yes, actually No",
            "FN": "FN: Predicted No, actually Yes"
        }
        cell_colors = {"TP": GREEN, "TN": BLUE, "FP": RED, "FN": ORANGE}
        
        # Add numbers below each notation
        numbers = [
            ("TP", 30), ("TN", 50), ("FP", 10), ("FN", 10)
        ]
        
        # First, adjust the table to make room for numbers
        for row in range(1, 3):
            for col in range(1, 3):
                cell = cm_table.get_cell((row, col))
                for mob in cell:
                    if isinstance(mob, Text):
                        mob.shift(UP * 0.3)  # Move text up in the cell
        
        # Now add numbers below the notations
        for key, val in numbers:
            row, col = cell_coords[key]
            cell = cm_table.get_cell((row, col))
            
            # Find the text object in the cell (TP/TN/FP/FN)
            for mob in cell:
                if isinstance(mob, Text) and mob.text in ["TP", "TN", "FP", "FN"]:
                    # Create number text with matching color
                    num = Text(
                        f"{val}",
                        font_size=28,
                        color=cell_colors[key]
                    )
                    # Position number directly below the notation
                    num.next_to(mob, DOWN, buff=0.1)
                    
                    # Add the number to the scene
                    self.play(FadeIn(num))
                    self.wait(0.3)
                    break
        
        self.wait(1.5)
        
        # Explain each cell one by one
        for key in ["TP", "TN", "FP", "FN"]:
            # Show description below the table
            desc = Text(
                cell_descs[key],
                font_size=28,
                color=cell_colors[key]
            ).next_to(cm_table, DOWN, buff=0.8)
            
            self.play(FadeIn(desc))
            self.wait(1.2)
            self.play(FadeOut(desc))
            
        self.wait(0.5)

        # Remove the example header if it exists
        # (no header is written now)

        # Accuracy (below table)
        acc_formula = MathTex(r"\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}", font_size=38)
        acc_calc = MathTex(r"= \frac{30 + 50}{100} = 0.80", font_size=38)
        acc_formula.next_to(cm_table, DOWN, buff=0.5)
        acc_calc.next_to(acc_formula, DOWN, buff=0.2)
        self.play(Write(acc_formula))
        self.wait(0.5)
        self.play(Write(acc_calc))
        self.wait(1.5)
        self.play(FadeOut(acc_formula), FadeOut(acc_calc))

        # Precision (below table)
        prec_formula = MathTex(r"\text{Precision} = \frac{TP}{TP + FP}", font_size=38)
        prec_calc = MathTex(r"= \frac{30}{30 + 10} = 0.75", font_size=38)
        prec_formula.next_to(cm_table, DOWN, buff=0.5)
        prec_calc.next_to(prec_formula, DOWN, buff=0.2)
        self.play(Write(prec_formula))
        self.wait(0.5)
        self.play(Write(prec_calc))
        self.wait(1.5)
        self.play(FadeOut(prec_formula), FadeOut(prec_calc))

        # Recall (below table)
        recall_formula = MathTex(r"\text{Recall} = \frac{TP}{TP + FN}", font_size=38)
        recall_calc = MathTex(r"= \frac{30}{30 + 10} = 0.75", font_size=38)
        recall_formula.next_to(cm_table, DOWN, buff=0.5)
        recall_calc.next_to(recall_formula, DOWN, buff=0.2)
        self.play(Write(recall_formula))
        self.wait(0.5)
        self.play(Write(recall_calc))
        self.wait(1.5)
        self.play(FadeOut(recall_formula), FadeOut(recall_calc))

        # F1-Score (below table)
        f1_formula = MathTex(r"F_1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}", font_size=38)
        f1_calc = MathTex(r"= 2 \cdot \frac{0.75 \cdot 0.75}{0.75 + 0.75} = 0.75", font_size=38)
        f1_formula.next_to(cm_table, DOWN, buff=0.5)
        f1_calc.next_to(f1_formula, DOWN, buff=0.2)
        self.play(Write(f1_formula))
        self.wait(0.5)
        self.play(Write(f1_calc))
        self.wait(1.5)
        self.play(FadeOut(f1_formula), FadeOut(f1_calc))

        # Summary Table
        summary_title = Text("Summary Table", font_size=36, color=YELLOW)
        summary_table = Table([
            ["Metric", "Formula", "Value"],
            ["Accuracy", "(TP + TN) / Total", "0.80"],
            ["Precision", "TP / (TP + FP)", "0.75"],
            ["Recall", "TP / (TP + FN)", "0.75"],
            ["F1-Score", "2 × (P × R) / (P + R)", "0.75"]
        ],
            include_outer_lines=True,
            element_to_mobject_config={"font_size": 30}
        ).scale(0.85).next_to(summary_title, DOWN, buff=0.3)
        self.play(Write(summary_title))
        self.play(Create(summary_table))
        self.wait(2)
        self.play(FadeOut(summary_title), FadeOut(summary_table))

        # Choosing the right metric
        choose_title = Text("Choosing the Right Metric", font_size=36, color=WHITE)
        choose_text = Text(
            "If false positives are costly: use Precision.\nIf false negatives are dangerous: use Recall.\nIf you need balance: go for F1-Score.",
            font_size=30
        ).next_to(choose_title, DOWN, buff=0.3)
        self.play(Write(choose_title), Write(choose_text))
        self.wait(2)
        self.play(FadeOut(choose_title), FadeOut(choose_text))

        # Bonus: Specificity
        spec_title = Text("Bonus: Specificity (True Negative Rate)", font_size=34, color=BLUE)
        spec_formula = MathTex(r"\text{Specificity} = \frac{TN}{TN + FP} = \frac{50}{50 + 10} = 0.83", font_size=36).next_to(spec_title, DOWN, buff=0.2)
        spec_explain = Text("Shows how well the model detects actual negatives.", font_size=28).next_to(spec_formula, DOWN, buff=0.2)
        self.play(Write(spec_title), Write(spec_formula))
        self.play(Write(spec_explain))
        self.wait(2)
        self.play(FadeOut(spec_title), FadeOut(spec_formula), FadeOut(spec_explain), FadeOut(cm_table), FadeOut(title))
