# main.py
import kivy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.imagelist import SmartTileWithLabel
from kivy.core.window import Window

from database import DataBase

Window.size = (390,763)

class HomeExplorer(Screen):
    pass

class GothLabel(FloatLayout):
    pass

class AthleticLabel(FloatLayout):
    pass

class ProfessionalLabel(FloatLayout):
    pass

class CasualLabel(FloatLayout):
    pass

class PhotoTile(SmartTileWithLabel):
    pass

class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    userType = ObjectProperty(None)
    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                user = authentication.create_user_with_email_and_password(self.email.text, self.password.text)
                self.reset()
                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        try:
            authentication.sign_in_with_email_and_password(self.email.text, self.password.text)
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        
        except:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    pass
class Profile(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""
    def logOut(self):
        sm.current = "login"

class advisor(Screen):
    tip = ObjectProperty(None)
    current = ""

    def send(self):
        messageSent() 

class seeker(Screen):   # page where the seeker sees the advice given by the advisor 
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


class seeker_1(Screen):  # ability to report advice after advice has been declined 
    pass 

class WindowManager(ScreenManager):
    pass


def messageSent():
    pop = Popup(title='Tip Sent!',
                content=Label(text='Your Tip has been sent!'),
                size_hint=(None, None), size=(400, 400))   
    pop.open()

sm = ScreenManager()

sm = WindowManager()
db = DataBase("users.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"),Profile(name="profile"),seeker(name="seeker_sees"), seeker_1(name="report_advice"), advisor(name="advisor_sends")]

class MyMainApp(MDApp):
    def build(self):
        kv = Builder.load_file("my.kv")
        screens = [
                   LoginWindow(name="login"), 
                   CreateAccountWindow(name="create"),
                   MainWindow(name="main"),
                   Profile(name="profile")

                  ]
        for i in screens: 
            sm.add_widget(i)
        sm.current = "login"
        return sm

if __name__ == "__main__":
    MyMainApp().run()