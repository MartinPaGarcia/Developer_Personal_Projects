import random

# arreglo de 10 numero random del 0 al 10
arreglo = [random.randint(0,10) for _ in range(10)]

# contador de 0
contador  = 0
for i in arreglo:
    if i == 0:
        contador = contador + 1
    


print("El numero de 0 en el arreglo es: ", contador )

print (arreglo)