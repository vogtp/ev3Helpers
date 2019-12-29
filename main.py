#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import papiHilfe 

# warten zum starten
papiHilfe.warten_am_anfang()

# Ab hier programieren


# Haupt-Schleife 
# Läuft bis: stop=False  (gesetzt wird)
stop=False
while not stop:
    # Hier kommt das Program, das Laufen soll während der Roboter aktiv ist

    # Abbruch wenn irgend ein Knofp gedrückt wird
    if papiHilfe.knopf_gedrückt():
        # Damit wird die Haupt-Schleide gestopped
        stop=True
    wait(10)

# Ab hier kann aufgeräumt werden
brick.sound.beeps(7)