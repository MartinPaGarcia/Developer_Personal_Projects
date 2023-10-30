---
banner: "https://images.pling.com/img/00/00/63/21/82/1779108/dudt1.jpg"
banner_y: 0.3
---

#Network #Cisco 

# Configuration Files

Now you know the basic configurations of a switch, including passwords a banner messages. This topic will show you how to save your configurations.

Firstly, you need to understand that there are two types of system file that store the device configuration:

* **Startup-config** - This is a saved configuration file that is stored in NVRAM. It contains all the commands that will run upon startup or reboot. 
* **Running-config** - This is stored in Random Access Memory (RAM). It reflects the current configuration. modifying a running configuration affects the operation of a Cisco device immediately, RAM is volatile memory. It loses all this contents when the devices are powered off or restarted.

The **show running-config** privileged EXEC mode command is used to view the running config. As shown in the example, the command will list the complete configuration currently stored in RAM. 


``` shell
[Switch>enable
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

# After the Running configuration

If changes made to the running config do not have the desired effect and the running-config has no yet been saved, you can restore the device to its previous configuration.  Remove the changed commands individually, or reload the device using the reload privileged EXEC mode command to restore the startup-config.

The downside to using the **reload** command to remove an unsaved running config is the brief amount of time the device will be offline, causing network downtime.

When a reload is initiated, the iOS will detect that the running config has changes that were not saved to the startup configuration. A prompt will appear to ask whether to save the changes. To discard the changes, enter n or no.

Alternatively, if undesired changes were saved to the startup config, it may be necessary to clear all the configurations. This requires erasing the startup config and restarting the device. The startup config is removed by using the erase startup-config privileged EXEC mode command. After the command is issued, the switch will prompt you for confirmation. Press Enter to accept.

After removing the startup config from NVRAM, reload the device to remove the current running config file from RAM. On reload, a switch will load the default startup config that originally shipped with the device.

# Capture Configuration to a Text File

Configuration files can also be saved and archived to a text document. This sequence of steps ensures that a working copy of the configuration file is available for editing or reuse later.

For example, assume that a switch has been configured, and the running config has been saved on the device.

**Step 1.** Open terminal emulation software, such as PuTTY or Tera Term, that is already connected to a switch.
![[Screenshot 2023-02-23 at 1.40.14.png]]

**Step 2.** Enable logging in the terminal software and assign a name and file location to save the log file. The figure displays that **All session output** will be captured to the file specified (i.e., MySwitchLogs).

![[Screenshot 2023-02-23 at 1.40.55.png]]

**Step 3.** Execute the **show running-config** or **show startup-config** command at the privileged EXEC prompt. Text displayed in the terminal window will be placed into the chosen file.

``` shell
Sw-Floor-1# **show running-config**
Building configuration...
(output omitted)
```

**Step 4.** Disable logging in the terminal software. The figure shows how to disable logging by choosing the **None** session logging option.

![[Screenshot 2023-02-23 at 1.42.27.png]]

The text file created can be used as a record of how the device is currently implemented. The file could require editing before being used to restore a saved configuration to a device.

To restore a configuration file to a device:

**Step 1.** Enter global configuration mode on the device.

**Step 2.** Copy and paste the text file into the terminal window connected to the switch.

The text in the file will be applied as commands in the CLI and become the running configuration on the device. This is a convenient method of manually configuring a device.

