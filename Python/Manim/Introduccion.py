from manim import *

class Intro(Scene):
    def construct(self):

        image = ImageMobject("logoTEC.png")
        image.scale(1)
        text1 = Text("Discriminación socioeconómica", color=YELLOW).move_to(ORIGIN)  # Center of the screen
        
        text2 = Text("Elaborado por:", color=WHITE, font_size=32)
        text3 = Text("• Martín Palomares García A01066569", color=BLUE, font_size=26)
        text4 = Text("• Ivanna Garibay Lorea A01748694", color=PINK, font_size=26)
        text5 = Text("• Camila Delgado Gómez A01635485", color=PURPLE, font_size=26)
   
        self.play(Write(text1))  
        self.play(ApplyMethod(text1.move_to, UP+ UP + UP + LEFT * 2))
        self.wait(1.5)

        text2.next_to(text1, DOWN  * 3, aligned_edge=LEFT, buff=0.2)
        text3.next_to(text2,  DOWN * 2, aligned_edge=LEFT, buff=0.2)
        text4.next_to(text3,  DOWN * 2 , aligned_edge=LEFT, buff=0.2) 
        text5.next_to(text4,  DOWN * 2 , aligned_edge=LEFT, buff=0.2)

        image.next_to(text1, RIGHT + DOWN, buff=1.0)

       
       

        self.play(Write(text2), Write(text3), Write(text4), Write(text5))  
        self.play(FadeIn(image))
        self.wait(2)
        self.play(FadeOut(text2), FadeOut(text3), FadeOut(text4), FadeOut(text5))
        self.play(FadeOut(image))
        self.play(FadeOut(text1))