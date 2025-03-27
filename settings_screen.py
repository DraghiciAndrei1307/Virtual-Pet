from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)

        # Setăm dimensiunile ferestrei
        self.screen_width = Window.width
        self.screen_height = Window.height

        # Layout pentru setări
        self.layout = BoxLayout(orientation="vertical")
        self.layout.size = (self.screen_width, self.screen_height)

        # Buton pentru a închide setările
        self.back_button = Button(text="Back to Start", size_hint=(None, None), size=(200, 50))
        self.back_button.bind(on_press=self.go_back)
        self.layout.add_widget(self.back_button)

        self.add_widget(self.layout)

    def go_back(self, instance):
        self.parent.current = 'start'  # Schimbăm înapoi la StartScreen
