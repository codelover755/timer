import time
from tkinter import *
from tkinter import messagebox

timer = Tk()
timer.geometry("400x400")
timer.title("Countdown")

hour = StringVar()
minute = StringVar()
second = StringVar()

def start_timer():

hour.set("00")
minute.set("00")
second.set("00")

h_entry = Entry(timer,textvariable=hour)
m_entry = Entry(timer,textvariable=minute)
s_entry = Entry(timer,textvariable=second)
start = Button(timer,text="Start",command=start_timer)

h_entry.place(x=80,y=20)
m_entry.place(x=130,y=20)
s_entry.place(x=180,y=20)

timer.mainloop()