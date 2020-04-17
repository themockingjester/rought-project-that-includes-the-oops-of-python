import search_item_popup
from record_availability_checker import record_availability_checker
from kivy.uix.popup import Popup
from words_filter import words_filter
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

import MainFile

from kivy.uix.label import Label
class search_item_class(App):
    data = ''


    def build(self):
        self.popup = Popup(title='Test popup',
                           content=Button(text='search', size_hint=(.15, .10), pos_hint={'x': .30, 'y': .30}),
                           auto_dismiss=False)
        self.popup.content.bind(on_press=self.popup.dismiss)
        self.main_layout2 = FloatLayout(size=(50, 50))
        label1 = Label(text='Enter name of the item',
                      size_hint=(.20, .10),
                      pos_hint={'x': .2, 'y': .70})
        self.main_layout2.add_widget(label1)
        self.textbox1 = TextInput(

            multiline=False, readonly=False, font_size=40, size_hint = (.35, .1), pos_hint={'x': .50, 'y': .70}

        )
        self.main_layout2.add_widget(self.textbox1)


        button1 = Button(
            text='search',

        size_hint = (.15, .10),
            pos_hint={'x': .30, 'y': .30}
        )
        button1.bind(on_press=self.search)
        self.main_layout2.add_widget(button1)
        button2 = Button(
            text='Back',

            size_hint=(.15, .10),
            pos_hint={'x': .55, 'y': .30}
        )
        button2.bind(on_press=self.back)

        #self.objret = textbox(self.textbox1.text,self.textbox2.text)
        self.main_layout2.add_widget(button2)

        return self.main_layout2
    def back(self,instance):

        self.main_layout2.clear_widgets()
        f=MainFile.MainApp()
        f.run()


    def search(self, instance):
        search_item_class.data = self.textbox1.text
        self.main_layout2.clear_widgets()
        f=search_item_popup.search_item_class()
        f.run()
