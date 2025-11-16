from manim import *

class MagicMethodsTutorial(Scene):
    def construct(self):
        # Scene 1: Title and Introduction
        title = Text("✨ Python Magic Methods", font_size=48, color=BLUE)
        subtitle = Text("Making Your Objects Pythonic", font_size=32, color=YELLOW)
        
        self.play(Write(title))
        self.play(Write(subtitle.next_to(title, DOWN, buff=0.5)))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 2: What Are Magic Methods?
        title2 = Text("1️⃣ What Are Magic Methods?", font_size=42, color=BLUE)
        self.play(Write(title2))
        self.play(title2.animate.to_edge(UP))
        
        definition = VGroup(
            Text("Special methods that control object behavior", font_size=28, color=WHITE),
            Text("• Start and end with double underscores: __method__", font_size=24, color=YELLOW),
            Text("• Called automatically by Python in specific situations", font_size=24, color=YELLOW),
            Text("• Make your objects work with built-in functions/operators", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title2, DOWN, buff=1)
        
        self.play(Write(definition[0]))
        self.play(Write(definition[1:]))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # New Scene: Common Magic Methods
        title_common = Text("🔍 Common Magic Methods", font_size=42, color=BLUE)
        self.play(Write(title_common))
        self.play(title_common.animate.to_edge(UP))
        
        # Categorize common magic methods
        categories = VGroup(
            Text("1. Object Creation & Initialization", font_size=28, color=YELLOW),
            Text("   • __new__: Object creation", font="Monospace", font_size=20, color=WHITE),
            Text("   • __init__: Object initialization", font="Monospace", font_size=20, color=WHITE),
            Text("   • __del__: Object cleanup", font="Monospace", font_size=20, color=WHITE),
            
            Text("\n2. String Representation", font_size=28, color=YELLOW),
            Text("   • __str__: Human-readable string", font="Monospace", font_size=20, color=WHITE),
            Text("   • __repr__: Unambiguous representation", font="Monospace", font_size=20, color=WHITE),
            
            Text("\n3. Comparison Operators", font_size=28, color=YELLOW),
            Text("   • __eq__, __ne__: ==, !=", font="Monospace", font_size=20, color=WHITE),
            Text("   • __lt__, __gt__: <, >, <=, >=", font="Monospace", font_size=20, color=WHITE),
            
            Text("\n4. Numeric Operations", font_size=28, color=YELLOW),
            Text("   • __add__, __sub__: +, -", font="Monospace", font_size=20, color=WHITE),
            Text("   • __mul__, __truediv__: *, /", font="Monospace", font_size=20, color=WHITE),
            
            Text("\n5. Container Methods", font_size=28, color=YELLOW),
            Text("   • __len__: len(obj)", font="Monospace", font_size=20, color=WHITE),
            Text("   • __getitem__, __setitem__: obj[key]", font="Monospace", font_size=20, color=WHITE),
            Text("   • __contains__: x in obj", font="Monospace", font_size=20, color=WHITE),
            
            Text("\n6. Context Managers", font_size=28, color=YELLOW),
            Text("   • __enter__, __exit__: with statement", font="Monospace", font_size=20, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).scale(0.8).next_to(title_common, DOWN, buff=0.8)
        
        # Animate categories one by one
        self.play(Write(categories[0:4]))
        self.wait(0.5)
        self.play(Write(categories[4:7]))
        self.wait(0.5)
        self.play(Write(categories[7:10]))
        self.wait(0.5)
        self.play(Write(categories[10:13]))
        self.wait(0.5)
        self.play(Write(categories[13:17]))
        self.wait(0.5)
        self.play(Write(categories[17:]))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Continue with the rest of the tutorial
        title3 = Text("2️⃣ Why Use Magic Methods?", font_size=42, color=BLUE)
        self.play(Write(title3))
        self.play(title3.animate.to_edge(UP))
        
        # Scene 3: Why Use Magic Methods?
        title3 = Text("2️⃣ Why Use Magic Methods?", font_size=42, color=BLUE)
        self.play(Write(title3))
        self.play(title3.animate.to_edge(UP))
        
        benefits = VGroup(
            Text("Make your objects work like built-in types", font_size=28, color=YELLOW),
            Text("• Support operators (+, -, *, /, ==, <, >, etc.)", font_size=24, color=WHITE),
            Text("• Work with built-in functions (len(), str(), print())", font_size=24, color=WHITE),
            Text("• Enable context managers (with statement)", font_size=24, color=WHITE),
            Text("• Make your code more intuitive and readable", font_size=24, color=WHITE),
            
            Text("\nWithout them:", font_size=28, color=RED).shift(UP*0.5),
            Text("• Your objects feel clunky and un-Pythonic", font_size=24, color=WHITE),
            Text("• Need to call methods like obj.get_length() instead of len(obj)", font_size=24, color=WHITE),
            Text("• Can't use with standard Python idioms", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.9).next_to(title3, DOWN, buff=0.8)
        
        self.play(Write(benefits[0:5]))
        self.wait(1)
        self.play(Write(benefits[5:]))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 4: Intuition/Analogy
        title4 = Text("🤔 Intuition: Magic Methods as Social Skills", font_size=42, color=BLUE)
        self.play(Write(title4))
        self.play(title4.animate.to_edge(UP))
        
        analogy = VGroup(
            Text("Think of objects as people and magic methods as social skills:", font_size=28, color=YELLOW),
            Text("• __str__: How you introduce yourself", font_size=24, color=WHITE),
            Text("• __add__: How you collaborate with others", font_size=24, color=WHITE),
            Text("• __eq__: How you compare yourself to others", font_size=24, color=WHITE),
            Text("• __len__: How you measure your capabilities", font_size=24, color=WHITE),
            Text("• __enter__/__exit__: How you handle responsibilities", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title4, DOWN, buff=1)
        
        self.play(Write(analogy[0]))
        self.wait(0.5)
        self.play(LaggedStart(*[Write(p) for p in analogy[1:]], lag_ratio=0.2))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 5: Under the Hood
        title5 = Text("🔍 Under the Hood", font_size=42, color=BLUE)
        subtitle5 = Text("How Python Calls Magic Methods", font_size=32, color=YELLOW)
        
        self.play(Write(title5))
        self.play(Write(subtitle5.next_to(title5, DOWN, buff=0.3)))
        self.play(title5.animate.to_edge(UP), subtitle5.animate.to_edge(UP).shift(DOWN*0.8))
        
        calls = VGroup(
            Text("Python translates operations to method calls:", font_size=28, color=WHITE),
            Text("• print(obj)  →  obj.__str__()", font="Monospace", font_size=22, color=YELLOW),
            Text("• len(obj)    →  obj.__len__()", font="Monospace", font_size=22, color=YELLOW),
            Text("• obj1 + obj2 →  obj1.__add__(obj2)", font="Monospace", font_size=22, color=YELLOW),
            Text("• obj1 == obj2 →  obj1.__eq__(obj2)", font="Monospace", font_size=22, color=YELLOW),
            Text("• obj[key]    →  obj.__getitem__(key)", font="Monospace", font_size=22, color=YELLOW),
            Text("• with obj:   →  obj.__enter__() / obj.__exit__()", font="Monospace", font_size=22, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(subtitle5, DOWN, buff=1)
        
        self.play(Write(calls[0]))
        self.wait(0.5)
        self.play(LaggedStart(*[Write(c) for c in calls[1:]], lag_ratio=0.2))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # Scene 6: Best Practices
        title6 = Text("💡 Best Practices", font_size=42, color=BLUE)
        self.play(Write(title6))
        self.play(title6.animate.to_edge(UP))
        
        practices = VGroup(
            Text("1. Be consistent with built-in behavior", font_size=28, color=YELLOW),
            Text("   • If you implement __eq__, also implement __hash__", font_size=22, color=WHITE),
            Text("   • __str__ should be readable, __repr__ unambiguous", font_size=22, color=WHITE),
            
            Text("\n2. Use operator overloading wisely", font_size=28, color=YELLOW),
            Text("   • Only implement operations that make sense for your class", font_size=22, color=WHITE),
            Text("   • Follow the principle of least surprise", font_size=22, color=WHITE),
            
            Text("\n3. Performance considerations", font_size=28, color=YELLOW),
            Text("   • __slots__ for memory-efficient classes", font_size=22, color=WHITE),
            Text("   • __getattr__ and __setattr__ can be slow", font_size=22, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.9).next_to(title6, DOWN, buff=1)
        
        self.play(Write(practices[0:3]))
        self.wait(1)
        self.play(Write(practices[3:6]))
        self.wait(1)
        self.play(Write(practices[6:]))
        self.wait(3)
        
        # Final slide
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        final = VGroup(
            Text("🎉 Key Takeaways", font_size=48, color=YELLOW),
            Text("• Magic methods make your objects Pythonic", font_size=32, color=WHITE),
            Text("• They enable operator overloading and built-in functions", font_size=32, color=WHITE),
            Text("• Implement them to make your classes intuitive", font_size=32, color=WHITE),
            Text("• Follow Python's conventions and best practices", font_size=32, color=WHITE)
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(final[0]))
        self.play(LaggedStart(*[Write(p) for p in final[1:]], lag_ratio=0.3))
        self.wait(3)
