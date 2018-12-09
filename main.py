import kivy
kivy.require('1.10.1')
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

class Navigation(FloatLayout):
    # Changes color of background
    # Parameter "txtIn" is name of color to use
    def changeColor(self, txtIn):
        if (txtIn.text == "black"):
            Window.clearcolor = (0, 0, 0, 1)
        elif (txtIn.text == "green"):
            Window.clearcolor = (0, 0.6, 0.1, 1)
        elif (txtIn.text == "blue"):
            Window.clearcolor = (0, 0.2, 0.5, 1)
        elif (txtIn.text == "purple"):
            Window.clearcolor = (0.3, 0, 0.4, 1)
        elif (txtIn.text == "red"):
            Window.clearcolor = (0.7, 0, 0, 1)
        elif (txtIn.text == "pink"):
            Window.clearcolor = (1, 0.5, 1, 1)
        elif (txtIn.text == "default"):
            Window.clearcolor = (0.41, 0.41, 0.41, 1)
        else:
            txtIn.text = "unavailable color"

class Information(ScreenManager):
    pass

class SlothFacts(Screen):
    pass

class HBadgerFacts(Screen):
    pass

class KiwiFacts(Screen):
    pass

class MainPanel(GridLayout):
    pass

Builder.load_file("mainPanel.kv")

class Complex(App):
    Window.clearcolor = (0.41, 0.41, 0.41, 1)
    def build(self):
        return MainPanel()

if __name__ == "__main__":
    Complex().run()



