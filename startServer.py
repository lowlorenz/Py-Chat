import server,time,socket

serv = server.Server()

while(True):
    try:
        serv.acceptSock()
        serv.broadcastMessages()

    except socket.timeout:          # Whenever acceptSock() doesn't add anything
        pass                        # a Timeout Exception is thrown

    except:
        serv.close()
