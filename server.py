#CMPT 371 Lab2 
#Alina Lapushkina
#Implementation of a simple web server in Python
################################################

import socket
#initialize host = '' (s.t. the socket is reachable by any address the machine happens to have) and port = 80 (normal port):
HOST, PORT = '', 8080
#create a socket of IPv4 protocols family and connection-oriented TCP type:
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#set an option to allow to reuse the same address:
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#bind the socket to the host and a port:
server_socket.bind((HOST, PORT))
#tell the socket to accept up to 5 connect requests in a queue:
server_socket.listen(5)
print 'Serving HTTP on port %s ...' % PORT
while True:
    (client_socket, client_address) = server_socket.accept()
    try:
        #accept connections from outside:
        request = client_socket.recv(1024)
        #receive the request from the client:
        filename = request.split()[1]
        f = open(filename[1:])
        data = f.read();
        print request, "REQUEST"
        client_socket.sendall('HTTP/1.1 200 OK\r\n')
        for i in range(0, len(data)):
            client_socket.send(data[i])
        #disconnecting client socket:
        client_socket.close()

    #send error message if file not found:
    except IOError:
        client_socket.send('404 Not Found')
        client_socket.close()

server_socket.close()
    
 
    
