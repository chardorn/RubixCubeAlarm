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

alarmTime = "1234"
alarm_ = tk.Label(root, text = "Alarm: " + alarmTime[0:2] + ":" + alarmTime[2:4], bg='skyblue', font=('times',18))

entry = tk.Entry(root)
entry.grid(column=0,row=3)

def tm(event=None):
    time_ = tk.Label(root)
    time_ .config(text='{}'.format(time.asctime()))
    time_.config(bg='skyblue', font=('times',50))
    time_.grid(column=0,row=0, padx=5, pady=5)
    root.after(1000,thread)

def alarm(event=None):
    alarm_.grid(column=0,row=1, padx=5, pady=5)
    root.after(1000,thread)

def resetAlarm(event=None):
    alarmTime = entry.get()
    alarm_ .config(text = "Alarm: " + alarmTime[0:2] + ":" + alarmTime[2:4])

def thread(event=None):
    t = threading.Thread(target=tm)
    t.start()

def quit(event=None):
    root.destroy()
    
def blink(event=None):
    alarming = False
    while True:
        currentTime = time.strftime("%H%M")
        print("Current time: " + currentTime)
        print("Alarm time: " + alarmTime)
        if currentTime == alarmTime:
            alarming = True
            timeForAlarm = True
        time.sleep(1)
        while alarming == True:
            led.on()
            time.sleep(0.2)
            led.off()
            time.sleep(0.2)
        
def takePicture():
    while alarming == True: #TO DO: change to while alarming = True
        print("Taking picture...")
        os.system("sudo fswebcam -s 2 --no-banner --save test.jpg")
        #result = subprocess.Popen("sudo fswebcam -s 2 --no-banner --save test.jpg", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
        #out, err = result.communicate()
        time.sleep(3)
        #os.system("sudo ~/Downloads/usbreset /dev/bus/usb/001/024")
    

reset_btn = tk.Button(root, text='Reset Alarm', command=resetAlarm)
reset_btn.config(relief='ridge')
reset_btn.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)
reset_btn.bind('<Return>', resetAlarm)

tm()
alarm()

t1 = threading.Thread(target=blink)
t1.start()

root.mainloop()
root.after(1000,thread)



#QUIT BUTTON
#qt_btn = tk.Button(root, text='quit', command=quit)
#qt_btn.config(relief='ridge')
#qt_btn.grid(row=1, column=2, padx=5, pady=5, ipadx=5, ipady=5)
#qt_btn.bind('<Return>', quit)



