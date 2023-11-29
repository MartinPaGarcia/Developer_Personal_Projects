from manim import *

class Escala(Scene):
    def construct(self):
        title = Text("Escala: 1-10 (1 = No integrado, 10 = integrado)")
        title.to_edge(UP)

        data = {
            "3":3,
            "4":1,
            "5":2,
            "6":2,
            "7":4,
            "8":8,
            "9":3,
            "10":3,
        }

        # Convertir las claves y los valores del diccionario en listas
        bar_names = list(data.keys())
        values = list(data.values())
        
        x_values = [key for key in data]
        colors = ["#00FF00" if int(key) > 6 else "#FF0000" for key in x_values]

        bar_chart = BarChart(
            values=values,
            bar_names=bar_names,
            bar_colors=colors,
            y_range=[0, 10, 1],
            y_length=5,
            x_length=10
        )

        self.play(Write(title))
        self.play(Create(bar_chart), run_time=3)
        self.wait(1)

        labels = bar_chart.get_bar_labels()
        self.play(Write(labels))
        self.wait(1)

        conclusion = Text("La mayoria se siente mayormente integrado", color=WHITE)
        conclusion.next_to(bar_chart, DOWN)
        self.play(Write(conclusion))
        self.wait(10)
        self.play(FadeOut(title))
        self.play(FadeOut(labels), FadeOut(bar_chart))

        self.play(FadeOut(conclusion))
