---
banner: "https://wallpaperaccess.com/full/1973703.jpg"
banner_y: 0.516
---
#Network #Network 

# Basic IOS Command Structure

This topic covers the basic structure of command for the Cisco iOS.  As a network administrator, you should understand the basic iOS command structure to be able to use the CLI for device configuration.

> [!info] Remember that commands in Cisco iOS device are meant to be run with certain privileges.
> 


![[Screenshot 2023-02-22 at 22.23.10.png]]

* **Keyword** - This is a specific parameter defined in the operating system. (In the figure, **ip protocols**)
* **Argument** - This is not predefined; it is a value or variable defined by the user (in the figure, **192.168.10.5**)

> [!important] After entering each complete command, including any keywords and arguments, press the enter key to submit the command
> 

# iOS Command Syntax Check

Remember that many commands might require one or more arguments. It is important to determine the keywords and arguments required for a command.

As identified in the table, boldface text indicates commands and keywords that are entered as shown. Italic text indicates an argument for which the user provides the value.

![[Screenshot 2023-02-22 at 22.31.01.png]]

## Syntax 

* **Description** command is a description *string*; the argument is a string value provided by the user.
* The **description** command is typically used to identify the purpose of an interface.
	*  For instance, entering the command, description connects to the main headquarters office switch, describes where the other device is at the end of the connection. 


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
Switch>enable
Switch# ?
	configure
	connect
	copy
	debug
	delete
	dir
	disable
	disconnect
	enable
	erase
	exit
	logout
	more
	no
	ping
	reload
	resume
	setup
	show
	--More--
	ssh
	telnet
	terminal
	traceroute
	undebug
	vlan
	write
Switch#configure termal
Switch(config)>?
	boot
	cdp
	clock
	crypto
	do
	enable
	end
	exit
	hostname
	interface
	ip
	line
	mac
	mac-address-table
	mls
	no
	port-channel
	privilege
	--MORE--
	service
	snmp-server
	spanning-tree
	username
	vlan
	vtp
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

# Hot Keys and Shortcuts

![[Screenshot 2023-02-22 at 22.35.53.png]]

> [!note] While the **Delete** key typically deletes the character to the right of the prompt, the IOS command structure does not recognize the Delete key.
> 

> [!tip] If a command output produces more text that can be displayed in a terminal window, the iOS will display a "--More--" prompt. 
> 

The following table describes the keystrokes that can be used when this prompt is displayed:

![[Screenshot 2023-02-23 at 0.00.43.png]]

This table lists commands used to exit out an operation: 

![[Screenshot 2023-02-23 at 0.01.22.png]]

