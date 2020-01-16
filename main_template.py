#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from reden import Reden
import papiHilfe 

# warten zum starten
#papiHilfe.wartenAmAnfang()

# Ab hier programieren


# Haupt-Schleife 
while 1:
    # Hier kommt das Program, das Laufen soll während der Roboter aktiv ist


    
    if papiHilfe.knopfGedruckt():
        # Damit wird die Haupt-Schleide gestopped
        break
        
    wait(10)

# Ab hier kann aufgeräumt werden
brick.sound.beeps(7)