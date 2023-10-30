---
banner: "https://cdn.wallpapersafari.com/38/86/dpkw9F.jpg"
banner_y: 0.256
---

#Network #Cisco 

# Operating iOS Access

As you know, all end devices require operating system (OS). The Kernel, as shown in the figure, is the portion of the OS that interacts directly with the computer hardware, it is in charge of managing low the low level resources such as CPU, memory, input/output devices, etc. And provides the interface for applications to communicate with the hardware. 

![[Screenshot 2023-02-20 at 20.53.43.png]]

* **Shell** - The user interface that allows users to request specific task from the computer. These requests can be made either through the CLI or GUI interfaces.
* **Kernel** - Communicates between the hardware and software of a computer and manages how hardware resources are used to meet software requirements.
* **Hardware** - The physical part of a computer including underlying electronics.

When using a CLI (Command Line Interface) the user directly interacts with the system in a text-based environment. The system then executes the commands, often providing textual output.
The CLI requires very little overheat to operate. However, it does require that the user have knowledge of the underlying command structure that controls the system.

``` shell
analyst@secOps ~]$ ls 
Desktop Downloads lab.support.files second_drive
[analyst@secOps ~]$
```

# GUI

A GUI such as Windows, macOS, Linux KDE, Apple iOS, or Android allows the user to interact with the system using an environment of graphical icons, menus, and windows. The GUI example in the figure is more user-friendly and requires less knowledge of the underlying command structure that controls the system. For this reason, most users rely on GUI environments.

![[Screenshot 2023-02-20 at 21.10.29.png]]

> [!info] The operating system on home routers is usually called _firmware_. The most common method for configuring a home router is by using a web browser-based GUI.
> 

# Purpose of an OS

We have learned about networks so far, but operating systems are not far from a PC operating system. Through a GUI, a PC operating system enables the interaction with the user with the following actions:

* **Mouse** - to make selections and run programs.
* **Text-based** - commands.
* **To View Output** - on a monitor.

A CLI-based network operating system (e.g., the Cisco iOS on a switch or router) enables a network technician to do the following actions: 

* **Use a keyboard** -to run CLI-based network programs.
* **Use a keyboard** to enter text and text-based commands.
* **View** - output on a monitor.

Cisco devices run particular iOS versions of their proprietary software. While iOS devices can upgrade their software to obtain additional capabilities.

# Access methods 

As we have learned before, a switch is capable of forwarding the traffic by default and does not need to be explicitly configured to operate. For example, two hosts connected to the same new switch would be able to communicate.

Regardless of the default behavior of a new switch, all of them should be configured and secured to operate. 

![[Screenshot 2023-02-20 at 22.07.10.png]]

> [!info] Some devices, such as routers, may also support a legacy auxiliary port that was used to establish a CLI session remotely over a telephone connection using a modem. Similar to a console connection, the AUX port is out-of-band and does not require networking services to be configured or available.
> 

<br>
<br>
<br>
<br>

# Terminal Emulation programs

There are many ways you can emulate programs, for example: connect to a network device either by a serial connection over a console port, or by an SSH/Telnet connection. These programs help you to enhance your productivity by adjusting window sizes, and other UI interactions.

## PuTTY

![[Screenshot 2023-02-20 at 22.35.17.png]]

<br>
 <br>

<br>


## Tera Term

![[Screenshot 2023-02-20 at 22.35.43.png]]

## SecureCRT

![[Screenshot 2023-02-20 at 22.36.12.png]]



![[Screenshot 2023-02-20 at 22.41.01.png]]