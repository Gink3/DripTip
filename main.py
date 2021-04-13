# main.py

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.core.window import Window


Clock.max_iteration = 20
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
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""
    def OpenProfile(self):
        MainWindow.current = self.email.text
        self.reset()
        sm.current = "profile"

    def on_enter(self, *args):
        print("hi")

    def OpenAdvisor(self):
        sm.current = "advisor_sends"

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


class WindowManager(ScreenManager):
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

    def build(self):
        kv = Builder.load_file("my.kv")
        screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"),Profile(name="profile")]
        for i in screens: 
            sm.add_widget(i)
        sm.current = "login"
        return sm

if __name__ == "__main__":
    MyMainApp().run()