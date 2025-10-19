from manim import *

class GradientDescentDerivation(Scene):
    def construct(self):
        # Slide 1: Cost function
        slide1 = MathTex(
            r"J(w, b) = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})^2",
            font_size=70
        ).move_to(ORIGIN)
        self.play(FadeIn(slide1, scale=0.9))
        self.wait(2)
        self.play(FadeOut(slide1))

        # Slide 2: Substitute model
        slide2 = VGroup(
            MathTex(r"\hat{y}^{(i)} = wx^{(i)} + b", font_size=60),
            MathTex(r"J(w, b) = \frac{1}{m} \sum_{i=1}^{m} (wx^{(i)} + b - y^{(i)})^2", font_size=60)
        ).arrange(DOWN, buff=1.2).move_to(ORIGIN)
        self.play(FadeIn(slide2, scale=0.9))
        self.wait(2)
        self.play(FadeOut(slide2))

        # Slide 3: Partial derivatives
        slide3 = VGroup(
            MathTex(r"\frac{\partial J}{\partial w} = \frac{1}{m} \sum_{i=1}^{m} 2(wx^{(i)} + b - y^{(i)}) x^{(i)}", font_size=56),
            MathTex(r"\frac{\partial J}{\partial b} = \frac{1}{m} \sum_{i=1}^{m} 2(wx^{(i)} + b - y^{(i)})", font_size=56)
        ).arrange(DOWN, buff=1.2).move_to(ORIGIN)
        self.play(FadeIn(slide3, scale=0.9))
        self.wait(2)
        self.play(FadeOut(slide3))

        # Slide 4: Simplified gradients
        slide4 = VGroup(
            MathTex(r"\frac{\partial J}{\partial w} = \frac{1}{m} \sum_{i=1}^{m} (wx^{(i)} + b - y^{(i)}) x^{(i)}", font_size=56),
            MathTex(r"\frac{\partial J}{\partial b} = \frac{1}{m} \sum_{i=1}^{m} (wx^{(i)} + b - y^{(i)})", font_size=56)
        ).arrange(DOWN, buff=1.2).move_to(ORIGIN)
        self.play(FadeIn(slide4, scale=0.9))
        self.wait(2)
        self.play(FadeOut(slide4))

        # Slide 5: Update rules
        slide5 = VGroup(
            MathTex(r"w \leftarrow w - \alpha \frac{\partial J}{\partial w}", font_size=65),
            MathTex(r"b \leftarrow b - \alpha \frac{\partial J}{\partial b}", font_size=65)
        ).arrange(DOWN, buff=1.2).move_to(ORIGIN)
        self.play(FadeIn(slide5, scale=0.9))
        self.wait(2)
        self.play(FadeOut(slide5))

        # Slide 6: Summary
        summary = Text(
            "This is how gradient descent is derived\nfrom the cost function!",
            font_size=48,
            color=GREEN
        ).move_to(ORIGIN)
        self.play(FadeIn(summary, scale=0.9))
        self.wait(2)
        self.play(FadeOut(summary))

# To render this scene, run:
# manim -pql gradient_descent_derivation.py GradientDescentDerivation
