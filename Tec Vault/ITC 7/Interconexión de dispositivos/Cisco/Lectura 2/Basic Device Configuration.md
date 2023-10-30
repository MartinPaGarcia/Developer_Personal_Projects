---
banner: "https://wallpaperaccess.com/full/6905518.jpg"
banner_y: 0.464
---
#Network #Cisco 

# Device Names

By now, you should be ready to configure devices! The first configuration command on any device should be to give it a unique device name or hostname. By default, all devices are assigned a factory default name. For example, a Cisco iOS switch is "Switch".

What should I do if all devices were left with their default names? This is a problem, because, you are not going to be able to identify devices as easily. For instance, how would know that you are connected to the right device when accessing it remotely using SSH? The hostname provides confirmation that you are connected to the correct device.

> [!hint] The default name shout be named to something more descriptive. Choosing names wisely will make it easier to be remembered .
> 

## Tips for naming new devices

* Start with a letter
* Contain no spaces
* End with a letter or digit
* Use only letters, digits, and dashes
* Be less than 64 characters

> [!important] Organizations must name convention that makes it easy and intuitive to identify a specific device. 

The following is an example of three switches, spanning three different floors, are interconnected together in a network. The naming convention that was used incorporated the location and the purpose of each device. Network documentation should explain how these names were chosen so additional devices can be named accordingly.

![[Screenshot 2023-02-23 at 0.36.46.png]]

# Password guidelines

Always remember that using a weak password will make your system more vulnerable to attacks. That's why all network devices must be configured with a password to limit administrative access.

All network devices must limit administrative access by securing privileged EXEC, user EXEC, and remote Telnet access with passwords. In addition, all passwords should be encrypted and legal notifications provided. The following are recommendations of how strong passwords must be assigned:

* Use passwords that are more than eight characters in length 
* Use a combination of characters (upper, lowercase, and special characters)
* Avoid using the same password for all devices
* Do not use common words because they are easily guessed

> [!info] Most of the labs in this course use simple passwords such as **cisco** or **class**. These passwords are considered weak and easily guessable and should be avoided in production environments. We only use these passwords for convenience in a classroom setting, or to illustrate configuration examples.
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

``` shell
Sw-Floor-1# **configure terminal**
Sw-Floor-1(config)# **enable secret class**
Sw-Floor-1(config)# **exit**
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













![[Screenshot 2023-02-23 at 0.38.50.png]]![[Screenshot 2023-02-23 at 0.39.01.png]]