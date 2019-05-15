import socket


"""
First of all we made a socket.
Then we resolved google’s ip and lastly we connected to google.
Now we need to know how can we send some data through a socket.
necessary function:
socket()
bind()
listen()
accept()
connect()
connect_ex()
send()
recv()
close()
"""
# server name
server_name = 'www.pythonprogramming.net'
port = 80
# AF_INET ipv4 connection, SOCK_STREAM tcp protocol
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting to a server ($ ping www.pythonprogramming.net)
ip = socket.gethostbyname(server_name)
print(ip)

# connecting to the server
sock.connect((ip, port))

print("the socket has successfully connected to pythonprogramming on port == {}s".format(ip))

"""
For sending data the socket library has a sendall function. This function allows you to send data to a server to which 
the socket is connected and server can also send data to the client using this function.
"""

# Next bind to the port
# we have not typed any ip in the ip field instead we have inputted an empty string this makes the server listen to
# requests coming from other computers on the network
"""
Network devices (for example, routers and switches), have finite bandwidth available and their own inherent system 
limitations. They have CPUs, memory, buses, and interface packet buffers, just like our clients and servers. TCP 
relieves you from having to worry about packet loss, data arriving out-of-order, and many other things that invariably 
happen when you’re communicating across a network.

Starting in the top left-hand column, note the API calls the server makes to setup a “listening” socket:
socket()
bind()
listen()
accept()

The client calls connect() to establish a connection to the server and initiate the three-way handshake. The handshake 
step is important since it ensures that each side of the connection is reachable in the network, in other words that the
 client can reach the server and vice-versa. It may be that only one host, client or server, can reach the other.
In the middle is the round-trip section, where data is exchanged between the client and server using calls to send() and
 recv().
At the bottom, the client and server close() their respective sockets.
"""
HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    """
    The values passed to bind() depend on the address family of the socket. In this example, we’re using socket.AF_INET 
    (IPv4). So it expects a 2-tuple: (host, port). host can be a hostname, IP address, or empty string. If an IP address
    is used, host should be an IPv4-formatted address string. The IP address 127.0.0.1 is the standard IPv4 address for
    the loopback interface, so only processes on the host will be able to connect to the server. If you pass an empty 
    string, the server will accept connections on all available IPv4 interfaces. port should be an integer from 1-65535 
    (0 is reserved). It’s the TCP port number to accept connections on from clients. Some systems may require superuser 
    privileges if the port is < 1024.
    """
    s.bind((HOST, PORT))
    s.listen(5)
    """
    accept() blocks and waits for an incoming connection. When a client connects, it returns a new socket object 
    representing the connection and a tuple holding the address of the client. 
    """
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

