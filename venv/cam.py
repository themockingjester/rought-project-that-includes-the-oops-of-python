import base64

from kivy.app import App
from kivy.core.window import Window
import threading
from  kivy.core.camera import camera_opencv
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.camera import Camera
from kivy.core.camera import camera_opencv

from kivy.uix.button import Button
import additem


class CameraExample(App):
    pictaken=False
    imagedata=""
    def build(self):


        self.layout = FloatLayout(size=(50, 50))

        # Create a camera object
        self.cameraObject = Camera(play=False)

        self.cameraObject.play = True

        self.cameraObject.resolution = (300, 300)  # Specify the resolution

        # Create a button for taking photograph

        self.camaraClick = Button(text="Take Photo")

        self.camaraClick.size_hint = (.1, .1)

        self.camaraClick.pos_hint = {'x': .30, 'y': .10}

        # bind the button's on_press to onCameraClick

        self.camaraClick.bind(on_press=self.onCameraClick)
        self.back = Button(text="back")

        self.back.size_hint = (.1, .1)

        self.back.pos_hint = {'x': .60, 'y': .10}

        # bind the button's on_press to onCameraClick

        self.back.bind(on_press=self.backclick)

        # add camera and button to the layout

        self.layout.add_widget(self.cameraObject)

        self.layout.add_widget(self.camaraClick)
        self.layout.add_widget(self.back)

        # return the root widget

        return self.layout
    
    # Take the current frame of the video as the photo graph

    def onCameraClick(self, *args):
        self.cameraObject.play = False
        self.cameraObject.export_to_png('/root/thisisthepicof.jpg')
        with open("/root/thisisthepicof.jpg", "rb") as imageFile:


            CameraExample.imagedata = base64.standard_b64encode(imageFile.read())
            print('given size',len(CameraExample.imagedata))
            CameraExample.pictaken=True


    def backclick(self, *args):
        print('hi')
        self.layout.clear_widgets()
        self.cameraObject.resolution = (-1,-1)
        

        app1 = additem.additem1()

        app1.run()

        self.layout.walk_reverse()



# Start the Camera App

