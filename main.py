#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
t_sensor = TouchSensor(Port.S1)
l_sensor = ColorSensor(Port.S3)
pushy = Motor(Port.A) 
mover= Motor(Port.C)  
Green = -45
Blue = 132
Red = 343
Yellow = 507
list2 = []
list1= ["Orange Peel", "Television", "Format", "Include", "Incredible", "Woof", "Gecko", "Sabooboo", "never gonna give you up", "Caydance", "Ellie", "Cammie", "Nareh", "Whitney", "Dragon", "Geometry", "Purple", "Star", "Book", "Monkey", "Mickey", "Boogers", "Dogman", "Smelly", "Chicken", "Tin can", "Person", "Shoe", "Paper", "Rock", "Algae", "Light Purple", "Maroon", "Onomatopoeia", "Lime", "Tequila", "Vampire", "Book", "Puppet", "lymeric", ""]
while t_sensor.pressed() == False:
    mover.run(-700)
mover.stop()
mover.reset_angle(0) 
pushy.run_until_stalled(500) 
pushy.reset_angle(0)

while ev3.buttons.pressed() != [Button.CENTER]:
    while ev3.buttons.pressed() == [Button.UP]:
        ev3.speaker.beep()
        list2.append(l_sensor.color())
        print(list2)
        while ev3.buttons.pressed() != []:
            pass

ev3.speaker.beep()
ev3.speaker.beep()
stop = -1
for x in range(len(list2)):
    stop = stop + 1
    # if color then motor go to color
    if list2[stop] == Color.GREEN:
        mover.run_target(1000,0)
    elif list2[stop] == Color.RED:
        mover.run_target(1000,405)
    elif list2[stop] == Color.YELLOW:
        mover.run_target(1000,540)
    elif list2[stop] == Color.BLUE:
        mover.run_target(1000,205)
    else:
        continue
    Say = random.randint(0, len(list1)-1)
    ev3.speaker.say(list1[Say])
    pushy.run_target(600,-250)
    wait(40)
    pushy.run_target(600,-25)

    



# Step 1: detect color, beep. add to list(Do this until botton pressed)
#  (for each color on list) Step 2: move to color area
#  drop the color
# Step 4: Repeat, check list.
