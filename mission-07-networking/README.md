--> Task 7.1

> LAN: is a group of devices of connected together in small area. example- one building or campus (home, school lab)

> MAN: a network that covers a whole city or large town, so it’s bigger than a LAN but smaller than a WAN. example- a city or metro area

> WAN: a network that covers a very large area, like multiple cities, countries, connecting many smaller networks (LANs and MANs) together. example- countries or the whole world (the internet)

> DNS: it translates human-friendly website names like google.com into the numeric IP addresses that computers use to find each other.

> Router: a device that connects different networks together and directs data between them

> Protocol: a set of agreed rules that define how devices communicate and exchange data over a network

> Packet switching: a method of sending data over a network by breaking it into small chunks called packets which travel 

> Client-server: a network model where a client (a device or program that requests a service) communicates with a server (a powerful computer that provides data or services in response)



--> Task 7.2

> A connectivity test checks whether one device can reach another over a network, and how well that connection is working. It also helps us check whether DNS works. 

> A DNS lookup shows how a domain name is resolved, along with the records stored for it.

> When we type a website name like google.com into our browser, DNS translates that name into the IP address our device needs to actually reach the site. Computers communicate using IP addresses, not names, so the browser can’t load anything until it knows the number


--> Task 7.3

When you open a website, a chain of steps runs in a fraction of a second. Here it is end to end, using the key terms.

1. The browser (the client)

You type `google.com`. Your browser is the client in the client-server model: it starts the conversation by requesting a service (the web page) from a server. It first checks its own cache to see if it already knows the site's address.

2. DNS lookup

Computers locate each other by IP address, not names, so the browser needs one. It asks a DNS resolver to translate google.com into an IP address. If the resolver doesn't know, it asks other DNS servers until it gets the answer and sends it back to the browser.

3. The network and router

Now the browser has a destination. Its request leaves your device and goes to your router which connects your LAN (home network) to the internet, a WAN The data is split into packets (packet switching) and routers along the way forward each packet toward the server's IP address, possibly over different paths.

4. Protocols

This only works because both sides follow agreed protocols:

- DNS for looking up the address
- TCP/IP for packaging, addressing, and delivering the packets reliably
- HTTP/HTTPS for the actual request and response between browser and server (HTTPS also encrypts it)

5. The server

The packets arrive at the web server which is always online, waiting for requests. It reads the HTTP request ("send me the home page") and finds the needed files: HTML, images, and so on.

6. The response

The server sends the page back as packets, which travel back through the routers to your router and then to your device. TCP/IP reassembles them in the correct order, and the browser reads the HTML, CSS, and images and displays the page.

