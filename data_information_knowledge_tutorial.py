from manim import *

class DataInformationKnowledgeTutorial(Scene):
    def construct(self):
        # Scene 1: Data – The Raw Material
        self.scene_data_raw()
        self.clear()

        # Scene 2: Information – Organized Data
        self.scene_information()
        self.clear()

        # Scene 3: Knowledge – Understanding & Insights
        self.scene_knowledge()
        self.clear()

        # Scene 4: Analogy (Super Simple)
        self.scene_analogy()
        self.clear()

        # Scene 5: Why This Matters
        self.scene_why_matters()
        self.clear()

    def scene_data_raw(self):
        title = Text("Data — The Raw Material", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        narration = VGroup(
            Text("Data = raw, unprocessed facts (symbols, numbers, words)", font_size=26, color=WHITE),
            Text("On its own, data has no context or meaning", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.8)
        self.play(Write(narration))

        # Visual: spreadsheet of random numbers/text without explanation
        grid = self._spreadsheet(rows=4, cols=6, labels=["25","30","28","27","Apple","Google","42","?","NA","17","30","MS"])
        grid.next_to(narration, DOWN, buff=0.8)
        self.play(FadeIn(grid, shift=UP))

        kitchen = Text("Like raw ingredients (flour, sugar, eggs) — not useful until organized", font_size=24, color=YELLOW)
        kitchen.next_to(grid, DOWN, buff=0.6)
        self.play(Write(kitchen))
        self.wait(1.5)

    def scene_information(self):
        title = Text("Information — Organized Data", font_size=50, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        narration = Text("Information = data with context and meaning (who/what/when/where)", font_size=26, color=WHITE)
        narration.next_to(title, DOWN, buff=0.8)
        self.play(Write(narration))

        # Example: Temperatures over 4 days
        data_lbl = Text("Data: 25, 30, 28, 27", font_size=24, color=WHITE).next_to(narration, DOWN, buff=0.6)
        info_lbl = Text("Information: Temperatures recorded over 4 days", font_size=24, color=YELLOW).next_to(data_lbl, DOWN, buff=0.3)
        self.play(Write(data_lbl))
        self.play(Write(info_lbl))

        chart = self._bar_chart(values=[25,30,28,27], labels=["Day 1","Day 2","Day 3","Day 4"]).next_to(info_lbl, DOWN, buff=0.8)
        self.play(FadeIn(chart, shift=UP))
        self.wait(1.5)

        # Another quick example
        ex2 = VGroup(
            Text("Data: Apple, Microsoft, Google", font_size=24, color=WHITE),
            Text("Information: Names of tech companies", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(chart, DOWN, buff=0.6)
        self.play(Write(ex2))
        self.wait(1)

    def scene_knowledge(self):
        title = Text("Knowledge — Understanding & Insights", font_size=50, color=TEAL_E)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        narration = Text("Knowledge = information + experience/understanding/reasoning (why/how)", font_size=26, color=WHITE).next_to(title, DOWN, buff=0.8)
        self.play(Write(narration))

        # Example: temperatures trend
        info_lbl = Text("Info: Daily temperatures", font_size=24, color=WHITE).next_to(narration, DOWN, buff=0.6)
        know_lbl = Text("Knowledge: Trend shows warming — summer may be starting", font_size=24, color=YELLOW).next_to(info_lbl, DOWN, buff=0.3)
        self.play(Write(info_lbl))
        self.play(Write(know_lbl))

        line = self._line_chart(values=[25,27,28,30]).next_to(know_lbl, DOWN, buff=0.8)
        self.play(Create(line))

        # Person + lightbulb
        person = self._icon_person()
        bulb = self._icon_bulb().next_to(person, UP, buff=0.2)
        side = VGroup(person, bulb).arrange(DOWN, buff=0.2).next_to(line, RIGHT, buff=1.0)
        self.play(FadeIn(side, shift=UP))
        self.wait(1.5)

        # Sales example
        sales = VGroup(
            Text("Data: list of sales numbers", font_size=24, color=WHITE),
            Text("Info: sales up 20% last month", font_size=24, color=WHITE),
            Text("Knowledge: ad campaign worked — repeat it", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(line, DOWN, buff=0.6)
        self.play(Write(sales))
        self.wait(1)

    def scene_analogy(self):
        title = Text("Analogy — Data → Information → Knowledge", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("Data: raw facts (letters)", font_size=26, color=WHITE),
            Text("Information: organized facts (words/sentences)", font_size=26, color=WHITE),
            Text("Knowledge: understanding (reading the book)", font_size=26, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        letters = VGroup(*[Text(ch, font_size=28, color=WHITE) for ch in list("A B C D E")] ).arrange(RIGHT, buff=0.2)
        words = VGroup(Text("HELLO", font_size=28, color=WHITE), Text("WORLD", font_size=28, color=WHITE)).arrange(RIGHT, buff=0.6)
        book = self._icon_book()
        learner = self._icon_person()
        row = VGroup(letters, words, book, learner).arrange(RIGHT, buff=0.8).next_to(bullets, DOWN, buff=0.8)
        self.play(FadeIn(row, shift=UP))
        self.wait(1.5)

    def scene_why_matters(self):
        title = Text("Why This Matters", font_size=48, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("We collect massive amounts of data — but it's noise without meaning", font_size=26, color=WHITE),
            Text("Processing → information; using it to decide → knowledge", font_size=26, color=WHITE),
            Text("This underpins data science, AI, business analytics", font_size=26, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        row = VGroup(
            self._badge("Data", self._icon_db(), BLUE_E),
            self._badge("Information", self._icon_chart(), TEAL_E),
            self._badge("Knowledge", self._icon_bulb(), YELLOW_E)
        ).arrange(RIGHT, buff=0.8).next_to(bullets, DOWN, buff=0.8)
        self.play(FadeIn(row, shift=UP))
        self.wait(2)

    # --- Helper visuals ---
    def _badge(self, label: str, icon: Mobject, color=BLUE):
        chip = RoundedRectangle(width=3.2, height=1.2, corner_radius=0.15, color=color, fill_color=BLACK, fill_opacity=0.85)
        icon_group = icon.copy().scale(0.6).next_to(chip.get_left(), RIGHT, buff=0.3)
        text = Text(label, font_size=24, color=color).next_to(icon_group, RIGHT, buff=0.4)
        return VGroup(chip, icon_group, text)

    def _spreadsheet(self, rows=4, cols=6, labels=None) -> VGroup:
        cells = VGroup()
        idx = 0
        for r in range(rows):
            row_cells = VGroup()
            for c in range(cols):
                rect = Rectangle(width=0.7, height=0.4, color=WHITE)
                txt = Text(labels[idx] if labels and idx < len(labels) else "", font_size=18, color=WHITE)
                txt.move_to(rect.get_center())
                row_cells.add(VGroup(rect, txt))
                idx += 1
            row_cells.arrange(RIGHT, buff=0)
            cells.add(row_cells)
        cells.arrange(DOWN, buff=0)
        table = VGroup(cells)
        return table

    def _bar_chart(self, values, labels) -> VGroup:
        # Simple bar chart using rectangles
        max_v = max(values) if values else 1
        bars = VGroup()
        lbls = VGroup()
        for v, lab in zip(values, labels):
            h = 0.05 * v
            bar = Rectangle(width=0.5, height=h, color=WHITE).set_fill(WHITE, opacity=0.2)
            bars.add(bar)
            lbls.add(Text(lab, font_size=18, color=WHITE))
        bars.arrange(RIGHT, buff=0.4)
        for i, bar in enumerate(bars):
            bar.align_to(ORIGIN, DOWN)
        # baseline and labels
        baseline = Line(LEFT* (len(values)*0.5), RIGHT*(len(values)*0.5), color=WHITE)
        baseline.next_to(bars, DOWN, buff=0.2)
        for label_mob, bar in zip(lbls, bars):
            label_mob.next_to(bar, DOWN, buff=0.1)
        chart = VGroup(bars, baseline, lbls)
        return chart

    def _line_chart(self, values) -> VGroup:
        # Simple polyline chart
        if not values:
            return VGroup()
        pts = []
        n = len(values)
        for i, v in enumerate(values):
            x = i * 0.8
            y = (v - min(values)) / max(1, (max(values) - min(values))) * 2.0
            pts.append(np.array([x, y, 0]))
        poly = VMobject(color=WHITE)
        poly.set_points_as_corners(pts)
        # axes
        x_axis = Line(LEFT*0.5, RIGHT*(0.8*(n-1)+0.5), color=WHITE)
        y_axis = Line(DOWN*0.3, UP*2.3, color=WHITE)
        grp = VGroup(x_axis, y_axis, poly)
        grp.shift(LEFT*0.5 + DOWN*0.8)
        return grp

    def _icon_person(self) -> VGroup:
        head = Circle(radius=0.15, color=WHITE)
        body = Line(ORIGIN, DOWN*0.5, color=WHITE)
        arms = VGroup(Line(ORIGIN, LEFT*0.3, color=WHITE), Line(ORIGIN, RIGHT*0.3, color=WHITE)).shift(DOWN*0.15)
        legs = VGroup(Line(ORIGIN, DOWN*0.35, color=WHITE).shift(LEFT*0.1), Line(ORIGIN, DOWN*0.35, color=WHITE).shift(RIGHT*0.1)).shift(DOWN*0.5)
        return VGroup(head, body, arms, legs)

    def _icon_bulb(self) -> VGroup:
        bulb = VGroup(Circle(radius=0.15, color=YELLOW), Rectangle(width=0.1, height=0.12, color=WHITE).next_to(ORIGIN, DOWN, buff=0))
        rays = VGroup(*[Line(ORIGIN, UP*0.25, color=YELLOW).rotate(i*PI/6) for i in range(12)]).shift(UP*0.1)
        return VGroup(bulb, rays)

    def _icon_book(self) -> VGroup:
        cover = RoundedRectangle(width=0.8, height=0.6, corner_radius=0.06, color=WHITE)
        spine = Rectangle(width=0.08, height=0.6, color=WHITE).next_to(cover, LEFT, buff=0)
        lines = VGroup(Line(LEFT*0.3, RIGHT*0.3, color=WHITE).shift(UP*0.1), Line(LEFT*0.3, RIGHT*0.3, color=WHITE), Line(LEFT*0.3, RIGHT*0.3, color=WHITE).shift(DOWN*0.1))
        lines.move_to(cover.get_center())
        return VGroup(cover, spine, lines)

    def _icon_db(self) -> VGroup:
        top = ArcBetweenPoints(LEFT*0.4, RIGHT*0.4, angle=PI/2, color=WHITE)
        body = Rectangle(width=0.8, height=0.5, color=WHITE).next_to(top, DOWN, buff=0)
        base = ArcBetweenPoints(RIGHT*0.4, LEFT*0.4, angle=PI/2, color=WHITE).next_to(body, DOWN, buff=0)
        return VGroup(top, body, base)

    def _icon_chart(self) -> VGroup:
        axes = VGroup(Line(ORIGIN, RIGHT*0.9, color=WHITE), Line(ORIGIN, UP*0.7, color=WHITE))
        bar = Rectangle(width=0.18, height=0.5, color=WHITE).set_fill(WHITE, opacity=0.2).move_to(RIGHT*0.5+UP*0.25)
        line = VMobject(color=WHITE)
        line.set_points_as_corners([np.array([0.1,0.1,0]), np.array([0.4,0.2,0]), np.array([0.8,0.6,0])])
        return VGroup(axes, bar, line)
