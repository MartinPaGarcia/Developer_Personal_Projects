---
banner: "https://www.nawpic.com/media/2020/minimalist-nawpic-1.png"
banner_y: 0.452
---

#Network #Cisco 

# Primary Command Modes

Previously we learned that all network devices require an OS and that they can b configured using the CLI or a GUI. CLI provides the network administrator with more precise control and flexibility than using CLI to navigate the Cisco iOS.

-   **User EXEC Mode** - This mode has limited capabilities, but is useful for basic operations. It allows only a limited number of basic monitoring commands, but does not allow the execution of any commands that might change the configuration of the device. The user EXEC mode is identified by the CLI prompt that ends with the > symbol.
-   **Privileged EXEC Mode** - To execute configuration commands, a network administrator must access privileged EXEC mode. Higher configuration modes, like global configuration mode, can only be reached from privileged EXEC mode. The privileged EXEC mode can be identified by the prompt ending with the # symbol.

| Command Esc Mode     | Description                                                                                                               | Default Device Prompt |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| User Exec Mode       | * Mode allows access to only a limited number of basic monitoring commands. * It is often referred to as "view-only" mode | >Switch >Router         |
| Privileged EXEC Mode | * Mode Allows access to all commands and features * Monitoring commands and execute configuration and management commands | Switch# Router#                      |

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


# Navigate Between iOS Modes







![[Screenshot 2023-02-20 at 23.34.32.png]]