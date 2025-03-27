from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
# Ecranul de Start
class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

        # Setăm dimensiunile ferestrei
        self.screen_width = Window.width
        self.screen_height = Window.height

        # Creăm layout-ul pentru butoane
        self.layout = BoxLayout(orientation="vertical")
        self.layout.size = (self.screen_width, self.screen_height)

        # Buton pentru setări
        self.settings_button = Button(text="Settings", size_hint=(None, None), size=(200, 50))
        self.settings_button.bind(on_press=self.go_to_settings)
        self.layout.add_widget(self.settings_button)

        # Buton pentru WorldScreen
        self.world_button = Button(text="Go to WorldScreen", size_hint=(None, None), size=(200, 50))
        self.world_button.bind(on_press=self.go_to_world_screen)
        self.layout.add_widget(self.world_button)

        self.add_widget(self.layout)

    def go_to_settings(self, instance):
        self.parent.current = 'settings'  # Schimbăm ecranul la setări

    def go_to_world_screen(self, instance):
        self.parent.current = 'worldscreen'  # Schimbăm ecranul la WorldScreen