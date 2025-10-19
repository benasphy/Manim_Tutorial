from manim import *

class LogisticRegressionHIVWorkflow(Scene):
    def construct(self):
        # Title
        title = Text("How Does Logistic Regression Work?", font_size=44, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Step explanations and visuals arranged vertically below the header
        # Place the HIV table directly under the header
        hiv_table = Table([
            ["Age", "CD4 Count", "Risk Factor", "HIV+? (Target)"],
            ["23", "550", "No", "0"],
            ["35", "200", "Yes", "1"],
            ["42", "320", "Yes", "1"],
            ["28", "700", "No", "0"],
            ["50", "180", "Yes", "1"]
        ],
            col_labels=None,
            include_outer_lines=True,
            top_left_entry=None,
            arrange_in_grid_config={"cell_alignment": RIGHT},
            element_to_mobject_config={"font_size": 28}
        ).scale(0.7)
        hiv_table.next_to(title, DOWN, buff=0.4)
        self.play(Create(hiv_table))
        self.wait(2)
        self.play(FadeOut(hiv_table))

        # Steps, each centered, with short explanations
        steps = [
            ("1. Prepare the data", YELLOW, "Each row is a patient.\nEach column is a variable.\nThe last column is HIV+? (0/1)."),
            ("2. Train the model", GREEN, "Show the table to the model.\nIt learns the best parameters\nto minimize prediction error."),
            ("3. Evaluate the model", ORANGE, "Test the model on new patients.\nCheck how well it predicts.\n(e.g. Accuracy = 90%)"),
            ("4. Make predictions", RED, "Use the trained model to predict\nHIV status for new patients.\nModel predicts: HIV+? → 1 (High risk)")
        ]
        for step, color, desc in steps:
            step_text = Text(step, font_size=38, color=color).move_to(UP*1.2)
            desc_text = Text(desc, font_size=29, color=WHITE, line_spacing=1.1).next_to(step_text, DOWN, buff=0.4)
            self.play(FadeIn(step_text), FadeIn(desc_text))
            self.wait(2)
            self.play(FadeOut(step_text), FadeOut(desc_text))
        self.play(FadeOut(title))

