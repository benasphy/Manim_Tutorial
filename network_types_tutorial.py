from manim import *

class NetworkTypesTutorial(Scene):
    def construct(self):
        # Scene 1: What is a Network?
        self.scene_what_is_network()
        self.clear()

        # Scene 2: LAN (Local Area Network)
        self.scene_lan()
        self.clear()

        # Scene 3: WAN (Wide Area Network)
        self.scene_wan()
        self.clear()

        # Scene 4: Wi‑Fi
        self.scene_wifi()
        self.clear()

        # Scene 5: Mobile Networks (3G, 4G, 5G)
        self.scene_mobile()
        self.clear()

        # Scene 6: Starlink & Satellite Internet
        self.scene_satellite()
        self.clear()

        # Scene 7: Comparing Them All
        self.scene_comparison()
        self.clear()

        # Scene 8: Closing
        self.scene_closing()
        self.clear()

    def scene_what_is_network(self):
        title = Text("What is a Network?", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("Two or more devices connected to share information", font_size=28, color=WHITE),
            Text("Networks range from tiny (home) to massive (the Internet)", font_size=28, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        # Visual: nodes + roads
        n1 = self._node_circle("PC")
        n2 = self._node_circle("Phone")
        n3 = self._node_circle("Printer")
        nodes = VGroup(n1, n2, n3).arrange(RIGHT, buff=2.0).next_to(bullets, DOWN, buff=0.8)
        roads = VGroup(Line(n1.get_right(), n2.get_left(), color=GRAY), Line(n2.get_right(), n3.get_left(), color=GRAY))
        self.play(FadeIn(nodes, shift=UP))
        self.play(Create(roads))
        self.wait(1.5)

    def scene_lan(self):
        title = Text("LAN (Local Area Network)", font_size=48, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        definition = Text("A network within a small area: home, school, office", font_size=26, color=WHITE).next_to(title, DOWN, buff=0.6)
        example = Text("Example: Laptop + Printer on the same home Wi‑Fi", font_size=24, color=WHITE).next_to(definition, DOWN, buff=0.4)
        features = VGroup(
            Text("Small area", font_size=24, color=WHITE),
            Text("Fast and secure (local)", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(example, DOWN, buff=0.4)
        self.play(Write(definition))
        self.play(Write(example))
        self.play(Write(features))

        # Visual: router with local devices
        router = self._icon_router()
        pc = self._node_box("Laptop", self._icon_device())
        printer = self._node_box("Printer", self._icon_printer())
        group = VGroup(pc, router, printer).arrange(RIGHT, buff=1.2).next_to(features, DOWN, buff=0.8)
        links = VGroup(Arrow(pc.get_right(), router.get_left(), buff=0.2, color=WHITE), Arrow(router.get_right(), printer.get_left(), buff=0.2, color=WHITE))
        self.play(FadeIn(group, shift=UP))
        self.play(LaggedStart(*[GrowArrow(a) for a in links], lag_ratio=0.15))
        self.wait(1)

    def scene_wan(self):
        title = Text("WAN (Wide Area Network)", font_size=48, color=TEAL_E)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        definition = Text("Connects LANs across cities, countries, world", font_size=26, color=WHITE).next_to(title, DOWN, buff=0.6)
        example = Text("Example: Internet; bank branches connected nationwide", font_size=24, color=WHITE).next_to(definition, DOWN, buff=0.4)
        features = VGroup(
            Text("Huge coverage", font_size=24, color=WHITE),
            Text("Fiber, undersea cables, satellites", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(example, DOWN, buff=0.4)
        self.play(Write(definition))
        self.play(Write(example))
        self.play(Write(features))

        # Visual: globe with connected LANs
        globe = self._icon_globe()
        lan1 = self._lan_cluster()
        lan2 = self._lan_cluster()
        lan3 = self._lan_cluster()
        ring = VGroup(lan1, lan2, lan3).arrange_in_grid(rows=1, cols=3, buff=1.4).next_to(globe, DOWN, buff=0.6)
        self.play(FadeIn(globe, shift=UP))
        self.play(FadeIn(ring, shift=UP))
        connectors = VGroup(Line(lan1.get_top(), globe.get_bottom(), color=GRAY), Line(lan2.get_top(), globe.get_bottom(), color=GRAY), Line(lan3.get_top(), globe.get_bottom(), color=GRAY))
        self.play(*[Create(c) for c in connectors])
        self.wait(1)

    def scene_wifi(self):
        title = Text("Wi‑Fi", font_size=48, color=YELLOW)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        definition = Text("Wireless connection to a LAN using radio waves", font_size=26, color=WHITE).next_to(title, DOWN, buff=0.6)
        example = Text("Example: Connect laptop/phone without Ethernet cable", font_size=24, color=WHITE).next_to(definition, DOWN, buff=0.4)
        features = VGroup(
            Text("Convenient, no wires", font_size=24, color=WHITE),
            Text("Range ~30–100 m; speed depends on router/plan", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(example, DOWN, buff=0.4)
        self.play(Write(definition))
        self.play(Write(example))
        self.play(Write(features))

        wifi = self._icon_wifi()
        devices = VGroup(self._node_circle("Phone"), self._node_circle("Laptop"), self._node_circle("TV")).arrange(RIGHT, buff=1.0)
        row = VGroup(wifi, devices).arrange(DOWN, buff=0.6).next_to(features, DOWN, buff=0.8)
        self.play(FadeIn(row, shift=UP))
        waves = VGroup(
            ArcBetweenPoints(LEFT*0.6, RIGHT*0.6, angle=PI/2, color=WHITE).next_to(wifi, UP, buff=0.2),
            ArcBetweenPoints(LEFT*0.9, RIGHT*0.9, angle=PI/2, color=WHITE).next_to(wifi, UP, buff=0.05)
        )
        self.play(Create(waves))
        self.wait(1)

    def scene_mobile(self):
        title = Text("Mobile Networks (3G / 4G / 5G)", font_size=48, color=MAROON_E)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        definition = Text("Phone connects via cell towers (no Wi‑Fi needed)", font_size=26, color=WHITE).next_to(title, DOWN, buff=0.6)
        generations = VGroup(
            Text("3G: basic mobile Internet", font_size=24, color=WHITE),
            Text("4G: fast; streaming and gaming", font_size=24, color=WHITE),
            Text("5G: ultra‑fast, low‑latency; IoT scale", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(definition, DOWN, buff=0.4)
        self.play(Write(definition))
        self.play(Write(generations))

        tower = self._icon_cell_tower()
        phone = self._node_box("Phone", self._icon_device())
        row = VGroup(tower, phone).arrange(RIGHT, buff=1.2).next_to(generations, DOWN, buff=0.8)
        self.play(FadeIn(row, shift=UP))
        signal = VGroup(
            ArcBetweenPoints(LEFT*0.2, RIGHT*0.2, angle=PI/2, color=WHITE).next_to(tower, RIGHT, buff=0.1),
            ArcBetweenPoints(LEFT*0.35, RIGHT*0.35, angle=PI/2, color=WHITE).next_to(tower, RIGHT, buff=-0.05)
        )
        self.play(Create(signal))
        self.wait(1)

    def scene_satellite(self):
        title = Text("Starlink & Satellite Internet", font_size=48, color=TEAL_E)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        definition = Text("Home dish talks to satellites in orbit to reach the Internet", font_size=26, color=WHITE).next_to(title, DOWN, buff=0.6)
        why = Text("Great for remote areas without cables/towers", font_size=24, color=WHITE).next_to(definition, DOWN, buff=0.4)
        self.play(Write(definition))
        self.play(Write(why))

        earth = self._icon_globe()
        sat = self._icon_satellite()
        dish = self._icon_dish()
        row = VGroup(earth, sat, dish).arrange(RIGHT, buff=1.0).next_to(why, DOWN, buff=0.8)
        self.play(FadeIn(row, shift=UP))
        link1 = DashedLine(dish.get_top(), sat.get_bottom(), color=WHITE)
        link2 = DashedLine(sat.get_left(), earth.get_right(), color=WHITE)
        self.play(Create(link1), Create(link2))
        self.wait(1.5)

    def scene_comparison(self):
        title = Text("Comparing Network Types", font_size=48, color=YELLOW)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        header = VGroup(
            Text("Network", font_size=24, color=YELLOW),
            Text("Coverage", font_size=24, color=YELLOW),
            Text("Speed", font_size=24, color=YELLOW),
            Text("Example Use", font_size=24, color=YELLOW)
        ).arrange(RIGHT, buff=1.2).next_to(title, DOWN, buff=0.6)

        rows = [
            ("LAN", "Small (home/office)", "Very fast", "Sharing files, printers"),
            ("WAN", "Global", "Slower than LAN", "Internet, global banking"),
            ("Wi‑Fi", "Local (building)", "Fast", "Home, cafés, airports"),
            ("4G/5G", "Wide (city/country)", "Very fast (5G ultra)", "Smartphones, IoT"),
            ("Starlink", "Global (remote areas)", "Medium‑fast", "Rural Internet, ships")
        ]
        table_rows = VGroup()
        for a, b, c, d in rows:
            row = VGroup(
                Text(a, font_size=22, color=WHITE),
                Text(b, font_size=22, color=WHITE),
                Text(c, font_size=22, color=WHITE),
                Text(d, font_size=22, color=WHITE)
            ).arrange(RIGHT, buff=0.8)
            table_rows.add(row)
        table_rows.arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(header, DOWN, buff=0.5)

        self.play(Write(header))
        self.play(Write(table_rows))
        self.wait(2)

    def scene_closing(self):
        title = Text("Closing", font_size=44, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        closing = Text(
            "LAN connects small areas; WAN spans the world. Wi‑Fi connects you wirelessly,\n"
            "mobile networks (4G/5G) keep you online everywhere, and satellites bring\n"
            "Internet from space. Together they keep us connected — at home, work, or sea.",
            font_size=26, color=WHITE, line_spacing=1.0
        ).next_to(title, DOWN, buff=0.8)
        self.play(Write(closing))
        self.wait(3)

    # --- Helpers (icons built from primitives) ---
    def _node_circle(self, label: str) -> VGroup:
        c = Circle(radius=0.35, color=WHITE)
        t = Text(label, font_size=20, color=WHITE).move_to(c.get_center())
        return VGroup(c, t)

    def _node_box(self, label: str, icon: Mobject) -> VGroup:
        box = RoundedRectangle(width=2.4, height=1.4, corner_radius=0.1, color=WHITE)
        text = Text(label, font_size=20, color=WHITE).next_to(box.get_bottom(), UP, buff=0.02)
        ico = icon.copy().scale(0.6).move_to(box.get_center())
        return VGroup(box, ico, text)

    def _lan_cluster(self) -> VGroup:
        r = self._icon_router().scale(0.8)
        d1 = self._node_circle("PC").scale(0.8)
        d2 = self._node_circle("Phone").scale(0.8)
        cluster = VGroup(d1, r, d2).arrange(RIGHT, buff=0.6)
        return cluster

    def _icon_router(self) -> VGroup:
        body = RoundedRectangle(width=1.2, height=0.6, corner_radius=0.1, color=WHITE)
        leds = VGroup(*[Dot(radius=0.03, color=GREEN).next_to(body.get_bottom(), UP, buff=0.15).shift(RIGHT*(i*0.12-0.24)) for i in range(5)])
        ant = VGroup(Line(ORIGIN, UP*0.3, color=WHITE).next_to(body, UP, buff=0.02), Line(ORIGIN, UP*0.3, color=WHITE).next_to(body, UP, buff=0.02).shift(RIGHT*0.4))
        return VGroup(body, leds, ant)

    def _icon_wifi(self) -> VGroup:
        base = Dot(radius=0.06, color=WHITE)
        a1 = ArcBetweenPoints(LEFT*0.3, RIGHT*0.3, angle=PI/2, color=WHITE).shift(UP*0.2)
        a2 = ArcBetweenPoints(LEFT*0.5, RIGHT*0.5, angle=PI/2, color=WHITE).shift(UP*0.4)
        return VGroup(base, a1, a2)

    def _icon_device(self) -> VGroup:
        screen = RoundedRectangle(width=1.0, height=0.7, corner_radius=0.08, color=WHITE)
        base = Rectangle(width=0.4, height=0.06, color=WHITE).next_to(screen, DOWN, buff=0.06)
        return VGroup(screen, base)

    def _icon_printer(self) -> VGroup:
        body = RoundedRectangle(width=1.2, height=0.7, corner_radius=0.08, color=WHITE)
        paper = Rectangle(width=0.7, height=0.4, color=WHITE).next_to(body, DOWN, buff=0)
        return VGroup(body, paper)

    def _icon_globe(self) -> VGroup:
        globe = Circle(radius=0.7, color=WHITE)
        lat = VGroup(Line(LEFT*0.55, RIGHT*0.55, color=WHITE).shift(UP*0.25), Line(LEFT*0.55, RIGHT*0.55, color=WHITE), Line(LEFT*0.55, RIGHT*0.55, color=WHITE).shift(DOWN*0.25))
        lon = VGroup(Arc(radius=0.7, start_angle=-PI/2, angle=PI, color=WHITE), Arc(radius=0.7, start_angle=PI/2, angle=PI, color=WHITE))
        return VGroup(globe, lat, lon)

    def _icon_cell_tower(self) -> VGroup:
        mast = Polygon(ORIGIN, UP*1.2+LEFT*0.2, UP*1.2+RIGHT*0.2, color=WHITE)
        waves = VGroup(
            ArcBetweenPoints(LEFT*0.2, RIGHT*0.2, angle=PI/2, color=WHITE).next_to(mast, RIGHT, buff=0.1),
            ArcBetweenPoints(LEFT*0.35, RIGHT*0.35, angle=PI/2, color=WHITE).next_to(mast, RIGHT, buff=-0.05)
        )
        return VGroup(mast, waves)

    def _icon_satellite(self) -> VGroup:
        body = Rectangle(width=0.4, height=0.2, color=WHITE)
        panel_l = Rectangle(width=0.25, height=0.35, color=WHITE).next_to(body, LEFT, buff=0.05)
        panel_r = Rectangle(width=0.25, height=0.35, color=WHITE).next_to(body, RIGHT, buff=0.05)
        dish = ArcBetweenPoints(LEFT*0.12, RIGHT*0.12, angle=PI/1.5, color=WHITE).next_to(body, DOWN, buff=0.02)
        return VGroup(body, panel_l, panel_r, dish)

    def _icon_dish(self) -> VGroup:
        bowl = ArcBetweenPoints(LEFT*0.25, RIGHT*0.25, angle=PI/1.2, color=WHITE)
        stand = Line(ORIGIN, DOWN*0.3, color=WHITE)
        return VGroup(bowl, stand)
