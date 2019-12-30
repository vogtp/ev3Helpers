from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Auto completion installieren:
# pip install pybricks-stubs

def knopf_gedrückt():
    """
    Ist ein Knopf gedrückt?
    """
    return any(brick.buttons())

def warten_bis_knopf_gedrückt():
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
    
    warten_bis_knopf_gedrückt()
    
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

def bilder_zeigen():
    '''
    Zeigt alle Bilder
    '''
    # Ist zu kompliziert im Moment
    import inspect 
    members = inspect.getmembers(ImageFile)
    members = [(name, data) for (name, data) in members if not name.startswith('_')]
    i=0
    while True:
        name, data = members[i]
        print('ImageFile.{}'.format(name))
        brick.display.clear()
        brick.display.image(data)
        brick.display.text("")
        brick.display.text('ImageFile.{}'.format(name))
        wait(50)
        buttons = brick.buttons()
        while not any(buttons):
            buttons = brick.buttons()
            wait(10)
        if Button.RIGHT in buttons:
            i += 1
        if Button.LEFT in buttons: 
            i -= 1
        if Button.CENTER in buttons:
            pass
        if Button.UP in buttons:
            i = 0
        if Button.DOWN in buttons:
            break

def sound_abspielen():
    '''
    Spielt alle Töne ab
    '''
    # Ist zu kompliziert im Moment
    import inspect 
    members = inspect.getmembers(SoundFile)
    members = [(name, data) for (name, data) in members if not name.startswith('_')]
    i=0
    while True:
        name, data = members[i]
        print('SoundFile.{}'.format(name))
        brick.display.clear()
        brick.display.text("")
        brick.display.text('SoundFile.{}'.format(name))
        brick.sound.file(data)
        wait(50)
        buttons = brick.buttons()
        while not any(buttons):
            buttons = brick.buttons()
            wait(10)
        if Button.RIGHT in buttons:
            i += 1
        if Button.LEFT in buttons: 
            i -= 1
        if Button.CENTER in buttons:
            pass
        if Button.UP in buttons:
            i = 0
        if Button.DOWN in buttons:
            break