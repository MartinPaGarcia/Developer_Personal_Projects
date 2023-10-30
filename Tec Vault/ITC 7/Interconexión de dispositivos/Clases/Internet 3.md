---
banner: "https://rare-gallery.com/mocahbig/394731-wallpaper-night-city-abstract-art-minimalist-4k.jpg"
banner_y: 0.524
---


# Time Division Multiplexing

* **Proceso digital** permite a varias conexiones compartir el ancho de banda de un enlace
* **Conexión** requiere una porción de tiempo dentro del enlace


![[Pasted image 20230220112722.png]]

# Conmutación de paquetes 

* No existe reserva de recursos
* Los datos se transmiten en trozos denominados paquetes 
* Cada paquete se trata de forma independiente, es decir, el emisor enumera cada paquete, le añade información de control y lo envía hacia su destino. Se utiliza normalmente en servicios sin conexión.


![[Pasted image 20230220113017.png]]

# Repaso de capas

* Capa 1 - Señales UDP Bits 
* Capa 2 - Enlace de datos Switch Mac Física Bios NIC. UDP frames
* Capa 3 - Red direccionamiento lógica IP IPV6 IPV4. UDP paquetes
* Capa 4 - Transporte TCP, DNS. UDP Segmentos
* Capa 5 - Sesión 
* Capa 6 - Presentación compresión
* Capa 7 - Aplicación 

# Tasa de Transferencia

![[Pasted image 20230220113937.png]]

# Métodos comunes de acceso CLI

* Consola
	* Usa una conexión serial de baja velocidad para conectar directamente un equipo al puerto de consola en el router o switch 
	* **Uso**
		* Configuración de inicio del dispositivo de red
		* Procedimientos de recuperación de desastres y resolución de problemas donde no es posible el acceso remoto.
		* Procedimientos de recuperación de contraseña
* **Telnet o SSH**
	* Sirve para acceder en forma remota a la sesión CLI (Telnet)
	* SSH → método más seguro para acceso remoto (*secure shell*)
* **Puerto auxiliar** 
	* Se establece la sesión con el CLI a través de una conexión telefónica


# Modos de operación (cambios)


``` shell
Switch enable (usuario)
Switch#configure terminal (privilegiado)
Switch(config)# (configuración)
```

## Nombre

``` shell
Switch(config)#hostname S1
```

## Para destrabar el equipo 
S1(config)#no ip domain-lookup

``` shell
S1(config)#no ip domain-lookup
```

## Password (modo privilegiado)

``` shell
S1(config)#enable secret (password)
```

## Mensaje del día 

``` shell
S1 (config)#banner motd #(mensaje del día)#
```

## Contraseña de consola 

``` shell
S1 (config) # line console 0 
S1 (conifg-line) # password (password)
S1 (config-line) # login
```

## Contraseña terminal virtual

``` shell
S1 (config) # line vty 0 4
S1 (conifg-line) # password (password)
S1 (config-line) # login
```


## Comandos para administrar el contenido de la NVRAM

``` shell
erase startup-config (Elimina el contenido de la NVRAM)

copy running-config startup-config (Almacena la configuración actual en RAM en la NVRAM)

show startup-config (Almacena la configuración actual en RAM en la NVRAM)

show startup-config (Visualiza la configuración guardada, que es el contenido de la NVRAM)

show running-config (Visualiza la configuración actual)
```



# Hacer una conexión entre dispositivos end device

Entrar a la computadora a la terminal

Mostrar dirección ip 

ipconfig /all

macOS

ifconfig

## Ver si las interfaces de los equipos están encendidas

show ip interface brief



# CSMA/CD

Para visualizar el diagrama, da click en el: 

![[CSMACD.canvas]]


Son HUB son poco confiables al momento de escalar una red, la red se vuelve más inestable debido a la cantidad de conexiones o interferencias que se ocasionan por los dispositivos que se van añadiendo a la misma


# Ethernet Frame Fields

![[Pasted image 20230221113426.png]]






# Ethernet Mac Address

![[Pasted image 20230221115112.png]]

# Frame processing


# Multicast
An ethernet multicast frame is received and processed by a group of devices that belong to the same multicast group:

* There is a destination MAC address of 01-00-5E when encapsulated data is an ipv4 multicast packet and destination MAC address of 33-33 when the encapsulated data is an IPv6 multicast packet 
* There are other reserved multicast destination MAC addresses for when the encapsulated data is not IP, such as Spanning Tree Protocol(STP)

# Broadcast MAC address

An ethernet broadcast frame is received and processed by every device on the  LAN. The features of an Ethernet broadcast are as follows:
* It has a destination MAC address of FF-FF-FF-FF-FF-FF in hexadecimal (48 one in binary).
* It is flooded out all ethernet switch ports
* The encapsulated data is in IPV4


# Switch Fundamentals


# Switch Learning and Fowarding

Examine the Source MAC address (Learn)

Every frame that enters a swtich is checked for new information lo learn. It does this by examining the source MAC address of the fram and the port number where the frame entered the switch. If the 
source MAC address does not exists

# Filtering


# Frame Forwarding  Methods on Cisco Switches

 * Store and foward switching
 * Cut through switching
 * A big advantage of store and foward
 * Store and foward switching

# Cut switching

* Fast forward
* Fragment free

# Memory Buffering on switches

| method            | description                                                                                                                                                                       |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Port-Based memory | Frames ares stored in queues that are linked to specific ports. A frame is transmitted to the outgoing port only. This delay occurs even if the other frames could be transmitted |
| Shared memory     | Deposits all frames into a common memory buffer. Te frames in the buffer are dynamically linked to the destination                                                                                                                                                                                  |


# Duplex 

There are two types of duplex settings used for communications on an ethernet network:

* Full-duplex - Both ends of the connection can send and receive simultaneously
* Half-duplex - Only one end of the connection can send at a time

Autonegotiation is an optimal is an optimal function found on most Ethernet switches and  NICs. It enables two devices to automatically negotiate the best speed and duplex capabilities.

> [!info] Gigabit ethernet ports only operate in full-duplex
> 


# Duplex and Speed Settings


# Auto-MDIX 

* Most switch devices now support the automatic medium-dependent interface crossover(auto-MDIX)
* The auto-MDIX feature is enabled by default on switches 

> [!info] A direct connection between a router and a host requires a corss-over connection
> 
