from manim import *

class OOPTutorial(Scene):
    def construct(self):
        # Scene 1: Title and Introduction
        title = Text("🏗️ Object-Oriented Programming (OOP)", font_size=48, color=BLUE)
        subtitle = Text("Organizing Code with Objects", font_size=32, color=YELLOW)
        
        self.play(Write(title))
        self.play(Write(subtitle.next_to(title, DOWN, buff=0.5)))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 2: What is OOP?
        title1 = Text("1️⃣ What is OOP?", font_size=42, color=BLUE)
        self.play(Write(title1))
        self.play(title1.animate.to_edge(UP))
        
        definition = VGroup(
            Text("OOP is a programming paradigm that organizes", font_size=28, color=WHITE),
            Text("code into reusable objects containing both", font_size=28, color=WHITE),
            Text("data (attributes) and behavior (methods).", font_size=28, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title1, DOWN, buff=1)
        
        self.play(Write(definition[0]))
        self.wait(0.3)
        self.play(Write(definition[1:]))
        self.wait(2)
        
        # Clear for real-world analogy
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 3: Real-world Analogy
        analogy_title = Text("🚗 Real-world Analogy", font_size=36, color=GREEN)
        self.play(Write(analogy_title))
        self.play(analogy_title.animate.to_edge(UP))
        
        # Create a car object visualization
        car = self.create_car()
        self.play(FadeIn(car))
        self.wait(1)
        
        # Show attributes
        attributes = VGroup(
            Text("Attributes (Data):", font_size=28, color=YELLOW),
            Text("• color = 'red'", font_size=24, color=WHITE),
            Text("• model = 'Tesla Model 3'", font_size=24, color=WHITE),
            Text("• speed = 0 km/h", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(RIGHT, buff=1)
        
        self.play(Write(attributes[0]))
        self.play(LaggedStart(*[Write(attr) for attr in attributes[1:]], lag_ratio=0.3))
        self.wait(1)
        
        # Show methods
        methods = VGroup(
            Text("Methods (Behavior):", font_size=28, color=YELLOW).next_to(attributes, DOWN, buff=1, aligned_edge=LEFT),
            Text("• start()", font_size=24, color=WHITE),
            Text("• accelerate()", font_size=24, color=WHITE),
            Text("• brake()", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        self.play(Write(methods[0]))
        self.play(LaggedStart(*[Write(meth) for meth in methods[1:]], lag_ratio=0.3))
        self.wait(2)
        
        # Clear for why OOP
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 4: Why OOP?
        why_title = Text("❓ Why Use OOP?", font_size=42, color=BLUE)
        self.play(Write(why_title))
        self.play(why_title.animate.to_edge(UP))
        
        reasons = VGroup(
            Text("1. Modularity", font_size=32, color=GREEN).to_edge(LEFT, buff=1),
            Text("• Reuse code with classes & objects", font_size=24, color=WHITE),
            
            Text("\n2. Scalability", font_size=32, color=GREEN).to_edge(LEFT, buff=1),
            Text("• Manage large codebases efficiently", font_size=24, color=WHITE),
            
            Text("\n\n3. Maintainability", font_size=32, color=GREEN).to_edge(LEFT, buff=1),
            Text("• Update one part without breaking others", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).scale(0.9)
        
        # Visual for modularity (building blocks)
        blocks = VGroup(*[
            Square(side_length=1, color=color, fill_opacity=0.6).shift(UP*0.5 + RIGHT*i*1.2)
            for i, color in enumerate([BLUE, GREEN, YELLOW, RED])
        ]).to_edge(RIGHT, buff=2)
        
        self.play(Write(reasons[0:2]))
        self.play(LaggedStart(*[GrowFromCenter(block) for block in blocks], lag_ratio=0.2))
        
        self.play(Write(reasons[2:4]))
        self.play(blocks.animate.arrange(RIGHT, buff=0.2).scale(1.2).shift(LEFT*0.5))
        
        self.play(Write(reasons[4:]))
        self.play(blocks.animate.arrange_in_grid(rows=2, buff=0.2).scale(0.8).shift(LEFT*0.5))
        
        self.wait(2)
        
        # Clear for Four Pillars
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 5: Four Pillars of OOP
        pillars_title = Text("🏛️ The Four Pillars of OOP", font_size=42, color=BLUE)
        self.play(Write(pillars_title))
        self.play(pillars_title.animate.to_edge(UP))
        
        # Pillar 1: Encapsulation
        self.pillar_slide(
            "1. Encapsulation",
            "Bundling data and methods that operate on that data within one unit.",
            "💊 Like a medicine capsule that hides its contents.",
            """
            class BankAccount:
                def __init__(self):
                    self.__balance = 0  # Private attribute
                
                def deposit(self, amount):
                    self.__balance += amount
                    
                def get_balance(self):
                    return self.__balance
            """
        )
        
        # Pillar 2: Abstraction
        self.pillar_slide(
            "2. Abstraction",
            "Hiding complex implementation details and showing only necessary features.",
            "🎛️ Like a car dashboard - you don't need to know how the engine works.",
            """
            from abc import ABC, abstractmethod
            
            class Shape(ABC):
                @abstractmethod
                def area(self):
                    pass
                    
            class Circle(Shape):
                def area(self):
                    return 3.14 * self.radius * self.radius
            """
        )
        
        # Pillar 3: Inheritance
        self.pillar_slide(
            "3. Inheritance",
            "Creating a new class using properties and methods of an existing class.",
            "👨‍👦 Like children inheriting traits from their parents.",
            """
            class Animal:
                def speak(self):
                    pass
                    
            class Dog(Animal):
                def speak(self):
                    return "Woof!"
                    
            class Cat(Animal):
                def speak(self):
                    return "Meow!"
            """
        )
        
        # Pillar 4: Polymorphism
        self.pillar_slide(
            "4. Polymorphism",
            "Using a single interface to represent different data types.",
            "🎭 The same method can behave differently for different classes.",
            """
            def make_animal_speak(animal):
                print(animal.speak())
                
            dog = Dog()
            cat = Cat()
            
            make_animal_speak(dog)  # Outputs: Woof!
            make_animal_speak(cat)  # Outputs: Meow!
            """
        )
        
        # Final slide
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        final = VGroup(
            Text("🎉 Key Takeaways", font_size=48, color=YELLOW),
            Text("• OOP organizes code into objects with data and behavior", font_size=28, color=WHITE),
            Text("• Encapsulation: Bundle data and methods together", font_size=28, color=WHITE),
            Text("• Abstraction: Hide complex implementation details", font_size=28, color=WHITE),
            Text("• Inheritance: Share code between classes", font_size=28, color=WHITE),
            Text("• Polymorphism: One interface, many implementations", font_size=28, color=WHITE)
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(final[0]))
        self.play(LaggedStart(*[Write(takeaway) for takeaway in final[1:]], lag_ratio=0.3))
        self.wait(3)
    
    def create_car(self):
        """Create a simple car using basic shapes"""
        # Car body
        body = Rectangle(height=1, width=2, color=RED, fill_opacity=0.8)
        
        # Car top
        top = Polygon(
            body.get_corner(UL) + UP*0.5 + RIGHT*0.3,
            body.get_corner(UR) + UP*0.5 + LEFT*0.3,
            body.get_corner(UR) + DOWN*0.3,
            body.get_corner(UL) + DOWN*0.3,
            color=RED, fill_opacity=0.6
        )
        
        # Wheels
        wheels = VGroup(*[
            Circle(radius=0.3, color=BLACK, fill_opacity=1).move_to(body.get_bottom() + DOWN*0.1 + x*1.2*RIGHT)
            for x in [-0.5, 0.5]
        ])
        
        # Windows
        windows = VGroup(*[
            Rectangle(height=0.3, width=0.6, color=BLUE_E, fill_opacity=0.6).move_to(top.get_center() + x*0.6*RIGHT)
            for x in [-0.5, 0.5]
        ])
        
        # Lights
        lights = VGroup(
            Rectangle(height=0.2, width=0.1, color=YELLOW, fill_opacity=1).next_to(body, LEFT, buff=0.1),
            Rectangle(height=0.2, width=0.1, color=RED, fill_opacity=1).next_to(body, RIGHT, buff=0.1)
        )
        
        return VGroup(body, top, wheels, windows, lights).scale(0.8).to_edge(LEFT, buff=2)
    
    def pillar_slide(self, title, definition, analogy, code_example):
        """Helper function to create consistent pillar slides"""
        # Clear previous content
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Create title
        title_text = Text(title, font_size=36, color=BLUE).to_edge(UP)
        self.play(Write(title_text))
        
        # Create definition
        def_text = Text(definition, font_size=24, color=WHITE, line_spacing=1.2)\
            .to_edge(UP, buff=1.5).to_edge(LEFT, buff=1)
        
        # Create analogy
        anal_text = Text(analogy, font_size=24, color=YELLOW, line_spacing=1.2)\
            .next_to(def_text, DOWN, buff=0.8).to_edge(LEFT, buff=1)
        
        # Create code block with simpler formatting
        code = Text(
            code_example,
            font="Monospace",
            font_size=18,
            color=WHITE,
            line_spacing=1.2,
        ).scale(0.8).to_edge(RIGHT, buff=1)
        
        # Add a background rectangle for the code
        code_background = SurroundingRectangle(
            code, color=BLUE, buff=0.5, fill_color=BLACK, fill_opacity=0.8
        )
        
        # Animate elements
        self.play(Write(def_text))
        self.wait(0.5)
        self.play(Write(anal_text))
        self.wait(0.5)
        
        # Create and animate code block
        self.play(Create(code_background))
        self.play(Write(code), run_time=2)
        self.wait(2)
