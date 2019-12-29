from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

def knopf_gedrückt():
    """
    Ist ein Knopf gedrückt?
    """
    return any(brick.buttons())

def warten_auf_knopf_gedrückt():
    """
    Warten bis ein Knopf gedrückt
    """
    while not knopf_gedrückt():
        wait(10)

def warten_am_anfang():
    """
    Am Anfang eines Programmes warten bis ein Knopf gedrückt wird und danach noch eine halbe Sekunde
    """
    # einmal piepsen
    brick.sound.beep()
    # licht auf rot
    brick.light(Color.RED)
    # bild: ?
    brick.display.image(ImageFile.QUESTION_MARK)
    # "hello" abspielen
    brick.sound.file(SoundFile.HELLO)
    
    warten_auf_knopf_gedrückt()
    
    # bild: /!\
    brick.display.image(ImageFile.WARNING)
    # licht auf gelb
    brick.light(Color.YELLOW)
    # "OK" abspielen
    brick.sound.file(SoundFile.OKAY)
    # 1/2 Sekunde warten
    wait(500)
    # dreinmal piepsen
    brick.sound.beeps(3)
    # Licht auf normal
    brick.light(None)
    # Bildschirm löschen
    brick.display.clear()   