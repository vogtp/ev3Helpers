from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

def warten():
    brick.sound.beep()
    brick.light(Color.RED)
    brick.display.image(ImageFile.QUESTION_MARK)
    brick.sound.file(SoundFile.HELLO)
    # nur das wichtig
    while not any(brick.buttons()):
        wait(10)
    # fertig wichtig
    brick.display.image(ImageFile.WARNING)
    brick.light(Color.YELLOW)
    brick.sound.file(SoundFile.OKAY)
    wait(500)
    brick.sound.beeps(3)
    brick.light(None)
    brick.display.clear()   