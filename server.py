#!/usr/bin/python           # This is server.py file

import socket               # Import socket module


class Server:

    global host,port,sock,connections,adresses,messages

    host = '192.168.178.30'     # Adress of my RaspberryPi
    host = '192.168.178.32'     # Adress of my Lubuntu Laptop
    port = 12345                # Our standart port
    sock = socket.socket()
    connections = []
    messages = []


    def __init__(self, port = 12345):
        sock.bind((host, port))        # Bind to the port
        sock.listen(5)
        sock.settimeout(0.5)

    def acceptSock(self):
        c, addr = sock.accept()    # Establish connection with client.
        c.settimeout(0.5)
        connections.append((c,addr))
        return (c, addr)

    def printConnections(self):
        for c in connections:
            print c

    def printMessages(self):
        for c in connections:
            try:
                message = c[0].recv(1024)
                print message
            except socket.timeout:
                pass

    def broadcastMessages(self):
        for c in connections:
            try:
                message = c[0].recv(1024)
                print message
                for reciever in connections:
                    #if reciever[1] != c[1]:
                    reciever[0].send(message)
            except socket.timeout:
                pass


    def close(self):
        sock.shutdown(socket.SHUT_RDWR)

    def getSocket(self):
        return sock
