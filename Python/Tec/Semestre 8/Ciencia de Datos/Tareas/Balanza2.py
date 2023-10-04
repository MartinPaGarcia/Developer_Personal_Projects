import random


def dado():
    dado=random.randint(1,6)
    return dado

def piedras():
    piedras = [10, 10, 10, 10, 10, 9.50, 10, 10, 10, 10]
    random.shuffle(piedras)
    return piedras


def lados(piedritas):
    num_piedras = len(piedritas)
    mitad = num_piedras // 2
    izquierda = piedritas[:mitad]
    derecha = piedritas[mitad:]
    return izquierda, derecha

def balanza(tira_dado, piedritas):
    intentos = tira_dado
    print(f"Tus intentos restantes son: {intentos}")
    print(f"Tienes {len(piedritas)} piedras, por lo tanto, tendrás que colocar {len(piedritas) // 2} en cada platillo")
    while intentos > 0 and len(piedritas) > 1:
        izquierda, derecha = lados(piedritas)
        piedritas = izquierda
        intentos -= 1
        print(f"Tus intentos restantes son: {intentos}")
        if len(piedritas) > 1:
            print(f"Tienes {len(piedritas)} piedras, por lo tanto, tendrás que colocar {len(piedritas) // 2} en cada platillo")
    if len(piedritas) == 1:
        print("¡Felicidades! Has encontrado la piedra más ligera.")
    else:
        print("Lo siento, has agotado tus intentos.")


def jugador():
    print("Digite su nombre: ")
    nombre = input()
    return nombre

def mensajes(jugador):
    print(f"Bienvenid@ {jugador} al juego de la balanza")
    print("Has recolectado 10 piedras de oro en el rio y son idénticas a simple vista.")
    print("Tu tarea es encontrar la piedra que pesa menos, y para eso, tienes una balanza.")
    print("La cantidad de veces que puedes usar la balanza está definida por un dado.")
    print("Si el dado te da un número menor a 3, se vuelve a tirar el dado, pero no te preocupes, no se te restará un intento.")
    print("Si el dado te da un número mayor a 3, se te restará un intento.")
    print("")

def main ():
    nombre = jugador()
    mensajitos = mensajes(nombre)
    
    print(mensajitos)
    tira_dado = dado()
    if tira_dado < 3:
        print("Es imposible ganar con menos de 3 intentos. ")
        print("Se vuelve a tirar el dado")
        tira_dado = dado()
    piedritas = piedras()
    laBalanza = balanza(tira_dado, piedritas)
    


if __name__ == '__main__':
    main()