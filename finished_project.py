import keyboard
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
    pyperclip.copy(shortened_url)
    messagebox.showinfo("СОКРАЩАТЕЛЬ ССЫЛОЕК", "ВАША ССЫЛКА В УКОРОЧЕННОМ ФОРМАТЕ СКОПИРОВАНА В БУФЕР ОБМЕНЯ")


def clear_entry():
    window_to_insert_a_link.delete(0, 'end')
    window_to_insert_a_link_two.delete(0, 'end')



window = Tk()
window.title('Сокращатель ссылок')
window.geometry('1000x250')
window["bg"] = "#68FCF5"
window.resizable(width=False, height=False)


label_instruction = Label(window, text="Введите ссылку:", font=("Arial Bold", 18), bg="#68FCF5")
label_instruction.place(x=36, y=10)


window_to_insert_a_link = ttk.Entry(window, width=40, font="Arial 27")
window_to_insert_a_link.place(x=40, y=35)


button_to_execute_the_code = ttk.Button(window, text="       СОКРАТИТЬ        ", command=shorten_url, style="TButton")
button_to_execute_the_code.place(relx=0.45, y=99, anchor=CENTER)


button_to_clear_entries = ttk.Button(window, text="        СТЕРЕТЬ ВСЕ      ", command=clear_entry)
button_to_clear_entries.place(relx=0.45, y=200, anchor=CENTER)


s = ttk.Style()
s.configure("TButton", foreground="blue", background="black")


label_result = Label(window, text="Результат:", font=("Arial Bold", 18), bg="#68FCF5")
label_result.place(x=36, y=110)


window_to_insert_a_link_two = ttk.Entry(window, width=40, font="Arial 27")
window_to_insert_a_link_two.place(x=40, y=135)

# while True:
#     if not(keyboard.on_pressed('q')):
#         break
#     elif keyboard.is_pressed('esc'):
#         print('esc')
#         quit()

while True:
    # Wait for the next event.
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name  == 'space':
        print('space was pressed')
        window.mainloop()

