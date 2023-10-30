
#Redes #Internet #Capas_OSI 

# 7 capas modelo OSI
* capa 1 Fisica
* capa 2 data link
* capa 3 red
* capa 4 transporte
* capa 5 sesion
* capa 6 presentacion
* capa 7 aplicacion

## Dispositivos de capas de red

* Capa 1 
	* Repetidor: Un repetidor recibe una señal, la regenera y la pasa. Este puede regenerar y temporizar la señal permitiendo que este viaje una distancia mayor en el medio ya que se incrementa la latencia.
	* Concentrador (HUB): este es un repetidor multipuertos que consiste en un pasivo y un activo
		* Pasivo: No se conecta a la corriente, solo pasa la señal
		* Activo:  Este amplifica la señal antes de enviarla a otros puertos
	* Extensión de dominio de colisión: Los repetidores regeneran y re temporizan los Bits, pero no pueden filtrar el flujo de tráfico por ellos. Los datos (Bits) que llegan a uno de los puertos del repetidor se envían a todos los demás puertos. El uso del repetidor extiende el dominio de colisión, por lo tanto, la red a amboslados del repetidor es un dominio de colisión de mayor tamaño
* Capa 2
	* Bridge: De la misma forma en que un repetidor puede entender la longitud una red para cubrir una mayor distancia, este equipo tiene la capaidad de reconocer las señales que deben pasar y bloqueando las que no, reduciendo el tráfico en la red.
	* Si el dispositivo esta en el mismo segemento, el bridge bloque la trama par ir a otros segmentos, eso se llama filtrad. Si el dispositvo destino esta en un segmento diferente lo reenvía por el segmento adecuado, de otra forma si es desconocido por el bridge, lo reenviará por todos los puertos excepto por el que llegó
	* Dmonio de colisión: Si se conectan varios computadores a un solo medio que no tiene otros dispositivos de "Networking conectados", esta constituye una situación básica de acceso compartido, y un domino de colisión. Según la tecnología específica utilizada, esa situación limita la cantidad de computadores que pueden usar esa parte del medio.
	* Switch Manejan un ancho de banda mayor ya me tratan cada segemento de forma individual
* Capa 3
	* Router (ruteador): Trabajan en la capa 3 es capaz de manejar grupos de redes, interconecta diversas tecnologías de capa 3 como son (Ehernet, FDDI, token Ring, etc.). Tambiénexamina los paquetes (capa 3)
	


# Conceptos

* Atenuacion 
* Ruido
* Dispersión 
* MAC
* Ancho de Banda: Rango de frecuencias que una señal electrica ocupa
* Segmentación de red (Bridge dispositivos capa 2)

# Modelos

##  Modelo TCP/IP 

Son dos protocolos uno es el TCP y el otro IP 

Tiene 4 capas

* Acceso a la red capas 1 y 2
* internet capa 3 
* transporte capa 4
* aplicacion capas 5, 6 y 7


# Protocolos

##  Protocolo CSMA/CD

Son dos protocolos de operación de Ethernet 

Escucha en el medio, si no hay transmisión, envía el mensaje, si no espera hasta que este libre; si hay una colisión, esperan ambos equipos un tiempo aleatorio y vuelven a intentar el envíon del mensaje.


*Diagrama TCPIP

## PDU Protocol Data Unit 

Peer-to-peer communication 

A continuación se presentan las capas del protocolo PDU:
* Capa 1 Data
* Capa 2 Segemento
* Capa 3 Paquete
* Capa 4  Frame
* Capa 5 Bits

## Información de control

En otras cosas, se identifican al origen y el destino de cada PDU

L2 -> L3 -> L4 -> Data

* L4 - Números de puertos
* L3 - Direcciones lógicas (IP address)
* L2 - Direcciones Físicas (MAC address)

# Formas de transmisión

La información digiral y la analogica puede ser codificada en una señal analogica o digital 

Tipos de señalización (Todo esto ocurre en la capa 1)

La señalización-modulación tiene diferentes tipos:

Digital AM
Digital FM
Digital PM
Diferencial binaria PSK
QPSK por cuadratura 




