import RPi.GPIO as GPIO
import time
import datetime
import signal
from guizero import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
"""
print("Hallo Armin !")
time.sleep(2)
print("=" * 45)
print("")
print("HIER NOCHMALS DIE WICHTIGSTEN INFOS VOR DEM START:")
print("-" * 36)
time.sleep(3)
print(" -Drücke 'shift + J' und danach enter um")
print("  den Giesprozess zu starten.")
print("")
time.sleep(4)
print(" -ACHTUNG!-----WICHTIG!--------")
print(" -UM DEN GIESSPROZESS SOFORT ZU STOPPEN,")
print("  DRÜCKE (CTRL + C)")
print("")
time.sleep(4)
print(" -ACHTUNG!-----WICHTIG!--------")
print("  Richte den Wasserausfluss dorthin wo er")
print("  hin gehört. Sobald du das Programm startest")
print("  wird die Pumpe für 30 min. beginnen zu pumpen!!!!")
print("")
print("=" * 45)
time.sleep(5)
print("")
input("Bitte bestätige mit der Enter-Taste, dass du diese Infos verstanden hast")
print("")"""
status = input("Automatischen Giessprozess jetzt starten? Ja = 'J' | Nein = 'N'")

if status == "J":
    try:
        print("")
        print("Stündliches Giessintervall läuft...")
        print("")
        print("--!!UM DAS INTERVALL ZU STOPPEN, DRÜCKE (CTRL + C)!!--")
        print("")
        print("")
        print("")
        now = datetime.datetime.now()
        fooo = open("status.txt", "a")
        fooo.write("\n\n"+"STATUSLESUNGEN AB DEM " + now.strftime("%d.%m.%y") + "-------------------------" + "\n\n")
        fooo.close()
        while True:
            now = datetime.datetime.now()
            print("")
            print(now.strftime("%X"),"Pumpe läuft...")  # Pump is now pumping
            foo = open("status.txt", "a")
            foo.write("-"+now.strftime("%d.%m")+" "+now.strftime("%X")+" Pumpe läuft..."+"\n")
            foo.close()
            GPIO.setup(17, GPIO.OUT)
            GPIO.output(17, GPIO.HIGH)
            time.sleep(600) # 600
            print("noch 20 min. ...")   # Pump will stop in 20 min. | 1800 - 600 = 1200 | 1200 / 60 = 20 min.
            time.sleep(600) # 600
            print("noch 10 min. ...")   # Pump will stop in 10 min. | 1800 - 1200 = 600 | 600 / 60 = 10 min.
            time.sleep(600) # 600
            now = datetime.datetime.now()
            print("")
            print(now.strftime("%X"),"Giessprozess beendet")    # Pump stopped pumping
            f = open("status.txt", "a")
            f.write("-"+now.strftime("%d.%m")+" "+now.strftime("%X")+" Giessprozess beendet."+"\n\n")
            f.close()
            GPIO.setup(17, GPIO.OUT)
            GPIO.output(17, GPIO.LOW)
            time.sleep(900) # 900
            print("noch 45 min. ...")      # Pump will start in 45 min. | 3600 - 900 = 2700 | 2700 / 60 = 45 min.
            time.sleep(900) # 900
            print("noch 30 min. ...")       # Pump will start in 30 min. | 2700 - 900 = 1800 | 1800 / 60 = 30 min.
            time.sleep(900) # 900
            print("noch 15 min. ...")       # Pump will start in 15 min. | 1800 - 900 = 900 | 900 / 60 = 15 min.
            time.sleep(900) # 900           # at the end the code will beginn from the hile loop again.
    except KeyboardInterrupt:
        GPIO.setup(17, GPIO.OUT)
        GPIO.output(17, GPIO.LOW)
        print("")
        print("")
        print("Der Giessprozess wurde mit CTRL + C gestoppt.")
        print("")
        foooo = open("status.txt", "a")
        foooo.write("-"+now.strftime("%d.%m")+" "+now.strftime("%X")+" Das Intervall wurde mit CTRL + C unterbrochen..." + "\n\n")
        foooo.close()
        print("Um das Programm nochmals zu starten,")
        print("schreibe 'python3 armin_relay.py' in das")
        print("Terminal und drücke enter")
else:
    print("Du hast den Start verweigert.")
