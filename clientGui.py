
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
        global layout
        layout = BoxLayout(orientation='vertical')
        layout.size = (800,600)
        for i in (20):
            labels.append(Label())
        self.add_widget(layout)

    def pushMessage(self, m):
        printMessages.append(m)
        while(len(printMessages) > 20):

        layout.add_widget( Label(text = m) )

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
