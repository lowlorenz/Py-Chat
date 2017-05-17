import client,time,socket,sys


c = client.Client(False)
c.startClient()

done = False

print("Have fun chatting")
while True:
    try:
        message = raw_input()
        if message is "exit":
            c.close()
            done = True
        else :
            c.write(message)
        incommingMessage = c.read()
        print incommingMessage

    except socket.timeout:
        pass

    except KeyboardInterrupt:
        c.close()
        exit()
    except:
        print "Something went wrong"
        print sys.exc_info()
        c.close()
