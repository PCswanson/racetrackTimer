#TextTimer
import time
from time import sleep
from datetime import datetime
from gpiozero import Button

starter_switch = Button(2)
t1Gate = DigitalInputDevice(3)
t2Gate = DigitalInputDevice(4)

run_number = 1
t1 = 0
t2 = 0
t1State = 0
t2State = 0

timer = 0



while True:

#display dateTime, run number
    print(datetime.now())
    print("Run #", run_number)


#wait for switch press
    starter_switch.wait_for_press()
    print("Ready for Race!")
#wait for switch unpress, start timer

    starter_switch.wait_for_release()
    timer = time.perf_counter()
    print("Race Begins!")

    while t1State == 0 or t2State == 0:
        if t1Gate.value:
            if t1State == 0:
                t1State = 1
                t1 = round(time.perf_counter() - timer,3)
        if t2Gate.value:
            if t2State == 0:
                t2State = 1
                t2 = round(time.perf_counter() - timer, 3)

#check for finish, when each finishes, assign time to track

#display time, run number, date time, save to file, return to top

    print("Track 1: ", t1)
    print("Track 2: ", t2)
    run_number = run_number + 1
    t1State = 0
    t2State = 0
