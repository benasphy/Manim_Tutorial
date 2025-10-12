from manim import *

class AssociationRuleLearningTutorial(Scene):
    def construct(self):
        # Part 1: Introduction (3 scenes)
        self.scene1_intro_part1()
        self.clear()
        self.scene1_intro_part2()
        self.clear()
        self.scene1_intro_part3()
        self.clear()
        
        # Part 2: Key Terminologies (3 scenes)
        self.scene2_terminologies_part1()
        self.clear()
        self.scene2_terminologies_part2()
        self.clear()
        self.scene2_terminologies_part3()
        self.clear()
        
        # Part 3: Apriori Algorithm (3 scenes)
        self.scene3_apriori_part1()
        self.clear()
        self.scene3_apriori_part2()
        self.clear()
        self.scene3_apriori_part3()
        self.clear()
        
        # Part 4: Eclat Algorithm (3 scenes)
        self.scene4_eclat_part1()
        self.clear()
        self.scene4_eclat_part2()
        self.clear()
        self.scene4_eclat_part3()
        self.clear()
        
        # Part 5: Real-World Applications (3 scenes)
        self.scene5_applications_part1()
        self.clear()
        self.scene5_applications_part2()
        self.clear()
        self.scene5_applications_part3()
    
    def scene1_intro_part1(self):
        # Title
        title = Text("Association Rule Learning", font_size=48, color=BLUE)
        subtitle = Text("Discovering Hidden Patterns in Data", font_size=32, color=WHITE)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(1)
        
        # Main points
        points = VGroup(
            Text("• Finds relationships between items in large datasets", font_size=28, color=YELLOW),
            Text("• Answers questions like 'If A, then B?'", font_size=28, color=YELLOW),
            Text("• Widely used in market basket analysis", font_size=28, color=YELLOW),
            Text("• Powers recommendation systems", font_size=28, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(subtitle, DOWN, buff=1)
        
        self.play(LaggedStart(
            *[Write(point) for point in points],
            lag_ratio=0.3
        ))
        self.wait(2)
    
    def scene1_intro_part2(self):
        title = Text("Why Association Rule Learning?", font_size=42, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Example
        example_title = Text("Real-World Example:", font_size=30, color=GREEN).to_edge(LEFT, buff=1)
        example = Text("If a customer buys bread, how likely are they to also buy butter?", 
                      font_size=26, color=WHITE, line_spacing=1.2)
        example.next_to(example_title, DOWN, buff=0.5, aligned_edge=LEFT)
        
        self.play(Write(example_title))
        self.play(Write(example))
        
        # Use cases
        uses = VGroup(
            Text("Common Applications:", font_size=28, color=YELLOW).to_edge(LEFT, buff=1),
            Text("• Product recommendations", font_size=24, color=WHITE).next_to(example, DOWN, buff=1, aligned_edge=LEFT),
            Text("• Store layout optimization", font_size=24, color=WHITE).next_to(example, DOWN, buff=1.8, aligned_edge=LEFT),
            Text("• Cross-selling strategies", font_size=24, color=WHITE).next_to(example, DOWN, buff=2.6, aligned_edge=LEFT)
        )
        
        self.play(Write(uses[0]))
        self.play(Write(uses[1:]))
        
        self.wait(3)
    
    def scene2_terminologies_part1(self):
        title = Text("Key Terminologies (1/2)", font_size=42, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Itemset
        itemset = VGroup(
            Text("1. Itemset", font_size=30, color=YELLOW, weight=BOLD),
            Text("A collection of one or more items", font_size=26, color=WHITE),
            Text("Example: {milk, bread, butter}", font_size=24, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=1)
        
        self.play(Write(itemset))
        self.wait(1)
        
        # Support
        support = VGroup(
            Text("2. Support", font_size=30, color=YELLOW, weight=BOLD),
            Text("Proportion of transactions containing an itemset", font_size=26, color=WHITE),
            MathTex(
                r"\text{Support}(A) = \frac{\text{Number of transactions containing } A}{\text{Total transactions}}",
                font_size=28
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(itemset, DOWN, buff=1, aligned_edge=LEFT)
        
        self.play(Write(support))
        self.wait(2)
    
    def scene2_terminologies_part2(self):
        title = Text("Key Terminologies (2/2)", font_size=42, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Confidence
        confidence = VGroup(
            Text("3. Confidence", font_size=30, color=YELLOW, weight=BOLD),
            Text("Likelihood of B being bought when A is bought", font_size=26, color=WHITE),
            MathTex(
                r"\text{Confidence}(A \Rightarrow B) = \frac{\text{Support}(A \cup B)}{\text{Support}(A)}",
                font_size=28
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=1)
        
        self.play(Write(confidence))
        self.wait(1)
        
        # Lift
        lift = VGroup(
            Text("4. Lift", font_size=30, color=YELLOW, weight=BOLD),
            Text("How much more likely A and B occur together", font_size=26, color=WHITE),
            MathTex(
                r"\text{Lift}(A \Rightarrow B) = \frac{\text{Confidence}(A \Rightarrow B)}{\text{Support}(B)}",
                font_size=28
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(confidence, DOWN, buff=1)
        
        lift_interpretation = VGroup(
            Text("Interpretation:", font_size=26, color=YELLOW, weight=BOLD),
            Text("• Lift > 1: Positive correlation", font_size=24, color=GREEN),
            Text("• Lift = 1: No correlation", font_size=24, color=YELLOW),
            Text("• Lift < 1: Negative correlation", font_size=24, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(lift, DOWN, buff=1)
        
        self.play(Write(lift))
        self.wait(1)
        self.play(Write(lift_interpretation))
        self.wait(2)
    
    def scene2_terminologies_part3(self):
        title = Text("Terminology in Practice", font_size=42, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Example scenario
        scenario = VGroup(
            Text("Example Scenario:", font_size=32, color=YELLOW, weight=BOLD),
            Text("• Total transactions: 1,000", font_size=24, color=WHITE),
            Text("• {Milk, Bread} appears in 300 transactions", font_size=24, color=WHITE),
            Text("• {Milk, Bread, Butter} appears in 200 transactions", font_size=24, color=WHITE),
            Text("• {Butter} appears in 500 transactions", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=1)
        
        self.play(Write(scenario))
        self.wait(2)
        
        # Calculations
        calculations = VGroup(
            Text("Calculations:", font_size=32, color=YELLOW, weight=BOLD),
            MathTex(
                r"\text{Support}(\{\text{Milk}, \text{Bread}\} \Rightarrow \{\text{Butter}\}) = \frac{200}{1000} = 0.2",
                font_size=26
            ),
            MathTex(
                r"\text{Confidence} = \frac{200}{300} \approx 0.67",
                font_size=26
            ),
            MathTex(
                r"\text{Lift} = \frac{0.67}{0.5} = 1.34",
                font_size=26
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(scenario, DOWN, buff=1)
        
        self.play(Write(calculations[0]))
        self.wait(0.5)
        self.play(Write(calculations[1]))
        self.wait(0.5)
        self.play(Write(calculations[2]))
        self.wait(0.5)
        self.play(Write(calculations[3]))
        
        # Interpretation
        conclusion = Text("Interpretation: 1.34x more likely to buy Butter with Milk & Bread", 
                         font_size=24, color=GREEN).next_to(calculations, DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(3)
    
    def scene3_apriori_part1(self):
        title = Text("Apriori Algorithm", font_size=42, color=BLUE)
        principle = Text("Principle: A larger itemset is only frequent if all its subsets are frequent", 
                        font_size=28, color=YELLOW, line_spacing=1.2)
        principle.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(Write(principle))
        
        # Overview
        overview = VGroup(
            Text("Apriori Overview:", font_size=30, color=YELLOW, weight=BOLD),
            Text("• Bottom-up approach to find frequent itemsets", font_size=26, color=WHITE),
            Text("• Uses a level-wise search using k-itemsets", font_size=26, color=WHITE),
            Text("• Applies the Apriori property to prune the search space", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(principle, DOWN, buff=1)
        
        self.play(Write(overview[0]))
        self.play(Write(overview[1:]))
        self.wait(2)
        
        # Example transactions
        transactions_title = Text("Example Transactions:", font_size=26, color=WHITE).next_to(overview, DOWN, buff=1)
        transactions = VGroup(
            Text("1. {Milk, Bread, Butter}", font="Monospace", font_size=22, color=GREEN),
            Text("2. {Bread, Butter}", font="Monospace", font_size=22, color=GREEN),
            Text("3. {Milk, Bread}", font="Monospace", font_size=22, color=GREEN),
            Text("4. {Milk, Butter}", font="Monospace", font_size=22, color=GREEN),
            Text("5. {Milk, Bread, Butter}", font="Monospace", font_size=22, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(transactions_title, DOWN, buff=0.5)
        
        self.play(Write(transactions_title))
        self.play(Write(transactions))
        self.wait(2)
        
    def scene3_apriori_part2(self):
        title = Text("Apriori: How It Works", font_size=42, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Step-by-step process
        steps = VGroup(
            Text("Apriori Algorithm Steps:", font_size=32, color=YELLOW, weight=BOLD),
            Text("1. Generate candidate 1-itemsets", font_size=26, color=WHITE),
            Text("2. Prune infrequent itemsets (support < min_support)", font_size=26, color=WHITE),
            Text("3. Generate candidate (k+1)-itemsets from frequent k-itemsets", font_size=26, color=WHITE),
            Text("4. Repeat steps 2-3 until no more frequent itemsets", font_size=26, color=WHITE),
            Text("5. Generate association rules from frequent itemsets", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(title, DOWN, buff=1)
        
        self.play(Write(steps[0]))
        self.play(Write(steps[1:]))
        self.wait(2)
        
        # Visualization of the process
        process = VGroup(
            Text("Visualization of the Process:", font_size=32, color=YELLOW, weight=BOLD),
            Text("1-itemsets → Prune → 2-itemsets → Prune → ...", font_size=26, color=WHITE),
            Text("Example with min_support = 2:", font_size=24, color=GREEN),
            Text("• {Milk}:3, {Bread}:4, {Butter}:4  (all ≥ 2)", font_size=22, color=WHITE),
            Text("• {Milk,Bread}:3, {Milk,Butter}:3, {Bread,Butter}:3", font_size=22, color=WHITE),
            Text("• {Milk,Bread,Butter}:2  (frequent)", font_size=22, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(steps, DOWN, buff=1)
        
        self.play(Write(process[0:2]))
        self.wait(0.5)
        self.play(Write(process[2:]))
        self.wait(3)
        
    def scene3_apriori_part3(self):
        title = Text("Apriori: Rule Generation", font_size=42, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Rule generation explanation
        explanation = VGroup(
            Text("Generating Association Rules:", font_size=32, color=YELLOW, weight=BOLD),
            Text("1. For each frequent itemset I, generate all non-empty subsets", font_size=24, color=WHITE),
            Text("2. For every subset A of I, form a rule A → (I - A)", font_size=24, color=WHITE),
            Text("3. Calculate confidence for each rule", font_size=24, color=WHITE),
            Text("4. Keep rules with confidence ≥ min_confidence", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(title, DOWN, buff=1)
        
        self.play(Write(explanation[0]))
        self.play(Write(explanation[1:]))
        self.wait(2)
        
        # Rule example
        rule = VGroup(
            Text("Example Rule: {Milk, Bread} → {Butter}", font_size=30, color=YELLOW, weight=BOLD),
            MathTex(
                r"\text{Support} = \frac{\text{Transactions with {Milk, Bread, Butter}}}{\text{Total transactions}} = \frac{3}{5} = 0.6",
                font_size=24
            ),
            MathTex(
                r"\text{Confidence} = \frac{\text{Support(\{Milk, Bread, Butter\})}}{\text{Support(\{Milk, Bread\})}} = \frac{3/5}{3/5} = 1",
                font_size=22
            ),
            MathTex(
                r"\text{Lift} = \frac{\text{Confidence}}{\text{Support(Butter)}} = \frac{1}{0.8} = 1.25",
                font_size=24
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(explanation, DOWN, buff=1)
        
        self.play(Write(rule[0]))
        self.wait(0.5)
        self.play(Write(rule[1]))
        self.wait(0.5)
        self.play(Write(rule[2]))
        self.wait(0.5)
        self.play(Write(rule[3]))
        
        # Interpretation
        interpretation = VGroup(
            Text("Interpretation:", font_size=28, color=YELLOW, weight=BOLD),
            Text("• Confidence = 1: 100% of the time, customers who buy", font_size=22, color=WHITE),
            Text("  Milk and Bread also buy Butter", font_size=22, color=WHITE),
            Text("• Lift > 1: Positive correlation between {Milk, Bread} and Butter", font_size=22, color=GREEN),
            Text("• Practical significance: Strong rule worth considering for promotions", font_size=22, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(rule, DOWN, buff=1, aligned_edge=LEFT)
        
        self.play(Write(interpretation))
        self.wait(3)
        
    def scene5_applications_part3(self):
        title = Text("Key Takeaways & Next Steps", font_size=42, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Key takeaways
        takeaways = VGroup(
            Text("Key Takeaways:", font_size=32, color=YELLOW, weight=BOLD),
            Text("• Association Rule Learning uncovers relationships in large datasets", font_size=24, color=WHITE),
            Text("• Apriori: Level-wise search with candidate generation and pruning", font_size=24, color=WHITE),
            Text("• Eclat: Depth-first search using vertical data format", font_size=24, color=WHITE),
            Text("• Support, Confidence, and Lift help evaluate rule quality", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(title, DOWN, buff=1)
        
        self.play(Write(takeaways[0]))
        self.play(Write(takeaways[1:]))
        self.wait(2)
        
        # Implementation tips
        tips = VGroup(
            Text("Implementation Tips:", font_size=32, color=YELLOW, weight=BOLD).next_to(takeaways, DOWN, buff=1),
            Text("• Start with high min_support and lower gradually", font_size=22, color=WHITE),
            Text("• Use confidence and lift to filter meaningful rules", font_size=22, color=WHITE),
            Text("• Consider computational complexity with large datasets", font_size=22, color=WHITE),
            Text("• Visualize results for better interpretation", font_size=22, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        self.play(Write(tips[0]))
        self.play(Write(tips[1:]))
        self.wait(2)
        
        # Next steps
        next_steps = VGroup(
            Text("Next Steps:", font_size=32, color=YELLOW, weight=BOLD).next_to(tips, DOWN, buff=1),
            Text("• Try implementing Apriori/Eclat on your own data", font_size=22, color=GREEN),
            Text("• Explore FP-Growth algorithm (another popular method)", font_size=22, color=WHITE),
            Text("• Learn about rule quality measures beyond support/confidence/lift", font_size=22, color=WHITE),
            Text("• Consider parallel implementations for large-scale datasets", font_size=22, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        self.play(Write(next_steps[0]))
        self.play(Write(next_steps[1:]))
        self.wait(3)
        
        # Final message
        final_msg = Text("Thank you for learning about Association Rule Learning!", 
                        font_size=32, color=YELLOW, weight=BOLD)
        self.play(ReplacementTransform(VGroup(title, takeaways, tips, next_steps), final_msg))
        self.wait(2)
        
    def scene5_applications_part2(self):
        title = Text("Applications (2/2)", font_size=42, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # More applications
        apps = VGroup(
            Text("3. Healthcare:", font_size=30, color=YELLOW, weight=BOLD),
            Text("• Disease-symptom relationships", font_size=26, color=WHITE),
            Text("• Drug interaction analysis", font_size=26, color=WHITE),
            Text("• Treatment effectiveness patterns", font_size=26, color=WHITE),
            Text("4. Other Applications:", font_size=30, color=YELLOW, weight=BOLD).next_to(apps[3], DOWN, aligned_edge=LEFT, buff=0.5),
            Text("• Web usage mining", font_size=26, color=WHITE),
            Text("• Fraud detection", font_size=26, color=WHITE),
            Text("• Bioinformatics", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(title, DOWN, buff=1)
        
        self.play(Write(apps[0:4]))
        self.play(title.animate.to_edge(UP))
        
        # Rule generation explanation
        explanation = VGroup(
            Text("Generating Association Rules:", font_size=32, color=YELLOW, weight=BOLD),
            Text("1. For each frequent itemset I, generate all non-empty subsets", font_size=24, color=WHITE),
            Text("2. For every subset A of I, form a rule A → (I - A)", font_size=24, color=WHITE),
            Text("3. Calculate confidence for each rule", font_size=24, color=WHITE),
            Text("4. Keep rules with confidence ≥ min_confidence", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(title, DOWN, buff=1)
        
        self.play(Write(explanation[0]))
        self.play(Write(explanation[1:]))
        self.wait(2)
        
        # Rule example
        rule = VGroup(
            Text("Example Rule: {Milk, Bread} → {Butter}", font_size=30, color=YELLOW, weight=BOLD),
            MathTex(
                r"\text{Support} = \frac{\text{Transactions with {Milk, Bread, Butter}}}{\text{Total transactions}} = \frac{3}{5} = 0.6",
                font_size=24
            ),
            MathTex(
                r"\text{Confidence} = \frac{\text{Support(\{Milk, Bread, Butter\})}}{\text{Support(\{Milk, Bread\})}} = \frac{3/5}{3/5} = 1",
                font_size=22
            ),
            MathTex(
                r"\text{Lift} = \frac{\text{Confidence}}{\text{Support(Butter)}} = \frac{1}{0.8} = 1.25",
                font_size=24
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(explanation, DOWN, buff=1)
        
        self.play(Write(rule[0]))
        self.wait(0.5)
        self.play(Write(rule[1]))
        self.wait(0.5)
        self.play(Write(rule[2]))
        self.wait(0.5)
        self.play(Write(rule[3]))
        
        # Interpretation
        interpretation = VGroup(
            Text("Interpretation:", font_size=28, color=YELLOW, weight=BOLD),
            Text("• Confidence = 1: 100% of the time, customers who buy", font_size=22, color=WHITE),
            Text("  Milk and Bread also buy Butter", font_size=22, color=WHITE),
            Text("• Lift > 1: Positive correlation between {Milk, Bread} and Butter", font_size=22, color=GREEN),
            Text("• Practical significance: Strong rule worth considering for promotions", font_size=22, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(rule, DOWN, buff=1, aligned_edge=LEFT)
        
        steps = VGroup(
            Text("2. Algorithm Steps:", font_size=30, color=YELLOW, weight=BOLD),
            Text("1. Convert horizontal format to vertical format (TID-lists)", font_size=22, color=WHITE),
            Text("2. For each item, find its TID-list", font_size=22, color=WHITE),
            Text("3. For each pair of items, compute intersection of TID-lists", font_size=22, color=WHITE),
            Text("4. If intersection size ≥ min_support, keep the itemset", font_size=22, color=WHITE),
            Text("5. Recursively combine itemsets and repeat", font_size=22, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(data_format, DOWN, buff=1)
        
        self.play(Write(steps[0]))
        self.play(Write(steps[1:]))
        self.wait(3)
        
        # Vertical data format
        vertical_title = Text("Vertical Data Format:", font_size=26, color=WHITE).next_to(steps, DOWN, buff=1)
        vertical_data = VGroup(
            Text("{Milk}: {T1, T3, T4, T5}", font="Monospace", font_size=22, color=GREEN),
            Text("{Bread}: {T1, T2, T3, T5}", font="Monospace", font_size=22, color=GREEN),
            Text("{Butter}: {T1, T2, T4, T5}", font="Monospace", font_size=22, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(vertical_title, DOWN, buff=0.5)
        
        self.play(Write(vertical_title))
        self.play(Write(vertical_data))
        self.wait(2)

    def scene4_eclat_part1(self):
        title = Text("Eclat Algorithm", font_size=42, color=BLUE)
        principle = Text("Principle: Uses vertical data format and set intersections", 
                        font_size=28, color=YELLOW, line_spacing=1.2)
        principle.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(Write(principle))
        
        # Overview
        overview = VGroup(
            Text("Eclat Overview:", font_size=30, color=YELLOW, weight=BOLD),
            Text("• Depth-first search approach for frequent itemset mining", font_size=24, color=WHITE),
            Text("• Uses vertical data format (TID-lists) for efficiency", font_size=24, color=WHITE),
            Text("• Faster than Apriori for dense datasets with many transactions", font_size=24, color=WHITE),
            Text("• Memory-intensive due to storing TID-lists", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(principle, DOWN, buff=1)
        
        self.play(Write(overview[0]))
        self.play(Write(overview[1:]))
        self.wait(2)
        
    def scene4_eclat_part2(self):
        title = Text("Eclat: How It Works", font_size=42, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Data format explanation
        data_format = VGroup(
            Text("1. Data Format Conversion:", font_size=30, color=YELLOW, weight=BOLD),
            Text("Horizontal Format:", font_size=26, color=WHITE, weight=BOLD),
            Text("T1: {A,B,C}\nT2: {A,C,D}\nT3: {B,C,D}", font="Monospace", font_size=22, color=GREEN),
            Text("Vertical Format (TID-lists):", font_size=26, color=WHITE, weight=BOLD),
            Text("A: {T1,T2}\nB: {T1,T3}\nC: {T1,T2,T3}\nD: {T2,T3}", font="Monospace", font_size=22, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(title, DOWN, buff=1)
        
        self.play(Write(data_format[0:3]))
        self.wait(1)
        self.play(Write(data_format[3:]))
        self.wait(2)
        
        # Algorithm steps
        steps = VGroup(
            Text("2. Algorithm Steps:", font_size=30, color=YELLOW, weight=BOLD),
            Text("1. Convert horizontal format to vertical format (TID-lists)", font_size=22, color=WHITE),
            Text("2. For each item, find its TID-list", font_size=22, color=WHITE),
            Text("3. For each pair of items, compute intersection of TID-lists", font_size=22, color=WHITE),
            Text("4. If intersection size ≥ min_support, keep the itemset", font_size=22, color=WHITE),
            Text("5. Recursively combine itemsets and repeat", font_size=22, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(data_format, DOWN, buff=1)
        
        self.play(Write(steps[0]))
        self.play(Write(steps[1:]))
        self.wait(3)
        
    def scene4_eclat_part3(self):
        title = Text("Eclat: Set Intersection", font_size=42, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Set intersection example with explanation
        explanation = VGroup(
            Text("Finding Support with Set Intersection:", font_size=30, color=YELLOW, weight=BOLD),
            Text("To find support of {Milk, Bread}:", font_size=26, color=WHITE),
            MathTex(
                r"\text{Support}(\{\text{Milk}, \text{Bread}\}) = |\{T1, T3, T5\}| = 3",
                font_size=28
            ),
            Text("Which means {Milk, Bread} appears in 3 transactions", font_size=24, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(title, DOWN, buff=1).to_edge(LEFT, buff=1)
        
        self.play(Write(explanation))
        self.wait(2)
        
        # Advantages
        advantages = VGroup(
            Text("Advantages of Eclat:", font_size=30, color=YELLOW, weight=BOLD),
            Text("• More efficient than Apriori for dense datasets", font_size=26, color=WHITE),
            Text("• Uses less memory due to vertical format", font_size=26, color=WHITE),
            Text("• Faster for large datasets with many items", font_size=26, color=WHITE),
            Text("• Better performance with many transactions", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(explanation, DOWN, buff=1, aligned_edge=LEFT)
        
        self.play(Write(advantages))
        self.wait(3)

    def scene1_intro_part1(self):
        title = Text("Introduction to Association Rule Learning", font_size=42, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # What is ARL?
        arl = VGroup(
            Text("What is Association Rule Learning?", font_size=32, color=YELLOW, weight=BOLD),
            Text("• A technique for discovering interesting patterns in data", font_size=26, color=WHITE),
            Text("• Finds relationships between items in a dataset", font_size=26, color=WHITE),
            Text("• Used in market basket analysis, recommendation systems, and more", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(title, DOWN, buff=1)
        
        self.play(Write(arl))
        self.wait(2)
        
        # Key concepts
        concepts = VGroup(
            Text("Key Concepts:", font_size=32, color=YELLOW, weight=BOLD),
            Text("• Support", font_size=28, color=WHITE),
            Text("• Confidence", font_size=28, color=WHITE),
            Text("• Lift", font_size=28, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(arl, DOWN, buff=1)
        
        self.play(Write(concepts))
        self.wait(2)

    def scene1_intro_part2(self):
        title = Text("Why Association Rule Learning?", font_size=42, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Common applications
        apps = VGroup(
            Text("Common Applications:", font_size=32, color=YELLOW, weight=BOLD),
            Text("• Market Basket Analysis", font_size=28, color=WHITE),
            Text("• Recommendation Systems", font_size=28, color=WHITE),
            Text("• Cross-selling Strategies", font_size=28, color=WHITE),
            Text("• Product Placement", font_size=28, color=WHITE),
            Text("• Medical Diagnosis", font_size=28, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(title, DOWN, buff=1)
        
        self.play(Write(apps[0]))
        self.play(Write(apps[1:]))
        self.wait(2)
        
    def scene1_intro_part3(self):
        title = Text("ARL in Action", font_size=42, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Real-world impact
        impact = VGroup(
            Text("Real-world Impact:", font_size=32, color=YELLOW, weight=BOLD),
            Text("• 30% increase in sales from product recommendations", font_size=24, color=WHITE),
            Text("• 25% improvement in customer satisfaction scores", font_size=24, color=WHITE),
            Text("• 40% reduction in search time for relevant content", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(title, DOWN, buff=1)
        
        # Business value
        value = VGroup(
            Text("Business Value:", font_size=32, color=YELLOW, weight=BOLD),
            Text("• Increased revenue through cross-selling", font_size=24, color=WHITE),
            Text("• Improved customer experience with personalized suggestions", font_size=24, color=WHITE),
            Text("• Better inventory management through demand prediction", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(impact, DOWN, buff=1)
        
        self.play(Write(impact))
        self.wait(1.5)
        self.play(Write(value))
        self.wait(3)
        
    def scene5_applications_part1(self):
        title = Text("Real-World Applications (1/2)", font_size=42, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # E-commerce
        ecommerce = VGroup(
            Text("🛒 E-commerce & Retail:", font_size=30, color=YELLOW, weight=BOLD),
            Text("• Product recommendations (People who bought X also bought Y)", font_size=24, color=WHITE),
            Text("• Cross-selling suggestions (Frequently bought together)", font_size=24, color=WHITE),
            Text("• Market basket analysis (Which items are often purchased together?)", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(title, DOWN, buff=1).to_edge(LEFT, buff=1)
        
        self.play(Write(ecommerce))
        self.wait(2)
        
        # Media
        media = VGroup(
            Text("🎬 Media & Content:", font_size=30, color=YELLOW, weight=BOLD),
            Text("• Content recommendations (Because you watched X, you might like Y)", font_size=24, color=WHITE),
            Text("• Playlist generation (Songs that are often played together)", font_size=24, color=WHITE),
            Text("• Next video/article suggestions (Readers who liked X also read Y)", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(ecommerce, DOWN, buff=1, aligned_edge=LEFT)
        
        self.play(Write(media))
        self.wait(2)

    def scene5_applications_part2(self):
        title = Text("Real-World Applications (2/2)", font_size=42, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Healthcare
        healthcare = VGroup(
            Text("🏥 Healthcare:", font_size=30, color=YELLOW, weight=BOLD),
            Text("• Drug interaction analysis (Which medications are often prescribed together?)", font_size=24, color=WHITE),
            Text("• Symptom-disease correlation (Which symptoms co-occur with certain diseases?)", font_size=24, color=WHITE),
            Text("• Treatment effectiveness (Which treatments are most effective for which conditions?)", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(title, DOWN, buff=1).to_edge(LEFT, buff=1)
        
        self.play(Write(healthcare))
        self.wait(2)
        
        # Additional Applications
        other = VGroup(
            Text("🌐 Other Applications:", font_size=30, color=YELLOW, weight=BOLD),
            Text("• Fraud detection (Which transactions are likely fraudulent?)", font_size=24, color=WHITE),
            Text("• Website navigation (Which pages are often visited in sequence?)", font_size=24, color=WHITE),
            Text("• Customer behavior analysis (What are common customer journeys?)", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(healthcare, DOWN, buff=1, aligned_edge=LEFT)
        
        self.play(Write(other))
        self.wait(2)
        
        # Key Takeaways
        takeaways = VGroup(
            Text("🔑 Key Takeaways:", font_size=32, color=YELLOW, weight=BOLD).to_edge(DOWN, buff=0.5),
            Text("• ARL reveals hidden patterns in transaction data", font_size=24, color=WHITE),
            Text("• Apriori: Bottom-up approach, uses horizontal format", font_size=24, color=WHITE),
            Text("• Eclat: Uses vertical format, efficient for large datasets", font_size=24, color=WHITE),
            Text("• Support, confidence, and lift help identify meaningful rules", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(DOWN, buff=0.5)
        
        self.play(Write(takeaways))
        self.wait(3)

# Run with: manim -pql association_rule_learning_tutorial.py AssociationRuleLearningTutorial
