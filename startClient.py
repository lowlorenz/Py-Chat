import client,time

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
    except:
        c.close()
        done = True
