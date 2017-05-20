
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

    def __init__(self):
        pass
        global layout
        layout = BoxLayout(orientation='vertical')

    def pushMessage(self, m):
        l = Label(text = m )
        layout.add_widget( l )

    def testMessages(self):
        self.counter += 1
        self.pushMessage(str(self.counter))

class ClientGui(App):

    def build(self):
        print "Start"
        m = Messenger()
        Clock.schedule_interval(m.testMessages, 0.5)
        return m


if __name__ == '__main__':
    ClientGui().run()
