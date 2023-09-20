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

def pesado(estatura, peso):
    pesado_estatura = (sum(1 / peso * estatura)) / sum(1 / peso)
    return pesado_estatura

def varianza(edad, estatura, peso):
    n = len(edad)
    varianza_edad = (sum(edad - promedio_edad)) ** 2 / n - 1
    varianza_estatura = (sum(estatura - promedio_estatura)) ** 2 / n - 1
    varianza_peso =  (sum(peso - promedio_peso)) ** 2 / n - 1

    return varianza_edad, varianza_estatura, varianza_peso

def main():
    nombre = ["Jose", "Katia", "Azul", "Diego", "Martín", "Fer", "Marissa", "Iker", "Emilio", "Santiago"]
    edad = [18, 18, 18, 18, 25, 19, 19, 19, 18, 19]
    estatura =[1.75, 1.66, 1.55, 1.70, 1.72, 1.68, 1.55, 1.65, 1.72, 1.79]
    peso = [72, 60, 50, 62, 67, 56, 46, 83, 64, 70]
    
    promedios = promedio(edad, estatura, peso)
    pesado_estatura = pesado(estatura, peso)
    print(f"La edad promedio es: {promedios[0]}")
    print(f"La estatura promedio es: {promedios[1]}")
    print(f"El peso promedio es: {promedios[2]}")
    #Ahora el promedio pesado
    print(f"La estatura del más pesado es: {pesado_estatura}")

    


if __name__ == "__main__":
    main()