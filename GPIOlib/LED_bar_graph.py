from gpiozero import LEDBarGraph
from time import sleep



graph = LEDBarGraph(5,6,13,19,26,20)

''' in LEDBarGraph, we can give values like 1/2 and half the LEDs glow.
That is not possible in LED board. In LED Board, we need to give individual values'''

while True:
    graph.value = 1 #(1,1,1,1,1,1)
    sleep(1)
    graph.value = 1/2 #(1,1,1,0,0,0)
    sleep(1)
    graph.value = -1/2 #(0,0,0,1,1,1)
    sleep(1)
    graph.value = 1/4 #(1,0,0,0,0,0)
    sleep(1)
    graph.value = -1/4 #(0,0,0,0,0,1)
    sleep(1)
    graph.value = -1 #(1,1,1,1,1,1)
    sleep(1)
    graph.value = 0 #(0,0,0,0,0,0,0)
    sleep(1)
