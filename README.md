# Automatic-watering-system
A system, which **waters** plants via **raspberry pi** (3) and a **relay** connected to a water pump every hour for 30 minutes.

[Connection](#connection)

[Executing the script](#executing-the-script)

[Interrupting the script](#interrupting-the-script)

[Status](#status)

## Connection
The connection between the Raspberry pi and the relay is shown in the **Connection.pdf** File.

If you are **NOT** using the given python code above, the connection might be different.

## Executing the script
To execute the python script, go into the directory, where the file is safed and write
```__your-directory__ python watering_intervall.py```.

## Interrupting the script
To interrupt the script immediately press (Ctrl + C).

Now you are free, to open and edit the status.txt file as you'll learn in the next chapter

## Status
Every time, the code is executed, a status.txt file will appear in the same directory, where the python script is saved. The content of this file will be:
- date and time on wich the script was executed
- date and time on wich the script was stopped (Ctrl + c)
- date and time on wich the pump started and stopped pumping
- entire duration in days, hours and minutes

The script appends informations to this file, every time the pump starts or stops.

**NOTE !** Do not open or edit this file, while the script is in execution, otherwise the informations could be dammaged.
