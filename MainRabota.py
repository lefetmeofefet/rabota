import time
import math
import random
import pyautogui

def random_range(min, max):
    num1 = random.random()
    num1 *= max
    num1 += min
    return num1

screen_size_x, screen_size_y = pyautogui.size()

# moves the mouse from where it is to Destination
# gets: the destination x and destination y
# returns: nothing
def mouse(destination_x, destination_y):
    x,y = pyautogui.position() #current position
    while x != destination_x and y != destination_y:
        angle = math.atan2(destination_x - x,destination_y - y) # angle randomizing:
        angle_random = random_range(-0.2, 0.2)
        angle = angle + angle_random + 0.2
        mouse_move = random_range(screen_size_x / 100,screen_size_x / 50) # movement randomizing:

        x += int(math.sin(angle) * mouse_move)
        y += int(math.cos(angle) * mouse_move)
        pyautogui.moveTo(x, y) # moves with angle to Destination

        if(-10 < destination_x - x < 10 and -10 < destination_y - y < 10): # jumps to the end when close:
            pyautogui.moveTo(destination_x, destination_y)
            x = destination_x
            y = destination_y


    print(pyautogui.position())

mouse(1000, 1000)