import os
import subprocess
import threading

device_name = "USB Camera"

def takePicture():
        print("Taking picture...")
        #os.system("imagesnap test.jpg -d \"" + device_name +"\"")
        os.system("sudo fswebcam -s 2 --no-banner --save test.jpg")
        #result = subprocess.Popen("imagesnap test.jpg -device_name USB Camera", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
        #out, err = result.communicate()
        #print(out)
        print("Done!")
        #os.system("python label_image_upgraded.py --image=$HOME/Documents/RubixCubeAlarm/images/test.jpg")

#t1 = threading.Thread(target=blinkLED)
#t2 = threading.Thread(target=checkCube)
t3 = threading.Thread(target=takePicture)

#t1.start()
#t2.start()
t3.start()

#t1.join()
#t2.join()
t3.join()
print("DONE!")
