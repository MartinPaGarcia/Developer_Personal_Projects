'''
Autor: Isabela Corena
Maticula: 
Fecha: 19/09/2023

'''

def promedio(edad, estatura, peso):
    promedio_edad = (sum(edad))/len(edad)
    promedio_estatura = (sum(estatura))/len(estatura)
    promedio_peso = (sum(peso))/len(peso)

    return promedio_edad, promedio_estatura, promedio_peso

# Calcula la estatura del más pesado
def pesado(estatura, peso):
    
    return 0

# Calcula la varianza de la edad, estatura y peso
def varianza(edad, estatura, peso, promedio_edad, promedio_estatura, promedio_peso):
    n = len(edad)
    
    suma_edad = 0
    suma_estatura = 0
    suma_peso = 0

    for i in range(n):
        suma_edad += (edad[i] - promedio_edad) ** 2
        suma_estatura += (estatura[i] - promedio_estatura) ** 2
        suma_peso += (peso[i] - promedio_peso) ** 2

    varianza_edad = suma_edad / (n - 1)
    varianza_estatura = suma_estatura / (n - 1)
    varianza_peso = suma_peso / (n - 1)

    return varianza_edad, varianza_estatura, varianza_peso

def main():
    nombre = ["Jose", "Katia", "Azul", "Diego", "Martín", "Fer", "Marissa", "Iker", "Emilio", "Santiago"]
    edad = [18, 18, 18, 18, 25, 19, 19, 19, 18, 19]
    estatura =[1.75, 1.66, 1.55, 1.70, 1.72, 1.68, 1.55, 1.65, 1.72, 1.79]
    peso = [72, 60, 50, 62, 67, 56, 46, 83, 64, 70]
    
    promedios = promedio(edad, estatura, peso)
    pesado_estatura = pesado(estatura, peso)
    varianza_edad, varianza_estatura, varianza_peso = varianza(edad, estatura, peso, *promedios)

    #Promedios
    print(f"La edad promedio es: {promedios[0]}")
    print(f"La estatura promedio es: {promedios[1]}")
    print(f"El peso promedio es: {promedios[2]}")

    #Ahora el promedio pesado
    print(f"Promedio pesado: {pesado_estatura}")

    #Varianzas
    print(f"La varianza de la edad es: {varianza_edad}")
    print(f"La varianza de la estatura es: {varianza_estatura}")
    print(f"La varianza del peso es: {varianza_peso}")

    


if __name__ == "__main__":
    main()