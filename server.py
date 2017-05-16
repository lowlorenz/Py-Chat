#!/usr/bin/python           # This is server.py file

import socket               # Import socket module


class Server:

    host = '192.168.178.30'     # Adress of my RaspberryPi
    port = 12345                # Our standart port
    sock = socket.socket(
        socket.AF_INET,         # Internetzugang (also nicht Unix \0.0"/)
        socket.SOCK_STREAM      # Verbindungsorientiertes Protokoll
    )
    closed = false
    connections = []
    adresses = []
    messages = []


    def __init__(self):
        s.bind((host, port))        # Bind to the port
        s.listen(5)
        while not closed:
            c, addr = s.accept()    # Establish connection with client.
            connections.append(c)
            adresses.append(c)
            messages.append(sock.recv(1024))

    def getclosed(self):
        return closed

    def setClosed(self, closed):
        closed = closed
