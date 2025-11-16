from manim import *

class PythonSetsTutorial(Scene):
    def construct(self):
        # Scene 1 — What is a Set?
        title = Text("1️⃣ What is a Set in Python?", font_size=42, color=BLUE)
        definition = Text(
            "An unordered collection of unique elements\n"
            "No duplicates allowed, order doesn't matter",
            font_size=28,
            color=WHITE,
            line_spacing=1.2
        )
        
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.play(Write(definition.next_to(title, DOWN, buff=0.5)))
        
        # Bag of items analogy
        bag = Ellipse(width=3, height=4, color=YELLOW, fill_opacity=0.1)
        bag_label = Text("Bag of Items", font_size=24, color=YELLOW).next_to(bag, DOWN)
        
        items = []
        colors = ["#FF6B6B", "#6BCB77", "#4D96FF", "#9772FB"]
        for i, (char, color) in enumerate(zip("ABCD", colors)):
            item = Circle(radius=0.3, color=color, fill_opacity=0.8)
            text = Text(char, font_size=20, color=WHITE).move_to(item)
            items.append(VGroup(item, text).move_to(bag.get_center() + np.random.uniform(-1, 1, 3)))
        
        self.play(Create(bag), Write(bag_label))
        self.play(*[GrowFromCenter(item) for item in items])
        self.wait(1)
        
        # Clean up for next scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=0.8
        )
        
        # Scene 2 — Example and Description
        title2 = Text("2️⃣ Set Example: Fruits", font_size=40, color=BLUE)
        self.play(Write(title2))
        self.play(title2.animate.to_edge(UP))
        
        # Set creation code
        code = '''# Creating a set of fruits
fruits = {"apple", "banana", "cherry", "apple"}'''
        
        code_mob = Text(code, font="Monospace", font_size=24, color=YELLOW)
        code_mob.next_to(title2, DOWN, buff=0.7)
        
        # Output
        output = Text("Output: {'apple', 'banana', 'cherry'}", 
                     font="Monospace", font_size=24, color=GREEN)
        output.next_to(code_mob, DOWN, buff=0.7)
        
        # Explanation
        explanation = Text(
            "• Even though 'apple' was added twice,\n"
            "  only one copy is kept in the set\n"
            "• Order is not guaranteed",
            font_size=24,
            color=WHITE,
            line_spacing=1.2
        )
        explanation.next_to(output, DOWN, buff=0.7)
        
        self.play(Write(code_mob))
        self.wait(0.5)
        self.play(Write(output))
        self.wait(0.5)
        self.play(Write(explanation))
        self.wait(2)
        
        # Clean up for next scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != title2],
            title2.animate.scale(0.8).to_corner(UL, buff=0.5),
            run_time=0.8
        )
        
        # Scene 3 — Under the Hood
        title3 = Text("3️⃣ How Sets Work: Hash Tables", font_size=40, color=BLUE)
        self.play(Transform(title2, title3))
        
        # Scene 3.1 - Hash Table Explanation
        title = Text("How Sets Work: Hash Tables", font_size=36, color=YELLOW)
        title.to_edge(UP)
        
        explanation = Text(
            "• Use hash tables for fast lookups (O(1) time)\n"
            "• Each element has a unique hash value\n"
            "• No duplicate elements allowed\n"
            "• Order is not preserved",
            font_size=24,
            color=WHITE,
            line_spacing=1.2
        )
        explanation.next_to(title, DOWN, buff=0.7)
        
        self.play(Write(title))
        self.play(Write(explanation))
        self.wait(2)
        
        # Clear for next slide
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 3.2 - Hash Table Visualization
        title3 = Text("Hash Table Implementation", font_size=36, color=BLUE)
        title3.to_edge(UP)
        self.play(Write(title3))
        
        # Hash table visualization
        table = VGroup()
        rows = 5
        cols = 1
        cell_width = 2.5
        cell_height = 0.8
        
        # Create hash table cells
        for i in range(rows):
            row = VGroup()
            for j in range(cols):
                cell = Rectangle(
                    width=cell_width,
                    height=cell_height,
                    stroke_color=WHITE,
                    stroke_width=2
                )
                if i == 0:
                    # Header
                    cell.set_fill(BLUE, opacity=0.3)
                    text = Text(f"Hash {i}", font_size=20, color=WHITE)
                else:
                    # Data cells
                    cell.set_fill(BLACK, opacity=0.8)
                    if i == 1:
                        text = Text("'apple' → hash: 12345", font_size=16, color=GREEN)
                    elif i == 2:
                        text = Text("'banana' → hash: 67890", font_size=16, color=GREEN)
                    elif i == 3:
                        text = Text("'cherry' → hash: 13579", font_size=16, color=GREEN)
                    else:
                        text = Text("...", font_size=20, color=GRAY)
                
                text.move_to(cell.get_center())
                row.add(VGroup(cell, text))
            
            row.arrange(RIGHT, buff=0)
            table.add(row)
        
        table.arrange(DOWN, buff=0, aligned_edge=LEFT)
        table.to_edge(RIGHT, buff=1.5)
        table.shift(UP * 0.5)
        
        # Set visualization (on the left)
        fruits_set = VGroup()
        fruits = ["apple", "banana", "cherry"]
        colors = ["#FF6B6B", "#6BCB77", "#4D96FF"]
        
        for i, (fruit, color) in enumerate(zip(fruits, colors)):
            item = Circle(radius=0.4, color=color, fill_opacity=0.2)
            text = Text(fruit, font_size=16, color=color)
            group = VGroup(item, text).arrange(DOWN, buff=0.1)
            group.color = color
            fruits_set.add(group)
        
        fruits_set.arrange(DOWN, buff=0.8)
        fruits_set.to_edge(LEFT, buff=1.5)
        fruits_set.shift(UP * 0.5)
        
        # Animate table and set elements
        self.play(Create(table))
        self.play(LaggedStart(
            *[GrowFromCenter(fruit) for fruit in fruits_set],
            lag_ratio=0.3
        ))
        
        # Connect set to hash table with arrows
        for i, (fruit, color) in enumerate(zip(fruits_set, colors)):
            # Create arrow from set element to hash table (left to right)
            arrow = Arrow(
                fruit[0].get_right(),
                table[i+1][0].get_left(),
                color=color,
                buff=0.1,
                stroke_width=3,
                tip_length=0.2
            )
            self.play(Create(arrow), run_time=0.8)
        
        # Performance note
        performance = Text(
            "O(1) average time complexity for operations",
            font_size=22,
            color=YELLOW
        )
        performance.next_to(table, DOWN, buff=1)
        
        self.play(Write(performance))
        self.wait(2)
        
        # Clean up
        self.play(*[FadeOut(mob) for mob in self.mobjects])
