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

alarmTime = "0000"
alarming = False

def setAlarmTime(newTime):
    global alarmTime
    alarmTime = newTime
    
def getAlarmTime():
    global alarmTime
    return alarmTime

def setAlarming(value):
    global alarming
    alarming = value

def getAlarming():
    global alarming
    return alarming

setAlarmTime("0000")

alarm_ = tk.Label(root, text = "Alarm: " + getAlarmTime()[0:2] + ":" + getAlarmTime()[2:4], bg='skyblue', font=('times',18))

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
    setAlarmTime(entry.get())
    alarm_ .config(text = "Alarm: " + getAlarmTime()[0:2] + ":" + getAlarmTime()[2:4])

def thread(event=None):
    t = threading.Thread(target=tm)
    t.start()

def quit(event=None):
    root.destroy()
    
def checkTime(event=None):
    while True:
        setAlarming(False)
        currentTime = time.strftime("%H%M")
        print("Current time: " + currentTime)
        print("Alarm time: " + getAlarmTime())
        if currentTime == getAlarmTime():
            setAlarming(True)
            t1.start()
            t2.start()
            t3.start()
            t3.join()
            t1.join()
            t2.join()
            
        time.sleep(1)
        
    
def blink(event=None):
    while getAlarming() == True:
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)
        
def takePicture():
    while getAlarming() == True:
        print("Taking picture...")
        os.system("sudo fswebcam -s 2 --no-banner --save test.jpg")
        time.sleep(3)
        
def checkSolved():
    print("Checking cube...")
    result = subprocess.Popen("python -m scripts.label_image --image=test.jpg", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
    out, err = result.communicate()
    newString = out[36:44]
    compare = str(newString, "utf-8")
    print(compare)
    if compare == "solved (":
        setAlarming(False)
        print("DONE!!!!")
    
    

reset_btn = tk.Button(root, text='Reset Alarm', command=resetAlarm)
reset_btn.config(relief='ridge')
reset_btn.grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5)
reset_btn.bind('<Return>', resetAlarm)

tm()
alarm()

main = threading.Thread(target=checkTime)
t1 = threading.Thread(target=blink)
t2 = threading.Thread(target=takePicture)
t3 = threading.Thread(target=checkSolved)

main.start()

root.mainloop()
root.after(1000,thread)
