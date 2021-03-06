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
        self.number_thunders = 5

    def playsound(self,wavefile):
        f1 = os.path.join(os.path.dirname(__file__), 'wav')
        f2 = os.path.join(f1,wavefile)
        pygame.mixer.music.load(f2)
        pygame.mixer.music.play()

    def turnoffsound(self):
        pygame.mixer.music.stop()

    def select_random_thunder(self):
        number = int(round(np.random.uniform(1, self.number_thunders, 1)[0],0))
        print number
        sound_path = 'thunder/thunder' + str(number) + '.wav'
        print sound_path
        return sound_path

    def testsound(self):
        """Test function using test.wav"""
        self.playsound('test.wav')

    def thunder(self):
        """Thunder sound"""
        self.playsound(self.select_random_thunder())

    def thunder_turnon(self):
        """Turn on the thunder sound"""
        self.turnoffsound()
        self.playsound(self.select_random_thunder())

    def thunder_thurnoff(self):
        """Turn off the thunder sound"""
        #self.playsound("thunder/thunder1.wav")
        self.turnoffsound()

    def rainandthunderstorm(self):
        """Sound of rain and thunder"""
        self.playsound("thunder/thunder1-2min.wav")

    def rainsound(self):
        """Rain sound"""
        self.playsound("rain/rain15s.wav")

    def lightrain(self):
        """Long sound of rain"""
        self.playsound("rain/rain70s.wav")