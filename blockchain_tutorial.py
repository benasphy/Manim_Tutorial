from manim import *

class BlockchainTutorial(Scene):
    def construct(self):
        # Scene 1: Why People Care About Blockchain & Crypto
        self.scene_benefits()
        self.clear()
        
        # Scene 2: The Risks
        self.scene_risks()
        self.clear()
        
        # Scene 3: Quick Recap
        self.scene_recap()

    def scene_benefits(self):
        # Title
        title = Text("Why Blockchain & Crypto?", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Create globe with connections
        globe = Circle(radius=2, color=BLUE, fill_opacity=0.2)
        connections = VGroup(*[
            Line(ORIGIN, np.array([np.cos(angle), np.sin(angle), 0]), color=YELLOW, stroke_width=2)
            for angle in np.linspace(0, 2*PI, 8, endpoint=False)
        ])
        
        # Benefits with icons
        benefits = VGroup(
            self._create_benefit_icon("1. Decentralization", "No single entity in control", 0, 2, BLUE),
            self._create_benefit_icon("2. Security", "Nearly unchangeable records", 2, 2, GREEN),
            self._create_benefit_icon("3. Global Access", "Internet = Participation", -2, 2, YELLOW),
            self._create_benefit_icon("4. Opportunities", "Investment • Art • Gaming", 0, -1, ORANGE)
        ).arrange_in_grid(rows=2, cols=2, buff=0.8)
        
        # Show globe animation
        self.play(Create(globe), run_time=1.5)
        self.play(Create(connections), run_time=2)
        self.wait(1)
        
        # Transform into benefits
        self.play(
            FadeOut(globe),
            FadeOut(connections),
            FadeIn(benefits, shift=UP)
        )
        self.wait(2)

    def scene_risks(self):
        # Title with warning
        title = Text("⚠️ The Risks ⚠️", font_size=48, color=RED)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Risk items with icons
        risks = VGroup(
            self._create_risk_icon("🎢", "Price Volatility", "Values change dramatically"),
            self._create_risk_icon("⚠️", "Scams & Frauds", "Many fake projects exist"),
            self._create_risk_icon("🔑", "Lost Access", "Lose password = Lose everything")
        ).arrange(DOWN, buff=0.8).scale(0.9)
        
        risks.next_to(title, DOWN, buff=1)
        
        # Show risks with animations
        for risk in risks:
            self.play(FadeIn(risk, shift=UP*0.5), run_time=0.8)
            self.wait(0.3)
        
        self.wait(1)
        
        # Final warning
        warning = Text("Always do your own research!", font_size=32, color=YELLOW)
        self.play(Write(warning))
        self.wait(2)
        
    def scene_recap(self):
        # Title
        title = Text("Quick Recap", font_size=48, color=PURPLE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Blockchain definition
        blockchain_def = VGroup(
            Text("Blockchain", font_size=36, color=BLUE),
            Text("A secure, digital notebook that no one can tamper with", font_size=24)
        ).arrange(DOWN, buff=0.3).to_edge(LEFT).shift(UP)
        
        # Crypto definition
        crypto_def = VGroup(
            Text("Cryptocurrencies", font_size=36, color=GREEN),
            Text("Digital money on blockchains (e.g., Bitcoin, Ethereum)", font_size=24)
        ).arrange(DOWN, buff=0.3).to_edge(RIGHT).shift(UP)
        
        # NFTs definition
        nft_def = VGroup(
            Text("NFTs", font_size=36, color=YELLOW),
            Text("Unique tokens proving digital ownership", font_size=24)
        ).to_edge(LEFT).shift(DOWN*0.5)
        
        # Pros and Cons
        pros_cons = VGroup(
            Text("Pros & Cons", font_size=36, color=ORANGE),
            Text("✓ Secure & Decentralized\n✓ Global Access\n✗ Volatile\n✗ Scams Exist", 
                font_size=24, line_spacing=1.5)
        ).arrange(DOWN, buff=0.3).to_edge(RIGHT).shift(DOWN*0.5)
        
        # Show all elements with animations
        self.play(Write(blockchain_def[0]))
        self.play(Write(blockchain_def[1]))
        self.wait(0.5)
        
        self.play(Write(crypto_def[0]))
        self.play(Write(crypto_def[1]))
        self.wait(0.5)
        
        self.play(Write(nft_def[0]))
        self.play(Write(nft_def[1]))
        self.wait(0.5)
        
        self.play(Write(pros_cons[0]))
        self.play(Write(pros_cons[1]))
        
        # Final message
        final_message = Text("The future of digital ownership is here!", 
                           font_size=32, color=GREEN)
        self.play(
            FadeOut(blockchain_def),
            FadeOut(crypto_def),
            FadeOut(nft_def),
            FadeOut(pros_cons),
            FadeIn(final_message)
        )
        self.wait(3)
    
    def _create_benefit_icon(self, title, desc, x, y, color):
        icon = VGroup(
            Text(title, font_size=28, color=color),
            Text(desc, font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.2)
        icon.shift(np.array([x, y, 0]))
        return icon
    
    def _create_risk_icon(self, emoji, title, desc):
        return VGroup(
            Text(emoji, font_size=36),
            Text(title, font_size=28, color=RED),
            Text(desc, font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.2)
