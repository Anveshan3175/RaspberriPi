from gpiozero import PWMLED
from signal import pause

led = PWMLED(17)


led.pulse() # pulse - fade in and out continously

pause()
