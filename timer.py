# Write your code here :-)
from guizero import App, Text, PushButton, Picture, ButtonGroup
import time
from time import sleep
from datetime import datetime
from gpiozero import Button

button = Button(2)

t1 = 0
t2 = 0

t1State = 0
t2State = 0

starterSwitch = 0
readyButton = 0

def race_reset():
    t1 = 0
    t2 = 0
    t1State = 0
    t2State = 0
    starterSwitch = 0

def t1_update():

    t1 = t1 + .01
    timer1_value.value = t1



app = App(title = 'Timer System', width=700, height=500, layout='grid', bg='white')


timer1_label = Text(app, text = 'Timer 1', size= 40, grid=[1,1])
spacer1 = Picture(app, image='timerspacer1.gif', grid=[2,1])
timer2_label = Text(app, text = 'Timer 2', size= 40, grid=[3,1])

timer1_value = Text(app, text = 0, size = 60, grid = [1,2])
timer2_value = Text(app, text = 0, size = 60, grid = [3,2])

spacer3 = Picture(app, image='timerspacer1.gif', grid=[1,3])
reset_button = PushButton(app, command=race_reset, text='Reset', grid=[1,4])

timer1_value.value = t1
timer2_value.value = t2



startReady = ButtonGroup(app, options=["Ready", "Not Ready"], selected = "Not Ready", grid = [4,1])


if button.is_pressed:
    startReady.value = "Ready"
else:
    startReady.value = "Not Ready"
app.display()
timer1_value.after(1, t1_update)