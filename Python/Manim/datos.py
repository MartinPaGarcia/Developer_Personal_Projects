from manim import *

class Aclaraciones(Scene):
    def construct(self):
        texto1 = Text(
            "Aclaraciones:",
            font_size=32,
            color=RED
        )

        texto2 = Text(
            "Aunque se vea como un trabajo simple, detrás de este video hay miles de ",
            font_size=24,
            color=WHITE
        )

        texto3 = Text(
            "líneas de código que fueron programadas con el propósito de generar el mejor contenido",
            font_size=24,
            color=WHITE
        )
        texto4 = Text(
            "posible para nuestro proyecto.",
            font_size=24,
            color=WHITE
        )

        texto5 = Text(
            "Utilizamos Python y manim para la elaboración de este video.",
            font_size=24,
            color=WHITE
        )

        # Alinea los textos uno debajo del otro
        texto1.next_to(texto2, UP + UP + UP)
        texto3.next_to(texto2, DOWN)
        texto4.next_to(texto3, DOWN)
        texto5.next_to(texto4, DOWN)

        self.play(Write(texto1))
        self.wait(1)
        self.play(Write(texto2))
        self.play(Write(texto3))
        self.play(Write(texto4))
        self.play(Write(texto5))
        self.wait(5)
        self.play(FadeOut(texto1))
        self.play(FadeOut(texto2))
        self.play(FadeOut(texto3))
        self.play(FadeOut(texto4))
        self.play(FadeOut(texto5))
