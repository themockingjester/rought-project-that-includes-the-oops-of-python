from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from record_adder import record_add
import additem
from words_filter import words_filter
from recordoverrider import recordoverride
class mypopup(App):
    def build(self):
        self.main_layout = FloatLayout(size=(50, 50))
        label = Label(text='item is already present at',size_hint=(.15, .1),
            pos_hint={'x': .2, 'y': .70})
        self.main_layout.add_widget(label)
        button1 = Button(
            text='continue',
            pos=(20, 700),
            size_hint=(.15, .1),
            pos_hint={'x': .2, 'y': .30}
        )
        button1.bind(on_press=self.on_button_press1)
        self.main_layout.add_widget(button1)
        button2 = Button(
            text='cancel',
            pos=(20, 700),
            size_hint=(.15, .1),
            pos_hint={'x': .50, 'y': .30}
        )
        button2.bind(on_press=self.on_button_press2)
        self.main_layout.add_widget(button2)
        return self.main_layout
    def on_button_press1(self, instance):

        x=additem.additem1.textbox1

        print('yash',x)
        y=additem.additem1.textbox2
        print('tash', y)

        obj = recordoverride(x,y)
        print('done')
        self.main_layout.clear_widgets()
        f = additem.additem1()
        f.run()

    def on_button_press2(self, instance):
        self.main_layout.clear_widgets()
        f = additem.additem1()
        f.run()