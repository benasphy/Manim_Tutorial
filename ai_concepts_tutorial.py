from manim import *

class AIConceptsTutorial(Scene):
    def construct(self):
        # Scene 1: What is AI?
        self.scene_what_is_ai()
        self.clear()
        
        # Scene 2: Why AI Matters
        self.scene_why_ai_matters()
        self.clear()

    def scene_what_is_ai(self):
        # Title
        title = Text("🧠 What is AI?", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Definition
        definition = VGroup(
            Text("AI (Artificial Intelligence):", font_size=32, color=YELLOW, weight=BOLD),
            Text("Computers doing smart things that usually", font_size=28, color=WHITE),
            Text("require human intelligence", font_size=28, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=0.8)
        
        self.play(Write(definition))
        self.wait(1)
        
        # Human vs AI comparison
        comparison = VGroup(
            Text("Human Brain:", font_size=28, color=GREEN, weight=BOLD).to_edge(LEFT, buff=1.5),
            Text("vs", font_size=24, color=WHITE).shift(UP*0.5),
            Text("AI System:", font_size=28, color=BLUE, weight=BOLD).to_edge(RIGHT, buff=1.5)
        ).arrange(RIGHT, buff=1.5).next_to(definition, DOWN, buff=1.0)
        
        human_features = VGroup(
            Text("• Learns from experience", font_size=24, color=GREEN),
            Text("• Solves problems", font_size=24, color=GREEN),
            Text("• Adapts to new situations", font_size=24, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(comparison[0], DOWN, buff=0.5).shift(LEFT*0.5)
        
        ai_features = VGroup(
            Text("• Processes data", font_size=24, color=BLUE),
            Text("• Recognizes patterns", font_size=24, color=BLUE),
            Text("• Makes predictions", font_size=24, color=BLUE)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(comparison[2], DOWN, buff=0.5).shift(RIGHT*0.5)
        
        self.play(Write(comparison))
        self.play(
            LaggedStart(
                *[Write(feature) for feature in human_features],
                *[Write(feature) for feature in ai_features],
                lag_ratio=0.3
            )
        )
        self.wait(1)
        
        # AI in simple terms
        simple_terms = VGroup(
            Text("In Simple Terms:", font_size=32, color=YELLOW, weight=BOLD),
            Text("AI = Teaching computers to think and learn", font_size=28, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(human_features, DOWN, buff=1.0).to_edge(LEFT, buff=1.5)
        
        self.play(Write(simple_terms))
        
        # Visual: Robot head with brain
        robot_head = self._create_robot_head()
        robot_head.next_to(simple_terms, RIGHT, buff=1.0)
        self.play(DrawBorderThenFill(robot_head))
        
        self.wait(2)

    def scene_why_ai_matters(self):
        # Title
        title = Text("🌍 Why AI Matters", font_size=50, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # AI Applications
        apps = VGroup(
            self._create_ai_application("🏥 Healthcare", "Early disease detection"),
            self._create_ai_application("🎓 Education", "Personalized learning"),
            self._create_ai_application("💼 Business", "Smarter decisions"),
            self._create_ai_application("📱 Daily Life", "Voice assistants, translations")
        ).arrange_in_grid(rows=2, cols=2, buff=1.0).next_to(title, DOWN, buff=1.0)
        
        self.play(LaggedStart(*[FadeIn(app, shift=UP*0.5) for app in apps], lag_ratio=0.3))
        self.wait(1)
        
        # AI vs ML vs DL
        comparison_title = Text("AI vs ML vs Deep Learning", font_size=36, color=YELLOW)
        comparison_title.next_to(apps, DOWN, buff=1.0)
        self.play(Write(comparison_title))
        
        ai_ml_dl = VGroup(
            self._create_concept_card("🤖 AI", "Making machines intelligent"),
            Arrow(LEFT, RIGHT, color=WHITE).scale(0.8),
            self._create_concept_card("📊 ML", "Teaching with data"),
            Arrow(LEFT, RIGHT, color=WHITE).scale(0.8),
            self._create_concept_card("🧠 Deep Learning", "Brain-inspired learning")
        ).arrange(RIGHT, buff=0.5).next_to(comparison_title, DOWN, buff=0.8)
        
        self.play(LaggedStart(*[FadeIn(item, shift=UP*0.3) for item in ai_ml_dl], lag_ratio=0.2))
        
        # Final message
        final_message = Text("AI is transforming our world, one algorithm at a time!", 
                           font_size=32, color=BLUE)
        final_message.next_to(ai_ml_dl, DOWN, buff=1.0)
        self.play(Write(final_message))
        
        self.wait(2)
    
    def _create_ai_application(self, icon, text):
        group = VGroup(
            Text(icon, font_size=36),
            Text(text, font_size=24, color=WHITE)
        ).arrange(DOWN, buff=0.3)
        return group
    
    def _create_concept_card(self, title, description):
        card = VGroup(
            Text(title, font_size=28, color=YELLOW, weight=BOLD),
            Text(description, font_size=22, color=WHITE)
        ).arrange(DOWN, buff=0.3)
        return card
    
    def _create_robot_head(self):
        head = Circle(radius=1.0, color=WHITE, fill_opacity=0.2)
        left_eye = Circle(radius=0.15, color=BLUE, fill_opacity=1).shift(LEFT*0.3 + UP*0.2)
        right_eye = Circle(radius=0.15, color=BLUE, fill_opacity=1).shift(RIGHT*0.3 + UP*0.2)
        mouth = ArcBetweenPoints(
            LEFT*0.4 + DOWN*0.2, 
            RIGHT*0.4 + DOWN*0.2, 
            angle=-PI/2,
            color=WHITE
        )
        return VGroup(head, left_eye, right_eye, mouth)
