import vigenere

# Elaborado por Juan Pablo Ruiz y Martin Palomares
# Problema 2 
# RECUERDA CORRER PRIMERO EL ARCHIVO VIGENERE.PY PARA PODER ACCEDER A LA VARIABLE GLOBAL laLlaveAmo
# Sabemos que es el orden correcto, pero los hackers no queremos que adivinene nuestro siguiente...


def elCifrador(texto, clave):
    textoCifrado = ""
    alfabeto = "abcdefghijklmnopqrstuvwxyz " # 27 caracteres contando el espacio

    for i, caracter in enumerate(texto):
        if caracter in alfabeto:
            letraClave = clave[i % len(clave)]
            desplazar = alfabeto.index(letraClave)
            caracterCifrado = alfabeto[(alfabeto.index(caracter) + desplazar) % len(alfabeto)]
            textoCifrado += caracterCifrado
        else:
            textoCifrado += caracter
        
    return textoCifrado

def podremosDescifrar(textoCifrado, clave):
    textoDescifrado = ""
    alfabeto = "abcdefghijklmnopqrstuvwxyz " # 27 caracteres contando el espacio

    for i, caracter in enumerate(textoCifrado):
        if caracter in alfabeto:
            letraClave = clave[i % len(clave)]
            desplazar = alfabeto.index(letraClave)
            caracterDescifrado = alfabeto[(alfabeto.index(caracter) - desplazar) % len(alfabeto)]
            textoDescifrado += caracterDescifrado
        else:
            textoDescifrado += caracter
        
    return textoDescifrado


def main():
    vigenere.main() #Traemos la funcion main del archivo vigenere.py
    texto_prueba = "Un joven padawan aun eres"
    clave_prueba = "yoda"
    textoCifrado = elCifrador(texto_prueba, clave_prueba)

    print(f"Texto original: {texto_prueba}")
    print(f"Clave: {clave_prueba}")
    print(f"Texto cifrado: {textoCifrado}")
    print("")
    textoDescifrado = podremosDescifrar(textoCifrado, clave_prueba)
    print("Prueba de descifrado: ")
    print(f"Texto descifrado: {textoDescifrado}")
    print("")
    print("")
    # Recuerda que para que funcione se debe ejecutar primero el archivo vigenere.py
    # De otra manera no se podra acceder a la variable global laLlaveAmo
    print ("Ahora a descifrar el archivo cipher2.txt") 
    clave_prueba = vigenere.laLlaveAmo 
    with open("cipher2.txt", "r") as archivo:
        contenido = archivo.read()
    
    texto_prueba = contenido

    textoDescifrado = podremosDescifrar(contenido, clave_prueba)
    print(f"Texto descifrado: {textoDescifrado}")

    print (f"La clave es: {clave_prueba}")

if __name__ == "__main__":
    main()