import numpy as np
import pygame
import os
import sys

class Sounds:
    def __init__(self):
        """Init"""


    def playsound(self,wavefile):
        f1 = os.path.join(os.path.dirname(__file__), 'wav')
        f2 =  os.path.join(f1,wavefile)
        pygame.mixer.music.load(f2)
        pygame.mixer.music.play()

    def testsound(self):
        """Test function using test.wav"""
        self.playsound('test.wav')

    def thunder(self):
        """Thunder sound"""