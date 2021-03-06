try:
    import RPi.GPIO as GPIO
except ImportError:
    import fake_rpi.GPIO as GPIO

import numpy as np
import time
import threading

pin = 26

def background(f):
    '''
    a threading decorator
    use @background above the function you want to run in the background
    '''
    def background_function(*a, **kw):
        thread = threading.Thread(target=f, args=a, kwargs=kw)
        thread.daemon = True
        thread.start()
    return background_function

class Lightning:
    def __init__(self):
        """Init classs for lightning"""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin,GPIO.OUT)

    def turnOn(self):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin,GPIO.HIGH)

    def turnOff(self):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin,GPIO.LOW)

    def isOn(self):
        value = GPIO.input(pin)
        return value

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

    @background
    def lightning_rainandthunderstorm(self):
        """Blinking lights"""

        for i in range(0, 4):
            self.turnOn()
            delay = np.random.uniform(0.3, 1.5, 1)[0]
            #delay
            time.sleep(delay)
            #Desligar a luz
            self.turnOff()
            delay2 = np.random.uniform(3, 10, 1)[0]
            time.sleep(delay2)