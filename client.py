#!/usr/bin/python           # This is client.py file


import socket               # Import socket module


class Client:


    def __init__(self):
        global sock,port,ip
        ip = raw_input("Enter you IP here : ")
        port = int(raw_input("Enter you Port here :"))

        if ip is '':            #just for testing, should be delted later
            ip = '192.168.178.30'
        if port < 10:
            port = 12345

        sock = socket.socket()

    def startClient(self):
        sock.connect((ip,int(port)))

    def write(self, message):
        sock.send(message)
