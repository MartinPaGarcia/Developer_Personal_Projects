import matplotlib.pyplot as plt # Importar la librería matplotlib para graficar



    # nombres_empleados = [Massimo]
    # meses_ventas = [1]
    # total_ventas = [1000001]

    # nombres_empleados = [Massimo, Martin]
    # meses_ventas =      [1,            1]
    # total_ventas =      [1000001,    400]
    # indices =           [0,            1]


    # empleados_elegibles = []
    # mejores_meses = []



def opciones(opcion): # Definir función para mostrar las opciones
    # Listas para almacenar las ventas de los empleados
    nombres_empleados = []
    meses_ventas = []
    total_ventas = []
    empleados_elegibles = []
    mejores_meses = []

    while opcion != 3:
        if opcion == 1:
            nombre_empleado = input("Nombre del empleado: ") # Solicitar nombre del empleado como cadena de caracteres
            mes_ventas = int(input("Mes de ventas (1, 2, 3, etc.): ")) # Solicitar mes de ventas como número entero
            total_venta = float(input("Total de ventas anuales: ")) # Solicitar total de ventas anuales como número flotante
            nombres_empleados.append(nombre_empleado)
            meses_ventas.append(mes_ventas)
            total_ventas.append(total_venta)
            print("")
            menu()
            opcion = int(input("Selecciona una opción: "))
            print("")

        if opcion ==2:
            contador = 0
            print ("Opcion 2")
            while contador < len(nombres_empleados):
                if total_ventas[contador] >= 1000000:
                    empleados_elegibles.append(nombres_empleados[contador])
                contador += 1
            print("")
            print(f"Empleados elegibles para el bono:{empleados_elegibles}")
            menu()
            opcion = int(input("Selecciona una opción: "))
            print("")
                
            for i in range(len(nombres_empleados)): # i = 0
                if total_ventas[i] > 1000000:
                    empleados_elegibles.append(nombres_empleados[i])
        
        if opcion > 3 or opcion < 1:
            print("Opción no válida. Por favor, selecciona una opción válida.")
            print("")
            menu()
            opcion = int(input("Selecciona una opción: "))
            print("")




def menu(): # Definir función para mostrar el menú
    print("1. Ingresar datos de ventas")
    print("2. Mostrar datos de ventas")
    print("3. Salir")


def main(): # Definir función principal
    print("Bienvenido al programa de ventas de la empresa")
    menu()
    opcion = int(input("Selecciona una opción: "))
    opciones(opcion)
    print("Gracias por usar el programa.")






if __name__ == "__main__":
    main()









#         ventas_por_mes = {}

#         for mes in meses_ventas:
#             if mes not in ventas_por_mes:
#                 ventas_por_mes[mes] = 1
#             else:
#                 ventas_por_mes[mes] += 1

#         print("\nEmpleados elegibles para el bono:")
#         for empleado in empleados_elegibles:
#             print(empleado)

#         print("\nMeses con ventas totales más altas:")
#         for mes, ventas in ventas_por_mes.items():
#             if ventas == max(ventas_por_mes.values()):
#                 mejores_meses.append(mes)
#         for mes in mejores_meses:
#             print(mes)

#         print("\nNúmero de ventas en cada mes:")
#         for mes, ventas in ventas_por_mes.items():
#             print(f"{mes}: {ventas}")

#         # Graficar los vendedores con mayores ventas en el año
#         plt.figure(figsize=(10, 5))
#         plt.bar(nombres_empleados, total_ventas)
#         plt.xlabel("Vendedor")
#         plt.ylabel("Ventas Totales en el Año")
#         plt.title("Vendedores con Mayores Ventas en el Año")
#         plt.xticks(rotation=45)
#         plt.show()

#         # Graficar los meses con las ventas totales más altas
#         plt.figure(figsize=(10, 5))
#         plt.bar(mejores_meses, [ventas_por_mes[mes] for mes in mejores_meses])
#         plt.xlabel("Mes")
#         plt.ylabel("Ventas Totales")
#         plt.title("Meses con Ventas Totales Más Altas")
#         plt.xticks(rotation=45)
#         plt.show()

#         # Graficar el número de ventas en cada mes
#         plt.figure(figsize=(10, 5))
#         plt.bar(ventas_por_mes.keys(), ventas_por_mes.values())
#         plt.xlabel("Mes")
#         plt.ylabel("Número de Ventas")
#         plt.title("Número de Ventas en Cada Mes")
#         plt.xticks(rotation=45)
#         plt.show()

#     elif opcion == '3':
#         break
#     else:
#         print("Opción no válida. Por favor, selecciona una opción válida.")

# print("Gracias por usar el programa.")