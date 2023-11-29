from manim import *

class ImageAnimation(Scene):
    def construct(self):
        # Cargar una imagen PNG
        image = ImageMobject("mapa_de_calor.png")  

  
        image.scale(1.5)

    
        image.move_to(ORIGIN)

 
        self.play(FadeIn(image))


        self.wait(10)

        self.play(FadeOut(image))
