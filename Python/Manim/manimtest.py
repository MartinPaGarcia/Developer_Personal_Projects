from manim import *

class SocioeconomicSurveyBarChart(Scene):
    def construct(self):
        title = Text("Discriminación por nivel socioeconómico")
        title.to_edge(UP)

        data = {
            "Sí": 3,
            "No": 23,
        }

        # Convertir las claves y los valores del diccionario en listas
        bar_names = list(data.keys())
        values = list(data.values())

        colors = ["#FF0000", "#FFFF00", "#00FF00"]

        bar_chart = BarChart(
            values=values,
            bar_names=bar_names,
            bar_colors=colors,
            y_range=[0, 25, 5],
            y_length=5,
            x_length=5
        )

        self.play(Write(title))
        self.play(Create(bar_chart), run_time=3)
        self.wait(1)

        labels = bar_chart.get_bar_labels()
        self.play(Write(labels))
        self.wait(1)

        conclusion = Text("La mayoria se siente moderadamente comoda", color=WHITE)
        conclusion.next_to(bar_chart, DOWN)
        self.play(Write(conclusion))
        self.wait(2)
