from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MainApp(MDApp):
    def build(self):
        self.title='KivyMD Dashboard'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"


if __name__ == '__main__':
    MainApp().run()