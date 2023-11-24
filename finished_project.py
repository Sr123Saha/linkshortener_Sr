# Сюда закидываем чистый код без описания и коментариев
#("16.11.2023.")
#("17.11.2023")
#("19.11.2023")# редоктирование под главвное меню
import pyperclip
import pyshorteners
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
def delete_all(self):
    self.text.delete(0, 'end')
def shorten_url():
    original_url = window_to_insert_a_link.get()

    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(original_url) 

    window_to_insert_a_link_two.delete(0, 'end')
    window_to_insert_a_link_two.insert(0, shortened_url)


window =  Tk()
window.title('Сокращятель ссылок')
window.geometry('1000x250')
window["bg"] = "#68FCF5"
window.resizable(width=False , height=False)
1
button = Label(window, text = "BВЕДИТЕ ССЫЛКУ" ,font=("Arial Bold", 18))
button["bg"] = "#68FCF5"
button.place(x=36, y=10)

window_to_insert_a_link = ttk.Entry(window , width=40, font="Arial 27")# это размер окошка для ссылки
window_to_insert_a_link.place(x = 40 , y = 35) 

button_to_execute_the_code = ttk.Button(window, text="                  СОКРАТИТЬ                   ", command=shorten_url, style="TButton")
button_to_execute_the_code.place(relx=0.45, y=99, anchor=CENTER)
s = ttk.Style()
s.configure("TButton", foreground="blue" , background="black" )


button_two = Label(window ,text = "РЕЗУЛЬТАТ" ,font=("Arial Bold", 18))
button_two["bg"] = "#68FCF5"
button_two.place(x=36, y=110)
window_to_insert_a_link_two = ttk.Entry(window , width=40, font="Arial 27")# это размер окошка для ссылки
window_to_insert_a_link_two.place(x = 40 , y = 135) 


window.mainloop()