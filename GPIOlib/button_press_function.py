from gpiozero import Button
from signal import pause

def say_hello():
    print("Hello !! Button is pressed ")


button = Button(2)  # connect +Ve terminal of button to GPIO2 and -Ve of button to GND of raspberri 

button.when_pressed = say_hello  ## be careful not use say_hello()

pause()
