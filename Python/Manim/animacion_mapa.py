from manim import *

class ImageAnimation(Scene):
    def construct(self):
        # Cargar una imagen PNG
        image = ImageMobject("mapa_de_calor.png")  # Reemplaza "nombre_de_tu_imagen.png" con la ruta de tu imagen PNG

        # Escala la imagen según sea necesario
        image.scale(1.5)

        # Posiciona la imagen en el centro de la pantalla
        image.move_to(ORIGIN)

        # Anima la aparición de la imagen
        self.play(FadeIn(image))

        # Espera un tiempo
        self.wait(10)

        # Anima la desaparición de la imagen
        self.play(FadeOut(image))
