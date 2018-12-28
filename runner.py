import tkinter as tk
import threading
import os
import subprocess
from gpiozero import LED
import time
from time import sleep

led = LED(17)

root = tk.Tk()
root.configure(background='skyblue')

alarm = "1234"
alarmTime_ = tk.Label(root, text = "Alarm: " + alarm[0:2] + ":" + alarm[2:4], bg='skyblue', font=('times',18))

entry = tk.Entry(root)
entry.grid(column=0,row=3)

def tm(event=None):
    time_ = tk.Label(root)
    time_ .config(text='{}'.format(time.asctime()))
    time_.config(bg='skyblue', font=('times',50))
    time_.grid(column=0,row=0, padx=5, pady=5)
    root.after(1000,thread)

def alarmTime(event=None):
    alarmTime_.grid(column=0,row=1, padx=5, pady=5)
    root.after(1000,thread)

def resetAlarm(event=None):
    alarm = entry.get()
    alarmTime_ .config(text = "Alarm:" + alarm[0:2] + ":" + alarm[2:4])

def thread(event=None):
    t = threading.Thread(target=tm)
    t.start()

def quit(event=None):
    root.destroy()


tm()
alarmTime()

reset_btn = tk.Button(root, text='Reset Alarm', command=resetAlarm)
reset_btn.config(relief='ridge')
reset_btn.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)
reset_btn.bind('<Return>', resetAlarm)

#qt_btn = tk.Button(root, text='quit', command=quit)
#qt_btn.config(relief='ridge')
#qt_btn.grid(row=1, column=2, padx=5, pady=5, ipadx=5, ipady=5)
#qt_btn.bind('<Return>', quit)

root.mainloop()
while True: #TO DO: change to while truw
    led.on()
    print("on")
    time.sleep(0.2)
    led.off()
    print("off")
    time.sleep(0.2)

#root.after(1000,thread)

