# Drip Tip
# Main file for application
# Example for you hoes
#
#
from kivy.app import App
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image 
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

  
class advisor_gives(Widget):   # page where the advisor can give advice to seeker 
    pass 

class MainApp(App):
    def build(self):
        return advisor_gives()





MainApp().run()