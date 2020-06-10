""" This program alternates between short and long flashes """

import RPi.GPIO as GPIO

import time

# define constants
LED1 = 29
LED2 = 31
LED3 = 33
LED4 = 35
LED5 = 37
LED6 = 36
LED7 = 38
LED8 = 40

# define variables
sleepTime = 0.1
flashCount = 0

#setup GPIO mode
GPIO.setmode(GPIO.BOARD)

#Define IO pins used in this programs. The IO pins are connected to LEDs
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)
GPIO.setup(LED4,GPIO.OUT)
GPIO.setup(LED5,GPIO.OUT)
GPIO.setup(LED6,GPIO.OUT)
GPIO.setup(LED7,GPIO.OUT)
GPIO.setup(LED8,GPIO.OUT)

# Set values onto LEDs - ON or OFF
def setLEDs(setValue):
    GPIO.output(LED1, setValue)
    GPIO.output(LED2, setValue)
    GPIO.output(LED3, setValue)
    GPIO.output(LED4, setValue)
    GPIO.output(LED5, setValue)
    GPIO.output(LED6, setValue)
    GPIO.output(LED7, setValue)
    GPIO.output(LED8, setValue)


while True:
    setLEDs(GPIO.HIGH)
    time.sleep(sleepTime)
    setLEDs(GPIO.LOW)
    time.sleep(sleepTime)

    flashCount = flashCount + 1

    if flashCount == 3:
        flashCount = 0

        if sleepTime == 0.1:
            sleepTime = 0.5
        else:
            sleepTime = 0.1
    



    
