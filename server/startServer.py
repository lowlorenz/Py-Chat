import server,time,socket

serv = server.Server()

while(True):

    try :
        print serv.acceptSock()
    except socket.timeout:          # Whenever acceptSock() doesn't add anything
        pass                        # a Timeout Exception is thrown
    except KeyboardInterrupt:
        print "close server"
        serv.close()
        exit()

    try:
        serv.broadcastMessages()
    except socket.timeout:          # Whenever a timeout fires
        pass                        # a Timeout Exception is thrown
    except KeyboardInterrupt:
        print "close server"
        serv.close()
        exit()
