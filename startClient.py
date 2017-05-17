import client,time,socket,sys,thread

def send():
    try:
        message = raw_input()
        if message is "exit":
            c.close()
            done = True
        else :
            c.write(message)
    except socket.timeout:
        pass
        break
    except:
        print "Something went wrong"
        print sys.exc_info()
        c.close()
        done = True

def recieve():
    try:
        incommingMessage = c.read()
        print incommingMessage

    except socket.timeout:
        pass
        break
    except:
        print "Something went wrong"
        print sys.exc_info()
        c.close()
        done = True


c = client.Client(False)
c.startClient()

done = False

print("Have fun chatting")
while not done:
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
        break
    except:
        print "Something went wrong"
        print sys.exc_info()
        c.close()
        done = True
