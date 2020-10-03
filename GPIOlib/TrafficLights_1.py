from gpiozero import TrafficLights
from time import sleep


lights = TrafficLights(2,3,4)
'''
Connect RED LED to GPIO2
Connect AMBER LED to GPIO3
Connect GREEN LED to GPIO4
Connect GND frpm Pie to -ves of all LEDS
'''


lights.green.on()


while True:
    sleep(10)
    lights.green.off()
    lights.amber.on()
    sleep(1)
    lights.amber.off()
    lights.red.on()
    sleep(10)
    lights.amber.on()
    sleep(1)
    lights.green.on()
    lights.amber.off()
    lights.red.off()
    
