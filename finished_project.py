import pyperclip
import pyshorteners
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

def shorten_url():
    original_url = window_to_insert_a_link.get()

    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(original_url) 

    window_to_insert_a_link_two.delete(0, 'end')
    window_to_insert_a_link_two.insert(0, shortened_url)



window =  Tk()
window.title(' ТИТП ЧЕТ СОКР ССЫЛ')
window.geometry('700x250')
window.resizable(width=False , height=False)

button = Label(window, text = "BВЕДИТЕ ССЫЛКУ")
button.place(x=50, y=10)

window_to_insert_a_link = ttk.Entry(window , width=40, font="Arial 20")# это размер окошка для ссылки
window_to_insert_a_link.place(x = 40 , y = 35) 

button_to_execute_the_code = ttk.Button(window , text="СОКРАТИТЬ(ДА ЭТО КРИК)",  command=shorten_url)
button_to_execute_the_code.place(relx = 0.49, y = 90, anchor=CENTER)


button_two = Label(window ,text = "РЕЗУЛЬТАТ")
button_two.place(x=50, y=110)
window_to_insert_a_link_two = ttk.Entry(window , width=40, font="Arial 20")# это размер окошка для ссылки
window_to_insert_a_link_two.place(x = 40 , y = 135) 


window.mainloop()