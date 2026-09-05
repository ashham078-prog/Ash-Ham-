from kivy.app import App
from kivy.uix.label import Label

class EliroxApp(App):
    def build(self):
        return Label(text='Elirox App is Working!')

EliroxApp().run()
