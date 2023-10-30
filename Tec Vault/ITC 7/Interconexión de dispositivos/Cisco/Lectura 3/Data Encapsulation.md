---
banner: "https://www.online-tech-tips.com/wp-content/uploads/2020/04/WallpaperAccess.jpg"
banner_y: 0.536
---

#Network  #Cisco 

# Segmenting messages

Knowing the OSI reference model and TCP/IP protocol model will come handy when you learn about how data is encapsulated it moves across a network. It is not as simple as a physical letter being sent.

In theory, simple methods of communication such as videos, email messages with large attachments could be sent to a destination from a source as one massive, uninterrupted stream of bits. The downside is that this large streams of data will slow down the network for other devices. So, large streams of data will delay the network as a result. 

The best approach is to divide the message into smaller, more manageable pieces to be sent over a network. Segmentation is essential because networks that use the TCP/IP protocol suite send data in individual IP packets. Similar to sending a letter in different postcards. Packets containing segments for the same destination can be sent over different paths.

This leads to segmenting messages, having two primary benefits:

* **Increases Speed** - Breaking up a large data stream into smaller packets makes it possible to send a lot of data quickly over a network without clogging up the connection. This means that multiple conversations can happen at the same time on the network, which is called multiplexing.
* **Increases efficiency** - If one small part of the data (called a segment) can't make it to its destination because of a network problem or too much traffic, only that small part needs to be resent. This is better than having to resend the entire big chunk of data.

## Analogy

Let's say you're a teacher, and you need to explain a complex topic, such as photosynthesis, to your students. Instead of trying to explain the entire process in one go, you might segment the information into smaller, more manageable pieces.

For example, you could start by explaining what photosynthesis is and why it's important. Then, you could break down the process into its different stages and explain each one separately. You might even use visual aids, such as diagrams or videos, to help your students better understand the information.

By segmenting the information in this way, you make it easier for your students to understand the topic and remember the different parts of the process. This approach can also help your students stay engaged and interested in the material, as it allows them to absorb the information in smaller, bite-sized pieces rather than trying to understand everything all at once.

Segmentation image example

![[Screenshot 2023-02-20 at 8.00.53.png]]

Multiplexing image example

![[Screenshot 2023-02-20 at 8.01.23.png]]

# Sequencing 

Segmentation and multiplexing can be complicated when used to send messages over a network. This is because they add extra steps and details to the process. Imaging having a 100-page letter, but each envelope to be addressed individually. By doing this, it is possible that envelopes arrive to the destination in a different order. Consequently, the information in the envelope would need to sequence number to ensure that the receiver could reassemble the pages in the proper order.

Network communications needs to have each segment of the message, and it must go through a similar process to ensure that it gets to the correct destination and can be reassembled into the content of the original message, as shown in the figure. TCP is responsible for sequencing the individual segments.

![[Screenshot 2023-02-20 at 9.16.20.png]]

# Protocol Data Units

As the application data is passed down the protocol stack on its way to be transmitted across the network media, various protocol information is added at each level. **This is known as the encapsulation process**

> [!info] Although the UDP PDU is called datagram, IP packets are sometimes also referred to as IP datagrams.

The form that a piece of data takes at any layer is called protocol data unit (PDU). During the encapsulation, each succeeding layer encapsulates the PDU that receives from the layer above in accordance with the protocol being used. At each step of the process, a PDU has a different name to reflect its new functions. PDUs are named according to the protocols of the TCP/IP suite. The PDUs for each form of data are shown in the figure.

![[Screenshot 2023-02-20 at 9.40.46.png]]

* **Data** - The general term for the PDU used at the application layer
* **Segment** - Transport layer PDU
* **Packet** - Network layer PDU
* **Frame** - Data Link layer PDU
* **Bits** - Physical layer PDU used when physically transmitting data over the medium

> [!info] If the transport layer header is TCP, then it is a segment.  If the Transport header is UDP then it is a datagram
> 


# Encapsulation Example

When messages are being sent on a network, the encapsulation process works from top to bottom. At each layer, the upper layer information is considered data within the encapsulated protocol. For example, the TCP segment is considered data within the packet.

![[Screenshot 2023-02-20 at 10.03.30.png]]

# De-encapsulation Example

This process is reversed at the receiving host and is known as de-encapsulation. De-encapsulation is the process used by a receiving device to remove one or more of the protocol headers. The data is de-encapsulated as it moves up the stack toward the end-user application.

![[Screenshot 2023-02-20 at 10.04.25.png]]

![[Screenshot 2023-02-20 at 9.56.13.png]]