from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty
import math
from kivymd.uix.dialog import MDDialog

class HomeScreen(Screen):
    weight = NumericProperty(40)

    def increase(self):
        self.weight = self.weight +1
    def decrease(self):
        if self.weight >0:
            self.weight = self.weight -1
    def calculate_bmi(self):
        h = round(self.ids.height_value.value) / 100
        bmi = self.weight / (h*h)
        if bmi < 18.5:
            weight_range = 'UnderWeight! '
        elif bmi >=18.5 and bmi <=24.9:
            weight_range = 'Normal'
        elif bmi >=25 and bmi <= 29.9 :
            weight_range = 'OverWeight'
        else:
            weight_range = 'Obese!'
        dialog = MDDialog(title="BMI", text=f'Your BMI is {round(bmi)}\nYou are {weight_range}', size_hint=[0.8, 0.3])
        dialog.open()



class Mainapp(MDApp):
    def __init__(self):
        Window.size = (400, 600)
        super(Mainapp, self).__init__()

Mainapp().run()
