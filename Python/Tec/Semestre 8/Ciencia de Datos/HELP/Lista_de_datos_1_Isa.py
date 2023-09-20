nombre = ["Jose", "Katia", "Azul", "Diego", "Martín", "Fer", "Marissa", "Iker", "Emilio", "Santiago"]
edad = [18, 18, 18, 18, 25, 19, 19, 19, 18, 19]
estatura =[1.75, 1.66, 1.55, 1.70, 1.72, 1.68, 1.55, 1.65, 1.72, 1.79]
peso = [72, 60, 50, 62, 67, 56, 46, 83, 64, 70]

promedio_edad = (sum(edad))/len(edad)
promedio_estatura = (sum(estatura))/len(estatura)
promedio_peso = (sum(peso))/len(peso)

print(promedio_edad)
print(promedio_estatura)
print(promedio_peso)

pesado_estatura = (sum(1 / "peso" * estatura)) / sum(1 / "peso")
print(pesado_estatura)

varianza_edad = (sum(edad - promedio_edad)) ** 2 / n - 1
varianza_estatura = (sum(estatura - promedio_estatura)) ** 2 / n - 1
varianza_peso =  (sum(peso - promedio_peso)) ** 2 / n - 1