import json
from settings import language
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'wight', 700)
Config.set('graphics', 'height', 700)
from kivy.app import App
from kivymd.app import MDApp

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
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

colors = {
'Red': {'50': 'FFEBEE',
'100': 'FFCDD2',
'200': 'EF9A9A',
'300': 'E57373',
'400': 'EF5350',
'500': 'F44336',
'600': 'E53935',
'700': 'D32F2F',
'800': 'C62828',
'900': 'B71C1C',
'A100': 'FF8A80',
'A200': 'FF5252',
'A400': 'FF1744',
'A700': 'D50000'},
"Teal": {
"50": "e4f8f9",
"100": "bdedf0",
"200": "97e2e8",
"300": "79d5de",
"400": "6dcbd6",
"500": "6ac2cf",
"600": "63b2bc",
"700": "5b9ca3",
"800": "54888c",
"900": "486363",
"A100": "bdedf0",
"A200": "97e2e8",
"A400": "6dcbd6",
"A700": "5b9ca3",
},
"Blue": {
"50": "e3f3f8",
"100": "b9e1ee",
"200": "91cee3",
"300": "72bad6",
"400": "62acce",
"500": "589fc6",
"600": "5191b8",
"700": "487fa5",
"800": "426f91",
"900": "35506d",
"A100": "b9e1ee",
"A200": "91cee3",
"A400": "62acce",
"A700": "487fa5",
},
"Light": {
"StatusBar": "E0E0E0",
"AppBar": "F5F5F5",
"Background": "FDE50A",
"CardsDialogs": "FFFFFF",
"FlatButtonDown": "cccccc",
},
"Dark": {
"StatusBar": "000000",
"AppBar": "212121",
"Background": "FDE50A",
"CardsDialogs": "424242",
"FlatButtonDown": "999999",
}
}


class WindowApp(MDApp):
    def build(self):
        with open('json/config.json', 'r', encoding='utf-8') as language_info:
            self.language_info = json.load(language_info)['Language']
        with open('json/language.json', 'r', encoding='utf-8') as language:
            if self.language_info == 'russian':
                self.language_check = json.load(language)['russian']['Window']
            else:
                self.language_check = json.load(language)['english']['Window']

        self.fl = FloatLayout()
        with open('json/config.json', 'r', encoding='utf-8') as config:  # r открыть UTF-8 кодировка
            self.config = json.load(config)
            self.balance0 = self.config['Balance']

        self.txtinpu1 = TextInput(text="", size_hint=(0.4, 0.4), pos_hint={'x': 0, 'y': 0.6})

        self.txtinpu2 = TextInput(text="", size_hint=(0.2, 0.04), pos_hint={'x': 0.1, 'y': 0.35})

        self.gamelabel = Label(text=self.language_check['gamelabel'], pos_hint={'x': 0, 'y': 0.38}, size_hint=(0.4, 0.4), font_size='30sp',
                               color=[.92, 0, .06, 1])
        self.gamelabel2 = Label(text=self.language_check['gamelabel2'], pos_hint={'x': 0, 'y': 0.23}, size_hint=(0.4, 0.4), font_size='30sp',
                               color=[.92, 0, .06, 1])
        self.balance = Label(text=self.language_check['balance'], pos_hint={'x': 0, 'y': 0.13}, size_hint=(0.4, 0.4), font_size='30sp',
                               color=[.92, 0, .06, 1])
        self.balance2 = Label(text=str(self.balance0), pos_hint={'x': 0.06, 'y': 0.08}, size_hint=(0.4, 0.4), font_size='30sp',
                             color=[.92, 0, .06, 1])

        self.btn2 = Button(text=self.language_check['btn2'], on_press=self.bl_window2, size_hint=(0.2, 0.095),
                           pos_hint={'x': 0.6, 'y': 0.91})
        self.btn3 = Button(text=self.language_check['btn3'], on_press=self.bl_window4, size_hint=(0.2, 0.095),
                           pos_hint={'x': 0.8, 'y': 0.91})
        self.btn4 = Button(text=self.language_check['btn4'], on_press=self.bl_window5, size_hint=(0.2, 0.095),
                           pos_hint={'x': 0.8, 'y': 0.814})

        self.dropdown_language = DropDown()
        self.dropdown_language.container.spacing = 2
        self.btn5 = Button(text=self.language_check['btn5'], on_press=self.dropdown_language.open, size_hint=(0.2, 0.095),
                           pos_hint={'x': 0.15, 'y': 0.15})

        self.gamebtn = Button(text=self.language_check['gamebtn'], size_hint=(0.2, 0.095),
                              pos_hint={'x': 0.2, 'y': 0.45}, on_press=self.gameran)
        self.gamebtn2 = Button(text=self.language_check['gamebtn2'], size_hint=(0.2, 0.095),
                               pos_hint={'x': 0, 'y': 0.45}, on_press=self.gameran2)

        self.dropdown_color = DropDown()
        self.dropdown_color.container.spacing = 2
        self.btn1 = Button(text=self.language_check['btn1'], on_press=self.dropdown_color.open, size_hint=(0.2, 0.095),
                           pos_hint={'x': 0.4, 'y': 0.91})

        self.dropbtn = Button(text="green", size_hint_y=None, height=44, on_press=self.bl_window)
        self.dropbtn2 =Button(text="temnogreen", size_hint_y=None, height=44, on_press=self.bl_window3)

        self.btn_dialog = MDFlatButton(text='ok')  # кнопка в диалоге
        self.dialog_popup = MDDialog(title='Ошибка.', text='Не хватает денежных средств \nПополните счёт',
                                     buttons=[self.btn_dialog])
        self.btn_dialog.bind(on_press=self.dialog_popup.dismiss)

        self.btn_dialog2 = MDFlatButton(text='ok')  # кнопка в диалоге
        self.dialog_popup2 = MDDialog(title='Ошибка.', text='Вы не ввели денежные средства',
                                     buttons=[self.btn_dialog2])
        self.btn_dialog2.bind(on_press=self.dialog_popup2.dismiss)

        self.btn_dialog3 = MDFlatButton(text='ok')  # кнопка в диалоге
        self.dialog_popup3 = MDDialog(title='Ошибка.', text='минимальная сумма 100 рублей',
                                      buttons=[self.btn_dialog3])
        self.btn_dialog3.bind(on_press=self.dialog_popup3.dismiss)

        self.dropdown_color.add_widget(self.dropbtn)
        self.dropdown_color.add_widget(self.dropbtn2)
        self.droplang1 = Button(text='rus', size_hint_y=None, height=44, on_press=self.bl_translate)
        self.droplang2 = Button(text='eng', size_hint_y=None, height=44, on_press=self.bl_window6)

        self.dropdown_language.add_widget(self.droplang1)
        self.dropdown_language.add_widget(self.droplang2)
        for element in [self.btn1, self.txtinpu1, self.btn2, self.btn3, self.gamelabel, self.gamebtn, self.gamebtn2,
                        self.gamelabel2, self.txtinpu2, self.btn4, self.balance, self.balance2, self.btn5]:
            self.fl.add_widget(element)
        self.theme_cls.colors = colors
        self.theme_cls.theme_style = 'Light'
        return self.fl

    def bl_window(self, instance):      # Поменять цвет окна
        Window.clearcolor = (.4, .88, .6, 1)

    def bl_window3(self, instance):     # Поменять цвет окна
        Window.clearcolor = (.0, .1, .1, 1)

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

    def bl_window5(self, instance):
        self.txtinpu1.text = ""
        self.txtinpu2.text = ""

    def bl_window6(self, instance):     # перевод языка eng
        if self.language_info == 'russian':
            language(self, 'english')
            self.language_info = 'english'

    def bl_translate(self, instance):   #rus
        if self.language_info == 'english':
            language(self, 'russian')
            self.language_info = 'russian'

    def gameran(self, instance):        # казино
        if self.txtinpu2.text == "":
            self.dialog_popup2.open()
        elif self.balance0 <= 0:
            self.dialog_popup.open()
        elif int(self.txtinpu2.text) <= 100:
            self.dialog_popup3.open()
        else:
            gamerun = random.randint(0, 10)
            formula2 = (int(self.txtinpu2.text) * 1.2)
            if gamerun >= 4:
                self.txtinpu1.text += "\n" + "Вы проиграли" + "\n"
                self.balance0 -= int(self.txtinpu2.text)
                self.balance2.text = str(self.balance0)
            else:
                self.txtinpu1.text += "\n" + "Вы выиграли" + "\n" + str(int(formula2)) + " " + "Рублей" + "\n"
                self.balance0 += int(formula2)
                self.balance2.text = str(self.balance0)

            self.save_json()
    def gameran2(self, instance):
        if self.txtinpu2.text == "":
            self.dialog_popup2.open()
        elif self.balance0 <= 0:
            self.dialog_popup.open()
        elif int(self.txtinpu2.text) <= 100:
            self.dialog_popup3.open()
        else:
            gamerun = random.randint(0, 10)
            formula1 = (int(self.txtinpu2.text) * 1.5)
            if gamerun >= 4:
                self.txtinpu1.text += "\n" + "Вы проиграли" + "\n"
                self.balance0 -= int(self.txtinpu2.text)
                self.balance2.text = str(self.balance0)
            else:
                self.txtinpu1.text += "\n" + "Вы выиграли" + "\n" + str(int(formula1)) + " " + "Рублей" + "\n"
                self.balance0 += int(formula1)
                self.balance2.text = str(self.balance0)
        self.save_json()

    def save_json(self):
        with open('json/config.json', 'r', encoding='utf-8') as config:  # r открыть UTF-8 кодировка
            self.config = json.load(config)
            self.config['Balance'] = self.balance0
        with open('json/config.json', 'w', encoding='utf-8') as config:
            json.dump(self.config, config, indent=3, ensure_ascii=False)    # w перезаписать данные, self. то что загружаем , 2 куда загружаем

    def language(self, lang):
        main_language = ((self.gamelabel, 'gamelabel'), (self.gamelabel2, 'gamelabel2'), (self.balance0, 'balance'))


if __name__=="__main__":
    WindowApp().run()