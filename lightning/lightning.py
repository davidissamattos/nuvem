try:
    import RPi.GPIO as GPIO
except ImportError:
    import fake_rpi.GPIO as GPIO

import numpy as np
import time

pin = 26

class Lightning:
    def __init__(self):
        """Init classs for lightning"""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin,GPIO.OUT)

    def turnOn(self):
        GPIO.output(pin,GPIO.HIGH)

    def turnOff(self):
        GPIO.output(pin,GPIO.LOW)

    def teach_lightning(self):
        """Ensinando a namorada"""
        # Ligar a luz
        self.turnOn()

        # delay
        time.sleep(0.5)

        # Desligar a luz
        self.turnOff()

    def lightning1(self):
        """Generates a lightning"""

    def lightning_rain(self):
        """Light without blinking"""
        self.turnOn()

    def lightning_turnon(self):
        """Turn on the lights"""
        self.turnOn()

    def lightning_turnoff(self):
        """Turn off the lights"""
        self.turnOff()

    def lightning_rainandthunderstorm(self):
        """Blinking lights"""
        #Ligar a luz
        self.turnOn()

        delay = np.random.uniform(0.3, 1.5, 1)[0]
        #delay
        time.sleep(delay)

        #Desligar a luz
        self.turnOff()