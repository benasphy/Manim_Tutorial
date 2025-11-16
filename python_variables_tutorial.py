from manim import *

# Color palette
CODE_COLOR = '#2d2d2d'
KEYWORD_COLOR = YELLOW
IDENT_COLOR = '#00bfff'
STR_COLOR = '#ffa500'
ERROR_COLOR = RED
HIGHLIGHT = YELLOW

class PythonVariablesTutorial(Scene):
    def construct(self):
        # Scene 1 — Introduction
        title = Text("🐍 Python Variables — Step-by-Step Guide", font_size=54, color=WHITE)
        subtitle = Text("From basics to what happens in memory", font_size=32, color=GREY_B)
        subtitle.set_opacity(0)
        self.play(FadeIn(title))
        self.wait(0.7)
        # Typing effect for subtitle
        for i in range(1, len(subtitle.text)+1):
            subtitle.set_opacity(1)
            subtitle.text = "From basics to what happens in memory"[:i]
            self.add(subtitle.next_to(title, DOWN, buff=0.4))
            self.wait(0.04)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))

        # Scene 2 — What is a Variable?
        defn = Text("A variable is a name that refers to a value in memory.", font_size=38, color=WHITE)
        self.play(FadeIn(defn))
        self.wait(1.2)
        # Box analogy
        box = Square(side_length=1.2, color=BLUE).shift(DOWN*0.5)
        val = Text("42", font_size=44, color=YELLOW).move_to(box)
        label = Text("age", font_size=36, color=KEYWORD_COLOR).next_to(box, DOWN, buff=0.3)
        self.play(Transform(defn, label), FadeIn(box), FadeIn(val))
        self.wait(0.7)
        self.play(FadeIn(label))
        self.wait(0.7)
        # Transition to memory reference
        self.play(FadeOut(box), FadeOut(val), FadeOut(label), FadeOut(defn))
        mem_text = Text("In Python, variables point to objects in memory —\nthey don’t store values directly.", font_size=32, color=WHITE)
        self.play(FadeIn(mem_text))
        self.wait(1.2)
        # Diagram: name → object → value
        name = Text("name", font_size=34, color=KEYWORD_COLOR).shift(LEFT*3)
        arrow1 = Arrow(name.get_right(), RIGHT*0.2, buff=0.08, color=WHITE)
        obj = Rectangle(width=1.3, height=0.8, color=GREY_B).move_to(RIGHT*1)
        obj_label = Text("object", font_size=28, color=WHITE).move_to(obj)
        arrow2 = Arrow(obj.get_right(), RIGHT*3.2, buff=0.08, color=WHITE)
        val2 = Text("42", font_size=36, color=YELLOW).shift(RIGHT*4.2)
        self.play(FadeOut(mem_text), FadeIn(name), Create(arrow1), FadeIn(obj), FadeIn(obj_label))
        self.play(Create(arrow2), FadeIn(val2))
        self.wait(1.5)
        self.play(FadeOut(name), FadeOut(arrow1), FadeOut(obj), FadeOut(obj_label), FadeOut(arrow2), FadeOut(val2))

        # Scene 3 — What Happens Under the Hood?
        code1 = Code(
            code='message = "Hello Python world!"\nprint(message)',
            tab_width=4, background="window", language="python",
            font="Monospace", line_spacing=0.9, font_size=32,
            style="monokai"
        ).to_edge(UP)
        self.play(FadeIn(code1))
        self.wait(0.8)
        interp = Text("Python Interpreter Starts", font_size=32, color=KEYWORD_COLOR).next_to(code1, DOWN, buff=0.6)
        self.play(FadeIn(interp))
        self.wait(0.8)
        self.play(FadeOut(interp))
        readfile = Text("Your .py file is read line by line.", font_size=28, color=WHITE).next_to(code1, DOWN, buff=0.6)
        self.play(FadeIn(readfile))
        self.wait(0.7)
        self.play(FadeOut(readfile))
        bytecode = Text("Interpreter translates to bytecode\nfor the Python Virtual Machine (PVM)", font_size=28, color=WHITE).next_to(code1, DOWN, buff=0.6)
        self.play(FadeIn(bytecode))
        self.wait(0.9)
        self.play(FadeOut(bytecode))
        # Animate assignment
        assign = SurroundingRectangle(code1.code[0], color=HIGHLIGHT, buff=0.09)
        self.play(Create(assign))
        self.wait(0.7)
        str_obj = Rectangle(width=2.6, height=0.9, color=GREY_B).shift(DOWN*1.1+LEFT*2.5)
        str_val = Text('"Hello Python world!"', font_size=28, color=STR_COLOR).move_to(str_obj)
        self.play(FadeIn(str_obj), FadeIn(str_val))
        msg_name = Text("message", font_size=32, color=KEYWORD_COLOR).next_to(str_obj, UP, buff=0.1).shift(LEFT*0.2)
        msg_arrow = Arrow(msg_name.get_bottom(), str_obj.get_top(), buff=0.07, color=WHITE)
        self.play(FadeIn(msg_name), Create(msg_arrow))
        # Namespace dict
        ns_dict = RoundedRectangle(width=4.3, height=1.2, corner_radius=0.18, color=BLUE).shift(DOWN*2.1+RIGHT*1.7)
        ns_label = Text("namespace", font_size=22, color=KEYWORD_COLOR).next_to(ns_dict, UP, buff=0.05)
        ns_entry = Text('{ "message": <mem_addr> }', font_size=26, color=WHITE).move_to(ns_dict)
        self.play(FadeIn(ns_dict), FadeIn(ns_label), FadeIn(ns_entry))
        self.wait(1.2)
        # Animate print
        self.play(Indicate(code1.code[1], color=HIGHLIGHT))
        out_box = Rectangle(width=3.5, height=0.65, color=YELLOW).next_to(code1, DOWN, buff=1.6)
        out_txt = Text('Hello Python world!', font_size=28, color=YELLOW).move_to(out_box)
        self.play(FadeIn(out_box), FadeIn(out_txt))
        self.wait(1.2)
        self.play(FadeOut(code1), FadeOut(assign), FadeOut(str_obj), FadeOut(str_val), FadeOut(msg_name), FadeOut(msg_arrow), FadeOut(ns_dict), FadeOut(ns_label), FadeOut(ns_entry), FadeOut(out_box), FadeOut(out_txt))

        # Scene 4 — Changing a Variable’s Value
        code2 = Code(
            code='message = "Hello Python world!"\nprint(message)\n\nmessage = "Hello Python Crash Course world!"\nprint(message)',
            tab_width=4, background="window", language="python", font="Monospace", font_size=30, style="monokai"
        ).to_edge(UP)
        self.play(FadeIn(code2))
        self.wait(0.7)
        # Animate first assignment
        assign1 = SurroundingRectangle(code2.code[0], color=HIGHLIGHT, buff=0.09)
        self.play(Create(assign1))
        str_obj1 = Rectangle(width=2.6, height=0.9, color=GREY_B).shift(DOWN*1.1+LEFT*2.5)
        str_val1 = Text('"Hello Python world!"', font_size=26, color=STR_COLOR).move_to(str_obj1)
        msg_name1 = Text("message", font_size=30, color=KEYWORD_COLOR).next_to(str_obj1, UP, buff=0.1).shift(LEFT*0.2)
        msg_arrow1 = Arrow(msg_name1.get_bottom(), str_obj1.get_top(), buff=0.07, color=WHITE)
        self.play(FadeIn(str_obj1), FadeIn(str_val1), FadeIn(msg_name1), Create(msg_arrow1))
        self.wait(0.5)
        self.play(Indicate(code2.code[1], color=HIGHLIGHT))
        out_box1 = Rectangle(width=3.5, height=0.65, color=YELLOW).next_to(code2, DOWN, buff=1.6)
        out_txt1 = Text('Hello Python world!', font_size=26, color=YELLOW).move_to(out_box1)
        self.play(FadeIn(out_box1), FadeIn(out_txt1))
        self.wait(0.6)
        # Animate reassignment
        self.play(Create(SurroundingRectangle(code2.code[3], color=HIGHLIGHT, buff=0.09)))
        str_obj2 = Rectangle(width=3.5, height=0.9, color=GREY_B).shift(DOWN*1.1+RIGHT*2.2)
        str_val2 = Text('"Hello Python Crash Course world!"', font_size=26, color=STR_COLOR).move_to(str_obj2)
        msg_arrow2 = Arrow(msg_name1.get_bottom(), str_obj2.get_top(), buff=0.07, color=WHITE)
        self.play(FadeIn(str_obj2), FadeIn(str_val2), Transform(msg_arrow1, msg_arrow2))
        self.wait(0.5)
        self.play(Indicate(code2.code[4], color=HIGHLIGHT))
        out_box2 = Rectangle(width=4.7, height=0.65, color=YELLOW).next_to(code2, DOWN, buff=2.4)
        out_txt2 = Text('Hello Python Crash Course world!', font_size=26, color=YELLOW).move_to(out_box2)
        self.play(FadeIn(out_box2), FadeIn(out_txt2))
        self.wait(0.8)
        # Fade out old object (garbage collection)
        self.play(FadeOut(str_obj1), FadeOut(str_val1))
        self.wait(0.4)
        self.play(FadeOut(code2), FadeOut(msg_name1), FadeOut(msg_arrow1), FadeOut(str_obj2), FadeOut(str_val2), FadeOut(out_box1), FadeOut(out_txt1), FadeOut(out_box2), FadeOut(out_txt2))

        # Scene 5 — Rules for Naming Variables
        rules_title = Text("Rules for Naming Variables in Python", font_size=38, color=WHITE).to_edge(UP)
        rules = [
            ("Can contain letters, numbers, and underscores (_)", True, "user_age"),
            ("Must start with a letter or underscore, not a number", True, "_result"),
            ("No spaces — use _ instead", False, "user age"),
            ("Avoid Python keywords (print, for, class, etc.)", False, "print"),
            ("Keep names short but descriptive", True, "student_name"),
            ("Avoid names that look like numbers (O vs 0, l vs 1)", False, "l1 = 1"),
            ("Use lowercase for variables, uppercase for constants", True, "PI = 3.14"),
        ]
        rule_mobs = VGroup()
        for i, (rule, valid, example) in enumerate(rules):
            icon = Text("✅" if valid else "❌", font_size=30, color=GREEN if valid else ERROR_COLOR)
            rule_txt = Text(rule, font_size=28, color=WHITE if valid else ERROR_COLOR)
            ex = Text(example, font_size=28, color=KEYWORD_COLOR if valid else ERROR_COLOR)
            mob = VGroup(icon, rule_txt, ex).arrange(RIGHT, buff=0.45).shift(DOWN*0.5 + DOWN*i*0.75)
            rule_mobs.add(mob)
        self.play(FadeIn(rules_title))
        for mob in rule_mobs:
            self.play(FadeIn(mob))
            self.wait(0.3)
        self.wait(1.2)
        self.play(FadeOut(rules_title), *[FadeOut(mob) for mob in rule_mobs])

        # Scene 6 — Avoiding Name Errors
        code3 = Code(
            code='message = "Hello!"\nprint(mesage)',
            tab_width=4, background="window", language="python", font="Monospace", font_size=32, style="monokai"
        ).to_edge(UP)
        self.play(FadeIn(code3))
        self.wait(0.7)
        self.play(Indicate(code3.code[0], color=HIGHLIGHT))
        self.wait(0.3)
        self.play(Indicate(code3.code[1], color=HIGHLIGHT))
        # Error animation
        error_box = Rectangle(width=6.2, height=0.8, color=ERROR_COLOR).next_to(code3, DOWN, buff=1.1)
        error_txt = Text("NameError: name 'mesage' is not defined", font_size=28, color=ERROR_COLOR).move_to(error_box)
        self.play(FadeIn(error_box), FadeIn(error_txt))
        self.wait(0.8)
        # Magnifying glass over namespace
        ns_dict2 = RoundedRectangle(width=4.3, height=1.2, corner_radius=0.18, color=BLUE).shift(DOWN*2.1+RIGHT*1.7)
        ns_label2 = Text("namespace", font_size=22, color=KEYWORD_COLOR).next_to(ns_dict2, UP, buff=0.05)
        ns_entry2 = Text('{ "message": <mem_addr> }', font_size=26, color=WHITE).move_to(ns_dict2)
        magnifier = Circle(radius=0.5, color=YELLOW).move_to(ns_dict2.get_right()+RIGHT*0.7)
        mag_glass = VGroup(magnifier, Line(magnifier.get_top(), magnifier.get_top()+UP*0.5, color=YELLOW)).set_z_index(2)
        self.play(FadeIn(ns_dict2), FadeIn(ns_label2), FadeIn(ns_entry2))
        self.play(FadeIn(mag_glass))
        self.wait(1.2)
        self.play(FadeOut(code3), FadeOut(error_box), FadeOut(error_txt), FadeOut(ns_dict2), FadeOut(ns_label2), FadeOut(ns_entry2), FadeOut(mag_glass))

        # Scene 7 — Mental Model Recap
        recap_code = Code(
            code='a = 42',
            tab_width=4, background="window", language="python", font="Monospace", font_size=32, style="monokai"
        ).to_edge(UP)
        self.play(FadeIn(recap_code))
        self.wait(0.7)
        recap_obj = Rectangle(width=1.5, height=0.9, color=GREY_B).shift(DOWN*1.1+LEFT*1.2)
        recap_val = Text('42', font_size=36, color=YELLOW).move_to(recap_obj)
        recap_name = Text("a", font_size=32, color=KEYWORD_COLOR).next_to(recap_obj, UP, buff=0.1)
        recap_arrow = Arrow(recap_name.get_bottom(), recap_obj.get_top(), buff=0.07, color=WHITE)
        self.play(FadeIn(recap_obj), FadeIn(recap_val), FadeIn(recap_name), Create(recap_arrow))
        self.wait(0.7)
        # Diagram: name → object → value
        name2 = Text("name", font_size=34, color=KEYWORD_COLOR).shift(LEFT*3)
        arrow1b = Arrow(name2.get_right(), RIGHT*0.2, buff=0.08, color=WHITE)
        obj2 = Rectangle(width=1.3, height=0.8, color=GREY_B).move_to(RIGHT*1)
        obj_label2 = Text("object", font_size=28, color=WHITE).move_to(obj2)
        arrow2b = Arrow(obj2.get_right(), RIGHT*3.2, buff=0.08, color=WHITE)
        val2b = Text("42", font_size=36, color=YELLOW).shift(RIGHT*4.2)
        self.play(FadeIn(name2), Create(arrow1b), FadeIn(obj2), FadeIn(obj_label2))
        self.play(Create(arrow2b), FadeIn(val2b))
        self.wait(1.5)
        self.play(FadeOut(recap_code), FadeOut(recap_obj), FadeOut(recap_val), FadeOut(recap_name), FadeOut(recap_arrow), FadeOut(name2), FadeOut(arrow1b), FadeOut(obj2), FadeOut(obj_label2), FadeOut(arrow2b), FadeOut(val2b))
