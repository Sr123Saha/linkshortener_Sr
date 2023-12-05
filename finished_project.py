
import pyperclip
import pyshorteners
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
class Application:
    def __init__(self):
        window = Tk()
        window.title('ПРОГРАММА ДЛЯ СОКРАЩЕНИЯЙ ССЫЛОК')
        window.geometry('1000x250')
        window["bg"] = "#91908D"
        window.resizable(width=False, height=False)
def shorten_url():
    original_url = window_to_insert_a_link.get()
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(original_url)
    window_to_insert_a_link_two.delete(0, 'end')
    window_to_insert_a_link_two.insert(0, shortened_url)
    pyperclip.copy(shortened_url)
    messagebox.showinfo("ПРОГРАММА ДЛЯ СОКРАЩЕНИЯЙ ССЫЛОК", "ВАША ССЫЛКА В УКОРОЧЕННОМ ФОРМАТЕ СКОПИРОВАНА В БУФЕР ОБМЕНЯ")

def clear_entry():
    window_to_insert_a_link.delete(0, 'end')
    window_to_insert_a_link_two.delete(0, 'end')

window = Tk()
window.title('ПРОГРАММА ДЛЯ СОКРАЩЕНИЯЙ ССЫЛОК')
window.geometry('1000x250')
window["bg"] = "#91908D"
window.resizable(width=False, height=False)

label_instruction = Label(window, text="Введите ссылку:", font=("Arial Bold", 18), bg="#91908D")
label_instruction.place(x=36, y=5)

window_to_insert_a_link = ttk.Entry(window, width=40, font="Arial 27",)
window_to_insert_a_link.place(x=40, y=35)

button_to_execute_the_code = ttk.Button(window, text="       СОКРАТИТЬ        ", command=shorten_url, style="TButton")
button_to_execute_the_code.place(relx=0.45, y=99, anchor=CENTER)

button_to_clear_entries = ttk.Button(window, text="        СТЕРЕТЬ ВСЕ      ", command=clear_entry)
button_to_clear_entries.place(relx=0.45, y=200, anchor=CENTER)

s = ttk.Style()
s.configure("TButton", foreground="#000000", background="black")

label_result = Label(window, text="Результат:", font=("Arial Bold", 18), bg="#91908D")
label_result.place(x=36, y=105)

window_to_insert_a_link_two = ttk.Entry(window, width=40, font="Arial 27")
window_to_insert_a_link_two.place(x=40, y=135)

window.mainloop()
def keypress(event):
    if event.keycode == 86:
        event.widget.event_generate('<<Paste>>')
    elif event.keycode == 67:
        event.widget.event_generate('<<Copy>>')
    elif event.keycode == 88:
        event.widget.event_generate('<<Cut>>')


if __name__ == '__main__':
    app = Application()