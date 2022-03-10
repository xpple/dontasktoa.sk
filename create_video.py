from manim import *


class CreateVideo(Scene):
    def construct(self):
        dont_ask_to_ask = Text("Don't ask to ask!", gradient=(RED, GREEN, BLUE), font_size=100)
        self.play(Create(dont_ask_to_ask))
        instead = Text("Instead...", slant=ITALIC, font_size=100)
        self.play(ReplacementTransform(dont_ask_to_ask, instead))
        just_ask = Text("Just ask!", color=RED, font_size=150)
        self.play(
            FadeOut(instead, shift=UP),
            FadeIn(just_ask, shift=UP)
        )
        self.wait()


with tempconfig({
    "format": "gif",
}):
    CreateVideo().render()
