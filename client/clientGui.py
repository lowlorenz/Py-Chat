
import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import client,time,socket,sys

class Bubble(Widget):
    l = Label()
    i = Image()

    def setColor(self, c):
        i.color = c

    def setText(self, m):
        l.text = m

class Messenger(Widget):

    counter = 0
    oldMessages = []
    printMessages = []
    labels = []

    cl = client.Client(False)

    def init(self):

        global cl
        cl = client.Client(False)
        cl.startClient()

        global layout,labels,printMessages,oldMessages,counter
        counter = 0
        oldMessages = []
        printMessages = []
        labels = []

        layout = BoxLayout(orientation='vertical')
        layout.size = (700,600)
        layout.pos = (0,30)

        for i in range (19):
            labels.append(Label())
            printMessages.append(('',2))

        for l in labels:
            layout.add_widget(l)
            l.add_widget( Image(
                            pos=(l.center_x,
                                 l.center_y),
                            color=(1,0,0))
                        )


        self.add_widget(layout)


    def pushMessage(self, m, author):
        if m is None or m is '':
            return

        printMessages.append((m,author))

        while(len(printMessages) > 19):
            oldMessages.insert(0,printMessages.pop(0))

        for i in range(19):
            labels[i].text, color = printMessages[i]
            if color == 0:    # einge Nachricht
                labels[i].color = [0.8,0.4,0.2,1]
            if color == 1:    # Nachricht von Chat
                labels[i].color = [0.2,0.7,0.6,1]
            if color == 2:    # Systemnachricht
                labels[i].color = [1,1,1,1]

    def testMessages(self,dt):
        self.counter += 1
        self.pushMessage(str(self.counter),0)

    def pushSocketInput(self,time):
        try:
            self.pushMessage(self.cl.read(),1)

        except socket.timeout:
            pass


    def test(self):
        self.cl.write("test")

class ClientGui(App):

    def build(self):
        m = Messenger()
        m.init()
        Clock.schedule_interval(m.pushSocketInput, 1)
        return m


if __name__ == '__main__':
    ClientGui().run()
