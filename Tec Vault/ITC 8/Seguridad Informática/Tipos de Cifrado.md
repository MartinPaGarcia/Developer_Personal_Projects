---
banner: "https://images.alphacoders.com/121/1218911.jpg"
banner_y: 0.616
---

#Seguridad 

+ Cifrado Vinegere
+ Cifrado Cesar 

Cifrados en las computadoras 

Está hecho al nivel de los bits, nivel de los bytes o a nivel, bloque.

La transposición y la sustitución aún se siguen usando, pero necesita estar hecho en una manera aleatoria

Las tablas que indican sustitución que son llamadas cajas S

También las funciones matemáticas con una inversa pueden ser usadas


Funciones reversibles Ejemplo: XOR

![[Pasted image 20230817182508.png]]


Métodos de cifrados criptográficos modernos 

Criptografía simétrica
+ Usa la misma llave pare encriptar y des-encriptar
+ Rápida
+ Usada para proteger la confidencialidad

Criptografía Asimétrica
+ Dos llaves, no pueden encriptar o des-encriptar con la misma
+ Usadas para autenticación o confidencialidad, pero no para ambas

Hashing
+ Únicas en una corta representación de datos
+ Usada para checar la integridad

# Code block chaining

CBC, en por sus siglas en inglés, requieren un vector del mismo tamaño de bloque

La salida del bloque previo es usada como el vector de inicialización

No puede ser ejecutado de manera paralela

Previene ataque estadístico

![[Pasted image 20230823175804.png]]

# Cipher Feedback (Stream)

CFB, es un cifrado que difiere del CBC con el uso del XOR con el texto, esto se hace a través de la encriptación del vector y la llave, no con el vector de inicialización.

Usa XOR del algoritmo y el texto como el próximo vector de inicialización. 

Necesita esperar por el bloque para completar previo al próximo

![[Pasted image 20230823175824.png]]

 # Output Feedback (Stream)

OFB, a diferencia del CFB en el cual se esperaba un texto cifrado previamente, ahora ya no lo necesito, una un generador (algoritmo criptográfico) como el vector de inicialización para el próximo bloque

OFB permite una ejecución paralela, después que los generadores de los outputs son generados.

![[Pasted image 20230823180806.png]]

# Counter mode (Stream/"Block")

Es como el ECB, pero incluye los vectores de inicialización.

El vector tiene un valor aleatorio que se queda igual, pero, es diferente para cada sesión Nonce (número arbitrario).

Cada bloque usa un counter

Es fácilmente usado de manera paralela, por lo que lo hace común en aplicaciones modernas.

Si un bloque es dañado, se puede recalcular fácilmente, ya que no están ligados entre sí.

![[Pasted image 20230823182441.png]]

# Qué es lo que provee la seguridad

## Llave

+ Tamaño
+ Se mantenga privada

## Algoritmo

+ Diseño
+ Implementación
+ Que se mantenga como un algoritmo privado no ayuda 


# Algoritmos Simétricos Comunes 

## Data Encryption Standard 

Fue publicado en 1977 por el estándar nacional NBS y la agencia de seguridad nacional (NSA) en Estados Unidos.

Algoritmo Lucifer creado por IBM 

![[Pasted image 20230823183538.png]]


## AES Advanced Encryption Standard

El AES, o Advanced Encryption Standard (Estándar de Cifrado Avanzado), es un algoritmo de cifrado en bloque ampliamente utilizado y considerado uno de los métodos de cifrado más seguros y eficientes. Fue seleccionado como el estándar de cifrado por el Instituto Nacional de Estándares y Tecnología (NIST) de los Estados Unidos en 2001, reemplazando al antiguo estándar Data Encryption Standard (DES).

El AES opera sobre bloques fijos de datos y se puede configurar para trabajar con bloques de 128 bits, utilizando claves de cifrado de 128, 192 o 256 bits. El algoritmo realiza una serie de transformaciones matemáticas y operaciones de sustitución y permutación para mezclar y confundir los datos en bloques. Esto resulta en un proceso altamente seguro que hace que sea extremadamente difícil para los atacantes revertir el cifrado sin conocer la clave correcta.

El AES ofrece varios modos de operación, como el modo ECB (Electronic Codebook), CBC (Cipher Block Chaining), CFB (Cipher Feedback), OFB (Output Feedback) y CTR (Counter), que permiten adaptarse a diferentes situaciones de cifrado, como la protección de mensajes largos o la encriptación de flujos de datos.

Una de las razones por las que AES es considerado seguro es su resistencia ante diversos tipos de ataques, como el criptoanálisis diferencial y el criptoanálisis lineal, que son metodologías para intentar descubrir la clave de cifrado mediante el análisis de patrones en los datos cifrados. AES ha demostrado ser resistente a estos y otros ataques conocidos hasta el momento, siempre y cuando se utilice de manera adecuada y se mantenga una clave segura.

En resumen, el AES es un algoritmo de cifrado sólido, eficiente y ampliamente adoptado que se utiliza en una amplia variedad de aplicaciones, desde la protección de datos en sistemas informáticos hasta la seguridad en las comunicaciones en línea.

# Criptografía de llave pública

+ Número de llaves
+ Distribución segura de llaves
+ No puede garantizar la seguridad



## Campos finitos

+ Operaciones + -

Con el campo finito que vamos a usar, se necesitan operaciones aritméticas modulares

+ 7 + 5 MOD 10
+ 2 * 7 MOD 10
+ 4 * 3 MOD 10
Algunas operaciones que pertenecen a P en campos que pertenecen a NP



## Diffie-Hellman

Permite obtener un valor privado compartido usando información que pueda ser compartida en con un canal no protegido

Ejemplo:

+ p = 47
+ g = 15

