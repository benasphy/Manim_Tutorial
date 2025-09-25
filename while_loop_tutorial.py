from manim import *

class WhileLoopTutorial(Scene):
    def construct(self):
        # Scene 1: Introduction
        self.intro_scene()
        
        # Scene 2: Syntax
        self.syntax_scene()
        
        # Scene 3: Under the Hood
        self.under_the_hood_scene()
    
    def intro_scene(self):
        # Title
        title = Text("🔄 Python While Loops", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Definition
        definition = VGroup(
            Text("A while loop repeats code while a condition is True.", font_size=28, color=WHITE),
            Text("Unlike for loops, while loops are condition-based, not sequence-based.", font_size=28, color=YELLOW),
            Text("This makes them flexible but requires careful handling!", font_size=28, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(title, DOWN, buff=1)
        
        self.play(Write(definition[0]))
        self.wait(0.5)
        self.play(Write(definition[1:]))
        
        # Water bottle analogy
        self.water_bottle_analogy()
        self.wait(2)
        self.clear()
    
    def water_bottle_analogy(self):
        # Create bottle outline
        bottle_outline = Rectangle(height=3, width=2, color=BLUE, stroke_width=3)
        
        # Create water level (starts empty)
        water_level = Rectangle(
            height=0, 
            width=1.9, 
            color=BLUE, 
            fill_opacity=0.5, 
            stroke_width=0
        ).align_to(bottle_outline, DOWN).set_y(bottle_outline.get_bottom()[1])
        
        # Group bottle components
        bottle = VGroup(bottle_outline, water_level)
        
        # Bottle neck
        neck = Rectangle(height=1, width=1, color=BLUE, stroke_width=3)\
            .next_to(bottle_outline, UP, buff=0)
        
        # Water stream
        water_stream = VGroup(
            Line(UP*0.5, UP*1.5, color=BLUE_E, stroke_width=6),
            Line(UP*0.5, UP*1.5, color=BLUE_E, stroke_width=4).shift(LEFT*0.3),
            Line(UP*0.5, UP*1.5, color=BLUE_E, stroke_width=4).shift(RIGHT*0.3)
        ).next_to(neck, UP, buff=0)
        
        # Full indicator
        full_text = Text("FULL", color=GREEN, font_size=24).next_to(bottle, RIGHT, buff=1)
        full_arrow = Arrow(bottle.get_right(), full_text.get_left(), buff=0.2, color=GREEN)
        
        # Initial setup
        self.play(Create(bottle), Create(neck))
        
        # Fill animation
        self.play(
            water_stream.animate.shift(UP * 0.5),
            run_time=0.5
        )
        
        for i in range(1, 4):  # Fill in 3 steps
            new_water = bottle[1].copy()
            new_water.set_height(i)
            new_water.align_to(bottle[0], DOWN)
            
            self.play(
                Transform(bottle[1], new_water),
                water_stream.animate.shift(UP * 0.1),
                run_time=0.7
            )
        
        # Show full
        self.play(
            FadeOut(water_stream),
            Write(full_text),
            GrowArrow(full_arrow)
        )
        
        # Explanation
        analogy = VGroup(
            Text("Water Bottle Analogy:", font_size=24, color=YELLOW),
            Text("• While (bottle is not full):", font_size=20, color=WHITE),
            Text("  • Keep pouring water", font_size=20, color=WHITE),
            Text("• When full → Stop pouring", font_size=20, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(DOWN, buff=1)
        
        self.play(Write(analogy[0]))
        self.play(Write(analogy[1:]))
        
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def syntax_scene(self):
        # Title
        title = Text("📝 While Loop Syntax", font_size=42, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Code example
        code_text = '''# Basic while loop
count = 0
while count < 5:    # Condition
    print(count)     # Code block
    count += 1       # Update condition'''
        
        # Create a background for the code
        code_bg = Rectangle(
            width=8, height=4,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=GREEN,
            stroke_width=2
        ).next_to(title, DOWN, buff=1)
        
        # Display code as text with syntax highlighting
        code_mob = Text(
            code_text,
            font="Monospace",
            font_size=20,
            color=WHITE,
            line_spacing=0.8,
            t2c={
                "while": BLUE,
                "print": YELLOW,
                "count": "#FF8C42"
            }
        ).scale(0.9).next_to(title, DOWN, buff=1.5)
        
        # Add a title for the code block
        code_title = Text("Basic While Loop:", font_size=24, color=YELLOW).next_to(code_bg, UP, buff=0.2)
        
        # Show code block
        self.play(
            Create(code_bg),
            Write(code_title),
            Write(code_mob)
        )
        
        # Explanation
        explanation = VGroup(
            Text("Key Components:", font_size=26, color=YELLOW).to_edge(LEFT, buff=2),
            Text("1. while keyword", font_size=22, color=WHITE),
            Text("2. Condition (must evaluate to True/False)", font_size=22, color=WHITE),
            Text("3. Colon (:)", font_size=22, color=WHITE),
            Text("4. Indented code block", font_size=22, color=WHITE),
            Text("5. Update condition (to avoid infinite loops!)", font_size=22, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(LEFT, buff=3).shift(UP*0.5)
        
        # Create separate text objects for highlighting
        while_text = Text("while", font="Monospace", font_size=20, color=BLUE).move_to(code_mob)
        condition_text = Text("count < 5", font="Monospace", font_size=20, color=GREEN).next_to(while_text, RIGHT, buff=0.1)
        colon_text = Text(":", font="Monospace", font_size=20, color=YELLOW).next_to(condition_text, RIGHT, buff=0.1)
        
        # Create highlights using the text objects
        highlights = [
            SurroundingRectangle(while_text, color=BLUE, buff=0.1, corner_radius=0.1),
            SurroundingRectangle(condition_text, color=GREEN, buff=0.1, corner_radius=0.1),
            SurroundingRectangle(colon_text, color=YELLOW, buff=0.1, corner_radius=0.1),
            SurroundingRectangle(code_mob[1], color=ORANGE, buff=0.1, corner_radius=0.1),  # print line
            SurroundingRectangle(code_mob[2], color=BLUE_C, buff=0.1, corner_radius=0.1)      # count line
        ]
        
        # Animate highlights and explanations
        for i, (highlight, exp) in enumerate(zip(highlights, explanation[1:])):
            self.play(Create(highlight))
            self.play(Write(exp))
            self.wait(0.5)
            if i < len(highlights) - 1:  # Keep the last highlight
                self.play(FadeOut(highlight))
        
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def under_the_hood_scene(self):
        # Scene 1: Condition Checking
        self.condition_checking()
        
        # Scene 2: Water Bottle Example
        self.water_bottle_example()
        
        # Scene 3: Guard Analogy
        self.guard_analogy()
        
        # Final message
        self.show_final_message()
    
    def condition_checking(self):
        # Title
        title = Text("🔄 How While Loops Work", font_size=42, color=ORANGE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Code example
        code_text = '''count = 0
while count < 3:    # Condition check
    print(count)     # Code block
    count += 1       # Update'''
        
        # Create a background for the code
        code_bg = Rectangle(
            width=7, height=4,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=BLUE,
            stroke_width=2
        ).to_edge(LEFT, buff=1)
        
        # Display code as text with syntax highlighting
        code_mob = Text(
            code_text,
            font="Monospace",
            font_size=20,
            color=WHITE,
            line_spacing=0.8,
            t2c={"while": BLUE, "print": YELLOW, "count": "#FF8C42"}
        ).scale(0.9).to_edge(LEFT, buff=1.5)
        
        # Execution flow
        flow = VGroup(
            Text("1. Check condition (count < 3)", font_size=22, color=YELLOW),
            Text("2. If True: execute code block", font_size=22, color=GREEN),
            Text("3. Update variables (count += 1)", font_size=22, color=BLUE_C),
            Text("4. Go back to step 1", font_size=22, color=YELLOW),
            Text("5. If False: exit loop", font_size=22, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).to_edge(RIGHT, buff=2)
        
        # Show code and flow
        self.play(
            Create(code_bg),
            Write(code_mob)
        )
        
        # Animate execution flow
        for i, step in enumerate(flow):
            self.play(Write(step), run_time=0.8)
            
            # Highlight relevant part of code
            if i == 0:  # Check condition
                highlight = SurroundingRectangle(code_mob[1][6:19], color=YELLOW, buff=0.1)
            elif i == 1:  # Execute block
                highlight = SurroundingRectangle(code_mob[2:4], color=GREEN, buff=0.1)
            elif i == 2:  # Update
                highlight = SurroundingRectangle(code_mob[3][4:13], color=BLUE_C, buff=0.1)
            elif i == 3:  # Loop back
                highlight = SurroundingRectangle(code_mob[1], color=YELLOW, buff=0.1)
            else:  # Exit
                highlight = SurroundingRectangle(code_mob[1][6:19], color=RED, buff=0.1)
            
            self.play(Create(highlight), run_time=0.5)
            self.wait(0.5)
            self.play(FadeOut(highlight))
        
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def water_bottle_example(self):
        # Title
        title = Text("💧 Water Bottle Example", font_size=42, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create bottle outline and water level separately
        bottle_outline = Rectangle(height=3, width=2, color=BLUE, stroke_width=3)
        water_level = Rectangle(
            height=0, 
            width=1.9, 
            color=BLUE, 
            fill_opacity=0.5, 
            stroke_width=0
        ).align_to(bottle_outline, DOWN).set_y(bottle_outline.get_bottom()[1])
        
        # Group them together
        bottle = VGroup(bottle_outline, water_level)
        
        # Add neck
        neck = Rectangle(height=1, width=1, color=BLUE, stroke_width=3).next_to(bottle_outline, UP, buff=0)
        
        # Water stream
        water_stream = VGroup(
            Line(UP*0.5, UP*1.5, color=BLUE_E, stroke_width=6),
            Line(UP*0.5, UP*1.5, color=BLUE_E, stroke_width=4).shift(LEFT*0.3),
            Line(UP*0.5, UP*1.5, color=BLUE_E, stroke_width=4).shift(RIGHT*0.3)
        ).next_to(neck, UP, buff=0)
        
        # Code
        code_text = '''water_level = 0
bottle_capacity = 3

while water_level < bottle_capacity:
    print(f"Adding water... {water_level+1}/{bottle_capacity}")
    water_level += 1
    # Animate water filling here

print("Bottle is full!")'''
        
        code_bg = Rectangle(
            width=7, height=5,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=GREEN,
            stroke_width=2
        ).to_edge(RIGHT, buff=1)
        
        code_mob = Text(
            code_text,
            font="Monospace",
            font_size=16,
            color=WHITE,
            line_spacing=0.9,
            t2c={"while": BLUE, "print": YELLOW, "water_level": "#FF8C42", "bottle_capacity": "#FF8C42"}
        ).scale(0.8).to_edge(RIGHT, buff=1.5)
        
        # Show bottle and code
        self.play(Create(bottle), Create(neck))
        self.play(
            Create(code_bg),
            Write(code_mob)
        )
        
        # Animate filling
        water_level = 0
        bottle_capacity = 3
        
        while water_level < bottle_capacity:
            # Show water stream
            self.play(
                water_stream.animate.shift(UP * 0.5),
                run_time=0.3
            )
            
            # Increase water level
            new_water = bottle[1].copy()
            new_height = (water_level + 1) * (bottle[0].height / bottle_capacity)
            new_water.stretch_to_fit_height(new_height)
            new_water.align_to(bottle[0], DOWN)
            
            self.play(
                Transform(bottle[1], new_water),
                water_stream.animate.shift(UP * 0.1),
                run_time=0.7
            )
            
            # Highlight current line in code
            highlight = SurroundingRectangle(
                code_mob[3 + water_level],
                color=YELLOW,
                buff=0.1,
                corner_radius=0.1
            )
            
            self.play(Create(highlight), run_time=0.5)
            self.play(FadeOut(highlight), run_time=0.3)
            
            water_level += 1
        
        # Show full
        full_text = Text("Bottle is full!", color=GREEN, font_size=24).next_to(bottle, DOWN, buff=0.5)
        self.play(
            FadeOut(water_stream),
            Write(full_text)
        )
        
        # Highlight final print statement
        highlight = SurroundingRectangle(
            code_mob[8],
            color=GREEN,
            buff=0.1,
            corner_radius=0.1
        )
        self.play(Create(highlight))
        
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def guard_analogy(self):
        # Title
        title = Text("👮 Guard at the Door Analogy", font_size=42, color=PURPLE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create door and guard
        door = RoundedRectangle(
            height=4, width=2,
            color=WHITE,
            fill_color="#8B4513",
            fill_opacity=1,
            corner_radius=0.2
        )
        
        # Create a simple stick figure guard
        head = Circle(radius=0.2, color=BLUE, fill_opacity=1)
        body = Line(ORIGIN, DOWN * 0.5, color=BLUE, stroke_width=4)
        left_arm = Line(ORIGIN, LEFT * 0.5, color=BLUE, stroke_width=4)
        right_arm = Line(ORIGIN, RIGHT * 0.5, color=BLUE, stroke_width=4)
        left_leg = Line(ORIGIN, LEFT * 0.3 + DOWN * 0.5, color=BLUE, stroke_width=4)
        right_leg = Line(ORIGIN, RIGHT * 0.3 + DOWN * 0.5, color=BLUE, stroke_width=4)
        
        # Group all parts together
        guard = VGroup(head, body, left_arm, right_arm, left_leg, right_leg)
        guard.scale(0.8).next_to(door, RIGHT, buff=1)
        
        # Position the body parts relative to head
        body.next_to(head, DOWN, buff=0)
        left_arm.next_to(body.get_top(), LEFT, buff=0)
        right_arm.next_to(body.get_top(), RIGHT, buff=0)
        left_leg.next_to(body.get_bottom(), LEFT/2, buff=0)
        right_leg.next_to(body.get_bottom(), RIGHT/2, buff=0)
        
        # Create an arm for the guard to raise
        guard_arm = Line(
            body.get_top() + LEFT*0.2,
            body.get_top() + LEFT*1.0,
            color=BLUE,
            stroke_width=4
        )
        
        # Function to create a simple stick figure
        def create_stick_figure(color=BLUE, scale=1.0):
            head = Circle(radius=0.2 * scale, color=color, fill_opacity=1)
            body = Line(ORIGIN, DOWN * 0.5 * scale, color=color, stroke_width=4 * scale)
            left_arm = Line(ORIGIN, LEFT * 0.3 * scale, color=color, stroke_width=4 * scale)
            right_arm = Line(ORIGIN, RIGHT * 0.3 * scale, color=color, stroke_width=4 * scale)
            left_leg = Line(ORIGIN, LEFT * 0.2 * scale + DOWN * 0.4 * scale, color=color, stroke_width=4 * scale)
            right_leg = Line(ORIGIN, RIGHT * 0.2 * scale + DOWN * 0.4 * scale, color=color, stroke_width=4 * scale)
            
            figure = VGroup(head, body, left_arm, right_arm, left_leg, right_leg)
            
            # Position the parts
            body.next_to(head, DOWN, buff=0)
            left_arm.next_to(body.get_top(), LEFT, buff=0)
            right_arm.next_to(body.get_top(), RIGHT, buff=0)
            left_leg.next_to(body.get_bottom(), LEFT/3, buff=0)
            right_leg.next_to(body.get_bottom(), RIGHT/3, buff=0)
            
            return figure
        
        # Create people waiting in line
        people = VGroup(*[
            create_stick_figure(color=color, scale=0.5)
            for color in [RED, GREEN, YELLOW, ORANGE]
        ]).arrange(DOWN, buff=0.5).to_edge(LEFT, buff=2)
        
        # Condition check
        condition_text = Text("Condition: Has ticket?", font_size=24, color=YELLOW)
        condition_box = SurroundingRectangle(condition_text, color=YELLOW, buff=0.3)
        condition = VGroup(condition_box, condition_text).next_to(guard, UP, buff=1)
        
        # Show scene
        self.play(Create(door), Create(guard), Create(guard_arm))
        self.play(Write(people))
        self.play(Write(condition))
        
        # Animate people going through
        for i, person in enumerate(people):
            # Person moves to guard
            self.play(
                person.animate.next_to(guard_arm.get_end(), LEFT, buff=0.2),
                run_time=0.7
            )
            
            # Guard checks condition
            check_text = Text("Checking...", font_size=20, color=YELLOW).next_to(condition, UP, buff=0.5)
            self.play(Write(check_text))
            
            if i < len(people) - 1:  # Let all but last person through
                # Condition is True
                result_text = Text("✅ Allowed", font_size=20, color=GREEN).move_to(check_text)
                self.play(Transform(check_text, result_text))
                
                # Person enters
                self.play(
                    person.animate.next_to(door, RIGHT, buff=0.2).set_opacity(0.5),
                    FadeOut(check_text)
                )
            else:
                # Last person gets rejected
                result_text = Text("❌ No ticket!", font_size=20, color=RED).move_to(check_text)
                self.play(Transform(check_text, result_text))
                self.wait(0.5)
                
                # Show loop ends
                stop_text = Text("Loop ends here!", font_size=24, color=RED).to_edge(DOWN, buff=1)
                self.play(Write(stop_text))
                self.wait(1)
                self.play(FadeOut(check_text), FadeOut(stop_text))
        
        # Explanation
        explanation = VGroup(
            Text("Guard Analogy:", font_size=26, color=YELLOW),
            Text("• while (person has ticket):", font_size=22, color=WHITE),
            Text("  • Let them in", font_size=22, color=GREEN),
            Text("• When no ticket → Stop", font_size=22, color=RED),
            Text("• Just like a while loop's condition!", font_size=22, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(DOWN, buff=1)
        
        self.play(Write(explanation[0]))
        self.play(Write(explanation[1:]))
        
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def show_final_message(self):
        final = Text("Now you understand Python while loops! 🎉", font_size=36, color=GREEN)
        self.play(Write(final))
        self.wait(2)
        self.clear()

# For the person SVG (fallback if not available)
class Person(Circle):
    def __init__(self, **kwargs):
        super().__init__(radius=0.5, color=WHITE, fill_opacity=1, **kwargs)
