import os
import search_item
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
import spinner
import additem
import total_items

class MainApp(App):
    def build(self):

        print(os.getcwd())
        self.main_layout = FloatLayout(size=(50, 50))


        button1 = Button(
            text='Add Item',
            pos=(20,700),
        size_hint = (.15, .1),
            pos_hint={'x': .2, 'y': .70}
        )
        button1.bind(on_press=self.on_button_press1)
        self.main_layout.add_widget(button1)
        button2 = Button(
            text='Search Item',
            pos=(20, 700),
            size_hint=(.15, .1),
            pos_hint={'x': .50, 'y': .70}
        )
        button2.bind(on_press=self.on_button_press2)
        self.main_layout.add_widget(button2)
        button3 = Button(
            text='All Items',
            pos=(20, 700),
            size_hint=(.15, .1),
            pos_hint={'x': .2, 'y': .30}
        )
        button3.bind(on_press=self.on_button_press3)
        self.main_layout.add_widget(button3)

        button4 = Button(
            text='Total Items',
            pos=(20, 700),
            size_hint=(.15, .1),
            pos_hint={'x': .50, 'y': .30}
        )
        button4.bind(on_press=self.on_button_press4)
        self.main_layout.add_widget(button4)
        return  self.main_layout
    def on_button_press1(self,instance):
        self.main_layout.clear_widgets()
        app1 = additem.additem1()
        app1.run()
        print('hi')

    def on_button_press2(self,instance):
        self.main_layout.clear_widgets()
        f=search_item.search_item_class()
        f.run()

    def on_button_press3(self,instance):
        self.main_layout.clear_widgets()
        f = spinner.spin()
        f.run()
    def on_button_press4(self,instance):
        self.main_layout.clear_widgets()
        f = total_items.total_item_class()
        f.run()
if __name__ == "__main__":
    app = MainApp()
    app.run()
