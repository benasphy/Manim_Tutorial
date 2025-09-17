from manim import *

class ForLoopTutorial(Scene):
    def construct(self):
        # Scene 1: Introduction
        self.intro_scene()
        
        # Scene 2: Syntax
        self.syntax_scene()
        
        # Scene 3: Under the Hood
        self.under_the_hood_scene()
    
    def intro_scene(self):
        # Title
        title = Text("🔄 Python For Loops", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Definition
        definition = VGroup(
            Text("A loop repeats a block of code multiple times.", font_size=28),
            Text("In Python, for loops iterate over sequences.", font_size=28),
            Text("It's like a teacher taking attendance!", font_size=28, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(title, DOWN, buff=1)
        
        self.play(Write(definition[0]))
        self.wait(0.5)
        self.play(Write(definition[1]))
        self.wait(0.5)
        self.play(Write(definition[2]))
        self.wait(1)
        
        # Teacher analogy
        self.teacher_analogy()
        self.wait(2)
        self.clear()
    
    def teacher_analogy(self):
        # Create a simple teacher using basic shapes
        head = Circle(radius=0.5, color=BLUE, fill_opacity=0.5)
        body = Rectangle(height=1, width=0.8, color=BLUE, fill_opacity=0.5).next_to(head, DOWN, buff=0)
        teacher = VGroup(head, body).to_edge(LEFT)
        
        # Add a pointer (like a hand)
        pointer = Line(ORIGIN, RIGHT*1.5, color=RED, stroke_width=8, tip_length=0.2).add_tip()
        pointer.next_to(teacher, RIGHT, buff=0.1)
        teacher.add(pointer)
        
        # Create student list
        students = ["Alice", "Bob", "Charlie", "Diana"]
        student_list = VGroup(*[
            Text(f"• {name}", font_size=24) for name in students
        ]).arrange(DOWN, aligned_edge=LEFT).next_to(teacher, RIGHT, buff=2)
        
        # Create checkmarks that will appear
        checks = VGroup(*[
            Text("✓", color=GREEN, font_size=24).next_to(name, RIGHT, buff=0.5)
            for name in student_list
        ])
        
        # Show teacher and list
        self.play(Create(teacher), run_time=1.5)
        self.play(Write(student_list))
        
        # Animate checking names with pointer movement
        for i in range(len(students)):
            # Move pointer to current student
            target_pointer = pointer.copy().next_to(student_list[i], LEFT, buff=0.1)
            self.play(
                Transform(pointer, target_pointer),
                student_list[i].animate.set_color(YELLOW),
                run_time=0.5
            )
            self.play(
                FadeIn(checks[i], shift=RIGHT),
                student_list[i].animate.set_color(GREEN),
                run_time=0.5
            )
            self.wait(0.3)
        
        # Clean up
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def syntax_scene(self):
        # Title
        title = Text("📝 For Loop Syntax", font_size=42, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create code text
        code_text = '''for item in sequence:
    # code block'''
        
        # Create a background for the code
        code_bg = Rectangle(
            width=6, height=2,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=BLUE,
            stroke_width=2
        ).next_to(title, DOWN, buff=1)
        
        # Display code as text
        code_mob = Text(
            code_text,
            font="Monospace",
            font_size=24,
            color=WHITE,
            line_spacing=0.8,
            tab_width=4
        ).next_to(title, DOWN, buff=1.2)
        
        # Explanation
        explanation = VGroup(
            Text("• item: variable that takes each value", font_size=24, color=YELLOW),
            Text("• sequence: collection to loop through", font_size=24, color=YELLOW),
            Text("• Indented code runs for each item", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).to_edge(DOWN, buff=1)
        
        # Animation
        self.play(Create(code_bg), Write(code_mob))
        self.wait(1)
        
        # Create highlight boxes for different parts using Rectangle
        # For 'for' keyword
        for_highlight = Rectangle(
            width=1.7, height=0.7,
            color=BLUE,
            stroke_width=2,
            fill_opacity=0.2
        ).move_to(code_mob.get_corner(UL) + RIGHT * 1.0 + DOWN * 0.35)
        
        # For 'in' keyword
        in_highlight = Rectangle(
            width=1.0, height=0.7,
            color=GREEN,
            stroke_width=2,
            fill_opacity=0.2
        ).move_to(code_mob.get_corner(UL) + RIGHT * 2.8 + DOWN * 0.35)
        
        # For 'sequence' part
        sequence_highlight = Rectangle(
            width=4.0, height=0.7,
            color=YELLOW,
            stroke_width=2,
            fill_opacity=0.2
        ).move_to(code_mob.get_corner(UL) + RIGHT * 5.8 + DOWN * 0.35)
        
        # Animate the highlights
        self.play(Create(for_highlight))
        self.wait(0.5)
        self.play(ReplacementTransform(for_highlight, in_highlight))
        self.wait(0.5)
        self.play(ReplacementTransform(in_highlight, sequence_highlight))
        self.wait(0.5)
        
        # Clean up the last highlight
        self.play(FadeOut(sequence_highlight))
        
        # Show explanation
        self.play(Write(explanation[0]))
        self.play(Write(explanation[1]))
        self.play(Write(explanation[2]))
        
        # Example with numbers
        numbers_example = VGroup(
            Text("Example:", font_size=28, color=WHITE).to_edge(LEFT, buff=2),
            Text(
                '''numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num * 2)''',
                font="Monospace",
                font_size=20,
                color=WHITE,
                line_spacing=0.8,
                tab_width=4
            ).next_to(title, DOWN, buff=4).to_edge(LEFT, buff=2)
        )
        
        output = Text("2\n4\n6\n8\n10", font="Monospace", color=GREEN, font_size=20)
        output.next_to(numbers_example[1], RIGHT, buff=1)
        
        self.play(Write(numbers_example[0]))
        self.play(Write(numbers_example[1]))
        self.wait(1)
        self.play(Write(output))
        
        self.wait(3)
        self.clear()
    
    def under_the_hood_scene(self):
        # Scene 1: Iterator Explanation
        self.iterator_explanation()
        
        # Scene 2: Music Playlist Analogy
        self.playlist_analogy()
        
        # Scene 3: Visual Iteration Demo
        self.visual_iteration_demo()
        
        # Final message
        self.show_final_message()
    
    def iterator_explanation(self):
        # Title
        title = Text("🔧 Under the Hood: Iterators", font_size=42, color=ORANGE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Explanation
        explanation = VGroup(
            Text("Python's for loop uses iterators:", font_size=28, color=YELLOW),
            Text("1. iter(sequence) creates an iterator", font_size=24, color=WHITE),
            Text("2. next(iterator) gets the next item", font_size=24, color=WHITE),
            Text("3. Raises StopIteration when done", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(title, DOWN, buff=1)
        
        # Code demonstration
        code_text = '''# What actually happens:
iterator = iter([1, 2, 3])
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# next(iterator)  # Raises StopIteration'''

        # Create a background for the code
        code_bg = Rectangle(
            width=6, height=4,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=BLUE,
            stroke_width=2
        ).to_edge(RIGHT, buff=1)
        
        # Display code as text
        code_mob = Text(
            code_text,
            font="Monospace",
            font_size=16,
            color=WHITE,
            line_spacing=0.8,
            tab_width=4
        ).scale(0.9).to_edge(RIGHT, buff=1.2)
        
        # Add a title for the code block
        code_title = Text("How it works:", font_size=20, color=YELLOW).next_to(code_bg, UP, buff=0.2)
        
        # Show explanation and code
        self.play(Write(explanation[0]))
        self.wait(0.5)
        self.play(Write(explanation[1:]))
        
        # Show code block
        self.play(
            Create(code_bg),
            Write(code_title),
            Write(code_mob)
        )
        self.wait(3)
        
        # Clean up for next scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def playlist_analogy(self):
        # Title
        title = Text("🎵 Music Playlist Analogy", font_size=42, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create a simple music player visualization
        player = RoundedRectangle(
            width=6, height=3,
            color=WHITE,
            fill_color="#333333",
            fill_opacity=1,
            corner_radius=0.5
        ).scale(0.8)
        
        screen = RoundedRectangle(
            width=5, height=1.5,
            color=WHITE,
            fill_color="#000000",
            fill_opacity=1,
            corner_radius=0.3
        ).next_to(player, UP, buff=0.2)
        
        # Song list
        songs = ["1. Sweet Child O' Mine", "2. Bohemian Rhapsody", "3. Stairway to Heaven"]
        song_texts = VGroup(*[
            Text(song, font_size=18, color=WHITE) for song in songs
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(screen)
        
        # Controls
        play_button = Circle(radius=0.4, color=GREEN, fill_opacity=0.5)
        next_button = Circle(radius=0.4, color=BLUE, fill_opacity=0.5).next_to(play_button, RIGHT, buff=0.5)
        
        play_icon = Text("▶", font_size=24, color=WHITE).move_to(play_button)
        next_icon = Text("⏭", font_size=24, color=WHITE).move_to(next_button)
        
        controls = VGroup(play_button, next_button, play_icon, next_icon).next_to(screen, DOWN, buff=0.5)
        
        # Show player
        self.play(Create(player), Create(screen))
        self.play(Write(song_texts))
        self.play(Create(controls))
        
        # Highlight first song
        highlight = SurroundingRectangle(song_texts[0], color=YELLOW, buff=0.2, corner_radius=0.1)
        self.play(Create(highlight))
        
        # Animate next button press
        self.play(
            next_button.animate.set_fill(BLUE, 0.8),
            next_icon.animate.scale(1.2),
            run_time=0.5
        )
        self.play(
            next_button.animate.set_fill(BLUE, 0.5),
            next_icon.animate.scale(1/1.2),
            highlight.animate.move_to(song_texts[1])
        )
        
        # Show end of playlist
        self.play(
            next_button.animate.set_fill(BLUE, 0.8),
            next_icon.animate.scale(1.2),
            run_time=0.5
        )
        self.play(
            next_button.animate.set_fill(BLUE, 0.5),
            next_icon.animate.scale(1/1.2),
            highlight.animate.move_to(song_texts[2])
        )
        
        # Show end of playlist
        end_text = Text("End of Playlist", color=RED, font_size=20).next_to(controls, DOWN, buff=1)
        self.play(
            next_button.animate.set_fill(RED, 0.8),
            next_icon.animate.scale(1.2),
            run_time=0.5
        )
        self.play(
            next_button.animate.set_fill(RED, 0.5),
            next_icon.animate.scale(1/1.2),
            FadeIn(end_text)
        )
        
        # Analogy explanation
        analogy = VGroup(
            Text("This is similar to Python's iteration:", font_size=24, color=YELLOW).to_edge(DOWN, buff=1),
            Text("• iter() = Start playing the playlist", font_size=20, color=WHITE),
            Text("• next() = Press 'Next' to play the next song", font_size=20, color=WHITE),
            Text("• StopIteration = End of playlist", font_size=20, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(end_text, DOWN, buff=0.8)
        
        self.play(Write(analogy[0]))
        self.play(Write(analogy[1:]))
        
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def visual_iteration_demo(self):
        # Title
        title = Text("🔍 Visualizing Iteration", font_size=42, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create a list of items
        items = ["Apple", "Banana", "Cherry"]
        item_boxes = VGroup(*[
            RoundedRectangle(
                width=2, height=1,
                color=YELLOW,
                fill_color=BLUE,
                fill_opacity=0.3,
                corner_radius=0.2
            ) for _ in items
        ]).arrange(RIGHT, buff=0.5).shift(UP)
        
        item_texts = VGroup(*[
            Text(item, font_size=24, color=WHITE).move_to(box) 
            for item, box in zip(items, item_boxes)
        ])
        
        # Create iterator and pointer
        iterator_code = Text("fruits = ['Apple', 'Banana', 'Cherry']\niter_fruits = iter(fruits)",
                           font="Monospace", font_size=20, color=WHITE)
        pointer = Triangle(color=RED, fill_opacity=1).scale(0.2).rotate(-PI/2)
        
        # Position elements
        iterator_code.to_edge(LEFT, buff=1)
        item_boxes.next_to(title, DOWN, buff=1.5)
        pointer.next_to(item_boxes[0], DOWN, buff=0.5)
        
        # Show initial setup
        self.play(Write(iterator_code))
        self.play(Create(item_boxes), Write(item_texts))
        self.play(GrowFromCenter(pointer))
        
        # Animate iteration
        for i in range(len(items)):
            # Highlight current item
            self.play(
                item_boxes[i].animate.set_fill(YELLOW, 0.5),
                item_texts[i].animate.set_color(BLACK).set_stroke(WHITE, 0.5, background=True),
                pointer.animate.next_to(item_boxes[i], DOWN, buff=0.5)
            )
            
            # Show next() call
            next_call = Text(f"next(iter_fruits)  # Returns: '{items[i]}'",
                           font="Monospace", font_size=20, color=YELLOW)
            next_call.next_to(iterator_code, DOWN, buff=1).to_edge(LEFT, buff=1)
            
            self.play(Write(next_call))
            self.wait(0.5)
            
            if i < len(items) - 1:
                self.play(FadeOut(next_call))
        
        # Show StopIteration
        stop_text = Text("StopIteration", color=RED, font_size=24)
        stop_arrow = Arrow(pointer.get_bottom(), stop_text.get_top(), color=RED)
        
        self.play(
            pointer.animate.shift(RIGHT * 2.5).set_color(RED),
            GrowArrow(stop_arrow),
            Write(stop_text.next_to(stop_arrow.get_end(), DOWN))
        )
        
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def show_final_message(self):
        final = Text("Now you understand Python for loops! 🎉", font_size=36, color=GREEN)
        self.play(Write(final))
        self.wait(2)
        self.clear()

# Simple teacher class using basic shapes
class Teacher(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Head
        head = Circle(radius=0.5, color=BLUE, fill_opacity=0.5)
        # Body
        body = Rectangle(height=1, width=0.8, color=BLUE, fill_opacity=0.5).next_to(head, DOWN, buff=0)
        # Pointer (hand)
        pointer = Line(ORIGIN, RIGHT*1.5, color=RED, stroke_width=8, tip_length=0.2).add_tip()
        pointer.next_to(body, RIGHT, buff=0.1)
        
        self.add(head, body, pointer)
