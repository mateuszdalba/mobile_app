# Import kivy dependencies first
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList

# Import kivy UX components
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
# Import other kivy stuff
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.logger import Logger
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ListenPropety
from kivy.config import Config

Config.set('graphics', 'width', '550')
Config.set('graphics', 'height', '550')

# Import other dependencies
import cv2
import tensorflow as tf
#from layers import L1Dist
import os
import numpy as np


kv = Builder.load_file("main.kv")

# Declare both screens
class MenuScreen(Screen):
    pass

class PredictionScreen(Screen):
    pass

class ResultScreen(Screen):
    pass

class AboutSceen(Screen):
    pass



class MainApp(MDApp):
    def build(self):
        return kv

        # # Main layout components 
        # self.web_cam = Image(size_hint=(1,.8))
        # self.button = Button(text='Verify')
        # self.verification_label = Label(text="Verification Uninitiated", size_hint=(1,.1))

        # layout = BoxLayout(orientation='vertical')
        # layout.add_widget(self.web_cam)
        # layout.add_widget(self.button)
        # layout.add_widget(self.verification_label)

        # # Load tensorflow/keras model
        # #ToDo: Add my model for predicting Attractive or not
        # #self.model = tf.keras.models.load_model('siamesemodel.h5', custom_objects={'L1Dist':L1Dist})

        # # Setup video capture device
        # self.capture = cv2.VideoCapture(0)
        # Clock.schedule_interval(self.update, 1.0/33.0)
        
        # return layout

    # # Run continuously to get webcam feed
    # def update(self, *args):
    #     # Read frame from opencv
    #     ret, frame = self.capture.read()
    #     frame = frame[120:120+250, 200:200+250, :]

    #     buf = cv2.flip(frame, 0).tostring()
    #     img_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
    #     img_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
    #     self.web_cam.texture = img_texture

if __name__ == '__main__':
	MainApp().run()