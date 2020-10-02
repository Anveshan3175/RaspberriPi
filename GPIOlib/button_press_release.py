from gpiozero import Button
from signal import pause


def say_hello():
    print("hello.Button is pressed.")


def say_goodbye():
    print("Goodbye.Button is released")


button = Button (2) # Connect button positive to GPIO2


button.when_pressed = say_hello
button.when_released = say_goodbye       
