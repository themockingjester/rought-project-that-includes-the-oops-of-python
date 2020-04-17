
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import additem
from kivy.uix.label import Label
import cam

class donepopupclass(App):

    def build(self):

        self.main_layout2 = FloatLayout(size=(50, 50))
        label1 = Label(text='Done',font_size='55',
                       size_hint=(.20, .10),
                       pos_hint={'x': .40, 'y': .70})
        self.main_layout2.add_widget(label1)



        button1 = Button(
            text='Ok',

            size_hint=(.35, .10),
            pos_hint={'x': .35, 'y': .30}
        )
        button1.bind(on_press=self.ok)

        self.main_layout2.add_widget(button1)

        return self.main_layout2

    def ok(self, instance):
        cam.CameraExample.pictaken = False
        cam.CameraExample.imagedata = ""
        self.main_layout2.clear_widgets()
        f = additem.additem1()
        f.run()

