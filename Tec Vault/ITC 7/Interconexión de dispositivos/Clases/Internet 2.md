
# Conceptos

* Simplex
* Half duplex
* Full duplex
* Spectrum and Bandwith 
	* Spectrum
	* Absolut bandwidth
	* Effective bandwidth
	* DC component
* Analog and Digital Data transmissions


# Medio Físicos

Se divide en dos categorias

## Medios Guiados

* Cable Coaxial 
* Por Trenzado
* Fibra Optica

## Medios No Guiados

* Comunicación por satélites
* Microondas
* Ondas de Radio

# Medios de cobre

Este tipo de cableado es utilizado para las comucaciones de datos, genralmente consiste en una secuencia de alambres individuales de cobre que forman circuitos que cumplen objetivos específicos de señalización.


# Interferencia Electromagnetica (EMI)

Este tipo de interferencia de radiofrecuencia RFI: Las señales de EMI y RFI pueden distorsionar
y dañar las señales de datos que transportan los medios de cobre. Las posibles fuentes de EMI y RFI incluyen de radio y dispositivos electromagneticos como las luces o los motores eléctricos.

Crosstalk: se trata de una perturbación causada por los campos eléctricos o magnéticos de una señal de un hilo a la señal de un hilo adyacente.



# Coaxial 

Consiste en:
* Un conductor de cobre rodeado de una capa de aislante flexible
* Una malla de cobre tejida o una hoja metálica que actúa como segundo alambre del circuito y como blindaje para el conductor interno
* La segunda capa o blindaje reduce la cantidad de interferencia electromagnética externa
* La envoltura del cable recubre el blindaje

> [!faq] Anteriormente los LANs se conectaba con cables Coaxiales, solo que esto era una desventaja, ya que al momento de desconectar un equipo, toda la red se caía.


# Cable de par trenzado no blindado (UTP)

*Investigar*


## Estándares de cableado UTP

*Investigar*


568 -A 10/100/1000Base-TX Ethernet

![[Screenshot 2023-02-16 at 12.28.24.png]]

![[Screenshot 2023-02-16 at 12.28.43.png]]

# Fibra Óptica

* Existen fibras de plástico o de vidrio
* Los bits se codifican en la fibra como impulsos de luz.

Comparación entre cableado de cobre y de fibra óptica

* La fibra óptica es un medio inmune a la interferencia electromagnética y no conduce corriente eléctrica no deseada cuando existe un problema de conexión a tierra.
* La fibra puede utilizarse en longitudes mucho mayores que su contraparte de cobre sin la necesidad de regenerar la señal.

## Dificultades de la fibra óptica

* Más costoso que los medio de cobre
* Se necesitan diferentes habiliades y equipamiento para terminar y empalmar una gran cantidad de tráfico entre los servicios de distribución
* Más delicado que los medios de cobre

## Se utiliza principalmente

* Para la interconexión de los edificios 
* Como cableado backbone para conexiones punto a punto con una gran cantidad de tráfico entre los servicios de distribución de datos

## Fabricación de la fibra óptica

* Consisten en un revestimiento exterior de PVC y varios materiales de esfuerzo que rodean la fibra óptica y su revestimiento
* El revestimiento rodea la fibra de plástico o de vidrio y está diseñado para prevenir la perdida de luz

## Producción 

* Los láseres o diodos de emisión (LED) generan impulsos de luz que utilizan para representar los datos transmitidos com bits en los medios.
* Los dispositivos electrónicos semiconductores, denominados fotodiodos, detectan los impulsos de luz y los convierten en voltajes que pueden reconstruirse en tramos de datos.

# Fibra multimodo y monomodo

Los cables de fibra óptica pueden clasificarse en dos tipos:

* Monomodo 
	* Transporta un sólo rayo de luz, generalmente emitido desde un láser. Este tipo de fibra puede transmitir impulsos ópticos en distancias muy largas, ya que la luz del láser y es unidireccional, viaja a través del centro de la fibra.
* Multimodo
	* A menudo utiliza emisores de LED que no generan una única ola de luz coherente
	* La luz de un LED ingresa a la fibra multimodo en diferentes ángulos


![[Screenshot 2023-02-16 at 13.02.52.png]]