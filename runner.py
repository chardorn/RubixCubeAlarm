import threading
import os
import subprocess
from gpiozero import LED
import time
from time import sleep

led = LED(17)

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

def checkTime(event=None):
    while True:
        setAlarming(False)
        currentTime = time.strftime("%H%M")
        print("Current time: " + currentTime)
        print("Alarm time: " + getAlarmTime())
        alarmTime == currentTime #DELETE THIS LATER
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
    

main = threading.Thread(target=checkTime)
t1 = threading.Thread(target=blink)
t2 = threading.Thread(target=takePicture)
t3 = threading.Thread(target=checkSolved)

main.start()
