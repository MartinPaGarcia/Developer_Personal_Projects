# Elaborado por Juan Pablo Ruiz y Martin Palomares
# Problema 5

laLlaveAmo = None # Variable global 

def leerArchivo(nombreArchivo):
    try:
        with open(nombreArchivo, "r") as file:
            data = file.read()
            return data
    except FileNotFoundError:
        print('El archivo "{nombreArchivo}" no existe')
        return None



def frecuenciaPalabra(texto):
    alfabeto = "abcdefghijklmnopqrstuvwxyz " # 27 caracteres contando el espacio
    longitudTexto = len(texto)
    frecuencia = {char: texto.count(char)/longitudTexto for char in alfabeto}
    return frecuencia


def probableClave(textoCifrado, longitudClave):
    clave = ""

    for i in range(longitudClave):
        fragmento = textoCifrado[i::longitudClave]
        clave += encontrandoClave(fragmento)
    
    return clave


def encontrandoClave(fragmento):
    alfabeto = "abcdefghijklmnopqrstuvwxyz " # 27 caracteres contando el espacio

    frecuenciaFrag = {char: fragmento.count(char) for char in alfabeto}
    charterFrecMax = max(frecuenciaFrag, key=frecuenciaFrag.get)
    charClave = (alfabeto.index(charterFrecMax) - alfabeto.index(" ")) % len(alfabeto)

    return alfabeto[charClave]


def main():
    nombreArchivo = "cipher2.txt"
    textoCifrado = leerArchivo(nombreArchivo)
    claveTexto = 4

    if not textoCifrado:
        return
    frecuencia = frecuenciaPalabra(textoCifrado)
    global laLlaveAmo
    laLlaveAmo = probableClave(textoCifrado, claveTexto)

    print(f"La llave es: {laLlaveAmo}")

    print("")
    print ("Frecuencia de caracteres: ")
    for char, frec in frecuencia.items():
        print(f"{char}: {frec:2}%")
    


    
if __name__ == "__main__":
    main()