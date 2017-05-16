import server,time

serv = server.Server()
serv.acceptSock()

while(True):
    serv.printMessages()
