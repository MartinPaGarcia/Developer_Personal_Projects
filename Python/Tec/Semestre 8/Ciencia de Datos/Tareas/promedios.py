'''
Hecho por: Martín Palomares García
Matricula: A01066569
Fecha: 20/09/2023
Tarea: Promedios
'''

import numpy as np

def calcular_promedio(columna):
    return np.mean(columna.astype(float))

def calcular_varianza(columna):
    return np.var(columna.astype(float))

def calcular_promedio_ponderado(columna, pesos):
    return np.sum(columna.astype(float) * pesos) / np.sum(pesos)


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

    tabla = np.array(datos, dtype=object)

    imprimir_estadisticas(tabla)

if __name__ == "__main__":
    main()
