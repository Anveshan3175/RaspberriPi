import RPi.GPIO as GPIO

import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)


while True:
    GPIO.output(3,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(3,GPIO.LOW)
    time.sleep(0.5)

