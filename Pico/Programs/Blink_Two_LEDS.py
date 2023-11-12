"""
P0 to 1k resistor. 
P1 to another 1k resistor
Both resistors to long legs of LEDs
Short legs to gnd
Battery red to P39 (VSYS)
P38 to breadbpard gnd

"""

from machine import Pin
import time


led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)
led2.high()
time.sleep(3)
while True:
    led1.toggle()
    led2.toggle()
    time.sleep(1)
    
