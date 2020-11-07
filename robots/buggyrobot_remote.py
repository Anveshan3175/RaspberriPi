
from gpiozero import Robot
from bluedot import BlueDot


bd = BlueDot()
bd.wait_for_press()
print("you have pressed a blue dot")
##robot = Robot(left=(9,10), right=(7,8))  custom made
##robot = Robot(left=(9,10),right=(8,7))  first purchase
robot = Robot(left=(7,8),right=(10,9))  ##second purchase





def move(pos):
    if pos.top:
        robot.forward()
    elif pos.bottom:
        robot.backward()
    elif pos.right:
        robot.right()
    elif pos.left:
        robot.left()

def stop():
    robot.stop()


bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop






        
        
