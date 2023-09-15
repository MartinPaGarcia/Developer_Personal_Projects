import random 
import time
'''
Autor: Martín Palomares García
Fecha: 15/09/2023
Matricula: A01066569
Descripción: Programa que encuentra la piedra más ligera de 10 piedras utilizando una balanza.

'''

def piedras():
    n = 10
    piedras = []
    for i in range(n):
        piedras.append(random.randint(1, 1000))
    return piedras

def balanza(piedras):
    n = len(piedras)
    if n == 1:
        return piedras[0]
    elif n == 2:
        if piedras[0] < piedras[1]:
            return piedras[0]
        else:
            return piedras[1]
    else:
        mitad = n // 2
        lado1 = balanza(piedras[:mitad])
        lado2 = balanza(piedras[mitad:])
        if lado1 < lado2:
            return lado1
        else:
            return lado2


def main():
    print ("Balanza")
    pesos = piedras()
    print (f"Las piedras son: {pesos}")

    iniicio_tiempo = time.time()
    piedra_mas_ligera = balanza(pesos)
    fin_tiempo = time.time()
    
    tiempo_total = fin_tiempo - iniicio_tiempo
    print (f"La piedra más ligera es: {piedra_mas_ligera}")
    print (f"El tiempo total es: {tiempo_total:.4f} segundos")
    print (f"BigO es: Olog(n)")
if __name__ == "__main__":
    main()

