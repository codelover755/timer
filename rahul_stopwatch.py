import time
from tkinter import *
from tkinter import messagebox

timer = Tk()
timer.geometry("400x400")
timer.title("Countdown")

hour = StringVar()
minute = StringVar()
second = StringVar()
hour.set("00")
minute.set("00")
second.set("00")

              
h_entry = Entry(timer,textvariable=hour)
m_entry = Entry(timer,textvariable=minute)
s_entry = Entry(timer,textvariable=second)



def start_timer():
        try:

                temp = int(hour.get()) * 3600 + int(minute.get()) *60+ int(second.get())
        except:
                print("Please input the right value")
        while temp>-1:
                
               
                #mins, secs
                mins,secs= divmod(temp,60)
                hours=00
                if mins>60:
                        hours,mins= divmod(mins,60)


                hour.set("{00:2d}".format(hours))
                minute.set("{00:2d}".format(mins))
                second.set("{00:2d}".format(secs))

                timer.update()
                time.sleep(1)
                temp=temp-1
                if temp ==00:
                        messagebox.showinfo("Timer", "Time's Up")

start = Button(timer,text="Start",command=start_timer)

h_entry.place(x=80,y=20)
m_entry.place(x=130,y=20)
s_entry.place(x=180,y=20)
start.place(x=180,y=50)

timer.mainloop()