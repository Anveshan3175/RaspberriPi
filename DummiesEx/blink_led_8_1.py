import RPi.GPIO as GPIO
import time

""" Flash all 8 LEDS """
#Set the GPIO pin mode
GPIO.setmode(GPIO.BOARD)

GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)


while True:
    GPIO.output(29, GPIO.HIGH) #LED1
    GPIO.output(31, GPIO.HIGH)
    GPIO.output(33, GPIO.HIGH)
    GPIO.output(35, GPIO.HIGH)
    GPIO.output(37, GPIO.HIGH)
    GPIO.output(36, GPIO.HIGH)
    GPIO.output(38, GPIO.HIGH)
    GPIO.output(40, GPIO.HIGH)

    time.sleep(0.5)

    GPIO.output(29, GPIO.LOW)
    GPIO.output(31, GPIO.LOW)
    GPIO.output(33, GPIO.LOW)
    GPIO.output(35, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)
    GPIO.output(36, GPIO.LOW)
    GPIO.output(38, GPIO.LOW)
    GPIO.output(40, GPIO.LOW)

    time.sleep(0.5)
    
