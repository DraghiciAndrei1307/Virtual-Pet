from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window

class ShopScreen(Widget):
    def __init__(self, **kwargs):
        super(ShopScreen, self).__init__(**kwargs)
        self.popup = Popup(title="Shop", content=Label(text="Welcome to the Shop!"), size_hint=(None, None), size=(400, 400))

    def open(self):
        self.popup.open()

    def close(self):
        self.popup.dismiss()