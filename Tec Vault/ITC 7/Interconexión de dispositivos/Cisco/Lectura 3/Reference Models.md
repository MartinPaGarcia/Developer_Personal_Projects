---
banner: "https://wallpaperboat.com/wp-content/uploads/2021/03/16/71285/minecraft-minimalist-23.jpg"
banner_y: 0.364
---

#Network #Cisco 

# Benefits of Using a Layered Model

You cannot actually watch real packets travel across a real network, the way you can watch the components of a car being put together on an assembly line. so, it helps to have a way of thinking about a network so that you can imagine what is happening. A model is useful in these situations.

Complex concepts such as how a network operates can be difficult to explain and understand. For this reason, a layered model is used to modularize the operations of a network into manageable layers.

These are the benefits of using a layered model to describe network protocols and operations:

-   Assisting in protocol design because protocols that operate at a specific layer have defined information that they act upon and a defined interface to the layers above and below
-   Fostering competition because products from different vendors can work together
-   Preventing technology or capability changes in one layer from affecting other layers above and below
-   Providing a common language to describe networking functions and capabilities

As shown in the figure, there are two layered models that are used to describe network operations:

-   Open System Interconnection (OSI) Reference Model
-   TCP/IP Reference Model

![[Screenshot 2023-02-20 at 0.38.19.png]]

# The OSI Reference Model

The OSI reference model provides an extensive list of functions and services that can occur at each layer. This type of model provides consistency within all types of network protocols and services by describing what must be done at a particular layer, but not prescribing how it should be accomplished.

It also describes the interaction of each layer with the layers directly above and below. The TCP/IP protocols discussed in this course are structured around both the OSI and TCP/IP models. The table shows details about each layer of the OSI model. The functionality of each layer and the relationship between layers will become more evident throughout this course as the protocols are discussed in more detail.
![[Screenshot 2023-02-20 at 0.39.03.png]]

> [!info] The definitions of the standard and the TCP/IP protocols are discussed in a public forum and defined in a publicly available set of IETF RFCs. An RFC is authored by networking engineers and sent to other IETF members for comments.
> 

# The OSI and TCP/IP model Comparison 

The protocols that make up the TCP/IP protocol suite can also be described in terms of the OSI reference model. In the OSI model, the network access layer and the application layer of the TCP/IP model are further divided to describe discrete functions that must occur at these layers.

At the network access layer, the TCP/IP protocol suite does not specify which protocols to use when transmitting over a physical medium; it only describes the handoff from the internet layer to the physical network protocols. OSI Layers 1 and 2 discuss the necessary procedures to access the media and the physical means to send data over a network.
![[Screenshot 2023-02-20 at 0.41.18.png]]