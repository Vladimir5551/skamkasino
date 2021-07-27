import json
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'wight', 800)
Config.set('graphics', 'height', 800)
from kivy.app import App

from kivy.core.window import Window
Window.clearcolor = (.08, .08, .08, 1)

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
import sqlite3
import random
class window(App):
    def build(self):
        self.fl = FloatLayout()
        self.balance0 = 50000
        self.txtinpu1 = TextInput(text="", size_hint=(0.4, 0.4), pos_hint={'x': 0, 'y': 0.6})

        self.txtinpu2 = TextInput(text="", size_hint=(0.2, 0.04), pos_hint={'x': 0.1, 'y': 0.35})

        self.gamelabel = Label(text="Казино", pos_hint={'x': 0, 'y': 0.38}, size_hint=(0.4, 0.4), font_size='30sp',
                               color=[.92, 0, .06, 1])
        self.gamelabel2 = Label(text="Введите сумму денег", pos_hint={'x': 0, 'y': 0.23}, size_hint=(0.4, 0.4), font_size='30sp',
                               color=[.92, 0, .06, 1])
        self.balance = Label(text="Баланс: ", pos_hint={'x': 0, 'y': 0.13}, size_hint=(0.4, 0.4), font_size='30sp',
                               color=[.92, 0, .06, 1])
        self.balance2 = Label(text="0 ", pos_hint={'x': 0.06, 'y': 0.08}, size_hint=(0.4, 0.4), font_size='30sp',
                             color=[.92, 0, .06, 1])


        self.btn2 = Button(text="вывести строку бд", on_press=self.bl_window2, size_hint=(0.2, 0.095), pos_hint={'x': 0.6, 'y': 0.91})
        self.btn3 = Button(text="удалить строки из бд", on_press=self.bl_window4, size_hint=(0.2, 0.095),
                           pos_hint={'x': 0.8, 'y': 0.91})
        self.btn4 = Button(text="Почистить экраны", on_press=self.bl_window5, size_hint=(0.2, 0.095),
                           pos_hint={'x': 0.8, 'y': 0.814})

        self.dropdown_language = DropDown()
        self.dropdown_language.container.spacing = 2
        self.btn5 = Button(text="Выбрать язык", on_press=self.dropdown_language.open, size_hint=(0.2, 0.095),
                           pos_hint={'x': 0.15, 'y': 0.15})

        self.gamebtn = Button(text="Шанс выиграть 60% \nkoef=1.2", size_hint=(0.2, 0.095), pos_hint={'x': 0.2, 'y': 0.45}, on_press=self.gameran)
        self.gamebtn2 = Button(text="Шанс выиграть 50% \nkoef=1.5", size_hint=(0.2, 0.095), pos_hint={'x': 0, 'y': 0.45}, on_press=self.gameran2)
        self.dropdown_color = DropDown()
        self.dropdown_color.container.spacing = 2
        self.btn1 = Button(text="Поменять цвет окна", on_press=self.dropdown_color.open, size_hint=(0.2, 0.095), pos_hint={'x': 0.4, 'y': 0.91})

        self.dropbtn = Button(text="green", size_hint_y=None, height=44, on_press=self.bl_window)
        self.dropbtn2 =Button(text="temnogreen", size_hint_y=None, height=44, on_press=self.bl_window3)

        self.dropdown_color.add_widget(self.dropbtn)
        self.dropdown_color.add_widget(self.dropbtn2)
        self.droplang1 = Button(text='rus', size_hint_y=None, height=44, on_press=self.bl_window6)
        self.droplang2 = Button(text='eng', size_hint_y=None, height=44, on_press=self.bl_window6)

        self.dropdown_language.add_widget(self.droplang1)
        self.dropdown_language.add_widget(self.droplang2)
        for element in [self.btn1, self.txtinpu1, self.btn2, self.btn3, self.gamelabel, self.gamebtn, self.gamebtn2,
                        self.gamelabel2, self.txtinpu2, self.btn4, self.balance, self.balance2, self.btn5]:
            self.fl.add_widget(element)

        return self.fl

    def bl_window(self, instance):      # Поменять цвет окна
        Window.clearcolor = (.4, .88, .6, 1)

    def bl_window2(self, instance):
        self.txtinpu1.text = ""     # очищаем input от записей
        sqlite_connection = sqlite3.connect('sqltest.db')
        sql = sqlite_connection.cursor()
        group_gen = (row for row in sql.execute("SELECT * FROM rep"))
        for value in group_gen:     # Пробежка по всему циклу
            self.txtinpu1.text += "id" + " " + str(value[0]) + "\n" + "Product" + " " + str(value[1]) + "\n" + "color_code" + " " + str(value[2]) + "\n"

    def bl_window4(self, instance):
        sqlite_connection = sqlite3.connect('sqltest.db')
        cursor = sqlite_connection.cursor()
        sql_delete_query = """DELETE from rep where id = 1"""
        cursor.execute(sql_delete_query)
        sqlite_connection.commit()
        self.txtinpu1.text = "\n" + "запись удалена!" + "\n"
        cursor.close()
    def bl_window3(self, instance):
        Window.clearcolor = (.0, .1, .1, 1)

    def bl_window5(self, instance):
        self.txtinpu1.text = ""
        self.txtinpu2.text = ""

    def bl_window6(self, instance):
        pass
        # with open(json_menu) as configmenu:
        #    self.configmenu = json.load(json_menu)
        #    if self.configmenu['Russian'] == 'Russian':





    def gameran(self, instance):
        if self.txtinpu2.text != "" and int(self.txtinpu2.text) <= self.balance0:

            gamerun = random.randint(0, 10)
            formula2 = (int(self.txtinpu2.text) * 1.2)
            if gamerun >= 1:
                self.txtinpu1.text += "\n" + "Вы проиграли" + "\n"
                self.balance0 -= int(formula2)
                self.balance2.text = str(self.balance0)
            else:
                self.txtinpu1.text += "\n" + "Вы выиграли" + "\n" + str(formula2) + "\n"
                self.balance0 += int(formula2)
                self.balance2.text = str(self.balance0)

    def gameran2(self, instance):
        if self.txtinpu2.text != "" and int(self.txtinpu2.text) <= self.balance0:

            gamerun = random.randint(0, 10)
            formula1 = (int(self.txtinpu2.text) * 1.5)
            if gamerun >= 5:
                self.txtinpu1.text += "\n" + "Вы проиграли" + "\n"
                self.balance0 -= int(formula1)
                self.balance2.text = str(self.balance0)
            else:
                self.txtinpu1.text += "\n" + "Вы выиграли" + "\n" + str(formula1) + "\n"
                self.balance0 += int(formula1)
                self.balance2.text = str(self.balance0)


if __name__=="__main__":
    window().run()
