---
banner: "https://wallpapersmug.com/download/1366x768/6d3c26/dark-minimal-mountains.png"
banner_y: 0.164
---

#Network #Cisco 

# Network Protocol Overview

For end devices to be able to communicate over a network, each device must abide by the same set of rules. These rules are called protocols, and they have many functions in a network, This topic gives you an overview of network protocols.

This network protocols define a common format and set of rules for exchanging messages between devices. Protocols are then implemented by end devices and intermediary devices in software, hardware, or both. Each network has its own function format and rules for communications.

The Table lists the various types of protocols that are needed to enable communications across one or more networks.


| Protocol Type                    | Description                                                                                                                                                                                                                                            |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Network Communications Protocols | Protocols enable two or more devices to communicate over one or more networks. The ethernet family of technologies involves a variety of protocols such as IP, Transmission Control Protocol (TCP), HyperText Transfer Protocol (HTTP), and many more.  |
| Network Security Protocols       | Protocols secure data to provide authentication, data integrity, and encryption. Examples of secure protocols include Secure Shell (SSH), Secure Sockets Layer (SSL), and Transport Layer Security (TSL).                                               |
| Routing Protocols                | Protocols enable routers to exchange route information, compare path information, and then to select the best path to the destination network. Examples of routing protocols include Open Shortest Path First (OSPF) and Border Gateway Protocol (BGP). |
| Service Discovery Protocols      | Protocols are used for automatic detection of services. Examples of service discovery protocols include Dynamic Host Configuration Protocol (DHCP) which discovers services for IP address allocation, and Domain Name System (DNS) which is used to perform name-to-IP address translation.                                                                                                                                                                                                                                                       |

# Network Protocol functions

Network communications protocols are responsible for a variety of functions necessary for network communications between end devices. For example, the figure how does the computer send a message, across several network devices, to the server

![[Screenshot 2023-02-19 at 22.28.23.png]]

# Protocol interaction

A message sent over a computer network typically requires the use of several protocols, each one with its own functions and format. The figure shows some common network protocols used when a device sends a request to a web server for its web page.

![[Screenshot 2023-02-19 at 22.54.10.png]]

The protocols in the figure are described as follows:

* Hypertext Transfer Protocol (HTTP) - This protocol governs the way a web server and a web client interact. HTTP defines the content and formatting of requests and responses that are exchanged between the client and server. Both the client and the web server software implement HTTP as part of the application. HTTP relies on other protocols to govern how the messages are transported between the client and server.
* Transmission Control Protocol (TCP) - This protocol manages the individual conversations. TCP is responsible for guaranteeing the reliable delivery of the information and managing flow control between the end devices. 
* Internet Protocol (IP) - This protocol is responsible for delivering messages from the sender to the receiver. IP is used by routers to forward the messages across multiple networks.
* Ethernet - This protocol is responsible for the delivery of messages from one NIC to another NIC on the same Ethernet local area network (LAN).


![[Screenshot 2023-02-19 at 23.01.20.png]]
