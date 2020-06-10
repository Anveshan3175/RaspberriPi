""" Cyclon LED Flasher """

import RPi.GPIO as GPIO

import time

#Define list of LEDs
LEDs = [29,31,33,35,37,36,38,40]

#Set GPIO mode
GPIO.setmode(GPIO.BOARD)

for LED in LEDs:
    GPIO.setup(LED,GPIO.OUT)


while True:
    for LED in LEDs:
        GPIO.output(LED,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(LED,GPIO.LOW)

    for LED in LEDs[-2:1:-1]:
        GPIO.output(LED,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(LED,GPIO.LOW)        
        

