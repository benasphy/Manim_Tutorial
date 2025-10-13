from manim import *

class DigitalSafetyTutorial(Scene):
    def construct(self):
        # Part 1: What is Digital Safety?
        self.scene_what_is_digital_safety()
        self.clear()
        
        # Part 2: Safe Internet Practices
        self.scene_safe_practices()
        self.clear()
        
        # Part 3: Why It Matters
        self.scene_why_it_matters()

    def scene_what_is_digital_safety(self):
        # Title
        title = Text("What is Digital Safety?", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(2)
        
        # Main explanation
        explanation = Text(
            "Protecting computers, smartphones, and networks\nfrom digital attacks",
            font_size=36,
            line_spacing=1.5
        )
        
        # Analogy
        analogy = Text(
            "Just like locking your doors\nkeeps your home safe,\ncybersecurity protects\nyour digital life.",
            font_size=32,
            color=YELLOW
        )
        
        # Show explanation and then analogy
        self.play(ReplacementTransform(title, explanation))
        self.wait(3)
        self.play(ReplacementTransform(explanation, analogy))
        self.wait(4)

    def scene_safe_practices(self):
        title = Text("Safe Internet Practices", font_size=48, color=GREEN)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Create a list of practices
        practices = VGroup(
            Text("1. Use Strong Passwords", color=BLUE),
            Text("2. Enable Two-Factor Authentication (2FA)", color=BLUE),
            Text("3. Be Careful with Emails & Links", color=BLUE),
            Text("4. Keep Software Updated", color=BLUE),
            Text("5. Be Careful on Public Wi-Fi", color=BLUE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).scale(0.8)
        
        practices.next_to(title, DOWN, buff=1)
        
        # Show practices one by one
        for practice in practices:
            self.play(Write(practice), run_time=0.8)
            self.wait(0.5)
        
        self.wait(2)
        
        # Add visual for strong password
        self.clear()
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Strong password example
        weak_pass = Text("1234", color=RED, font_size=36)
        strong_pass = Text("C@tL0ver!2025", color=GREEN, font_size=36)
        
        weak_box = SurroundingRectangle(weak_pass, color=RED, buff=0.5)
        strong_box = SurroundingRectangle(strong_pass, color=GREEN, buff=0.5)
        
        weak_group = VGroup(weak_pass, weak_box).shift(UP)
        strong_group = VGroup(strong_pass, strong_box).shift(DOWN)
        
        self.play(Write(Text("Weak Password", font_size=28).next_to(weak_group, UP)))
        self.play(Create(weak_group[1]), Write(weak_group[0]))
        self.wait(1)
        
        self.play(Write(Text("Strong Password", font_size=28).next_to(strong_group, UP)))
        self.play(Create(strong_group[1]), Write(strong_group[0]))
        self.wait(3)

    def scene_why_it_matters(self):
        title = Text("Why Digital Safety Matters", font_size=48, color=RED)
        self.play(Write(title))
        self.wait(1)
        
        # Create impact items
        impacts = VGroup(
            Text("• Stolen Money", color=YELLOW),
            Text("• Lost Photos & Memories", color=YELLOW),
            Text("• Damaged Reputation", color=YELLOW),
            Text("• Identity Theft", color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.7).scale(1.2)
        
        impacts.next_to(title, DOWN, buff=1)
        
        # Show impacts one by one
        for impact in impacts:
            self.play(Write(impact), run_time=0.8)
            self.wait(0.5)
        
        # Final message
        final_message = Text("Be Smart, Stay Safe Online!", font_size=40, color=GREEN)
        self.play(
            FadeOut(title),
            FadeOut(impacts),
            FadeIn(final_message)
        )
        self.wait(3)
