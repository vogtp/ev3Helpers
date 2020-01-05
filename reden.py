from pybricks import ev3brick as brick
from pybricks.parameters import ( Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
import sys 
import os
from threading import Thread

class Reden(Thread):

    def __init__(self, german=True):
        self._german = german
        self._msg = None
        self.started = False
        #super().start()

    @staticmethod
    def sag( msg, german=True):
        if german:
            lang="-vde"
        os.system("/usr/bin/espeak -s 150 -a 200 --stdout '{}' {} > out.wav".format(msg,lang))
        brick.sound.file("out.wav",volume=100)

    def __call__(self, msg):
        if self.started:
            self._msg = msg
        else:
            Reden.sag(msg, self._german)


    def run(self):
       # self.popen = os.popen("/usr/bin/aplay -i",buffering=1)
        self.started = True
        self._espeak("Start reden")
        try:
            while 1:
                if self._msg:
                    msg = self._msg
                    self._msg = None
                    self._espeak(msg)
                pass
        except:
            pass
        finally:
            self.started = False
        
   

    def _espeak(self, msg):
        lang=""
        if self._german:
            lang="-vde"
        print(msg)
        os.system("/usr/bin/espeak -a 200 --stdout '{}' {} | /usr/bin/aplay -i".format(msg,lang))

        
      #  brick.sound.file("out.wav",volume=100)
      #popen.write("/usr/bin/espeak -a 200 --stdout 'test'")