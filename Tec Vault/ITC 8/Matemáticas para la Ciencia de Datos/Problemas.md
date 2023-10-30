---
banner: "https://www.codingem.com/wp-content/uploads/2021/10/juanjo-jaramillo-mZnx9429i94-unsplash-1024x683.jpg"
---

# Problema 1

  

1.- Una lista de 3 números enteros que el usuario escriba de manera aleatoria y que el programa escriba de mayor a menor

``` scss
// Pedir al usuario que ingrese los tres números enteros

escribir: "Ingresa el primero número"
leer numero1

escribir: "Ingresa el segundo número"
leer numero2

escribir: "Ingresa el tercer número"
leer numero3

// Encontrar el mayor número
mayor = numero1
si numero2 > mayor entonces
	mayor=numero2
fin si 
sinumero3 > mayor entonces
	mayor=numero3
fin si

// Encontrar el menor numero 

menor = numero1

si numero2 < menor entonces 
	menor = numero2
fin si
si numero3 < menor entonces
	menor = numero3
fin si

// Encontrar número del medio 

medio = numero1
si(numero2>menor) y (numero2<mayor)entonces
	medio = numero2
sino si (numero3 > menor) y (numero3 < mayor) entonces
	medio = numero3
fin si
```

# Diagrama problema 1![[Screenshot 2023-08-21 at 10.41.18 p.m..png]]


# Problema 2

## *Hice un pequeño tutorial que les pasé a mis compañeros para que pudieran resolver el problema*

Pida al usuario que ingrese los dos pagos quincenales que recibe y le indique el ISR, considerando que de acuerdo al salario total, será el porcentaje que se debe pagar:

  
* $0 - $644.58 -> 1.92%

* $644.58 - $5470.92 -> 6.40%

* $5470.92 - $9614.66 -> 10.88%

* $9614.66 - $11176.62 -> 1.92%


Sabemos que para este problema el _usuario_ debe ingresar a la computadora sus dos pagos quincenales, porque el ISR es en un mes. Por lo tanto, debemos ingresar los dos pagos quincenales para ver cuánto de ISR se debe pagar.

¿Cómo puedo indicarle a la computadora qué hacer?

Tratemos de descomponer el problema en pequeños pasos, lo que nos ayudará a guiar a la computadora. Es como si intentáramos explicarle un tema difícil a un niño de kínder.

Primero, sabemos que para este problema particular tenemos que calcular el ISR basado en mis ingresos mensuales.

Pero... La computadora no sabe ni siquiera qué es el dinero, ni mucho menos sabe cuánto gano. Así que primero debo almacenar los números en algún lugar, ¿no? Por lo tanto, lo primero que debemos hacer es pedirle al usuario que ingrese sus ganancias quincenales dos veces, ya que un mes contiene dos quincenas.

Ahora bien. Mi ganancia de mi primera quincena del mes de julio fue de $2500 pesos, y mi ganancia de la segunda quincena del mes de julio fue de $3400 porque hice muchos trabajos extras. Aunque con estos números no puedo hacer nada, me servirán para poder calcular mi ISR más adelante; mientras tanto, concentrémonos en resolver este problema.

Guardaré mis ganancias del mes en una caja (en este caso una variable). Una variable, en pocas palabras, es un lugar donde puedo almacenar información. En este caso, la información que almacenaré será la suma de dos números.

``` scss
# Aqui estamos guardando la suma de mis ganancias mensuales en una variable llamada "ganancia" (puede tener cualquier nombre)

# Escribe y lee son algo confusas, pero escribir quiere decir que la computadora "escribirá" el mensaje en la compu y leer, quiere decir que el usuario digitará un valor para que la computadora lo lea

escribe("Digita tu ganancia de tu primera quincena del mes: ")
lee quincena1

escribe("Digita tu ganancia de tu segunda quincena del mes")
lee quincena2


ganancia = quincena1 + quincena2
```

Si le pedimos a la computadora que escriba o que nos muestre la variable (en otras palabras) nos mostrará lo siguiente 

``` scss
"2900"
```

Eso es todo lo que se mostraría. Peeero, eso no es lo que necesitamos. Bueno, en realidad sí lo necesitamos, pero no de esta forma. Para lograrlo, contamos con las condiciones que nos proporcionaron al inicio, las cuales son:

* $0 - $644.58 → 1.92%

* $644.58 - $5470.92 → 6.40%

* $5470.92 - $9614.66 → 10.88%

* $9614.67 - $11176.62 → 1.92%

+ *El usuario no gana más de 11 mil pesos mensuales*

Estas son mis reglas inquebrantables. A partir de aquí, diseñaremos el código. Ya sabemos que debemos calcular el ISR basado en mis ingresos mensuales o de dos quincenas; por lo tanto, debemos seguir estas reglas.

Para indicarle a la computadora que debemos usar una pequeña instrucción llamada _'if'_ o _'sí'_ en español, imaginemos que estamos en un cruce en el camino. Si se cumple una condición que hemos establecido, elegimos una ruta específica a seguir. En caso contrario, tomamos otro camino o simplemente seguimos haciendo lo que estábamos haciendo antes.

Demos un ejemplo, pero este ejemplo no resuelve el problema; es solo demostrativo.

``` scss
# Numero al azar que asigne a la variable "numero"
numero = 5

# SI numero es mayor que 3, entonces... Escribe "El número es mayor que 3"
if numero > 3:
    print("El número es mayor que 3")

```

Ya casi terminamos, solo falta lo último. Si observamos bien, las condiciones originales que nos dieron para resolver el problema, son rangos de ganancias:

De 0 a 644.58

$0 - $644.58 → 1.92%

Esto significa que un _if_ por sí solo no nos servirá para evaluar. Necesitamos otra condición que proviene de la lógica. Se llama compuerta lógica "and" o "y" en español. ¿Qué significa? Lo explicaré con una analogía muy simple.

Imagina que tu hermano va al OXXO a comprar comida, pero tú eres muy floj@. Entonces, le dices a tu hermano:

Trae papas _y_ galletas.

Esto significa que cuando tu hermano vaya al OXXO, deberá comprar ambas cosas. Si no lo hace, te enojarás mucho porque no cumplirá con tu condición.

El código se vería de la siguiente manera:

``` scss
# Numero al azar que asigne a la variable "numero"
numero = 5

# SI numero es mayor que 3, entonces... Escribe "El número es mayor que 3"
if numero > 3 and numero < 10:
    print("El número es mayor que 3")
    print("El número es menor que 10")

```

SINO" o "ELIF" son otras condiciones que, como puedes intuir, son instrucciones que se ejecutarán en caso de que mi condición inicial no se cumpla. "ELSE" es una condición general en caso de que ninguna de las condiciones anteriores se cumpla.

``` scss
# Numero al azar que asigne a la variable "numero"
numero = 11


# SI numero es mayor que 3, entonces... Escribe "El número es mayor que 3"
if numero > 3 and numero < 10:
    print("El número es mayor que 3")
    print("El número es menor que 10")
elif numero > 10 and numero < 25: #sino
    print("El número es mayor que 10")
    print("El número es menor que 25")	
else:
	print("El número no está en rango")
```


Ya con todo lo que vimos anteriormente, resolver el problema es fácil:

``` scss
# Ganancia
escribe("Digita tu ganancia de tu primera quincena del mes: ")
lee quincena1

escribe("Digita tu ganancia de tu segunda quincena del mes ")
lee quincena2

ganancia = quincena1 + quincena2


# Por lo tanto, necesitamos comparar nuestra "ganancia" con los rangos de cálculo de ISR

SI ganancia>=0 y ganancia<=644.58:
	isr = 1.92 # Va con sangría porque solo si se cumple la condicion es cuando le daremos ese valor al ISR
SINO si ganancia>=644.59 y ganancia<=5470.92:
	isr = 6.40
SINO si ganancia >=5470.93 y ganancia<=9614.66
	isr = 10.88
SINO si ganancia>=9614.67 y ganancia<=11176.62
	isr = 12.92

print ("El ISR a pagar es: " + isr) #Puedes poner únicamente "escribe (isr)"
```

# Diagrama problema 2
 ![[Screenshot 2023-08-21 at 10.40.49 p.m..png]]

# Problema 3

``` scss
aprobados = 0
reprobados = 0

para i en rango(4):
	cal = leer_cadena ("Digita aprobado o reprobado: ")
	Si cal es igual a "aprobado":
		aprobados = aprobados + 1
	SiNo:
		reprobados = reprobados +1
	fin para
imprimir ("El numero de aprobados es: " + convertir_a_cadena(aprobados))

imprimir ("El numero de reprobados es: " + convertir_a_cadena(reprobados))

```

![[Screenshot 2023-08-23 at 11.39.32 p.m..png]]


![link](https://youtu.be/m2kdYzs_5SA)

Hice este pequeño tutorial para mis compañeros de clase, agrego el link de mi explicación.

https://youtu.be/m2kdYzs_5SA



