from manim import *

class GenerativeAITutorial(Scene):
    def construct(self):
        # Scene 1: What is Generative AI?
        self.scene_what_is_genai()
        self.clear()
        
        # Scene 2: How Generative AI Works
        self.scene_how_genai_works()
        self.clear()
        
        # Scene 3: Future of AI (3 parts)
        self.scene_future_ai_opportunities()
        self.clear()
        
        self.scene_future_ai_challenges()
        self.clear()
        
        self.scene_future_ai_balance()
        self.clear()

    def scene_what_is_genai(self):
        # Title
        title = Text("🖌️ What is Generative AI?", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Definition
        definition = VGroup(
            Text("AI that creates new content from learned patterns", font_size=32, color=YELLOW, weight=BOLD),
            Text("It doesn't just analyze—it generates something new!", font_size=28, color=WHITE)
        ).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=0.8)
        
        self.play(Write(definition))
        self.wait(1)
        
        # Examples
        examples_title = Text("Examples:", font_size=32, color=GREEN).next_to(definition, DOWN, buff=1.0)
        self.play(Write(examples_title))
        
        examples = VGroup(
            self._create_example("📝", "Text", "ChatGPT, stories, articles"),
            self._create_example("🎨", "Images", "DALL·E, MidJourney"),
            self._create_example("🎬", "Video", "AI-generated clips"),
            self._create_example("🎵", "Music", "Songs in any style")
        ).arrange(RIGHT, buff=0.8).next_to(examples_title, DOWN, buff=0.8)
        
        self.play(LaggedStart(*[FadeIn(example, shift=UP*0.5) for example in examples], lag_ratio=0.3))
        
        # Visual: Creative process
        lightbulb = self._create_lightbulb().scale(0.6).to_edge(DOWN, buff=1.0)
        self.play(DrawBorderThenFill(lightbulb))
        
        self.wait(2)

    def scene_how_genai_works(self):
        # Title
        title = Text("⚙️ How Does Generative AI Work?", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Models explanation
        models = VGroup(
            Text("Powered by:", font_size=32, color=YELLOW, weight=BOLD),
            Text("• Transformers (like GPT)", font_size=28, color=WHITE),
            Text("• GANs (Generative Adversarial Networks)", font_size=28, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=1.0).to_edge(LEFT, buff=1.5)
        
        self.play(Write(models))
        
        # Learning process
        learning = VGroup(
            Text("Learning Process:", font_size=32, color=GREEN, weight=BOLD).to_edge(LEFT, buff=1.5),
            Text("1. Trains on massive datasets", font_size=26, color=WHITE),
            Text("2. Identifies patterns and relationships", font_size=26, color=WHITE),
            Text("3. Generates new, unique outputs", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(models, DOWN, buff=1.0)
        
        self.play(Write(learning[0]))
        self.play(LaggedStart(*[Write(item) for item in learning[1:]], lag_ratio=0.5))
        
        # Example
        example = VGroup(
            Text("Example Prompt:", font_size=28, color=YELLOW, weight=BOLD),
            Text("\"A cat riding a skateboard in space\"", font_size=24, color=WHITE, weight=BOLD)
        ).arrange(DOWN, buff=0.5).next_to(learning, DOWN, buff=1.0)
        
        arrow = Arrow(UP, DOWN, color=YELLOW).next_to(example, DOWN, buff=0.3)
        output = Text("AI generates a brand new image!", font_size=28, color=GREEN).next_to(arrow, DOWN, buff=0.3)
        
        self.play(Write(example))
        self.play(Create(arrow))
        self.play(Write(output))
        
        self.wait(2)

    def scene_future_ai_opportunities(self):
        # Title
        title = Text("✨ Opportunities with AI", font_size=50, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Opportunities
        opportunities = VGroup(
            self._create_opportunity("🤖", "Automation", "Handles repetitive tasks"),
            self._create_opportunity("🚀", "New Industries", "AI art, tutoring, healthcare"),
            self._create_opportunity("📈", "Productivity", "Smarter business tools")
        ).arrange(RIGHT, buff=1.0).next_to(title, DOWN, buff=1.0)
        
        self.play(LaggedStart(*[FadeIn(opp, shift=UP*0.5) for opp in opportunities], lag_ratio=0.3))
        
        # Visual: Upward trend
        x_axis = Line(LEFT*3, RIGHT*3, color=WHITE).to_edge(DOWN, buff=1.5)
        y_axis = Line(DOWN*1, UP*2, color=WHITE).to_edge(LEFT, buff=3.0)
        
        trend = VGroup(
            Dot(radius=0.1, color=GREEN),
            Dot(radius=0.1, color=GREEN).shift(RIGHT*1.5 + UP*1.0),
            Dot(radius=0.1, color=GREEN).shift(RIGHT*3.0 + UP*2.0)
        )
        
        trend_line = VGroup(
            Line(trend[0], trend[1], color=GREEN),
            Line(trend[1], trend[2], color=GREEN)
        )
        
        self.play(Create(x_axis), Create(y_axis))
        self.play(Create(trend), Create(trend_line))
        
        self.wait(2)

    def scene_future_ai_challenges(self):
        # Title
        title = Text("⚠️ Challenges of AI", font_size=50, color=YELLOW)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Challenges
        challenges = VGroup(
            self._create_challenge("👔", "Job Displacement", "Some roles may be automated"),
            self._create_challenge("📚", "Skill Gaps", "Need for new technical skills"),
            self._create_challenge("⚖️", "Ethical Concerns", "Ownership, deepfakes, bias")
        ).arrange(RIGHT, buff=0.8).next_to(title, DOWN, buff=1.0)
        
        self.play(LaggedStart(*[FadeIn(chal, shift=UP*0.5) for chal in challenges], lag_ratio=0.3))
        
        # Visual: Scale
        scale_base = Line(LEFT*3, RIGHT*3, color=WHITE).to_edge(DOWN, buff=1.5)
        scale_center = Line(UP*0.5, DOWN*0.5, color=WHITE).shift(UP*0.5)
        left_side = Rectangle(width=1.5, height=0.8, fill_opacity=0.5, fill_color=GREEN, color=GREEN)\
            .next_to(scale_center, LEFT, buff=0).shift(LEFT*1.0 + UP*0.5)
        right_side = Rectangle(width=1.5, height=0.8, fill_opacity=0.5, fill_color=RED, color=RED)\
            .next_to(scale_center, RIGHT, buff=0).shift(RIGHT*1.0 + UP*0.5)
        
        self.play(Create(scale_base), Create(scale_center))
        self.play(FadeIn(left_side), FadeIn(right_side))
        
        self.wait(2)

    def scene_future_ai_balance(self):
        # Title
        title = Text("🌍 The Future Balance", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Key points
        points = VGroup(
            Text("AI won't replace humans—it will change how we work", font_size=32, color=WHITE),
            Text("Some jobs will disappear, but new ones will emerge:", font_size=28, color=YELLOW),
            Text("• AI Trainers • Prompt Engineers", font_size=26, color=WHITE),
            Text("• AI Ethics Specialists • AI-Human Collaboration", font_size=26, color=WHITE)
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).next_to(title, DOWN, buff=1.0).to_edge(LEFT, buff=1.5)
        
        self.play(Write(points[0]))
        self.play(Write(points[1]))
        self.play(LaggedStart(*[Write(p) for p in points[2:]], lag_ratio=0.5))
        
        # Visual: Human + AI
        human = self._create_human_icon().scale(0.8).to_edge(RIGHT, buff=2.0).shift(UP*0.5)
        plus = Text("+", font_size=72, color=WHITE).next_to(human, LEFT, buff=0.8)
        ai = self._create_ai_icon().scale(0.8).next_to(plus, LEFT, buff=0.8)
        equals = Text("=", font_size=72, color=WHITE).next_to(human, RIGHT, buff=0.8)
        combined = Text("Super Team!", font_size=36, color=GREEN).next_to(equals, RIGHT, buff=0.8)
        
        self.play(FadeIn(ai), FadeIn(plus), FadeIn(human), FadeIn(equals), FadeIn(combined))
        
        self.wait(2)
    
    def _create_example(self, emoji, title, description):
        return VGroup(
            Text(emoji, font_size=48),
            Text(title, font_size=24, color=YELLOW, weight=BOLD),
            Text(description, font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.2)
    
    def _create_lightbulb(self):
        bulb = Circle(radius=0.8, color=YELLOW, fill_opacity=0.3)
        base = Rectangle(width=0.4, height=0.5, color=GRAY, fill_opacity=1).next_to(bulb, DOWN, buff=0)
        return VGroup(bulb, base)
    
    def _create_opportunity(self, emoji, title, description):
        return VGroup(
            Text(emoji, font_size=48),
            Text(title, font_size=28, color=GREEN, weight=BOLD),
            Text(description, font_size=22, color=WHITE, width=3).center()
        ).arrange(DOWN, buff=0.3)
    
    def _create_challenge(self, emoji, title, description):
        return VGroup(
            Text(emoji, font_size=48),
            Text(title, font_size=28, color=YELLOW, weight=BOLD),
            Text(description, font_size=22, color=WHITE, width=3).center()
        ).arrange(DOWN, buff=0.3)
    
    def _create_human_icon(self):
        head = Circle(radius=0.5, color=WHITE, fill_opacity=0.3)
        body = Line(ORIGIN, DOWN*1.0, color=WHITE).next_to(head, DOWN, buff=0)
        arms = Line(LEFT*0.5, RIGHT*0.5, color=WHITE).next_to(body, UP, buff=0.3)
        legs = VGroup(
            Line(ORIGIN, DOWN*0.5 + LEFT*0.3, color=WHITE),
            Line(ORIGIN, DOWN*0.5 + RIGHT*0.3, color=WHITE)
        ).arrange(RIGHT, buff=0.6).next_to(body, DOWN, buff=0)
        return VGroup(head, body, arms, legs)
    
    def _create_ai_icon(self):
        chip = Square(side_length=1.0, color=BLUE, fill_opacity=0.3)
        circuits = VGroup(
            Line(ORIGIN, RIGHT*0.5, color=BLUE_C).shift(LEFT*0.25 + UP*0.25),
            Line(ORIGIN, RIGHT*0.3, color=BLUE_C).shift(RIGHT*0.2 + UP*0.1),
            Line(ORIGIN, RIGHT*0.4, color=BLUE_C).shift(LEFT*0.1 + DOWN*0.2)
        )
        return VGroup(chip, circuits)
