try:
    import RPi.GPIO as GPIO
except ImportError:
    import fake_rpi.GPIO as GPIO

import numpy as np

class Lightning:
    def __init__(self):
        """Init classs for lightning"""
        GPIO.setmode(GPIO.BCM)

    def testlamp(self):
        """Testing turning on and off the lamps in one second"""

    def lightning(self):
        """Generates a random lightning"""