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
    piedritas = piedras()
    intentos = tira_dado
    print(f"Tus intentos restantes son: {intentos}")
    print(f"Tienes {len(piedritas)} piedras, por lo tanto, tendrás que colocar {len(piedritas) // 2} en cada platillo")
    while intentos > 0 and len(piedritas) > 1:
        izquierda, derecha = lados(piedritas)
        sobrante = None
        if len(piedritas) % 2 != 0:
            sobrante = min(izquierda + derecha)
            if sobrante in izquierda:
                izquierda.remove(sobrante)
            else:
                derecha.remove(sobrante)
        if sum(izquierda) > sum(derecha):
            piedritas = derecha
        else:
            piedritas = izquierda

        if sobrante is not None:
            piedritas.append(sobrante)
        intentos -= 1
        print(f"Tus intentos restantes son: {intentos}")
        if len(piedritas) > 1:
            print(f"Tienes {len(piedritas)} piedras, por lo tanto, tendrás que colocar {len(piedritas) // 2} en cada platillo")
        print(f"Piedras restantes: {list(range(len(piedritas)))}")  
    

    if sum(izquierda) == sum(derecha):
        print(f"La piedra que pesa menos es: {piedritas[0]}")
    else:
        print(f"La piedra que pesa menos es: {piedritas[0]}")
    


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
    print("")
    print(f"El dado te dio: {tira_dado}")
    print("")
    balanza(tira_dado, piedritas)
    


if __name__ == '__main__':
    main()