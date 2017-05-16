import client,time

c = client.Client()
c.startClient()
print("Have fun chatting")
while True:
    c.write(raw_input())
