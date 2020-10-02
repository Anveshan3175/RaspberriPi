
from gpiozero import LED
from time import sleep

red = LED(17)


while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)


''' connect BCM-17 to LED positive and -ve to Rapsberri GND [Board pin 3]  '''

