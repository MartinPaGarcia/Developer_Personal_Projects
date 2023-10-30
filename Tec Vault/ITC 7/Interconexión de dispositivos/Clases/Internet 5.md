
# Network Layer (4th layer)


## Characteristics

Provides services to allow end devices to exchange data

IP version 4 (IPv4) and version 6 (IPv6) are the principle network layer communication protocols

The network layer performs four basic operations:

* Addressing end devices
* Encapsulation
* Routing
* De-encapsulation


# IP encapsulation

# Characteristics of IP

IP is meant to have low overhead and may be described as:
 * Connectionless
 * Best Effort 
 * Media Independent

## Connectionless

IP is Connectionless

* IP does not establish a connection with the destination before sending the packet

## Best Effort

IP is: best effort

* IP will not guarantee delivery of the packet
* IP has reduced overhead since there is no mechanism to resend data that is

## Media independent

IP is unreliable:

* Cannot fix packets
* Cannot retransmit after an error
* Cannot realign out of sequence
* must rely on other protocols

IP is media dependent 

*Research*


# Host Forwarding Decision

* Packets are always created at the source 
* Each host devices creates their own routing table
* A host can send packets to the following
	* Itself
	* Local hosts
	* Remote Hosts

# Default Gateways


# Host Routing Tables

![[Screenshot 2023-02-27 at 11.26.31.png]]


# Network and Host Options

* IPv4 is a 32-bit hierarchical address that is made up of a network portion and a host portion
* Determining the network portion versus the host portion, you must take the 32-bit steam
* A subnet mask is used to determine the network and host portion

![[Pasted image 20230227113131.png]]


## Network, host, and [[The Rules]] Addresses

* Within each network are three types of ip addresses
* Network address
* Host addresses
* Broadcast Address 


![[Pasted image 20230227113900.png]]

# Public and private IPv4 addresses

* As defined in RFC 1918, public IPv4 address are globally routed between internet service provider ISP routers.
* Private address, are common blocks of addresses used by most organizations to assign IPv4 addresses to internal hosts
* Private IPv4 addresses are not unique and can be used internally within any network

## Private IP examples

* A - 10.0.0.0/8
* B - 172.16.0.0/12
* C - 192.168.0.0/16


# Problems with large broadcast domains

* Large broadcast domain is that host can generate excessive broadcast
* The solution is to reduce the size of the network to create smaller broadcast domains in a process called subnetting
* Dividing the network 172.16.0.0/16 into two subnets of 200 users each: 172.16.0.0/24 and 172.16.1.0/24 
Broadcast are only propagated within the smaller broadcast domains


## IP addressing

* Default Subnet Mask for Class A:
