'''
Autor: Isabela Corena
Maticula: 
Fecha: 19/09/2023

'''

def calcular_promedio(valores):
    suma = sum(valores)
    promedio = suma / len(valores)
    return promedio

def calcular_varianza(valores, promedio):
    suma = 0
    for valor in valores:
        suma += (valor - promedio) ** 2
    varianza = suma / (len(valores) - 1)
    return varianza

def main():
    nombre = ["Jose", "Katia", "Azul", "Diego", "Martín", "Fer", "Marissa", "Iker", "Emilio", "Santiago"]
    edad = [18, 18, 18, 18, 25, 19, 19, 19, 18, 19]
    estatura =[1.75, 1.66, 1.55, 1.70, 1.72, 1.68, 1.55, 1.65, 1.72, 1.79]
    peso = [72, 60, 50, 62, 67, 56, 46, 83, 64, 70]

    promedio_edad = calcular_promedio(edad)
    promedio_estatura = calcular_promedio(estatura)
    promedio_peso = calcular_promedio(peso)

    varianza_edad = calcular_varianza(edad, promedio_edad)
    varianza_estatura = calcular_varianza(estatura, promedio_estatura)
    varianza_peso = calcular_varianza(peso, promedio_peso)

    print(f"La edad promedio es: {promedio_edad}")
    print(f"La estatura promedio es: {promedio_estatura}")
    print(f"El peso promedio es: {promedio_peso}")

    print(f"La varianza de la edad es: {varianza_edad}")
    print(f"La varianza de la estatura es: {varianza_estatura}")
    print(f"La varianza del peso es: {varianza_peso}")

if __name__ == "__main__":
    main()

