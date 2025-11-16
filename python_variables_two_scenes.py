from manim import *

PRIMARY = BLUE
ACCENT = YELLOW
GOOD = GREEN
WARN = ORANGE

class PythonVariablesTwoScenes(Scene):
    def construct(self):
        # Scene 1 — What is a Variable?
        title1 = Text("1️⃣ What is a Variable in Python?", font_size=46, color=PRIMARY)
        subtitle1 = Text(
            "A variable is a name (label) that refers to a value stored in memory.",
            font_size=30,
            color=WHITE,
        )
        self.play(FadeIn(title1))
        self.play(title1.animate.to_edge(UP))
        self.play(FadeIn(subtitle1.next_to(title1, DOWN, buff=0.4)))
        self.wait(0.6)

        # Box/Label analogy
        box = RoundedRectangle(width=2.6, height=1.5, corner_radius=0.15, color=PRIMARY)
        box_value = Text("42", font_size=50, color=ACCENT).move_to(box)
        name_label = Text("age", font_size=36, color=GOOD)
        name_tag = RoundedRectangle(width=1.6, height=0.6, corner_radius=0.15, color=GOOD).next_to(box, DOWN, buff=0.3)
        name_group = VGroup(name_tag, name_label.move_to(name_tag))

        helper = Text("Think: label on a box — the box holds the data, the label names it.", font_size=26)
        helper.next_to(name_group, DOWN, buff=0.5)

        self.play(FadeIn(box), FadeIn(box_value))
        self.play(FadeIn(name_group))
        self.play(Write(helper))
        self.wait(1.0)

        # Transition statement
        stmt = Text(
            "In Python, variables point to objects in memory (not raw bytes).",
            font_size=28,
            color=WHITE,
        ).to_edge(DOWN)
        self.play(FadeIn(stmt))
        self.wait(1.0)
        self.play(*map(FadeOut, [box, box_value, name_group, helper, subtitle1, stmt]))

        # Scene 2 — Under the Hood: age = 25
        title2 = Text("2️⃣ Under the Hood — What Really Happens", font_size=44, color=PRIMARY)
        self.play(ReplacementTransform(title1, title2))
        self.play(title2.animate.to_edge(UP))

        # Stylized code line (avoid Code() for compatibility)
        code_bg = RoundedRectangle(width=8.6, height=1.2, corner_radius=0.2, color=GREY_B)
        code_bg.set_fill(GREY_E, opacity=0.4)
        code_text = Text("age = 25", font_size=36, color=WHITE)
        code_line = VGroup(code_bg, code_text.move_to(code_bg)).next_to(title2, DOWN, buff=0.5)
        self.play(FadeIn(code_line))
        self.wait(0.3)

        # Step banner utility
        def step_banner(text, color=WHITE):
            banner = RoundedRectangle(width=9.6, height=0.9, corner_radius=0.15, color=color)
            banner.set_fill(color, opacity=0.12)
            label = Text(text, font_size=28, color=color)
            group = VGroup(banner, label.move_to(banner)).next_to(code_line, DOWN, buff=0.5)
            return group

        # Step 1: Create the object (int 25)
        step1 = step_banner("Create the object → an integer with value 25 in memory", color=GOOD)
        self.play(FadeIn(step1))
        int_obj = RoundedRectangle(width=2.8, height=1.4, corner_radius=0.15, color=WHITE)
        int_obj.set_fill(color=BLACK, opacity=0.4)
        int_val = Text("25", font_size=44, color=ACCENT).move_to(int_obj)
        int_badge = RoundedRectangle(width=1.0, height=0.5, corner_radius=0.12, color=GOOD)
        int_badge.set_fill(GREEN_E, opacity=0.6)
        int_label = Text("int object", font_size=20, color=WHITE).move_to(int_badge)
        badge_group = VGroup(int_badge, int_label).next_to(int_obj, UP, buff=0.15)
        # Move the entire object group much lower to prevent overlap with banner
        obj_group = VGroup(int_obj, int_val, badge_group).shift(LEFT*3 + DOWN*2.0)
        glow = SurroundingRectangle(int_obj, color=ACCENT, buff=0.08)
        glow.set_stroke(width=3)
        self.play(FadeIn(obj_group))
        self.play(Create(glow), run_time=0.35)
        self.wait(0.4)
        self.play(FadeOut(glow))

        # Step 2: Assign a reference (name → object)
        step2 = step_banner("Assign a reference → name 'age' points to that object", color=YELLOW)
        self.play(ReplacementTransform(step1, step2))
        name_tag2 = RoundedRectangle(width=1.8, height=0.7, corner_radius=0.15, color=YELLOW)
        name_tag2.set_fill(color=YELLOW_E, opacity=0.6)
        name_text2 = Text("age", font_size=32, color=BLACK).move_to(name_tag2)
        name_group2 = VGroup(name_tag2, name_text2).shift(LEFT*0.3 + DOWN*0.2)
        arrow_ref = Arrow(name_group2.get_left(), int_obj.get_right(), buff=0.12, color=YELLOW)
        self.play(FadeIn(name_group2))
        self.play(Create(arrow_ref))
        self.wait(0.5)

        # Step 3: Dynamic typing highlight
        step3 = step_banner(
            "Dynamic typing → Python infers type when you assign a value",
            color=WARN,
        )
        self.play(ReplacementTransform(step2, step3))
        # Show type badge near the name
        type_badge = RoundedRectangle(width=1.3, height=0.55, corner_radius=0.12, color=WARN)
        type_badge.set_fill(ORANGE, opacity=0.6)
        type_text = Text("type: int", font_size=22, color=BLACK).move_to(type_badge)
        type_group = VGroup(type_badge, type_text).next_to(name_group2, DOWN, buff=0.2)
        self.play(FadeIn(type_group))
        self.wait(0.6)

        # new object (str)
        str_obj = RoundedRectangle(width=3.6, height=1.4, corner_radius=0.15, color=WHITE)
        str_obj.set_fill(color=BLACK, opacity=0.4)
        str_val = Text("'twenty-five'", font_size=32, color=ACCENT).move_to(str_obj)
        str_badge = RoundedRectangle(width=1.2, height=0.5, corner_radius=0.12, color=GOOD)
        str_badge.set_fill(GREEN_E, opacity=0.6)
        str_label = Text("str object", font_size=20, color=WHITE).move_to(str_badge)
        str_group = VGroup(str_obj, str_val, VGroup(str_badge, str_label).next_to(str_obj, UP, buff=0.15)).shift(RIGHT*3.5 + DOWN*2.0)
        # rebind arrow
        arrow_rebind = Arrow(name_group2.get_right(), str_obj.get_left(), buff=0.12, color=YELLOW)
        self.play(FadeIn(str_group))
        self.play(Transform(arrow_ref, arrow_rebind))
        # type morph
        new_type_badge = type_badge.copy()
        new_type_text = Text("type: str", font_size=22, color=BLACK).move_to(new_type_badge)
        new_type_group = VGroup(new_type_badge, new_type_text).move_to(type_group)
        self.play(Transform(type_group, new_type_group))
        self.wait(0.8)

        # Clean end state
        outro = VGroup(title2, code_line, step3, name_group2, type_group, obj_group, str_group, arrow_ref)
        self.play(*[FadeOut(m) for m in outro])
        self.wait(0.2)

