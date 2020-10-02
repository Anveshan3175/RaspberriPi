from gpiozero import LED, Button
from signal import pause


led = LED(17)    ## LED positive to GPIO17  and LED negative to GND of Raspberri
button = Button(2) ## Button positive to GPIO2 and negative to GND of Raspberri


button.when_pressed =led.on
button.when_released = led.off

pause()
