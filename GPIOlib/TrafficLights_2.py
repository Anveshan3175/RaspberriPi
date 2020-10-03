from gpiozero import TrafficLights
from time import sleep
from signal import pause


lights = TrafficLights(2,3,4)
'''
Connect RED LED to GPIO2
Connect AMBER LED to GPIO3
Connect GREEN LED to GPIO4
Connect GND frpm Pie to -ves of all LEDS
'''

def traffic_light_sequence():
    while True:
        yield (0,0,1) #green
        sleep(10)
        yield(0,1,0) #amber
        sleep(1)
        yield(1,0,0) #red
        sleep(10)
        yield(1,1,0)
        sleep(1)


lights.source = traffic_light_sequence()

pause()
        
        
