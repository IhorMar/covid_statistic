import json
from tkinter import *
import tkinter.ttk
from covid.api import CovId19Data

api = CovId19Data(force=True)
# api = api.get_stats()

Country_Europea_Top10 = ['Germany', 'France', 'Italy', 'Spain', 'Poland', 'Romania', 'Netherlands', 'Belgium', 'Greece',
                         'Portugal']

Ukraine_city = ['АР Крим', 'Вінницька', 'Волинська', 'Дніпропетровська', 'Донецька', 'Житомирська', 'Закарпатська',
                'Запорізька', 'Івано-Франківська', 'Київська', 'Кіровоградська', 'Луганська', 'Львівська',
                'Миколаївська', 'Одеська', 'Полтавська', 'Рівненська', 'Сумська', 'Тернопільська', 'Харківська',
                'Херсонська', 'Хмельницька', 'Черкаська', 'Чернівецька', 'Чернігівська']


def create_second_window():
    first_window.destroy()
    second_window = Tk()
    second_window.geometry('600x400')
    second_window.title('Covid-19 information')
    second_window['bg'] = 'Blue'

    def insert_Text_Europe(event):
        Get = Combobox_Europe_second_window.get()
        Getstr1 = Field_Europe.insert(1.0, json.dumps(api.filter_by_country(Get), indent=0))

    Text_Europe = Label(second_window, text='Європа', font=('Arial', 14), bg='Blue', fg='White')
    Text_Europe.place(x=10, y=7)
    Combobox_Europe_second_window = tkinter.ttk.Combobox(second_window, values=Country_Europea_Top10, state='readonly')
    Combobox_Europe_second_window['values'] = (
        'Germany', 'France', 'Italy', 'Spain', 'Poland', 'Romania', 'Netherlands', 'Belgium', 'Greece', 'Portugal')
    Combobox_Europe_second_window.place(x=10, y=40)
    Field_Europe = Text(second_window, width=35, height=7)
    Field_Europe.place(x=270, y=7)
    Combobox_Europe_second_window.bind('<<ComboboxSelected>>', insert_Text_Europe)

    def insert_Text_Ukraine(event):
        Get = Combobox_Ukraine_second_window.get()
        Getstr1 = Field_Ukraine.insert(1.0, json.dumps(api.filter_by_country(Get), indent=0))

    Text_Ukraine = Label(second_window, text='Україна', font=('Arial', 14), bg='Blue', fg='White')
    Text_Ukraine.place(x=10, y=180)
    Combobox_Ukraine_second_window = tkinter.ttk.Combobox(second_window, values=Country_Europea_Top10, state='readonly')
    Combobox_Ukraine_second_window['values'] = ('')
    Combobox_Ukraine_second_window.place(x=10, y=213)
    Field_Ukraine = Text(second_window, width=35, height=7)
    Field_Ukraine.place(x=270, y=180)
    Combobox_Ukraine_second_window.bind('<<ComboboxSelected>>', insert_Text_Ukraine)


first_window = Tk()
first_window.geometry('600x400')
first_window.title('Covid-19 information')
first_window['bg'] = 'Blue'

txt1_first_window = Label(first_window, bg='Blue', fg='White', font=('Arial', 12), text='Актуальна інформація',
                          width=20, height=10)
txt1_first_window.place(x=240, y=30)
btn1_first_window = Button(first_window, bg='Black', fg='White', text='Дізнатися інформацію ', width=30, height=2,
                           command=create_second_window)
btn1_first_window.place(x=220, y=170)

first_window.mainloop()
