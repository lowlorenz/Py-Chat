#!/usr/bin/python           # This is client.py file


import socket               # Import socket module


class Client:


    def __init__(self, changeFlag):
        global sock,port,ip
        if changeFlag:
            ip = raw_input("Enter you IP here : ")
            port = int(raw_input("Enter you Port here : "))
        else:
            ip = '192.168.178.32'
            port = 12345

        sock = socket.socket()

    def startClient(self):
        sock.connect((ip,int(port)))

    def write(self, message):
        sock.send(message)

    def close(self):
        sock.close()
