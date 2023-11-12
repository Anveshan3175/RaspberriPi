"""
•	Push and hold the BOOTSEL button on the Pico.
•	Then connect to your computer using a micro USB cable.
•	Release BOOTSEL once the drive RPI-RP2 appears on your computer.
•	Drag and drop the UF2 file on to the RPI-RP2 drive. The Raspberry Pi Pico will reboot and will now run MicroPython. 
•	Thonny go to Tools > Options and click on the Interpreter tab. From the interpreter dropdown list select MicroPython (Raspberry Pi Pico). 
•	Place PICO on breadboard
•	Connect GP0 to resistor, Resistor to LED and LED to ground
•	Connect GND pin on Pico to GND
•	Run the program

P39 is VSYS
P38 is GND
P1 is GP0 (on the side of BOOTSEL)
Connect P1 (GP0) to resistor 1 k.
Connect Resistor to Long leg of LED
Connect short leg of LED to bread board gnd
Connect +ve of battery to P39
Connect P38 to Breadboard GND

"""

from machine import Pin
import utime
print("start1")
led = Pin(0, Pin.OUT)
print("start2")
led.low()
print("start3")
while True:
    print("in loop")
    led.toggle()
    print("Toggle")
    utime.sleep(1)
