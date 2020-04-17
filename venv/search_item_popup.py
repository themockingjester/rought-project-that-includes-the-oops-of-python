import base64

from kivy.uix.image import Image

from words_filter import words_filter
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import search_item
from record_availability_checker import record_availability_checker
import MainFile

from kivy.uix.label import Label
class search_item_class(App):
    def build(self):

        self.main_layout2 = FloatLayout(size=(50, 50))
        self.item = search_item.search_item_class().data
        obj = words_filter(self.item)
        self.item = obj.output()
        obj2 = record_availability_checker(self.item)
        self.value = obj2.get()
        ############################################### in case of camera #######################################
        '''img1 = obj2.get1()
        img2 = obj2.get2()
        img=img1+img2
        ####################convert txt to img################
        print(len(img))
        fh = open("/root/try.jpg", "wb")
        fh.write(base64.standard_b64decode(img))
        fh.close()
        ########################################
        string = '                          %s is at %s\n--------------------Check here---------------------' % (self.item,self.value)
        label1 = Label(text=string,font_size=40,
                      size_hint=(.20, .10),
                      pos_hint={'x': .40, 'y': .75})
        self.main_layout2.add_widget(label1)
        img = Image(source='/root/try.jpg',size_hint=(.70, .70),pos_hint={'x': .20, 'y': .14})
        self.main_layout2.add_widget(img)'''
        string = '         %s is at %s' % (
        self.item.strip(), self.value.strip())
        label1 = Label(text=string, font_size=40,
                       size_hint=(.20, .10),
                       pos_hint={'x': .40, 'y': .75})
        self.main_layout2.add_widget(label1)
        button1 = Button(
            text='Ok',

        size_hint = (.15, .10),
            pos_hint={'x': .45, 'y': .10}
        )
        button1.bind(on_press=self.ok)
        self.main_layout2.add_widget(button1)


        return self.main_layout2
    def ok(self,instance):

        self.main_layout2.clear_widgets()
        f=search_item.search_item_class()
        f.run()
