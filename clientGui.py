
import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.label import Label


class Messenger(Widget):

    counter = 0
    oldMessages = []
    printMessages = []
    labels = []


    def init(self):
        global layout,labels,printMessages,oldMessages,counter
        counter = 0
        oldMessages = []
        printMessages = []
        labels = []

        layout = BoxLayout(orientation='vertical')
        layout.size = (800,600)
        for i in range (19):
            labels.append(Label())
            printMessages.append('')

        for l in labels:
            layout.add_widget(l)

        self.add_widget(layout)

    def pushMessage(self, m):
        printMessages.append(m)
        while(len(printMessages) > 20):
            oldMessages.insert(0,printMessages.pop(0))
        for i in range(19):
            labels[i].text = printMessages[i]

    def testMessages(self,dt):
        self.counter += 1
        self.pushMessage(str(self.counter))

class ClientGui(App):

    def build(self):
        m = Messenger()
        m.init()
        Clock.schedule_interval(m.testMessages, 0.5)
        return m


if __name__ == '__main__':
    ClientGui().run()
