from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition  # Import pentru ScreenManager și Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Rectangle, Color


class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

        with self.canvas.before:
            Color(240/255, 180/255, 124/255, 1)  # Setează culoarea
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Asigurăm actualizarea corectă a dimensiunii și poziției
        self.bind(size=self.update_rect, pos=self.update_rect)

        # Creăm un AnchorLayout pentru a centra conținutul
        anchor_layout = AnchorLayout()

        # Creăm layout-ul pentru butoane
        self.layout = BoxLayout(orientation="vertical", size_hint=(None, None), size=(200, 150))  # Dimensiune fixă

        # Buton pentru WorldScreen
        self.world_button = Button(text="Start", size_hint=(None, None), size=(200, 50))
        self.world_button.bind(on_press=self.go_to_world_screen)
        self.layout.add_widget(self.world_button)

        # Buton pentru setări
        self.settings_button = Button(text="Settings", size_hint=(None, None), size=(200, 50))
        self.settings_button.bind(on_press=self.go_to_settings)
        self.layout.add_widget(self.settings_button)

        # Adăugăm BoxLayout-ul în AnchorLayout pentru centrare
        anchor_layout.add_widget(self.layout)

        self.add_widget(anchor_layout)

    def go_to_settings(self, instance):
        self.manager.current = 'settings'  # Schimbăm ecranul la setări

    def go_to_world_screen(self, instance):
        self.manager.current = 'worldscreen'  # Schimbăm ecranul la WorldScreen

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos  # Asigurăm că fundalul acoperă tot ecranul

# Ecranul de Setări
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
        self.manager.current = 'start'  # Schimbăm înapoi la StartScreen

# WorldScreen
class WorldScreen(Screen):
    def __init__(self, **kwargs):
        super(WorldScreen, self).__init__(**kwargs)

        self.screen_width = Window.width
        self.screen_height = Window.height

        # Setăm imaginea de fundal
        self.background_image = Image(source="./Fall - simplified_0.png", size=(self.screen_width, self.screen_height))
        self.background_image.fit_mode = "fill"
        self.add_widget(self.background_image)

        # Buton pentru a închide WorldScreen
        self.exit_button = Button(text="Back to Start", size_hint=(None, None), size=(200, 50), pos=(50, 50))
        self.exit_button.bind(on_press=self.go_back)
        self.add_widget(self.exit_button)

    def go_back(self, instance):
        self.manager.current = 'start'  # Schimbăm înapoi la StartScreen

# Aplicația principală
class MainApp(App):
    def build(self):
        # Creăm un ScreenManager
        sm = ScreenManager(transition = NoTransition())

        # Adăugăm ecranele
        sm.add_widget(StartScreen(name='start'))  # Ecranul de start
        sm.add_widget(SettingsScreen(name='settings'))  # Ecranul de setări
        sm.add_widget(WorldScreen(name='worldscreen'))  # WorldScreen

        return sm

if __name__ == "__main__":
    MainApp().run()
