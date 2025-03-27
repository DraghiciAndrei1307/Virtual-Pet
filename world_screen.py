from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen


from shop_screen import ShopScreen
from cat_room import CatRoom

class WorldScreen(Screen):
    def __init__(self, **kwargs):
        super(WorldScreen, self).__init__(**kwargs)

        self.screen_width = Window.width
        self.screen_height = Window.height

        # Setăm imaginea de fundal
        self.background_image = Image(source="./Fall - simplified_0.png")
        self.background_image.size = (self.screen_width, self.screen_height)
        self.background_image.fit_mode = "fill"  # ADAUGĂ LINIA ASTA
        self.add_widget(self.background_image)

        # Buton pentru a deschide camera de pisici
        self.cat_room_button = Button(text="Open Cat Room", size_hint=(None, None), size=(200, 50), pos=(50, 50))
        self.cat_room_button.bind(on_press=self.toggle_cat_room)
        self.add_widget(self.cat_room_button)

        # Buton pentru a deschide magazinul
        self.shop_button = Button(text="Open Shop", size_hint=(None, None), size=(200, 50), pos=(50, 120))
        self.shop_button.bind(on_press=self.toggle_shop_screen)
        self.add_widget(self.shop_button)

        # Instanțiem feronăriile
        self.cat_room = CatRoom()
        self.shop_screen = ShopScreen()

    def toggle_cat_room(self, instance):
        if not self.cat_room.popup._is_open:
            self.cat_room.open()
        else:
            self.cat_room.close()

    def toggle_shop_screen(self, instance):
        if not self.shop_screen.popup._is_open:
            self.shop_screen.open()
        else:
            self.shop_screen.close()