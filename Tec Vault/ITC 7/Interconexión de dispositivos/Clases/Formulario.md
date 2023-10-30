e---
banner: "https://assets.hongkiat.com/uploads/minimalist-dekstop-wallpapers/4k/original/12.jpg?3"
banner_y: 0.408
---

# iOS Help Features

## Useful commands 

``` shell
Switch> ?
	connect
	disable
	disconnect
	enable 
	exit 
	logout
	ping
	resume
	show
	telnet
	terminal
	traceroute
Switch(config)#

```

> [!info] The "?" lists all the exec command that are available to you depending on the user privileges. 

> [!important] Using "?" also helps the user to autocomplete commands based on an input.
> 

``` shell
Switch(config)#in?
interface
Switch(config)#interface ?
	Ethernet             IEE 802.3
	Fast Ethernet        FastEthernet IEEE 803.3
	GigabitEthernet      GigabitEthernet IEE 803.3
	Port-channel         Ethernet Channel of interfaces
	Vlan                 Ctalyst Vlans
	range                interface range command
Switch(config)#interface
```

## Command syntax checker

``` shell
Switch(config)#interface 33
		                 ^
% Invalid input detected at '^' marker
```

> [!info] This symbol '^' helps to isolate the error
> 

``` shell
Switch(config)#i
% Ambiguous command: "i"
Switch(config)#i ?
interface ip
Switch(config)#i
```

> [!info] Ambiguous indicates that the command is not clear, when adding the "?" we can notice that there are 2 commands starting with letter "i"
> 

``` shell
Switch(config)#interface 
% Incomplete command
Switch(config)#interface ?
	Ethernet             IEE 802.3
	Fast Ethernet        FastEthernet IEEE 803.3
	GigabitEthernet      GigabitEthernet IEE 803.3
	Port-channel         Ethernet Channel of interfaces
	Vlan                 Ctalyst Vlans
	range                interface range command
Switch(config)#interface Ethernet
```

> [!info] Incomplete means that your command is missing an argument, when adding the "?" we can see what arguments we can use
> 


# Password Configuration

To secure user EXEC mode access, enter line console configuration mode using the **line console 0** global configuration command, as shown in the example. The zero is used to represent the first (and in most cases the only) console interface. Next, specify the user EXEC mode password using the **password** "*password*" command. Finally, enable user EXEC access using the login command. 

``` shell
Sw-Floor-1# **configure terminal**
Sw-Floor-1(config)# **line console 0**
Sw-Floor-1(config-line)# **password cisco**
Sw-Floor-1(config-line)# **login**
Sw-Floor-1(config-line)# **end**
Sw-Floor-1#
```
Console access will now require a password before allowing access to the user EXEC mode.

To have administrator access to all iOS commands, including configuring a device, you must gain privileged mode access. It is the most important access method because it provides complete access to the device.

In the secure privileged EXEC access, use the **enable secret**  *password* global config command, as shown in the example.

## Secret pwd
``` shell
Sw-Floor-1# **configure terminal**
Sw-Floor-1(config)# **enable secret class**
Sw-Floor-1(config)# **exit**
Sw-Floor-1#
```

## VTY pwd

Only for TELNET communications 
``` shell
Sw-Floor-1# **configure terminal**
Sw-Floor-1(config)# **line vty (0 15)**
Sw-Floor-1(config-line)# **password (pwd)**
Sw-Floor-1(config-line)# **login**
Sw-Floor-1(config-line)# **exit**
Sw-Floor-1#
```

# Encrypt passwords

The startup-config and running-config files display most passwords in plaintext. This is a security threat because anyone can discover the passwords, use the **service-encryption** global config command as shown in the example.

``` shell
Sw-Floor-1# **configure terminal**
Sw-Floor-1(config)# **service password-encryption**
Sw-Floor-1(config)#
```
The command applies weak encryption to all unencrypted passwords. This applies only to passwords in the configuration file, not to passwords as they are sent over the network. The purpose is to keep unauthorized individuals from viewing passwords configuration file.

Use the **show running-config** command to verify that passwords are now encrypted. 

``` shell
Sw-Floor-1(config)# **end**
Sw-Floor-1# **show running-config**
!
(Output omitted)
!
line con 0
password 7 094F471A1A0A
login
!
line vty 0 4
 password 7 094F471A1A0A
 login
line vty 5 15
 password 7 094F471A1A0A
 login
!
!
end
```


# Banner Messages 

It is a declaration or a "WARNING" message that is displayed in case of an unauthorized use of information.

To display this message, the following command is required.

``` shell
Sw-Floor-1# **configure terminal** 
Sw-Floor-1(config)# **banner motd #Authorized Access Only#**
```


# Configuration Files

Now you know the basic configurations of a switch, including passwords a banner messages. This topic will show you how to save your configurations.

Firstly, you need to understand that there are two types of system file that store the device configuration:

* **Startup-config** - This is a saved configuration file that is stored in NVRAM. It contains all the commands that will run upon startup or reboot. 
* **Running-config** - This is stored in Random Access Memory (RAM). It reflects the current configuration. Modifying a running configuration affects the operation of a Cisco device immediately, RAM is volatile memory. It loses all this contents when the devices are powered off or restarted.

The **show running-config** privileged EXEC mode command is used to view the running config. As shown in the example, the command will list the complete configuration currently stored in RAM. 


``` shell
Switch>enable
Switch# /This indicates you are in privilaged Exec Mode
Switch#configure terminal
Enter Configuration commands, one per line. End with CNTL/Z.
Switch(config)# /This indicates you are in Global Config Mode
Switch(config)#interface vlan 1
Switch(config-if)# /This indicates you are Interface Configuration Mode](<Sw-Floor-1# show running-config
Building configuration...
Current configuration : 1351 bytes
!
! Last configuration change at 00:01:20 UTC Mon Mar 1 1993
!
version 15.0
no service pad
service timestamps debug datetime msec
service timestamps log datetime msec
service password-encryption
!
hostname Sw-Floor-1
!
(output omitted)
```

# Configuration Mode and Sub configuration modes

Users must enter global configuration mode, which is commonly called global config mode.

From here, CLI configuration changes are made that affect the operation of the device as a whole (so be careful). To identify whether you are working with this global config mode, you have to check if the prompt that appears in your CLI ends like this "**(config)#**" after the device name, such as **Switch(config)#**. 

Global configuration mode is meant to be accessed before other specific configuration modes. From global mode, the user can enter different sub configuration modes. Each of these modes allows the configuration of a particular part or function of the iOS device. Two common sub configuration modes include:

* **Line Configuration Mode** - Used to configure console, SSH, Telnet, or AUX access.
* **Interface Configuration Mode** - Used to configure a switch port or router network interface.

The mode is identified by the command-line prompt that is unique to that particular mode. By default, every prompt begins with the **device name**. Following this, the remainder of the prompt indicates the mode. For example, the default prompt for line configuration mode is **Switch(config-line)#** and the default prompt for interface configuration mode is **Switch(config-if)#**.

``` shell
Switch>enable
Switch# /This indicates you are in privilaged Exec Mode
Switch#configure terminal
Enter Configuration commands, one per line. End with CNTL/Z.
Switch(config)# /This indicates you are in Global Config Mode
Switch(config)#interface vlan 1
Switch(config-if)# /This indicates you are Interface Configuration Mode
```

> [!caution] Always check your CLI privileges before executing commands, they may not work if wrong privileges are used.

# Navigate Between iOS modes

Various commands are used to move in and out of command prompts. To move from user EXEC mode to privileged EXEC mode, use the **enable** command. Use the **disable** privileged EXEC mode command to return to user EXEC mode.

> [!info] Privileged EXEC mode is sometimes called _enable mode_.
> 

To move in and out of global configuration mode, use the **configure terminal** privileged EXEC mode command. To return to the privileged EXEC mode, enter the **exit** global config mode command.

There are many different sub configuration modes. For example, to enter line sub configuration mode, you use the **line** command followed by the management line type and number you wish to access. Use the **exit** command to exit a sub configuration mode and return to global configuration mode.

``` shell
Switch(config)# line console 0
Switch(config-line)# exit
Switch(config)#
```
To be able to move from any sub configuration mode of the global configuration mode to the mode one step above it in the hierarchy of modes, enter the exit command.

To move from any sub configuration mode to the privileged EXEC mode, enter the end command or enter the key combination Ctrl+Z



``` shell
Switch(config-line)# end 
Switch(config-if)# 

```


# Router information

``` shell
R1>enable 
R1#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is not set

        172.17.0.0/16 is variably subnetted, 4 subnets, 2 masks
C       172.17.10.0/24 is directly connected, GigabitEthernet0/0.10
L       172.17.10.1/32 is directly connected, GigabitEthernet0/0.10
C       172.17.30.0/24 is directly connected, GigabitEthernet0/0.30
L       172.17.30.1/32 is directly connected, GigabitEthernet0/0.30


R1#show ip interface brief 
Interface              IP-Address      OK? Method Status                Protocol 
GigabitEthernet0/0     unassigned      YES unset  up                    up 
GigabitEthernet0/0.10  172.17.10.1     YES manual up                    up 
GigabitEthernet0/0.30  172.17.30.1     YES manual up                    up 
GigabitEthernet0/1     unassigned      YES unset  administratively down down 
Vlan1                  unassigned      YES unset  administratively down down>)
```


## DHCP router configuration


``` shell
R1>enable 
R1(config)#ip dhcp excluded-address <low/mask> <high/mask> <-
R1(config)#ip dhcp pool lan0
R1(config)#network 10.5.0.0 255.255.255.240
R1(config)#default-router [10.5.0.1] = gateway
R1(config)#dns-server [10.5.0.10] = ip DNS
```

## Router configuration serial

``` shell
Router> enable
Routrer# Conf terminal
Router(config)#int s0/2/0
"En caso de DTE no establecer un clock rate"
Routrer(config-if)# Clock rate 64000  
Routrer(config-if)# ip address 172.16.101.22 255.255.255.252
Routrer(config-if)# No shut
Routrer(config-if)# exit
Routrer(config)# ip route 172.16.6.0 255.255.255.0 172.16.101.21
"Si tuvieras dos enlaces de la 101"
routrer(config)# ip route 172.16.101.16 255.255.255.252 172.16.101.21
```


# Configuration example router

``` shell
Router>enable
Router#conf terminal
Enter configuration commands, one per line. End with CNTL/Z.
Router(config)#line con 0
Router(config-line)#loggin synchronous
Router(config-line)#exit
Router(config)#no ip domain lookup
Router(config)#int g0/0/0
Router(config-if)#no shut
Router(config-if)#
%LINK-5-CHANGED: Interface GigabitEthernet0/0/0, changed state to up
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0/0, changed state to up
%LINK-5-CHANGED: Interface GigabitEthernet0/0/0.10, changed state to up
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0/0.10, changed state to up
Router(config-if)#int g0/0/0.10
Router(config-subif)#encapsulation dot1Q 10
Router(config-subif)#ip address 172.16.0.1 255.255.255.224
Router(config-if)#int g0/0/0.20
Router(config-subif)#encapsulation dot1Q 20
Router(config-subif)#ip address 172.16.0.33 255.255.255.224
Router(config-subif)#exit
Router(config)#ip dhcp pool 10
Router(dhcp-config)#network 172.16.0.0 255.255.255.224
Router(dhcp-config)#default-router 172.16.0.1
Router(dhcp-config)#
Router(dhcp-config)#ip dhcp pool vlan20
Router(dhcp-config)#network 172.16.0.32 255.255.255.224
Router(dhcp-config)#default-router 172.16.0.33
Router(dhcp-config)#ip dhcp exluded-address 172.16.0.1
Router(dhcp-config)#exit
Router(config)#ip dhcp excluded-address 172.16.0.1
Router(config)#ip dhcp excluded-address 172.16.0.33
Router(config)#
```

# Switch information

``` shell
Switch> **enable**
Switch#S1 #show interface trunk 
Port        Mode         Encapsulation  Status        Native vlan
Gig0/1      on           802.1q         trunking      1

Port        Vlans allowed on trunk
Gig0/1      1-1005

Port        Vlans allowed and active in management domain
Gig0/1      1,10,30

Port        Vlans in spanning tree forwarding state and not pruned
Gig0/1      1,10,30

S1#show interface ?
  Ethernet         IEEE 802.3
  FastEthernet     FastEthernet IEEE 802.3
  GigabitEthernet  GigabitEthernet IEEE 802.3z
  Port-channel     Ethernet channel port interface
  Vlan             Catalyst Vlans
  etherchannel     Show interface etherchannel information
  status           interface line status
  switchport       Show interface switchport information
  trunk            Show interface trunk information
  |                Output Modifiers
  %3Ccr%3E
S1#>)

```

## Default gateway 
D


## Configuration example switch

``` shell
Switch#conf t
Enter configuration commands, one per line. End with CNTL/Z.
Switch(config)#line con 0
Switch(config-line)#logging synchronous
Switch(config-line)#exit
Switch(config)#ip domain lookup
Switch(config)#vlan 10
Switch(config-vlan)#name vlan10
Switch(config-vlan)#vlan 20
Switch(config-vlan)#exit
Switch(config)#exit
Switch#
%SYS-5-CONFIG_I: Configured from console by console
Switch#sh vlan

VLAN  NAME
---- -------------------------------- --------- -------------------------------

1 default active Fa0/1, Fa0/2, Fa0/3, Fa0/4

Fa0/5, Fa0/6, Fa0/7, Fa0/8

Fa0/9, Fa0/10, Fa0/11, Fa0/12

Fa0/13, Fa0/14, Fa0/15, Fa0/16

Fa0/17, Fa0/18, Fa0/19, Fa0/20

Fa0/21, Fa0/22, Fa0/23, Fa0/24

Gig0/1, Gig0/2

10 vlan10 active
20 VLAN0020 active
1002 fddi-default active
1003 token-ring-default active
1004 fddinet-default active
1005 trnet-default active
  

VLAN  Type    SAID     MTU  Parent RingNo BridgeNo Stp BrdgMode Trans1  Trans2

---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------

1     enet   100001    1500   -      -       -       -      -      0      0

10    enet   100010    1500   -      -       -       -      -      0      0
 
20    enet   100020    1500   -      -       -       -      -      0      0

1002  fddi   101002    1500   -      -       -       -      -      0      0

1003  tr     101003    1500   -      -       -       -      -      0      0

1004  fdnet  101004    1500   -      -       -      ieee    -      0      0

1005  trnet  101005    1500   -      -       -      ibm     -      0      0

VLAN Type    SAID      MTU   Parent RingNo BridgeNo Stp BrdgMode Trans1 Trans2

---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
Remote SPAN VLANs

------------------------------------------------------------------------------
Primary Secondary Type              Ports
------- --------- ----------------- ------------------------------------------

Switch#
Switch#conf terminal
Enter configuration commands, one per line. End with CNTL/Z.
Switch(config)#int range fa0/1 - 12
Switch(config-if-range)#switchport mode access
Switch(config-if-range)#switchport access vlan 10
Switch(config-if-range)#int range fa0/13 - 24
Switch(config-if-range)#switchport mode access
Switch(config-if-range)#switchport access vlan 20
Switch(config-if-range)#int g0/1
Switch(config-if)#e
Switch(config-if)#
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to down
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to up
Switch(config-if)#
```