from manim import *

class NetworkingAndInternetTutorial(Scene):
    def construct(self):
        # Scene: Core Concepts of the Internet
        self.core_concepts_scene()
        self.clear()

        # Scene: How Data Travels (Client/Server, DNS, Packets, Routers)
        self.data_travel_scene()
        self.clear()

        # Scene: Why This Matters
        self.why_matters_scene()
        self.clear()

        # Scene: Closing
        self.closing_scene()
        self.clear()

    def core_concepts_scene(self):
        title = Text("Networking and the Internet", font_size=50, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("Your device (client) talks to other computers (servers)", font_size=28, color=WHITE),
            Text("Every device has an IP address — like a digital address", font_size=28, color=WHITE),
            Text("DNS translates names (like example.com) into IP addresses", font_size=28, color=WHITE),
            Text("Data is split into packets and routed across networks", font_size=28, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        # Visual chips
        client = self._badge("Client", self._icon_device(), BLUE_E)
        server = self._badge("Server", self._icon_server(), TEAL_E)
        dns = self._badge("DNS", self._icon_dns(), YELLOW_E)
        router = self._badge("Router", self._icon_router(), PURPLE_E)
        row = VGroup(client, server, dns, router).arrange(RIGHT, buff=0.8).next_to(bullets, DOWN, buff=0.8)
        self.play(FadeIn(row, shift=UP))
        self.wait(1.5)

    def data_travel_scene(self):
        title = Text("How Data Travels", font_size=48, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Layout: Client -> DNS -> Router(s) -> Server
        client = self._node_box("Client", self._icon_device())
        dns = self._node_box("DNS", self._icon_dns())
        r1 = self._node_box("Router", self._icon_router())
        r2 = self._node_box("Router", self._icon_router())
        server = self._node_box("Server", self._icon_server())

        chain = VGroup(client, dns, r1, r2, server).arrange(RIGHT, buff=1.0).next_to(title, DOWN, buff=1.0)
        self.play(FadeIn(chain, shift=UP))

        # Arrows between nodes
        arrows = VGroup(
            Arrow(client.get_right(), dns.get_left(), buff=0.2, color=WHITE),
            Arrow(dns.get_right(), r1.get_left(), buff=0.2, color=WHITE),
            Arrow(r1.get_right(), r2.get_left(), buff=0.2, color=WHITE),
            Arrow(r2.get_right(), server.get_left(), buff=0.2, color=WHITE)
        )
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15))

        # Packets moving along the path
        packet_bits = ["0101", "1010", "1100"]
        packets = VGroup(*[self._packet(label=b) for b in packet_bits])
        for i, pkt in enumerate(packets):
            pkt.move_to(client.get_right() + RIGHT*0.3 + UP*(0.2 - 0.2*i))
        self.play(*[FadeIn(pkt, shift=RIGHT) for pkt in packets])

        # Animate packets hopping node to node
        hops = [dns, r1, r2, server]
        for hop in hops:
            self.play(*[pkt.animate.move_to(hop.get_right() + RIGHT*0.3 + UP*(0.2 - 0.2*i)) for i, pkt in enumerate(packets)], run_time=0.8)
        self.wait(1)

        caption = VGroup(
            Text("Client asks DNS for IP address", font_size=24, color=WHITE),
            Text("Data is split into packets", font_size=24, color=WHITE),
            Text("Routers forward packets toward the server", font_size=24, color=WHITE),
            Text("Server responds; packets return via network", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(chain, DOWN, buff=0.8)
        self.play(Write(caption))
        self.wait(1.5)

    def why_matters_scene(self):
        title = Text("Why This Matters", font_size=48, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        bullets = VGroup(
            Text("Slow connections: packets may take longer routes", font_size=28, color=WHITE),
            Text("Website crashes: the server is overloaded", font_size=28, color=WHITE),
            Text("Security: intercepted packets can leak data", font_size=28, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=0.8)
        self.play(Write(bullets))

        # Small visuals
        slow = self._badge("Slow Route", self._icon_path_variants(), GRAY)
        overload = self._badge("Overload", self._icon_server_hot(), MAROON_E)
        lock = self._badge("Security", self._icon_lock(), TEAL_E)
        row = VGroup(slow, overload, lock).arrange(RIGHT, buff=0.8).next_to(bullets, DOWN, buff=0.8)
        self.play(FadeIn(row, shift=UP))
        self.wait(1.5)

    def closing_scene(self):
        title = Text("Closing", font_size=44, color=GREEN)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        closing = Text(
            "The Internet is a global network: clients talk to servers via IP addresses.\n"
            "DNS helps find servers; data is split into packets; routers guide them worldwide.\n"
            "Within milliseconds, you get your video, message, or website.",
            font_size=26, color=WHITE, line_spacing=1.0
        ).next_to(title, DOWN, buff=0.8)
        self.play(Write(closing))
        self.wait(3)

    # Helpers: badges and icons
    def _badge(self, label: str, icon: Mobject, color=BLUE):
        chip = RoundedRectangle(width=3.2, height=1.2, corner_radius=0.15, color=color, fill_color=BLACK, fill_opacity=0.85)
        icon_group = icon.copy().scale(0.55).next_to(chip.get_left(), RIGHT, buff=0.3)
        text = Text(label, font_size=24, color=color).next_to(icon_group, RIGHT, buff=0.4)
        return VGroup(chip, icon_group, text)

    def _node_box(self, label: str, icon: Mobject) -> VGroup:
        box = RoundedRectangle(width=2.6, height=1.6, corner_radius=0.12, color=WHITE)
        text = Text(label, font_size=22, color=WHITE).next_to(box.get_bottom(), UP, buff=0.02)
        ico = icon.copy().scale(0.7).move_to(box.get_center())
        return VGroup(box, ico, text)

    def _packet(self, label: str = "0101") -> VGroup:
        rect = RoundedRectangle(width=0.8, height=0.4, corner_radius=0.08, color=WHITE)
        bits = Text(label, font_size=18, color=WHITE).move_to(rect.get_center())
        return VGroup(rect, bits)

    def _icon_device(self) -> VGroup:
        screen = RoundedRectangle(width=1.0, height=0.7, corner_radius=0.08, color=WHITE)
        base = Rectangle(width=0.4, height=0.06, color=WHITE).next_to(screen, DOWN, buff=0.06)
        return VGroup(screen, base)

    def _icon_server(self) -> VGroup:
        rack = VGroup(
            RoundedRectangle(width=0.8, height=1.2, corner_radius=0.06, color=WHITE),
            Line(LEFT*0.25, RIGHT*0.25, color=WHITE).shift(UP*0.25),
            Line(LEFT*0.25, RIGHT*0.25, color=WHITE),
            Line(LEFT*0.25, RIGHT*0.25, color=WHITE).shift(DOWN*0.25)
        )
        leds = VGroup(*[Dot(radius=0.03, color=GREEN).shift(DOWN*0.4 + RIGHT*(i*0.08 - 0.2)) for i in range(5)])
        return VGroup(rack, leds)

    def _icon_dns(self) -> VGroup:
        globe = Circle(radius=0.35, color=WHITE)
        lat = VGroup(Line(LEFT*0.3, RIGHT*0.3, color=WHITE).shift(UP*0.15), Line(LEFT*0.3, RIGHT*0.3, color=WHITE), Line(LEFT*0.3, RIGHT*0.3, color=WHITE).shift(DOWN*0.15))
        lon = VGroup(Arc(radius=0.35, start_angle=-PI/2, angle=PI, color=WHITE), Arc(radius=0.35, start_angle=PI/2, angle=PI, color=WHITE))
        return VGroup(globe, lat, lon)

    def _icon_router(self) -> VGroup:
        body = RoundedRectangle(width=1.0, height=0.5, corner_radius=0.1, color=WHITE)
        wifi = VGroup(
            ArcBetweenPoints(LEFT*0.2, RIGHT*0.2, angle=PI/2, color=WHITE).shift(UP*0.1),
            ArcBetweenPoints(LEFT*0.35, RIGHT*0.35, angle=PI/2, color=WHITE).shift(UP*0.3)
        )
        return VGroup(body, wifi)

    def _icon_path_variants(self) -> VGroup:
        path1 = VGroup(Dot(color=WHITE), Line(ORIGIN, RIGHT*0.6, color=WHITE), Line(RIGHT*0.6, RIGHT*1.2+UP*0.3, color=WHITE))
        path2 = VGroup(Dot(color=WHITE), Line(ORIGIN, RIGHT*0.4, color=WHITE), Line(RIGHT*0.4, RIGHT*1.0+DOWN*0.4, color=WHITE))
        return VGroup(path1, path2)

    def _icon_server_hot(self) -> VGroup:
        rack = self._icon_server()
        heat = VGroup(
            ArcBetweenPoints(ORIGIN, UP*0.4, angle=PI/3, color=RED).shift(RIGHT*0.3),
            ArcBetweenPoints(ORIGIN, UP*0.35, angle=PI/3, color=ORANGE).shift(RIGHT*0.5)
        )
        return VGroup(rack, heat)

    def _icon_lock(self) -> VGroup:
        lock = VGroup(
            RoundedRectangle(width=0.7, height=0.7, corner_radius=0.12, color=WHITE),
            ArcBetweenPoints(LEFT*0.25, RIGHT*0.25, angle=PI/1.2, color=WHITE).shift(UP*0.5),
            Dot(radius=0.05, color=WHITE)
        )
        return lock
