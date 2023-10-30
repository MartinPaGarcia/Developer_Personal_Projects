---
banner: "https://edge.99images.com/photos/wallpapers/3d-abstract/4k-minimal%20android-iphone-desktop-hd-backgrounds-wallpapers-1080p-4k-0mbpn.jpg"
banner_y: 0.608
---

#Network #Cisco

# Network Protocol Suites

In many cases, protocols must be able to work with other protocols so that your online experience gives you everything you need for network communications. Protocol Suites are designed to work with each other seamlessly. 

A protocol suite is a group of inter-related protocols necessary to perform a communication function.

One of the best ways to visualize how the protocols within a suite interact is to view the interaction as a stack. A protocol stack shows how the individual protocols within a suite are implemented. The protocols are viewed in terms of layers, with each higher-level service depending on the functionality defined by the protocols shown in the lower levels. The lower layers of the stack are concerned with moving data over the network and providing services to the upper layer, which are focused on the content of the message being sent.

As illustrated in the figure, we can use layers to describe the activity occurring in face-to-face communication. At the bottom is the physical layer, where we have two people with voices saying words out loud. In the middle are the rules that stipulate the requirements of communication, including that common language must be chosen. At the top is the content layer, and this is where the content of the communication is actually spoken.

![[Screenshot 2023-02-19 at 23.20.42.png]]

# Evolution of Protocol Suites

A protocol suite is a set of protocols that work together to provide comprehensive network communication services. Since the 1970s there have been several different protocol suites. 

During the evolution of the network communications and the internet, there were several competing protocol suites, as shown in the figure.

![[Screenshot 2023-02-19 at 23.23.19.png]]

* Internet Protocol Suite or TCP/IP - This is the most common and relevant suite used today. The TCP/IP protocol suite is an open standard protocol suite maintained by the Internet Engineering Task Force (IETF).
* Open Systems Interconnection (OSI) Protocols - This is a family of protocols developed jointly in 1977 by the International Organization for Standardization (ISO) and the International Telecommunications Union (ITU). OSI protocol also included a seven-layer model called OSI reference model, categorizes the functions of its protocols. 
* AppleTalk - A short-lived proprietary protocol suite released by Apple Inc. in 1985 for Apple devices. In 1995, Apple adopted TCP/IP to replace AppleTalk. 
* Novell NetWare - A short-lived proprietary protocol suite and network operating system developed by Novell Inc. in 1983 using the IPX network protocol. In 1995, Novell adopted TCP/IP to replace IPX.

# TCP/IP Protocol Suite

TCP/IP includes many protocols and continues to evolve to support new services. Some of the more popular ones are shown in the figure.

![[Screenshot 2023-02-19 at 23.33.13.png]]

TCP/IP is the protocol suite used by the internet and the network today. TCP/IP has two important aspects for vendors and manufacturers:

* Open standard protocol suite - This means it is freely available to the public and can be used by any vendor on their hardware or their software.
* Standard-based protocol suite - This means it has been endorsed by the networking industry and approved by a standards organization. This ensures that products from different manufacturers can interoperate successfully.

## Application Layer

### Name system

* DNS - Domain Name System. Translates domain names, into IP addresses.

### Host Config 

* **DHCPv4** - Dynamic Host Configuration Protocol for IPv4. A DHCPv4 dynamically assigns IPv4 addressing information to DHCPv4 clients at start-up and allows the addresses to be re-used when no longer needed.
* **DHCPv6** - Dynamic Host Configuration Protocol for IPv6. A DHCPv6 dynamically assigns IPv6 addressing information to DHCPv6 clients at start-up and allows the addresses to be re-used when no longer needed.
* **SLAAC** - Stateless Address AutoConfiguration. A method that allows a device to obtain its IPv6 information without using DHCPv6 server.
 
### Email

* **SMTP** - Simple Mail Transfer Protocol. Enables clients to send email to a mail server, and enables servers to send email to other servers.
* **POP3** - Post Office Protocol Version 3. Enables clients to retrieve email from a mail server as well maintaining email on the server.
* **IMAP** - Internet Message Access Protocol. Enables clients to access email stored mail server as well as maintaining email on the server.

### File Transfer

*  **FTP** - File Transfer Protocol. Sets the rules that enable a user on one host to access and transfer files to and from another host over a network. FTP is a reliable, connection-oriented, and acknowledge file delivery protocol.
* **SFTP** - SSH File transfer Protocol. As an extension to Secure Shell (SSH) protocol, SFTP can be used to establish a secure file transfer session in which the file transfer is encrypted. SSH is a method for secure remote login that is typically used for accessing the command line of a device.

### Web and Web Service 

* **HTTP** - Hypertext Transfer Protocol. A set of rules for exchanging text, graphic images, sound, video, and other multimedia files of the World Wide Web (WWW)
* **HTTPS** - HTTP Secure. A secure form of HTTP that encrypts data that is exchanged over the WWW.
* **REST** - Representational Stat Transfer. A web services that uses application programming interfaces (APIs) and HTTP request to create web applications.

## Transport Layer

### Connection-Oriented 

* **TCP** - Transmission Control Protocol. Enables reliable communication between processes running on separate hosts and provides reliable, acknowledged transmissions that confirm successful delivery.

### Connectionless 

* **UDP** - User Datagram Protocol. Enables a Process running on a host to send packets to a process running on another host. However, UDP confirm successful datagram transmission.


## Internet Layer

### Internet Protocol

-   **IPv4** - Internet Protocol version 4. Receives message segments from the transport layer, packages messages into packets, and addresses packets for end-to-end delivery over a network. IPv4 uses a 32-bit address.
-   **IPv6** - IP version 6. Similar to IPv4, but uses a 128-bit address.
-   **NAT** - Network Address Translation. Translates IPv4 addresses from a private network into globally unique public IPv4 addresses.

### Messaging

-   **ICMPv4** - Internet Control Message Protocol for IPv4. Provides feedback from a destination host to a source host about errors in packet delivery.
-   **ICMPv6** - ICMP for IPv6. Similar functionality to ICMPv4 but is used for IPv6 packets.
-   **ICMPv6 ND** - ICMPv6 Neighbor Discovery. Includes four protocol messages that are used for address resolution and duplicate address detection.

### Routing Protocols

-   **OSPF** - Open Shortest Path First. Link-state routing protocol that uses a hierarchical design based on areas. OSPF is an open standard interior routing protocol.
-   **EIGRP** - EIGRP - Enhanced Interior Gateway Routing Protocol. An open standard routing protocol developed by Cisco that uses a composite metric based on bandwidth, delay, load and reliability.
-   **BGP** - Border Gateway Protocol. An open standard exterior gateway routing protocol used between Internet Service Providers (ISPs). BGP is also commonly used between ISPs and their large private clients to exchange routing information.


## Network Access Layer

### Address Resolution

-   **ARP** - Address Resolution Protocol. Provides dynamic address mapping between an IPv4 address and a hardware address.


> [!info] You may see other documentation state that ARP operates at the Internet Layer (OSI Layer 3). However, in this course we state that ARP operates at the Network Access layer (OSI Layer 2) because it's primary purpose is the discover the MAC address of the destination. A MAC address is a Layer 2 address.
> 


### Data Link Protocols

-   **Ethernet** - Defines the rules for wiring and signaling standards of the network access layer.
-   **WLAN** - Wireless Local Area Network. Defines the rules for wireless signaling across the 2.4 GHz and 5 GHz radio frequencies.

# TCP/IP Communication Process 

The figures demonstrate the complete communication process using an example of a web server transmitting data to a client.

Click the Play in the figure to view an animation of a web server encapsulating and sending a web page to a client

![[Screenshot 2023-02-20 at 0.08.06.png]]![[Screenshot 2023-02-20 at 0.08.34.png]]![[Screenshot 2023-02-20 at 0.09.03.png]]![[Screenshot 2023-02-20 at 0.17.06.png]]![[Screenshot 2023-02-20 at 0.17.18.png]]![[Screenshot 2023-02-20 at 0.17.28.png]]