
#Network #Cisco 

# Communications Fundamentals

Net works may vary in size, shape, and function. They can be as complex as devices across the internet, or simple as 2 computers connected directly to one cable, and anything in-between. However, simply having a wired or wireless physical connection between end devices is not enough to enable communications. But, for communications to occur, devices must know "how" to communicate.

People exchange ideas using communication methods. However, all communications have the following 3 elements:

* Message source (Sender) - Message sources are people, electronic devices, things that need to send a message to other individuals or devices.
* Message Destination (receiver) - The destination receives the messages, and interprets it.
* Channel - This is the pathway in which the media travels from the source to destination.


# Communications protocols

As you know, a message is whether by face-to-face communication or over a network is governed by rules called protocols. These protocols are specific to the type of communication method being used. In our daily communications, the rules we use to communicate over one medium, like phone calls, re not necessarily the same as the rules for using another medium, such as sending a letter.


## Analogy

Prior to communication, a person must agree on how to communicate. If communication is using voice, persons must first agree on the language. Next, when they have a message to share, they must be able to format that message in a way that is understandable.

If someone uses the English language, but poor sentence structure, the message can easily be misunderstood.


# Rule establishment

Before communications can occur, individuals must establish rules or agreements to govern the conversation, take the next message as an example: 

> [!example] Humans communication between govern rules. It is verydifficult tounderstand messages that are not correctly formatted and donot follow the established rules and protocols. A estrutura da gramatica, da lingua, da pontuacao e do sentence faz a configuracao humana compreensivel por muitos individuos diferentes.


 Notices how difficult it is to read the message because it is not formatted properly. It should be using rules (in this case like: grammar) that are necessary for effective communication, like the next example:

> [!example] Rules govern communication between humans. It is very difficult to understand messages that are not correctly formatted and do not follow the established rules and protocols. The structure of the grammar, the language, the punctuation and the sentence make the configuration humanly understandable for many different individuals.

Protocols must account for the following requirements to successfully deliver a message that is understood by the receiver:

* An identified sender and receiver
* Common language and grammar
* Speed and timing of delivery
* Confirmation or acknowledgement requirements

# Network Protocol Requirements

The protocols that are used in network communications share many of these fundamental traits (in addition to identifying the source and destination, computer and network protocol): 

* Message encoding
* Message formatting and [[Data Encapsulation]]
* Message size
* Message timing
* Message delivery options

# Message Encoding

One of the first steps to sending a message is encoding, this is a fundamental process of converting information into another acceptable form, for transmissions. Decoding reverses this process to interpret the information.

## Analogy

Imagine a person calls a friend to discuss the details of a beautiful sunset. 

To communicate the message, she converts her thoughts into an agreed upon language. She then speaks the words, using the sounds and inflections of spoken language that convey the message. Her friend listens to the description and decodes the sound to understand the message he received.

# Message Formatting and Encapsulation

When a message is sent from a source to destination, it must use a specific format or structure. Message formats depend on the type of message and the channel that is used to deliver the message.

## Analogy 

A common example of requiring the correct format in human communications is when sending a letter.

An envelope has the address of the sender and receiver, each located at the proper place on the envelope. If the destination address and formatting is not correct, the letter is not delivered.

The process of placing one message format (the letter) inside another message format (the envelope) is called encapsulation. De-Encapsulation occurs when the process is reversed by the recipient and the letter is removed from the envelope.

![[Screenshot 2023-02-19 at 20.32.51.png]]


## Network 

Similar to sending a letter, a message that is sent over a computer network follows specific format rules for it to be delivered and processed. 

Internet Protocol (IP) is a protocol with a similar function to the envelope example. In the figure, the fields of the internet version 6 (IPV6) packet identify the source of the packet and its destination. IP is responsible for sending a message from the message source to destination over one or more networks.

> [!info] The fields of the IPv6 packet are discussed in detail in another module
> 

![[Screenshot 2023-02-19 at 20.36.58.png]]

#  Message Size

Another rule of communication is message size. 

## Analogy

When people communicate with each other, the message that they send are usually broken into smaller parts or sentences. These sentences are limited in size to what the receiving person can process at one time, as shown in the figure. It also makes it easier for the receiver to read and comprehend.


![[Screenshot 2023-02-19 at 20.40.39.png]]


## Network

Likewise, when a long message is sent from one host to another over a network, it is necessary to break the message into smaller pieces, as shown in the figure below. The rules that govern the size of the pieces, or frames, communicated across the network are very strict. They can also be different, depending on the channel used. Frames that are too long or too short are not delivered.

The size restrictions of frames require the source host to break a long message into individual pieces that meet both the minimum and the maximum size requirements, The long message will be sent in separate frames, with each frame containing a piece of the original message. Each frame will also have its own addressing information. At the receiving host, the individual pieces of the message are reconstructed into the original message


![[Screenshot 2023-02-19 at 20.43.57.png]]


# Message Timing

Message timing is very important in network communications. Message timing includes the following:
* Flow Control - This is the process of managing the rate of data transmission. Flow control defines how much information can be sent and the speed at which it can be delivered. For example, if one person speaks too quickly, it may be difficult for the receiver to hear and understand the message. In network communication, there are protocols used by the source and destination devices to negotiate and manage the flow of information.
* Response Timeout - If a person asks a question and does not hear a response within an acceptable amount of time, the person assumes that no answer is coming and reacts accordingly. The person may repeat the question or, instead, may go on with the conversation. Host on the network use protocols that specify how long to wait for responses and what action to take if a response timeout occurs.
* Access Method - This determines when someone can send a message. Likewise, when a device wants to transmit on a wireless LAN, it is necessary for the WLAN network interface card (NIC) to determine whether the wireless medium is available.

![[Screenshot 2023-02-19 at 21.32.56.png]]


# Message Delivery Options

A message can be delivered in different ways

## Analogy 

Sometimes a person wants to communicate information to a single individual. At other times, the person may need to send information to a group of people at the same area 

![[Screenshot 2023-02-19 at 21.15.36.png]]

## Network

Network communications have a similar option to communicate. As shown in the figure below, there are three types of data communications

* Unicast - Information is being transmitted to a single end device.
![[Screenshot 2023-02-19 at 21.17.58.png]]
* Multicast - information being transmitted to one or more end devices.
![[Screenshot 2023-02-19 at 21.19.14.png]]
* Broadcast - information is being transmitted to all end devices
![[Screenshot 2023-02-19 at 21.20.18.png]]

# A Note About the Node Icon

Networking documents and topologies often represent networking and end devices using a node icon. Nodes are typically represented as a circle. The figure shows a comparison of the three different delivery options using node icons instead of computer icons. 


![[Screenshot 2023-02-19 at 21.36.26.png]]






![[Screenshot 2023-02-19 at 19.16.59.png]]





![[Screenshot 2023-02-19 at 19.19.01.png]]







![[Screenshot 2023-02-19 at 19.20.44.png]]