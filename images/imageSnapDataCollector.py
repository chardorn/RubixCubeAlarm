import os
import subprocess
import random

while (True):

        #check input of user

        value = input("Type U for unsolved, S for solved, T for tests, E for escape, B for background\n")

        rand = random.randint(1,100000)

        device_name = "USB Camera"

        if value == "U" or value == "u":
                print("U!")
                name = "imagesnap unsolved" + str(rand) + ".jpg -d \"" + device_name +"\""
                os.system(name)
                print("done!")
        elif value == "S" or value == "s":
                print("S!")
                name = "imagesnap solved" + str(rand) + ".jpg -d \"" + device_name +"\""
                os.system(name)
                print("done!")

        elif value == "T" or value == "t":
                print("T!")
                name = "imagesnap test" + str(rand) + ".jpg -d \"" + device_name +"\""
                os.system(name)
                print("done!")

        elif value == "B" or value == "b":
                print("B!")
                name = "imagesnap background" + str(rand) + ".jpg -d \"" + device_name +"\""
                os.system(name)
                print("done!")
       
        elif value == "E" or value == "e":
                break
                print("bye!")
                
        else:
                print("nope")
