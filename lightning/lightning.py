try:
    import RPi.GPIO as GPIO
except ImportError:
    import fake_rpi.GPIO as GPIO

import numpy as np

class Lightning:
    def __init__(self):
        """Init classs for lightning"""

    def lightning(self):
        """Generates a random lightning"""