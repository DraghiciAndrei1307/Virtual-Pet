from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window

class CatRoom(Widget):
    def __init__(self, **kwargs):
        super(CatRoom, self).__init__(**kwargs)
        self.popup = Popup(title="Cat Room", content=Label(text="Welcome to the Cat Room!"), size_hint=(None, None), size=(400, 400))

    def open(self):
        self.popup.open()

    def close(self):
        self.popup.dismiss()