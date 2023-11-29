from manim import *

class TextAnimation(Scene):
    def construct(self):
        # Creating text objects
        text1 = Text("Personas que respondieron: Sí", color=YELLOW).move_to(ORIGIN)  # Center of the screen
        
        text2 = Text("• Me criticó por el tipo de automovil, ya que es barato.", color=BLUE, font_size=32)
        text3 = Text("• He oído comentarios ofensivos por nivel socioeconómico.", color=BLUE, font_size=32)
        text4 = Text("• Chico del salón no quería relacionarse con becados.", color=BLUE, font_size=32)

        # Animating the first text to move to a corner
        self.play(Write(text1))  
        self.play(ApplyMethod(text1.move_to, UP+ UP + UP + LEFT * 2))
        self.wait(1.5)
        # Positioning subsequent texts
        text2.next_to(text1, DOWN  * 3, aligned_edge=LEFT, buff=0.2)
        text3.next_to(text2,  DOWN * 2, aligned_edge=LEFT, buff=0.2)
        text4.next_to(text3,  DOWN * 2 , aligned_edge=LEFT, buff=0.2)  # Corregir esta línea

        # text4.next_to(text3,  DOWN )  # Corregir esta línea
       
        # Animating the appearance of subsequent texts
        self.play(Write(text2), Write(text3), Write(text4))  # Animar text4 

        self.wait(5)

        self.play(FadeOut(text2), FadeOut(text3), FadeOut(text4))
        self.play(FadeOut(text1))