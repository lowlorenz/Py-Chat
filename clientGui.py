import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ReferenceListProperty,ObjectProperty,OptionProperty
from kivy.vector import Vector
from kivy.clock import Clock

from kivy.uix.button import Button


'''
class Message(Widget):

    def __init__
'''

class RightStack(StackLayout):

    pass

class LeftStack(StackLayout):

    pass

class Messenger(Widget):

    pass

class ClientGui(App):

    def build(self):
        return LeftStack()

if __name__ == '__main__':
    ClientGui().run()
