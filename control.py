import RPi.GPIO as GPIO
import time

class Relay:
    pin = [6, 13, 19, 26]

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for i in self.pin:
            GPIO.setup(i, GPIO.OUT)

    def set(self, pn, logic):
        GPIO.output(self.pin[pn-1], GPIO.HIGH if logic == 1 else GPIO.LOW)

class Speaker:
    pin = 5

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT)

    def beep(self, dur):
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(dur)
        GPIO.output(self.pin, GPIO.LOW)

