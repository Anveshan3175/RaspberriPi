from gpiozero import Button

button = Button(2) # connect +ve of button to GPIO2,nd -Ve to GND of Raspberri


button.wait_for_press()
print("BUtton was pressed")
