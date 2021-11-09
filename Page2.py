from tkinter import *

first_window = Tk()
first_window.geometry('600x400')
first_window.title('Covid-19')
first_window['bg'] = 'Blue'

Text_first_window = Label(first_window, text='Covid-19',bg='Blue', fg='White', font=('Arial', 35), width=10, height=1)
Text_first_window.place(x=170, y=110)
Button_Europe_first_window = Button(first_window, text='Європа', bg='Black', fg='White', font=('Arial', 13), width=17, height=2)
Button_Europe_first_window.place(x=20, y=220)
Button_Ukraine_first_window = Button(first_window, text='Україна', bg='Black', fg='White', font=('Arial', 13), width=19, height=2)
Button_Ukraine_first_window.place(x=212, y=220)
Button_Asia_first_window = Button(first_window, text='Азія', bg='Black', fg='White', font=('Arial', 13), width=17, height=2)
Button_Asia_first_window.place(x=420, y=220)

first_window.mainloop()
