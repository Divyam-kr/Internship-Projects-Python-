from tkinter import Tk
from tkinter import Label
import time 
import sys

Digi_clock = Tk()
Digi_clock.title("Digital Clock Project")

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)

Label(Digi_clock,font=("Roboto,60"),text="Digital Clock",bg="yellow",fg="red")    
clock = Label(Digi_clock, font=('Roboto', 60, 'bold'), bg='yellow', fg='red')
clock.pack()

get_time()
Digi_clock.mainloop()