

# IPv6

Tiene 128 bits, 64 de red y 64 de host, esta IP se empezó a implementar ya que IPV4  
quedó atrás en cantidad

* Dual stack: Ambos dispositivos corren el mismo protocolo
* Tunneling: Un método de transporte 
* Translantion: Traducción de una IPv6 a una IPv4

Configure and activate IPv6 on the GigabitEthernet 0/0/0 interface with the following addresses:

-   Use **g0/0/0** as the interface name
-   LLA - fe80::1:1
-   GUA - 2001:db8:acad:1::1/64
-   Activate the interface
-   Exit interface configuration mode


``` shell
R1(config)#interface g0/0/0
R1(config-if)#ipv6 address fe80::1:1 link-local
R1(config-if)#ipv6 address 2001:db8:acad:1::1/64
R1(config-if)#no shutdown
%LINK-3-UPDOWN: Interface GigabitEthernet0/0/0, changed state to up
R1(config-if)#exit

```
