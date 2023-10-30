---
banner: "https://wallpaper.dog/large/7517.jpg"
---

#Network #Cisco 

# Network Architecture

Networks are evolving rapidly, we rapidly changed simple connections, to connect our entire home to the internet with simple end devices.

As you may know, networks provide a wide range of applicactions and services, they need to be operated with a variety of cables and devices, which make up a physical infrastructure. The term network architecture, in this context refers to technologies that support the infrastructure. and the programmed services and rules, or protocols, that mov data accross the network.

As networks evolve, we have learned that there are four characteristics thta network architects must address to meet user expectations

* Fault to Tolerance
* Scalability 
* Quality of Service
* Security

# Fault to tolerance

This specific expecation is the one that limits the number of affecter devices during a failure. It's purpose is to allow quick recovery when such a failure occurs.  These networks depend on multiple paths between the source and destination of a  message. if one path fails, the messages are instantly sent over different link. That's why, having multiple paths to a destination is known as redundancy.


> [!info] Having Multiple paths to a destination is known  as redundancy. And this is a perfect expample of a Fault to tolerance expectation.


Implementing Packet-switched is a great practice, thus splits traffic into packets that are routed over a shared network. A single message, such as an email or a text message, is broken into multiple message blocks, called packets. Each packet has the necessary addressing information of the source and destination of the message, The routers within the network switch the packets based on the condition of the network at that moment.

![[Screenshot 2023-02-16 at 10.40.48.png]]

# Scalability

A scalable network expands quickly to support user demands. It does without degrading performance of services that are being accessed by existing users. The figure below accepted standards and protocols. 

> [!info] This is when designer follow accepted standards and protocols, then they can make an scalabe network

![[Screenshot 2023-02-16 at 10.47.36.png]]

# Quality of service

QOS is a requirement that is increasing nowadays. New applications need to be available to users over networks, such as streaming service, create higher expectations of the quality delivered by the services. As data, voice, and video content continue to converge onto the same network, QOS becomes a primary mechanism for managing congestion and ensuring reliable delivery of content to the users.

When a congestion occurs, the demand for the bandwidth exceeds the amount available. Network bandwidth in the number of bits that can be transmitted in a single second, or bits per second (bps). When simultaneous communications are attempted across the network, the demand for the network bandwidth can exceed availability, thus creating network congestion.

> [!info] A router can manage the flow of data and voice traffic, giving priority to voice communications if the network experiences congestion
> 

![[Screenshot 2023-02-16 at 10.56.39.png]]

# Network Security 

