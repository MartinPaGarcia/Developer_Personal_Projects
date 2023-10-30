---
banner: "https://cdn.wallpapersafari.com/42/34/w3xcOr.jpg"
banner_x: 0.57143
banner_y: 0.568
---

#Network #Cisco 

# Host Roles

As you may now, it is important that you are connected via (computer, tablet or smartphone) to a network, as we talk earlier in [[Network affect our lives]].
It is important to remember that devices are connected directly to a network communication are classified asa a hosts. Hosts are also called End devices as we learned in ([[Internet 1]]).
Some hosts are also called clients. The term "hosts" specifically refers to devices on the network that are assigned a number for communication purposes. This number identifies the host within a certain network. We know this term as Internet Protocol (IP) as shown in [[Modelo OSI]]. IP identifies the host and the network to which the host is attached.

Servers are computers with a specific software that allows them to provide precise information, like email or web pages, to other end devices on the network (not always the same). A server requires web server software in order to provide services to the network.

```ad-info
A computer with a server software can provide services simultaneously to many different clients 

```



Client connects to the internet and then to the server


![[Screenshot 2023-02-15 at 23.25.08.png]]
An example of client software is a web browser, like Google Chrome or FireFox. A simple computer can also run multiple types of client software. The following table lists three common types of software. 

| Type  | Description                                                                  |
| ----- | ---------------------------------------------------------------------------- |
| Email | The email server runs a server software. Clients use sofware such as outlook |
| Web   | The web server runs a web server. Clients use software such as Chrome        |
| File  | The file server stores files in a central location. Clients file explorer    |


# Peer-to-Peer

Both clients and servers usually run on separete computers, but there are some exceptions. Small buisnesses and homes, many computers function as servers and clients on the networkd. This type of network is often called Peer-to-Peer network.

![[Screenshot 2023-02-15 at 23.24.55.png]]

Advantages of Peer-to-Peer networking:
* Easy to set up
* Less complex
* Lower cost
* Can be used for simple tasks such as transfering files and sharing printers

Disadvantages
* No centralized administration
* Not as secure
* Not scalable
* All devices may act as bot clients and serers wich can slow their performance

# End devices 

We are more familiar with the end devices. To be able to distiguish one end device from another, each end devices has an address. When an end devices initiates communication, it uses the address of the end device destination to specify wher to deliver the message.

![[Screenshot 2023-02-15 at 23.29.14.png]]

```ad-info
An end device is either the source or destination of a message transmited over the network

```

# Intermediary devices

These type of devices are able to connect the individual (end devices) to the network. Theu also connect multiple individual networks to form an internetwork. They also provide connectivity, and ensure that data flows accross the network.

![[Screenshot 2023-02-15 at 23.37.53.png]]

Intermediary network devices perform some or all of these functions:

* Regenerate and retransmit communication signals
* Maintain information about pathways exists through the network and internetwork
* Direct data along alternate pathways when there is a link failure
* Notify other devices of errors
* Classify and direct messages according to priorities
* Permit or deny the flow of data, based on security

```ad-info
Not shown is a legacy Ethernet Hub. An ethernet hub is also known as a multiport repeater. Repeaters regenerate and retransmits communication signals. Notices that all intemediary devices perform the function of a repeater

```

# Network Media

Communications to be transmited accross a netwoork media. We know that media provides the channel over whichthe message travels from sourcer destination.

Modern networks primarily use three types of media to interconnect devices, as shown in the figure:

* Metal Wires whitin clables - Data is encoded into electrical impulses
* Glass or plastic fibers within cables (fiber-optic cable) - Data is encoded into pulses of light
* Wireless transmission - Data is encoded via modulation of specific frequencies of electormagnetic waves

![[Screenshot 2023-02-16 at 0.19.31.png]]
