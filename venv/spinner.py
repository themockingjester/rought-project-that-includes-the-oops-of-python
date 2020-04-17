import time

import pyautogui
from kivy.uix.spinner import Spinner
from kivy.base import runTouchApp
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from item_retriver import itemslist
import MainFile

class spin(App):
    textbox1 = ""
    textbox2 = ""

    def build(self):
        obj = itemslist()
        self.items=obj.get()
        try:
            self.items.remove(None)
        except:
            pass
        print(obj.get())
        self.main_layout2 = FloatLayout(size=(50, 50))
        self.spinner = Spinner(
            text='Click here',
            values=self.items,
            size_hint=(.15, .10),
            pos_hint={'x': .25, 'y': .30})

        self.main_layout2.add_widget(self.spinner)


        button1 = Button(
            text='Back',

            size_hint=(.15, .10),
            pos_hint={'x': .55, 'y': .30}
        )
        button1.bind(on_press=self.back)
        self.main_layout2.add_widget(button1)


        return self.main_layout2

    def back(self, instance):

        self.main_layout2.clear_widgets()
        time.sleep(.5)
        pyautogui.click(50,50)
        f = MainFile.MainApp()
        f.run()



