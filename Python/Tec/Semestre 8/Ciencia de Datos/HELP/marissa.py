'''
 import random 

print("En esta ronda...")
cantidadint = random.randint(1, 6)  
print(f"La cantidad de intentos que tienes para usar la balanza es: {cantidadint}")

piedras = (1000*9)
piedral = 950

for intento in range(cantidadint):
 
    print("Selecciona dos piedras entre (1-10) para poner en la balanza")
    piedra1 = int(input("Primera piedra: "))
    piedra2 = int(input("Segunda piedra: "))

'''

import random #importa la libreria random

def dado(): #funcion que genera un numero aleatorio entre 1 y 6
    dado = random.randint(1, 6)
    # Si dado es menor que 3 entonces no se puede usar la balanzam por lo tanto se vuelve a llamar a la funcion dado
    if dado < 3:
        print(f"La cantidad de intentos que tienes para usar la balanza es: {dado}")
        print("No puedes usar la balanza, vuelve a arrojar el dado")
        return dado()
    else: 
        return dado_resultado
 

def imprimeInstrucciones(): #funcion que imprime las instrucciones del juego
    print("Bienvenido, listo para el reto?")
    print("Tienes 10 piedras de oro idénticas a simple vista") 
    print("9 de ellas pesan 1 kg, la otra pesa 950 g")
    print("Necesitas distiguir la piedra que pesa menos y para eso, tienes de apoyo una balanza")
    print("La balanza solo se utilizar cierta cantidad de veces, esta es definida por un dado")
    print("")


def main(): #funcion principal aqui es donde se ejecuta el programa
    imprimeInstrucciones() #llama a la funcion que imprime las instrucciones
    print ("Arrojaremos el dado para saber cuantas veces puedes usar la balanza")
    cantidadint = dado() #llama a la funcion dado y guarda el valor en la variable cantidadint
    print(f"La cantidad de intentos que tienes para usar la balanza es: {cantidadint}")





if __name__ == "__main__":
    main()