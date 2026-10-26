How the Internet Works
The Internet is a global network of interconnected computers and servers that communicate with each other using standard protocols. When we enter a website address such as https://www.google.com into a browser, several steps happen behind the scenes to retrieve and display the webpage.
1. DNS (Domain Name System)
DNS works like the Internet’s phonebook. It translates a human-readable domain name, such as google.com, into an IP address that identifies the destination server. The browser may use a cached DNS result or contact a DNS resolver to find the address.
2. TCP/IP (Transmission Control Protocol / Internet Protocol)
TCP/IP enables devices to communicate across networks.
- IP: Routes packets of data toward the destination using IP addresses.
- TCP: Establishes a reliable connection, keeps data in order, and retransmits lost data when necessary.
For HTTPS websites, the browser also establishes encryption using TLS, usually after the TCP connection is established.
3. HTTP Request Lifecycle
HTTP (Hypertext Transfer Protocol) defines how browsers and web servers exchange requests and responses. HTTPS is the secure version, using TLS encryption.

When you visit a website:
1. Enter URL: You type https://www.google.com in the browser.
2. DNS lookup: The browser finds the server's IP address.
3. Connection: The browser establishes a connection using TCP and negotiates TLS for HTTPS.
4. HTTP request: The browser sends a request, such as GET /, to the server.
5. Server processing: The server processes the request and prepares a response.
6. HTTP response: The server sends a status code (such as 200 OK) and the requested content.
7. Rendering: The browser processes the HTML, CSS, JavaScript, and other resources to display the webpage.