"""  Use For Loops and Lists to blink LEDs"""

import RPi.GPIO as GPIO

import time

LEDs = [29,31,33,35,37,36,38,40]

# set board mode

GPIO.setmode(GPIO.BOARD)

for LED in LEDs:
    GPIO.setup(LED,GPIO.OUT)


def setLEDs(setValue):
    for LED in LEDs:
        GPIO.output(LED,setValue)


while True:
    for flashCount in range(3):
        setLEDs(GPIO.HIGH)
        time.sleep(0.1)
        setLEDs(GPIO.LOW)
        time.sleep(0.1)


    for flashCount in range(3):
        setLEDs(GPIO.HIGH)
        time.sleep(0.5)
        setLEDs(GPIO.LOW)
        time.sleep(0.5)
        

