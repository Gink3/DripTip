# main.py
import kivy
from database import DataBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.imagelist import SmartTileWithStar
from kivy.uix.image import Image
from kivy.core.window import Window

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

class PhotoTile(Image):
    pass

class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    userType = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":

                db.add_user(self.email.text, self.password.text, self.namee.text)

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
        if db.validate(self.email.text, self.password.text):
            Profile.current = self.email.text

            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class Profile(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created

class MainWindow(Screen):
    pass

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

sm = WindowManager()
db = DataBase("users.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"),Profile(name="profile"),seeker(name="seeker_sees"), seeker_1(name="report_advice"), advisor(name="advisor_sends")]

class MyMainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Gray"
        
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
    
    def callback1(self):
        sm.current = "profile"

if __name__ == "__main__":
    MyMainApp().run()