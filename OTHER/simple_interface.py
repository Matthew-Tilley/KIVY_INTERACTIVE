from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class MyFloat(FloatLayout):
    def foo(self):
        pass


class SimpleInterface(App):
    def build(self):
        return MyFloat()
    
    
if__name__=="__main__":
    SimpleInterface().run()