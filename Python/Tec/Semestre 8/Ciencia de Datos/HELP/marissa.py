import random

print("¡Bienvenido al reto de las piedras!")
print("Tienes 10 piedras de oro idénticas a simple vista.")
print("9 de ellas pesan 1 kg, la otra pesa 950 g.")
print("Tu tarea es encontrar la piedra que pesa menos, y para eso, tienes una balanza.")
print("La cantidad de veces que puedes usar la balanza está definida por un dado.")
print("")

piedras = [1, 1, 1, 1, 1, 0.950, 1, 1, 1, 1]
random.shuffle(piedras)

piedras_elegidas = []

cantidad_intentos = random.randint(1, 6)

while cantidad_intentos < 3:
    print("El valor del dado es menor a 3; se tira de nuevo.")
    cantidad_intentos = random.randint(1, 6)

print(f"La cantidad de intentos que tienes para usar la balanza es: {cantidad_intentos}")
print("")

suma_platillos = 0
intentos=1

if cantidad_intentos >0:
    print(f"Intento {intentos}:") 
    
    platillo_izquierdo = []
    platillo_derecho = []
    
    print("Elige las piedras para el platillo izquierdo (ingresa los números separados por espacios) piedras del 0 al 9:")
    elegidas_izq = input().split()

    
    print("Elige las piedras para el platillo derecho (ingresa los números separados por espacios) no utilices las que colocaste en el lado izquiero:")
    elegidas_der = input().split()

    
    for j in elegidas_izq:
        j = int(j)
        platillo_izquierdo.append(piedras[j - 1])
        piedras_elegidas.append(piedras[j - 1])
        
    for k in elegidas_der:
        k = int(k)
        platillo_derecho.append(piedras[k - 1])
        piedras_elegidas.append(piedras[k - 1])
        
    peso_platillo_izq = sum(platillo_izquierdo)
    peso_platillo_der = sum(platillo_derecho)
    
    print(f"Peso en el platillo izquierdo: {peso_platillo_izq} kg")
    print(f"Peso en el platillo derecho: {peso_platillo_der} kg")
    
    if peso_platillo_izq < peso_platillo_der:
        print("La balanza se inclina hacia la derecha.")
    elif peso_platillo_der < peso_platillo_izq:
        print("La balanza se inclina hacia la izquierda.")
   
    if cantidad_intentos==1:
        print("\nAhora, tienes que adivinar cuál es la piedra que pesa menos")
        piedra_adivinada = float(input("Ingresa la piedra que crees que pesa menos: "))

        if piedra_adivinada == 6:
            print("¡Has encontrado la piedra que pesa menos! ¡Felicidades!")
        else:
            print(f"Lo siento, la piedra que pesa menos no es la {piedra_adivinada}. Inténtalo de nuevo la próxima vez.")
    else:
        intentos +=1
    

while intentos !=cantidad_intentos:
    print(f"\nIntento {intentos}:")
    print("¿Qué piedras quieres poner en el platillo de la izquierda?")
    intentos +=1
        
    piedras2i = []
    for l in range(2):
        platoi2 = int(input())
        piedras2i.append(platoi2 - 1)
        
    print("¿En el platillo derecho qué piedras quieres? Deben ser 2:")
        
    piedras2d = []
    for m in range(2):
        platod2 = int(input())
        piedras2d.append(platod2 - 1)
        
    print("¿Qué piedra vas a descartar?")
        
    piedra1c = []
    for n in range(1):
        platoc = int(input())
        piedra1c.append(platoc - 1)
        
    piedras_2i = [piedras[x] for x in piedras2i]
    piedras_2d = [piedras[x] for x in piedras2d]
    piedra_1c = [piedras[x] for x in piedra1c]
        
    peso_platillo_izq_2 = sum(piedras_2i)
    peso_platillo_der_2 = sum(piedras_2d)
    suma_1c = sum(piedra_1c)
        
    print("Peso en el platillo izquierdo: {:.3f} kg".format(peso_platillo_izq_2))
    print("Peso en el platillo derecho: {:.3f} kg".format(peso_platillo_der_2))
    
    if suma_1c== .950:
        print("¡Has encontrado la piedra que pesa menos! ¡Felicidades!")
        break
    elif intentos == cantidad_intentos:
        print("\nAhora, tienes que adivinar cuál es la piedra que pesa menos")
        piedra_adivinada = float(input("Ingresa la piedra que crees que pesa menos: "))

        if piedra_adivinada == .950:
            print("¡Has encontrado la piedra que pesa menos! ¡Felicidades!")
        else:
            print(f"Lo siento, la piedra que pesa menos no es la {piedra_adivinada}. Inténtalo de nuevo la próxima vez.")