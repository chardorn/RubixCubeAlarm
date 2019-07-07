import os
import subprocess
from gpiozero import LED
import time
from time import sleep
import threading

def blinkLED():
    while alarming == True:
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)
    
def checkCube():
    while alarming == True:
        print("Checking cube...")
        result = subprocess.Popen("python /home/pi/RubixCubeAlarm/tensorflow-for-poets-2/scripts/label_image --image=test.jpg", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
        out, err = result.communicate()
        newString = out[36:44]
        compare = str(newString, "utf-8")
        if compare == "solved (":
            alarming = False
            print("DONE!!!!")
        
def takePicture():
    while alarming == True:
        print("Taking picture...")
        os.system("sudo fswebcam -s 2 --no-banner --save test.jpg")

#Set up needed variables
led = LED(17)
alarmTime = "2056"
timeForAlarm = False
led.on()
global alarming = True

#Test alarm portion
#TODO: change so it actually functions
while timeForAlarm == True:
    currentTime = time.strftime("%H%M")
    if currentTime == alarmTime:
        timeForAlarm = True

#Change test.jpeg to an unsolved picture
#os.system("source ./venv/bin/activate")
#os.system("convert unsolvedPic test.jpg")

t1 = threading.Thread(target=blinkLED)
t2 = threading.Thread(target=checkCube)
t3 = threading.Thread(target=takePicture)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
led.off()
print("DONE!")
