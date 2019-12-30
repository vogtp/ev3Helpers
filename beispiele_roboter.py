from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

#################################
# Roboter
#################################

# Ein roboter erstellen:
linker_motor = Motor(Port.B)
rechter_motor = Motor(Port.C)
rad_durchmesser=56
achsen_abstand=114
roboter = DriveBase(linker_motor, rechter_motor, rad_durchmesser, achsen_abstand)

# Fahren
geschwindigkeit = 10 # mm/s   (Milimeter pro Sekunde)
steuern = 0          # Grad/s (360 Grad ist ganzer Kreis)
zeit = 1000          # ms     (1000ms ist eine Sekunde)

# Fahren bis ein anderer Befehl kommt
roboter.drive(geschwindigkeit, steuern) 

# Eine zeitlang fahren
roboter.drive(geschwindigkeit, steuern, zeit) 

# Bremsen
roboter.stop(Stop.BRAKE)

# Stop.COAST -> nichts machen
# Stop.BRAKE -> bremsen
# Stop.HOLD  -> mit aller Kraft halten