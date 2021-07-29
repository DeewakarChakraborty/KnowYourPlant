from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
import requests 

class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass      

class ThirdWindow(Screen):
    pass

class AboutWindow(Screen):
    pass

class FlowerPredictionWindow(Screen):
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
            #print(filename[0])
            resp = requests.post("https://pytorch-flower-classifier.herokuapp.com/predict", files={'file': open(filename[0], 'rb')})
            str= resp.text.split(',')[0].split(':')[1][1:-1]
            self.ids.xyz.text = str

        except:
            pass
       

class LeafPredictionWindow(Screen):
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
            #print(filename[0])
            resp = requests.post("https://leaf-disease-classifier.herokuapp.com/predict", files={'file': open(filename[0], 'rb')})
            str = resp.text.split(',')[0].split(':')[1][1:-1]
            self.ids.abc.text = str

        except:
            pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('new_window.kv')

class KnowYourPlantApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    KnowYourPlantApp().run()