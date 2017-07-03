import numpy as np
import pygame
import os
import sys
import time

def Keepsoundon():
    f1 = os.path.join(os.path.dirname(__file__), 'wav')
    f2 = os.path.join(f1, 'whitenoise.wav')
    pygame.mixer.music.load(f2)
    print "playing sound"
    pygame.mixer.music.play()
    #pygame.mixer.music.set_volume()
    time.sleep(10)
    pygame.mixer.music.stop()

class Sounds:
    def __init__(self):
        """Init"""


    def playsound(self,wavefile):
        f1 = os.path.join(os.path.dirname(__file__), 'wav')
        f2 = os.path.join(f1,wavefile)
        pygame.mixer.music.load(f2)
        pygame.mixer.music.play()

    def testsound(self):
        """Test function using test.wav"""
        self.playsound('test.wav')

    def thunder(self):
        """Thunder sound"""
        self.playsound('thunder1.wav')

    def thunder_turnon(self):
        """Thunder sound"""
        self.playsound("thunder1.wav")

    def thunder_thurnoff(self):
        """Thunder sound"""
        self.playsound("thunder1.wav")