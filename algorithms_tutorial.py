from manim import *

class AlgorithmsTutorial(Scene):
    def construct(self):
        # Scene 1: What is an Algorithm?
        self.scene_what_is_algorithm()
        self.clear()

        # Scene 2: Why Algorithms Matter
        self.scene_why_algorithms_matter()
        self.clear()

        # Scene 3: Problem-Solving with Algorithms
        self.scene_problem_solving()
        self.clear()

        # Scene 4: Algorithms in Everyday Apps
        self.scene_everyday_apps()
        self.clear()

        # Scene 5: Quick Recap
        self.scene_recap()
        self.clear()

    def scene_what_is_algorithm(self):
        title = Text("What is an Algorithm?", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        definition = VGroup(
            Text("Step-by-step instructions to solve a problem", font_size=26, color=WHITE),
            Text("Not just for computers—humans use them daily", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.8)
        self.play(Write(definition))

        # Recipe vs Algorithm comparison
        recipe = VGroup(
            Text("Cooking Pasta:", font_size=22, color=YELLOW),
            Text("1. Boil water\n2. Add pasta\n3. Wait 10 min\n4. Drain\n5. Serve", 
                font_size=20, color=WHITE, line_spacing=1.2)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        algo = VGroup(
            Text("Find Word in Dictionary:", font_size=22, color=YELLOW),
            Text("1. Open book\n2. Go to section\n3. Narrow down\n4. Find word", 
                font_size=20, color=WHITE, line_spacing=1.2)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        comparison = VGroup(recipe, algo).arrange(RIGHT, buff=1.5).next_to(definition, DOWN, buff=0.8)
        self.play(FadeIn(comparison, shift=UP))
        
        computer_note = Text("In computers: written in programming languages", font_size=24, color=TEAL)
        computer_note.next_to(comparison, DOWN, buff=0.6)
        self.play(Write(computer_note))
        self.wait(1.5)

    def scene_why_algorithms_matter(self):
        title = Text("Why Algorithms Matter", font_size=48, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("• Heart of computer science", font_size=26, color=WHITE),
            Text("• Make apps fast and efficient", font_size=26, color=WHITE),
            Text("• Solve problems logically", font_size=26, color=WHITE),
            Text("• Power everything from Spotify to Google Maps", font_size=26, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        # Map visualization
        points = [LEFT*3 + DOWN*0.5, UP*0.5, RIGHT*3 + DOWN*0.5]
        path = VGroup(
            Dot(points[0], color=GREEN),
            Dot(points[1], color=YELLOW),
            Dot(points[2], color=RED)
        )
        lines = VGroup(
            Line(points[0], points[1], color=BLUE, stroke_width=4),
            Line(points[1], points[2], color=BLUE, stroke_width=4)
        )
        map_viz = VGroup(lines, path).next_to(bullets, DOWN, buff=0.8)
        
        self.play(Create(lines), Create(path))
        label = Text("Algorithm finds shortest path", font_size=24, color=WHITE).next_to(map_viz, DOWN, buff=0.3)
        self.play(Write(label))
        self.wait(1.5)

    def scene_problem_solving(self):
        title = Text("Problem-Solving with Algorithms", font_size=48, color=TEAL_E)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        steps = VGroup(
            Text("1. Understand the problem", font_size=24, color=WHITE),
            Text("2. Plan a solution (break it down)", font_size=24, color=WHITE),
            Text("3. Write clear steps", font_size=24, color=WHITE),
            Text("4. Test it thoroughly", font_size=24, color=WHITE),
            Text("5. Improve efficiency", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(title, DOWN, buff=0.8)
        self.play(Write(steps))

        # Example: Find largest number
        numbers = [5, 2, 9, 1, 7]
        number_objects = VGroup(*[
            Square(side_length=0.8, color=WHITE).add(Text(str(n), color=WHITE)) 
            for n in numbers
        ]).arrange(RIGHT, buff=0.3).next_to(steps, DOWN, buff=0.8)
        
        self.play(Create(number_objects))
        self.wait(0.5)
        
        # Highlight the process of finding max
        max_val = max(numbers)
        max_idx = numbers.index(max_val)
        
        for i in range(len(numbers)):
            self.play(number_objects[i].animate.set_fill(BLUE, opacity=0.3))
            if i > 0 and numbers[i] > max(numbers[:i]):
                self.play(number_objects[i].animate.set_fill(RED, opacity=0.5))
                if i < len(numbers) - 1:
                    self.play(number_objects[i].animate.set_fill(ORANGE, opacity=0.3))
            elif i > 0:
                self.play(number_objects[i].animate.set_fill(GRAY, opacity=0.3))
        
        # Final highlight on max
        self.play(number_objects[max_idx].animate.set_fill(GREEN, opacity=0.7).scale(1.2))
        
        algo_text = Text(f"Largest number is {max_val}", font_size=24, color=GREEN).next_to(number_objects, DOWN, buff=0.5)
        self.play(Write(algo_text))
        self.wait(1.5)

    def scene_everyday_apps(self):
        title = Text("Algorithms in Everyday Apps", font_size=48, color=PURPLE_E)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        apps = VGroup(
            self._app_card("YouTube", self._icon_play(), "Recommends videos"),
            self._app_card("Google", self._icon_search(), "Ranks web pages"),
            self._app_card("Banks", self._icon_shield(), "Detects fraud")
        ).arrange(RIGHT, buff=0.6).next_to(title, DOWN, buff=0.8)
        
        self.play(LaggedStart(*[FadeIn(app, shift=UP) for app in apps], lag_ratio=0.2))
        
        # Connecting line to show all use algorithms
        line = Line(LEFT*4, RIGHT*4, color=YELLOW).next_to(apps, DOWN, buff=0.8)
        label = Text("All powered by algorithms", font_size=28, color=YELLOW).next_to(line, DOWN, buff=0.3)
        self.play(Create(line), Write(label))
        
        without = Text("Without algorithms, computers wouldn't know what to do", font_size=24, color=WHITE)
        without.next_to(label, DOWN, buff=0.6)
        self.play(Write(without))
        self.wait(1.5)

    def scene_recap(self):
        title = Text("Quick Recap", font_size=50, color=GOLD_E)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        recap = VGroup(
            Text("• Algorithm = step-by-step instructions", font_size=26, color=WHITE),
            Text("• Used in cooking, math, and technology", font_size=26, color=WHITE),
            Text("• Power all digital services and apps", font_size=26, color=WHITE),
            Text("• Problem-solving: understand, plan, write, test, improve", font_size=26, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(title, DOWN, buff=0.8)
        self.play(Write(recap))
        
        # Algorithm visualization
        steps = VGroup(
            Circle(radius=0.3, color=BLUE, fill_opacity=0.2).add(Text("1")),
            Arrow(RIGHT*0.7, RIGHT*1.7, color=WHITE),
            Circle(radius=0.3, color=GREEN, fill_opacity=0.2).add(Text("2")),
            Arrow(RIGHT*2.7, RIGHT*3.7, color=WHITE),
            Circle(radius=0.3, color=RED, fill_opacity=0.2).add(Text("3"))
        ).arrange(RIGHT, buff=0).next_to(recap, DOWN, buff=1.0)
        
        self.play(Create(steps))
        self.wait(1.5)
        
        # Final message
        final = Text("Algorithms: The building blocks of technology", font_size=32, color=BLUE)
        final.next_to(steps, DOWN, buff=0.8)
        self.play(Write(final))
        self.wait(2)

    # Helper methods for creating UI elements
    def _app_card(self, name, icon, description):
        card = RoundedRectangle(width=3.0, height=2.0, corner_radius=0.15, color=WHITE)
        icon = icon.scale(0.5).move_to(card.get_center() + UP*0.3)
        name_text = Text(name, font_size=24, color=WHITE).next_to(icon, DOWN, buff=0.3)
        desc_text = Text(description, font_size=18, color=YELLOW, line_spacing=1.2).next_to(name_text, DOWN, buff=0.2)
        return VGroup(card, icon, name_text, desc_text)
    
    def _icon_play(self):
        return Triangle(color=RED, fill_opacity=1).scale(0.5)
    
    def _icon_search(self):
        circle = Circle(radius=0.5, color=BLUE, fill_opacity=0.2)
        handle = Line(ORIGIN, RIGHT*0.7+DOWN*0.7, color=BLUE).shift(RIGHT*0.35 + DOWN*0.35)
        return VGroup(circle, handle)
    
    def _icon_shield(self):
        shield = Polygon(UP, LEFT*0.7+DOWN*0.7, RIGHT*0.7+DOWN*0.7, color=GREEN, fill_opacity=0.2)
        base = Rectangle(width=1.4, height=0.3, color=GREEN, fill_opacity=0.2).next_to(shield, DOWN, buff=0)
        return VGroup(shield, base)
