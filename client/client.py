#!/usr/bin/python           # This is client.py file
import sys
import socket               # Import socket module


class Client:

    global sock
    sock = None

    def __init__(self, changeFlag):
        global sock
        sock = socket.socket()

        global port,ip
        if changeFlag:
            ip = raw_input("Enter you IP here : ")
            port = int(raw_input("Enter you Port here : "))
        else:
            ip = '192.168.178.32'   # Lubuntu
            ip = '87.123.138.95'    # Fritz Box external

            port = 12345

        global userName

        try:
            configFile = open("config.txt")
            config = configFile.read().split(',')
            userName = config[0].replace("Username :","")
            configFile.close()
        except IOError:
            blank = open("config.txt",'a')
            blank.write("Username : Blank,")
            blank.close()
            userName = "Blank"

    def startClient(self):
        sock.connect((ip,int(port)))
        sock.settimeout(0.1)

    def write(self, message):
        try:
            sock.send(userName + " : " + message)
        except socket.timeout:
            pass

    def read(self):
        try:
            return str(sock.recv(1024))
        except socket.timeout:
            pass

    def close(self):
        sock.close()
        print("Socket Closed !")
