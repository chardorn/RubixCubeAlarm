import os
import subprocess
from gpiozero import LED
import time
from time import sleep

led = LED(17)

alarmTime = "2056"
timeForAlarm = False


while timeForAlarm == True:
    currentTime = time.strftime("%H%M")
    if currentTime == alarmTime:
        timeForAlarm = True

led.on()

alarming = True

os.system("source ./venv/bin/activate")
os.system("convert unsolvedPic test.jpg")
time.sleep(5)

while alarming == True :
    print("STILL GOING")
    os.system("sudo fswebcam -s 2 --no-banner --save test.jpg")
    result = subprocess.Popen("python -m scripts.label_image --image=test.jpg", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
    out, err = result.communicate()
    newString = out[36:44]
    print("WE OUT HERE")
    compare = str(newString, "utf-8")
    if compare == "solved (":
        alarming = False
        print("DONE!!!!")
        led.off()
    
        



#os.system("cd tensorflow-for-poets-2/tf_files/")

#os.system("ls")
#os.system("cd tensorflow-for-poets-2")
#os.system("python -m scripts.label_image --image=test")



#THIS SHIT (ALMOST) WORKS KINDA
#result = subprocess.Popen("python -m scripts.label_image --image=test", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
#out, err = result.communicate()
#newString = out[36:44]
#print("Confidence of solved: ")
#print(newString)
#print(out)

#print(err)
#print(result.stdout.decode('utf-8'))

#subprocess.run("python -m scripts.label_image --image=tf_files/test")
