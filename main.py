import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.image import Image
from PIL import *


# Designate our .kv design file
kv=Builder.load_file('new_window.kv')


class MyLayout(Widget):

    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
            print(filename[0])

        except:
            pass


class FlowerApp(App):
    def build(self):
        Window.clearcolor = (153 / 255.0, 204 / 255.0, 255 / 255.0, 0.5)
        return MyLayout()


if __name__ == '__main__':
    FlowerApp().run()
