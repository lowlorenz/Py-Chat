#!/usr/bin/python           # This is client.py file


import socket               # Import socket module


class Client:

    ip = '127.0.1.1'
    port = 0
    global sock

    def __init__(self):
        ip = raw_input("Enter you IP here : ")
        port = int(raw_input("Enter you Port here :"))
        sock = socket.socket()

    def startClient(self):
        sock.connect((ip,int(port)))

    def write(self, message):
        sock.send(message)
