from manim import *

class PythonDictionariesTutorial(Scene):
    def construct(self):
        # Scene 1 - What is a Dictionary?
        title = Text("1️⃣ What is a Dictionary?", font_size=42, color=BLUE)
        definition = Text(
            "A collection of key-value pairs\n"
            "Think: Word → Meaning in a real dictionary",
            font_size=28,
            color=WHITE,
            line_spacing=1.2
        )
        
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.play(Write(definition.next_to(title, DOWN, buff=0.7)))
        
        # Real-life dictionary analogy
        analogy = VGroup(
            Text("Real Dictionary", font_size=24, color=YELLOW),
            Text("Word → Meaning", font_size=22, color=WHITE),
            Text("Python Dictionary", font_size=24, color=YELLOW).shift(DOWN * 1.5),
            Text("Key → Value", font_size=22, color=WHITE).next_to(Text("Python Dictionary", font_size=24), DOWN)
        ).arrange(DOWN, buff=0.5)
        analogy.next_to(definition, DOWN, buff=1)
        
        self.play(Create(analogy[0]))
        self.play(Write(analogy[1]))
        self.wait(0.5)
        self.play(Create(analogy[2]))
        self.play(Write(analogy[3]))
        self.wait(1)
        
        # Clean up for dictionary example
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # New slide for dictionary example
        title2 = Text("Dictionary Example", font_size=36, color=BLUE)
        title2.to_edge(UP)
        self.play(Write(title2))
        
        # Dictionary example
        dict_code = '''student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
print(student)'''
        
        code_mob = Text(dict_code, font="Monospace", font_size=20, color=YELLOW)
        code_mob.next_to(title2, DOWN, buff=0.7)
        
        self.play(Write(code_mob))
        self.wait(1)
        
        # Output
        output = Text("Output: {'name': 'Alice', 'age': 20, 'major': 'Computer Science'}",
                     font="Monospace", font_size=16, color=GREEN)
        output.next_to(code_mob, DOWN, buff=0.5)
        
        self.play(Write(output))
        self.wait(2)
        
        # Clean up for next scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 2 - Under the Hood
        title2 = Text("2️⃣ How Dictionaries Work", font_size=40, color=BLUE)
        title2.to_edge(UP)
        self.play(Write(title2))
        
        # Dictionary visualization
        pairs = [
            ("name", "Alice"),
            ("age", 20),
            ("major", "Computer Science")
        ]
        colors = ["#FF6B6B", "#6BCB77", "#4D96FF"]
        
        # Create key-value pairs
        kv_groups = VGroup()
        for i, ((key, value), color) in enumerate(zip(pairs, colors)):
            # Key with hash
            k_rect = RoundedRectangle(width=2, height=0.8, corner_radius=0.1, 
                                   color=color, fill_opacity=0.2)
            k_text = Text(f'"{key}"', font_size=16, color=color)
            k_hash = Text(f"hash: {hash(key) % 1000}", font_size=12, color=GRAY)
            k_group = VGroup(k_rect, k_text, k_hash.next_to(k_rect, DOWN, buff=0.1))
            
            # Arrow
            arrow = Arrow(ORIGIN, RIGHT*0.5, color=WHITE, buff=0.1)
            
            # Value
            v_rect = RoundedRectangle(width=2.5, height=0.8, corner_radius=0.1, 
                                   color=color, fill_opacity=0.1)
            v_text = Text(f'"{value}"', font_size=16, color=color)
            v_group = VGroup(v_rect, v_text)
            
            # Group them
            group = VGroup(k_group, arrow, v_group).arrange(RIGHT, buff=0.1)
            group.shift(DOWN * (i * 1.5 + 1))
            kv_groups.add(group)
        
        # Show lookup code first
        lookup_code = Text('student["age"]', font="Monospace", font_size=24, color=YELLOW)
        lookup_code.to_edge(UP, buff=0.7)
        self.play(Transform(title2, lookup_code))
        
        # Position key-value pairs higher up
        kv_groups.shift(UP * 0.3)
        
        # Show key-value pairs
        self.play(LaggedStart(
            *[Create(group) for group in kv_groups],
            lag_ratio=0.3
        ))
        
        # Hash table explanation (positioned below key-value pairs)
        explanation = Text(
            "• Keys are hashed for fast lookups (O(1) time)\n"
            "• Values are stored at the hash location\n"
            "• Keys must be hashable (immutable types)",
            font_size=20,
            color=YELLOW,
            line_spacing=1.2
        )
        explanation.next_to(kv_groups, DOWN, buff=0.7)
        
        self.play(Write(explanation))
        
        # Highlight the age key-value pair
        age_pair = kv_groups[1]  # age is the second pair
        self.play(
            age_pair[0][0].animate.set_fill(color=YELLOW, opacity=0.5),
            age_pair[2][0].animate.set_fill(color=YELLOW, opacity=0.3)
        )
        
        # Show value retrieval
        result = Text("→ 20", font_size=24, color=GREEN)
        result.next_to(lookup_code, RIGHT, buff=0.5)
        
        self.play(Write(result))
        self.wait(2)
        
        # Clean up
        self.play(*[FadeOut(mob) for mob in self.mobjects])
