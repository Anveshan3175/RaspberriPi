from gpiozero import Button

button = Button(2)  # button is connected to BCM 2

while True:
    if button.is_pressed:
        print("BUtton is pressed")
    else:
        print("Button is not pressed ")
