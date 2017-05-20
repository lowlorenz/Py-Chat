
import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import client,time,socket,sys



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
            printMessages.append('')

        for l in labels:
            layout.add_widget(l)

        self.add_widget(layout)


    def pushMessage(self, m):
        if m is None:
            return
        printMessages.append(m)
        while(len(printMessages) > 19):
            oldMessages.insert(0,printMessages.pop(0))
        for i in range(19):
            labels[i].text = printMessages[i]

    def testMessages(self,dt):
        self.counter += 1
        self.pushMessage(str(self.counter))

    def pushSocketInput(self,time):
        try:
            self.pushMessage(self.cl.read())

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
