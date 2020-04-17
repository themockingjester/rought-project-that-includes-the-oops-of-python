import threading
import donepopup
from kivy.uix.popup import Popup
import addfilepopup
from record_availability_checker import record_availability_checker
import cam
from words_filter import words_filter
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from record_adder import record_add
import MainFile
from kivy.core.camera import camera_opencv
from kivy.uix.camera import Camera
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
class additem1(App):
    textbox1=""
    textbox2=""
    def build(self):
        try:
            if cam.CameraExample.camvar==1:
                s=camera_opencv.CameraOpenCV()
                s.stop()
                cam.CameraExample.camvar=0
            else:
                pass
        except:
            pass
        self.main_layout2 = FloatLayout(size=(50, 50))
        label1 = Label(text='Enter name of the item',
                      size_hint=(.20, .10),
                      pos_hint={'x': .2, 'y': .70})
        self.main_layout2.add_widget(label1)
        self.textbox1 = TextInput(

            multiline=False, readonly=False, font_size=40, size_hint = (.35, .1), pos_hint={'x': .50, 'y': .70}

        )
        self.main_layout2.add_widget(self.textbox1)
        label2 = Label(text='Enter name of the location',
                       size_hint=(.20, .10),
                       pos_hint={'x': .2, 'y': .50})
        self.main_layout2.add_widget(label2)
        self.textbox2 = TextInput(

            multiline=False, readonly=False, font_size=40, size_hint=(.35, .1), pos_hint={'x': .50, 'y': .50}

        )
        self.main_layout2.add_widget(self.textbox2)
        ###################################################### this is the camera button ###########################################
        '''button1 = Button(
            text='Click here to add image of location',

        size_hint = (.35, .10),
            pos_hint={'x': .35, 'y': .30}
        )
        button1.bind(on_press=self.imagelocation)
        self.main_layout2.add_widget(button1)'''
        #######################################################################################################################
        button2 = Button(
            text='Submit',

            size_hint=(.15, .10),
            pos_hint={'x': .25, 'y': .10}
        )
        button2.bind(on_press=self.submit)
        button3 = Button(
            text='Back',

            size_hint=(.15, .10),
            pos_hint={'x': .65, 'y': .10}
        )
        button3.bind(on_press=self.back)
        self.main_layout2.add_widget(button3)
        #self.objret = textbox(self.textbox1.text,self.textbox2.text)
        self.main_layout2.add_widget(button2)


        return self.main_layout2
    def back(self,instance):

        self.main_layout2.clear_widgets()
        f=MainFile.MainApp()
        f.run()


    def submit(self, instance):
        ob = words_filter(self.textbox1.text)
        k = ob.output()
        obj = record_availability_checker(k)
        temp1 = obj.get()
        x = self.textbox1.text
        y = self.textbox2.text
        ob1 = words_filter(x)
        popup = Popup(title='Complete the details first', content=Button(text='ok'),
                      auto_dismiss=False)
        popup.content.bind(on_press=popup.dismiss)
        x = ob1.output()
        ob2 = words_filter(y)
        y = ob2.output()
        additem1.textbox1 = x
        additem1.textbox2 = y

        if temp1=="":
################################### this if is for when we have camera option################################
            '''if x != "" and y != "" and cam.CameraExample.pictaken==True:
                self.main_layout2.clear_widgets()
                z=cam.CameraExample.imagedata
                obj2=record_add(x,y,z)
                f = donepopup.donepopupclass()
                f.run()'''
###################################################################################################
            if x != "" and y != "":
                self.main_layout2.clear_widgets()

                obj2=record_add(x,y)
                f = donepopup.donepopupclass()
                f.run()
            else:
                self.main_layout2.clear_widgets()
                f = additem1()
                f.run()



        else:
            self.main_layout2.clear_widgets()
            f=addfilepopup.mypopup()
            f.run()

    def mycam(self):

        appmn = cam.CameraExample()

        appmn.run()


    def imagelocation(self,instance):
        print('hi')
        self.main_layout2.clear_widgets()


        t=threading.Thread(target=self.mycam())
        t.start()







        

