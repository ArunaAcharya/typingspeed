import tkinter as tk
from tkinter import *
import time
from tkinter import ttk


FONT_NAME= "Courier"
FONT= (FONT_NAME, 35, "bold")
total_time= 60
back_color="#FEFCF3"


window= tk.Tk()
window.title("Typing speed test")
window.resizable= False
window.config(background="#282A3A", padx=100, pady=100)
# frame= Frame(master=window, width=200, height=100)
# frame.grid(row= 4, column=0, columnspan=3)



def get_data():
    text= words.get()
    score = len((text.split(' ')))
    score_label.config(text= f"{score} words per minute")
    clear_text()


def clear_text():
    words.delete(0,END)
    timer_text.config(text=0)

def start_timer():
    global total_time

    while total_time >= 0:
        window.update()
        time.sleep(1)
        total_time -=1
        timer_text.config(text=f"0:{total_time}")
    clear_text()
    stop.invoke()

canvas= Canvas(width=500, height=50)

title= Label(text= "Fast Fingers", fg="white", background="#282A3A", font=('Arial,', 50))
title.grid(row=2, column=1, columnspan=3,pady=20)

words= tk.Entry(window, width=35, background="white",highlightthickness=0,  fg="black", font=('Arial', 30,))
words.grid(row=3, column=0, columnspan=3, pady=20)

timer_text= Label(text="1:00", font=('Arial', 24), fg="white", background="#009EFF", borderwidth=5,highlightcolor="#009EFF",highlightthickness=2, highlightbackground="white",)
timer_text.grid(row=3, column=3,  pady=20)

score_label= Label(text='', fg="black",  bg="#FEFCF3")
score_label.grid(row=4, column= 2 )

start= Button(text="🔁", highlightthickness=0,command=start_timer, width=2,background="blue", font=('Arial',30))
start.grid(row=3, column=4,  pady=20, padx=10)

keyboard_image= PhotoImage(file="keyboard.png")

label= Label(text="")
label.config(image=keyboard_image)
label.grid(row=5,column=0, columnspan=5)

stop= Button(window, command=get_data,background="#FEFCF3", highlightbackground="#FEFCF3",highlightthickness=0,highlightcolor="#FEFCF3" )
stop.grid(row=10, column=1, pady=1000)




window.update()
window.mainloop()
