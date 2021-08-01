import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
import requests 
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.app import MDApp

from android.permissions import request_permissions, Permission
request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE, Permission.INTERNET])

from android.storage import primary_external_storage_path
primary_ext_storage = primary_external_storage_path()

class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass      

class ThirdWindow(Screen):
    pass

class AboutWindow(Screen):
    pass

class FlowerPredictionWindow(Screen):
    pass

class LeafPredictionWindow(Screen):
    pass
    
    

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('new_window.kv')

class KnowYourPlantApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_manager_obj = MDFileManager( select_path = self.select_path,exit_manager = self. exit_manager,preview=True)

    def open_file_manager(self):
        self.file_manager_obj.show('primary_ext_storage') 
        #self.file_manager_obj = True
        #self.open_file_manager()

    def exit_manager(self):
        self.file_manager_obj.close()

    def select_path(self, path):
        print(path)   
        if(self.root.current_screen.name == 'third'):
            self.root.get_screen("LeafPredictionWindow").ids.my_image2.source = path
            resp = requests.post("https://leaf-disease-classifier.herokuapp.com/predict", files={'file': open(path, 'rb')})
            str= resp.text.split(',')[0].split(':')[1][1:-1]
            self.root.get_screen("LeafPredictionWindow").ids.abc.text = str
        else:
            self.root.get_screen("FlowerPredictionWindow").ids.my_image1.source = path
            resp = requests.post("https://pytorch-flower-classifier.herokuapp.com/predict", files={'file': open(path, 'rb')})
            str= resp.text.split(',')[0].split(':')[1][1:-1]
            self.root.get_screen("FlowerPredictionWindow").ids.xyz.text = str

        self.exit_manager() 
          

    def build(self):
        return kv

if __name__ == '__main__':
    KnowYourPlantApp().run()