from manim import *

class QuantumComputingTutorial(Scene):
    def construct(self):
        # Scene 1: Why Quantum Computing Matters
        self.scene_importance()
        self.clear()
        
        # Scene 2: The Challenges
        self.scene_challenges()
        
    def scene_importance(self):
        # Title
        title = Text("Why Quantum Computing Matters", 
                    font_size=48, 
                    color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.wait(0.5)
        
        # Main message
        main_text = Text(
            "It's not just about speed—\nit's about solving the unsolvable",
            font_size=32,
            color=YELLOW
        )
        self.play(Write(main_text))
        self.wait(2)
        self.play(FadeOut(main_text))
        
        # Application areas
        apps = VGroup(
            self._create_application(
                "🧪 Medicine",
                "• New drug discovery\n• Protein folding\n• Customized treatments",
                BLUE
            ),
            self._create_application(
                "📊 Finance",
                "• Risk analysis\n• Fraud detection\n• Portfolio optimization",
                GREEN
            ),
            self._create_application(
                "🌍 Climate",
                "• Weather modeling\n• Carbon capture\n• Energy optimization",
                TEAL
            ),
            self._create_application(
                "🔒 Cybersecurity",
                "• Breaking encryption\n• Secure communication\n• Quantum-safe security",
                PURPLE
            )
        ).arrange_in_grid(rows=2, cols=2, buff=0.8).scale(0.9)
        
        # Animate applications
        self.play(FadeIn(apps, shift=UP))
        self.wait(2)
        
        # Final message
        final_message = Text(
            "Imagine curing diseases, creating super-materials,\nor solving energy problems with quantum computing!",
            font_size=28,
            color=YELLOW
        )
        self.play(
            FadeOut(apps),
            FadeIn(final_message)
        )
        self.wait(3)
        
        # Final call to action
        cta = Text(
            "The quantum future is closer than you think!",
            font_size=32,
            color=GREEN
        )
        self.play(
            FadeOut(final_message),
            FadeIn(cta)
        )
        self.wait(2)
        
    def scene_challenges(self):
        # Title
        title = Text("The Challenges", font_size=48, color=RED)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Main message
        message = Text(
            "Quantum computers are still in their early days",
            font_size=32,
            color=YELLOW
        )
        self.play(Write(message))
        self.wait(2)
        self.play(FadeOut(message))
        
        # Challenges
        challenges = VGroup(
            self._create_challenge(
                "❄️ Extreme Cooling",
                "• Need to be near absolute zero\n• Colder than outer space",
                BLUE_C
            ),
            self._create_challenge(
                "⚠️ Super Sensitive",
                "• Tiny vibrations cause errors\n• Temperature changes affect stability",
                YELLOW
            ),
            self._create_challenge(
                "🏢 Limited Access",
                "• Only big companies and research labs\n• Google, IBM, universities",
                LIGHT_GRAY
            )
        ).arrange(DOWN, buff=0.6).scale(0.9)
        
        # Animate challenges
        self.play(FadeIn(challenges, shift=UP))
        self.wait(3)
        
        # Final message
        final_message = Text(
            "Despite these challenges, progress is happening fast!",
            font_size=28,
            color=GREEN
        )
        self.play(
            FadeOut(challenges),
            FadeIn(final_message)
        )
        self.wait(2)
    
    def _create_application(self, title, details, color):
        return VGroup(
            Text(title, font_size=32, color=color),
            Text(details, font_size=22, line_spacing=1.2)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
    def _create_challenge(self, icon, details, color):
        return VGroup(
            Text(icon, font_size=40),
            Text(details, font_size=24, line_spacing=1.3, color=color)
        ).arrange(RIGHT, buff=0.5, aligned_edge=UP)
