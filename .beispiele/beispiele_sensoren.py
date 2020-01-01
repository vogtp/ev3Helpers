from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

#################################
# Distanz Sensor
#################################

distanz_sensor = UltrasonicSensor(Port.S1)

# Distanz messen in mm
distanz = distanz_sensor.distance()

# Distanz schreiben
print("Distanz: ", distanz_sensor.distance(), " mm")

# Etwas machen, wenn Distanz zu kurz
if distanz_sensor.distance() < 100:
    print("Etwas ist nahe")