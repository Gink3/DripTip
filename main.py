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


Window.size = (390,763)

import pyrebase 

config = {
    "apiKey": "AIzaSyAdLveOQ86Z44LqHmTY-bQBQmMPQ1DW3HE",
    "authDomain": "driptip-37b83.firebaseapp.com",
    "databaseURL": "https://driptip-37b83-default-rtdb.firebaseio.com",
    "projectId": "driptip-37b83",
    "storageBucket": "driptip-37b83.appspot.com",
    "messagingSenderId": "201557623795",
    "appId": "1:201557623795:web:1cad1c77d610d48f990886",
    "measurementId": "G-NXFC49V69D"
}

firebase = pyrebase.initialize_app(config)
authentication = firebase.auth()

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


<<<<<<< HEAD
class seeker_1(Screen):  # ability to report advice after advice has been declined 
    pass 

class WindowManager(ScreenManager):
    pass


=======
>>>>>>> 24a07d5d3338f5ae3021e84c9b587fb89509ff39
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

def messageSent():
    pop = Popup(title='Tip Sent!',
                content=Label(text='Your Tip has been sent!'),
                size_hint=(None, None), size=(400, 400))   
    pop.open()

sm = ScreenManager()

class MyMainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Red"

<<<<<<< HEAD
sm = WindowManager()
db = DataBase("users.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"),Profile(name="profile"),seeker(name="seeker_sees"), seeker_1(name="report_advice"), advisor(name="advisor_sends")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"






class MyMainApp(App):
=======
>>>>>>> 24a07d5d3338f5ae3021e84c9b587fb89509ff39
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