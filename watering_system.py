import RPi.GPIO as GPIO
import time
import datetime
import signal
from guizero import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print("Hello !")
time.sleep(2)
print("=" * 45)
print("")
print("HERE THE MOST IMPORTANT INFORMATIONS:")
print("-" * 36)
time.sleep(3)
print(" -Press SHIFT + J and than enter,)
print("  to start the script.")
print("")
time.sleep(4)
print(" -NOTE!-----IMPORTANT!--------")
print(" -TO IMMEDIATELY STOP THE EXECUTION,")
print("  PRESS (CTRL + C)")
print("")
time.sleep(4)
print(" -NOTE!-----IMPORTANT!--------")
print("  ADJUST THE WATER OUTFLOW, TO BE WHERE IT SHOULD BE BEFORE EXECUTING THE SCRIPT!")
print("  AS SOON AS YOU START THE SCRIPT, THE PUMP WILL START PUMPING!!!)
print("")
print("=" * 45)
time.sleep(5)
print("")
input("Please press enter, to confirm that you have understood this informations.")
print("")
status = input("Would you like, to start the automatized waterin process? YES = 'Y' | NO = 'N'")

if status == "Y":
    try:
        print("")
        print("Hourly watering intervall runs...")
        print("")
        print("--!!To immediately interrupt the execution, press: (CTRL + C)!!--")
        print("")
        print("")
        print("")
        now = datetime.datetime.now()
        fooo = open("status.txt", "a")
        fooo.write("\n\n"+"STATUSREADINGS FROM " + now.strftime("%d.%m.%y") + "-------------------------" + "\n\n")
        fooo.close()
        while True:
            now = datetime.datetime.now()
            print("")
            print(now.strftime("%X"),"Pump runs...")  # Pump is now pumping
            foo = open("status.txt", "a")
            foo.write("-"+now.strftime("%d.%m")+" "+now.strftime("%X")+" Pump runs..."+"\n")
            foo.close()
            GPIO.setup(17, GPIO.OUT)
            GPIO.output(17, GPIO.HIGH)
            time.sleep(600) # 600
            print("yet 20 min. ...")   # Pump will stop in 20 min. | 1800 - 600 = 1200 | 1200 / 60 = 20 min.
            time.sleep(600) # 600
            print("yet 10 min. ...")   # Pump will stop in 10 min. | 1800 - 1200 = 600 | 600 / 60 = 10 min.
            time.sleep(600) # 600
            now = datetime.datetime.now()
            print("")
            print(now.strftime("%X"),"Watering process done")    # Pump stopped pumping
            f = open("status.txt", "a")
            f.write("-"+now.strftime("%d.%m")+" "+now.strftime("%X")+" Watering process done."+"\n\n")
            f.close()
            GPIO.setup(17, GPIO.OUT)
            GPIO.output(17, GPIO.LOW)
            time.sleep(900) # 900
            print("yet 45 min. ...")      # Pump will start in 45 min. | 3600 - 900 = 2700 | 2700 / 60 = 45 min.
            time.sleep(900) # 900
            print("yet 30 min. ...")       # Pump will start in 30 min. | 2700 - 900 = 1800 | 1800 / 60 = 30 min.
            time.sleep(900) # 900
            print("yet 15 min. ...")       # Pump will start in 15 min. | 1800 - 900 = 900 | 900 / 60 = 15 min.
            time.sleep(900) # 900           # at the end the code will beginn from the hile loop again.
    except KeyboardInterrupt:
        GPIO.setup(17, GPIO.OUT)
        GPIO.output(17, GPIO.LOW)
        print("")
        print("")
        print("The watering process was interrupted by pressing CTRL + C on your keyboard.")
        print("")
        foooo = open("status.txt", "a")
        foooo.write("-"+now.strftime("%d.%m")+" "+now.strftime("%X")+" The watering process was interrupted by pressing CTRL + C on your keyboard..." + "\n\n")
        foooo.close()
else:
    print("You refused to start.")
