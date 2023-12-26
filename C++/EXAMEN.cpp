#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    srand(static_cast<unsigned int>(time(0))); // Inicializar la semilla para números aleatorios

    const int size = 10;
    int arreglo[size];

    // Rellenar el arreglo con números aleatorios del 0 al 10
    for (int i = 0; i < size; ++i) {
        arreglo[i] = rand() % 11;
    }

    // Contador de 0s
    int contador = 0;
    for (int i = 0; i < size; ++i) {
        if (arreglo[i] == 0) {
            ++contador;
        }
    }

    // Imprimir el número de 0s en el arreglo
    std::cout << "El numero de 0 en el arreglo es: " << contador << std::endl;

    // Imprimir el arreglo
    std::cout << "El arreglo es: [";
    for (int i = 0; i < size; ++i) {
        std::cout << arreglo[i];
        if (i < size - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "]" << std::endl;

    return 0;
}
