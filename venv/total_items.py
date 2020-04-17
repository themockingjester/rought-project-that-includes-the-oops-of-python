from item_retriver import itemslist
from words_filter import words_filter
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import search_item
from record_availability_checker import record_availability_checker
import MainFile

from kivy.uix.label import Label
class total_item_class(App):
    def build(self):

        self.main_layout2 = FloatLayout(size=(50, 50))
        obj = itemslist()

        self.item = obj.get()


        string = 'Total number of records are :\n------------->   %s' % (len(self.item))
        label1 = Label(text=string,font_size=55,
                      size_hint=(.20, .10),
                      pos_hint={'x': .40, 'y': .70})
        self.main_layout2.add_widget(label1)
        button1 = Button(
            text='Ok',

        size_hint = (.15, .10),
            pos_hint={'x': .45, 'y': .30}
        )
        button1.bind(on_press=self.ok)
        self.main_layout2.add_widget(button1)


        return self.main_layout2
    def ok(self,instance):

        self.main_layout2.clear_widgets()
        f=MainFile.MainApp()
        f.run()
