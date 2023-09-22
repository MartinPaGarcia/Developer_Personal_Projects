'''
Hecho por: Martín Palomares García
Matricula: A01066569
Fecha: 20/09/2023
Tarea: Promedios

Lo compliqué mucho, porque estoy intentado aprender nuevas formas de hacer las cosas

'''

import numpy as np

def calcular_promedio(columna):
    return sum(columna.astype(float)) / len(columna)

def calcular_varianza(columna):
    varianza = 0
    promedio = calcular_promedio(columna)
    for i in range(len(columna)):
        varianza += (columna[i] - promedio) ** 2
    varianza /= len(columna)

    return varianza
    
def promedio_ponderado(columna):
    total = 0
    peso_total = 0
    for i in range(len(columna)):
        peso = 1 / columna[i]
        total += columna[i] * peso
        peso_total += peso
    if peso_total == 0:
        return 0
    promedio_ponderado = total / peso_total
    return promedio_ponderado

def imprimir_promedios_ponderados(datos):
    edades = datos[1:,1].astype(float)
    estaturas = datos[1:,2].astype(float)
    pesos = datos[1:,3].astype(float)

    promedio_ponderado_edades = promedio_ponderado(edades)
    promedio_ponderado_estaturas = promedio_ponderado(estaturas)
    promedio_ponderado_pesos = promedio_ponderado(pesos)

    print(f"Promedio ponderado de edades: {promedio_ponderado_edades}")
    print(f"Promedio ponderado de estaturas: {promedio_ponderado_estaturas}")
    print(f"Promedio ponderado de pesos: {promedio_ponderado_pesos}")

def imprimir_estadisticas(datos):
    edades = datos[1:,1].astype(float)
    estaturas = datos[1:,2].astype(float)
    pesos = datos[1:,3].astype(float)

    promedio_edades = calcular_promedio(edades)
    promedio_estaturas = calcular_promedio(estaturas)
    promedio_pesos = calcular_promedio(pesos)

    varianza_edades = calcular_varianza(edades)
    varianza_estaturas = calcular_varianza(estaturas)
    varianza_pesos = calcular_varianza(pesos)


    print(f"Promedio de edades: {promedio_edades}")
    print(f"Promedio de estaturas: {promedio_estaturas}")
    print(f"Promedio de pesos: {promedio_pesos}")
    print(f"Varianza de edades: {varianza_edades}")
    print(f"Varianza de estaturas: {varianza_estaturas}")
    print(f"Varianza de pesos: {varianza_pesos}")



def main():
    datos = [
        ["Nombre", "Edad", "Estatura", "Peso"],
        ["Isa", 18, 160, 50],
        ["Azul", 18, 155, 50],
        ["Jose", 18, 175, 72],
        ["Diego", 18, 170, 62],
        ["Alfonso", 19, 188, 83],
        ["Angel", 18, 170, 70],
        ["Marisa", 19, 155, 46],
        ["Rodrigo", 19, 174, 65],
        ["Tomas", 18, 170, 55],
        ["Iker", 19, 165, 83]
    ]

    datos_para_ponderados = [
        ["Nombre", "Edad", "Estatura", "Peso"],
        ["Isa", 18, 160, 50],
        ["Azul", 18, 155, 50],
        ["Jose", 18, 175, 72],
        ["Diego", 18, 170, 62],
        ["Alfonso", 19, 188, 83],
        ["Angel", 18, 170, 70],
        ["Marisa", 19, 155, 46],
        ["Rodrigo", 19, 174, 65],
        ["Tomas", 18, 170, 55],
        ["Iker", 19, 165, 83],
        ["Javier",19, 194, 96],
        ["Mariana",14, 142, 38],
        ["Sofia", 18,168,74],
        ["Erick",23,201,98]
    ]


    tabla = np.array(datos, dtype=object)
    tabla_para_ponderados = np.array(datos_para_ponderados, dtype=object)

    imprimir_estadisticas(tabla)
    imprimir_promedios_ponderados(tabla_para_ponderados)

if __name__ == "__main__":
    main()
