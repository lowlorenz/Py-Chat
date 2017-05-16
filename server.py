#!/usr/bin/python           # This is server.py file

import socket               # Import socket module


class Server:

    global host,port,sock,closed,connections,adresses,messages

    host = '192.168.178.30'     # Adress of my RaspberryPi
    port = 12345                # Our standart port
    sock = socket.socket()
    closed = False
    connections = []
    messages = []


    def __init__(self, port = 12345):
        sock.bind((host, port))        # Bind to the port
        sock.listen(5)
        sock.settimeout(5)

    def getClosed(self):
        return closed

    def setClosed(self, closed):
        closed = closed

    def acceptSock(self):
        c, addr = sock.accept()    # Establish connection with client.
        connections.append((c,addr))

    def printConnections(self):
        for c in connections:
            print c

    def printMessages(self):
        for c in connections:
            message = c[0].recv(1024)
            if message is not None:
                print message

    def close(self):
        for c in connections:
            c[0].close()
        sock.close()

    def getSocket(self):
        return sock
