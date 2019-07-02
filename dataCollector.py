import os
import subprocess

while (True):

        #check input of user

        value = input("Type U for unsolved, S for solved, T for tests, E for escape\n")

        if value == "U" or value == "u":
                print("U!")
                os.system("sudo fswebcam -s 2 --no-banner --save /Documents/RubixCubeAlarm/solved/unsolvedtest.jpg")
                print("done!")
                
        elif value == "S" or value == "s":
                print("S!")
                os.system("sudo fswebcam -s 2 --no-banner --save /Documents/RubixCubeAlarm/unsolved/solvedtest.jpg")
                print("done!")

        elif value == "T" or value == "t":
                print("S!")
                os.system("sudo fswebcam -s 2 --no-banner --save /Documents/RubixCubeAlarm/tests/test.jpg")
                print("done!")

        elif value == "B" or value == "b":
                print("B!")
                os.system("sudo fswebcam -s 2 --no-banner --save /Documents/RubixCubeAlarm/background/backgroundtest.jpg")
                print("done!")
       
        elif value == "E" or value == "e":
                break
                print("bye!")
                
        else:
                print("nope")
