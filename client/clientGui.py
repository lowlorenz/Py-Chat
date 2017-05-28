
import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.bubble import Bubble
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

import client,time,socket,sys

class Messenger(Widget):

    counter = 0
    oldMessages = []
    printMessages = []
    bubbles = []
    labels = []

    cl = client.Client(False)

    def init(self):

        global cl
        cl = client.Client(False)
        cl.startClient()

        global layout,bubbles,printMessages,oldMessages,counter,labels
        counter = 0
        oldMessages = []
        printMessages = []
        bubbles = []
        labels = []

        layout = BoxLayout(orientation='vertical')
        layout.size = (700,600)
        layout.pos = (0,30)
        layout.spacing = 5

        for i in range (19):
            labels.append(Label())
            bubbles.append(Bubble())
            bubbles[i].add_widget(labels[i])
            printMessages.append(('',2))

        for b in bubbles:
            layout.add_widget(b)


        self.add_widget(layout)


    def pushMessage(self, m, author):
        if m is None or m is '':
            return

        printMessages.append((m,author))

        while(len(printMessages) > 19):
            oldMessages.insert(0,printMessages.pop(0))

        for i in range(19):
            text, color = printMessages[i]

            labels[i].text = text
            labels[i].texture_update()
            labels[i].size = labels[i].texture_size

            if color == 0:    # einge Nachricht
                bubbles[i].background_image = 'pics/ownMessage.png'
                bubbles[i].arrow_image = 'pics/ownMessageArrow.png'
                bubbles[i].arrow_pos = 'left_bottom'
                bubbles[i].show_arrow = True

            if color == 1:    # Nachricht von Chat
                bubbles[i].background_image = 'pics/clientMessage.png'
                bubbles[i].arrow_image = 'pics/clientMessageArrow.png'
                bubbles[i].arrow_pos = 'right_bottom'
                bubbles[i].show_arrow = True

            if color == 2:    # Systemnachricht
                bubbles[i].show_arrow = False

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
        Window.clearcolor = (0.6, 0.6, 0.6, 0.5)
        m = Messenger()
        m.init()
        Clock.schedule_interval(m.pushSocketInput, 1)
        return m


if __name__ == '__main__':
    ClientGui().run()
