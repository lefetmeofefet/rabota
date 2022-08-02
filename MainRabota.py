import time
import math
import random
import pyautogui

def random_range(min, max):
    num1 = random.random()
    num1 *= max
    num1 += min
    return num1

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

screen_size_x, screen_size_y = pyautogui.size()

# moves the mouse from where it is to Destination
# gets: the destination x and destination y
# returns: nothing

ARRIVAL_DISTANCE = 10
ANGLE_MAX_ERROR = 0.2
ANGLE_CURVE = 0.15
MOUSE_SPEED_MIN = screen_size_x / 500
MOUSE_SPEED_MAX = screen_size_x / 400


def mouse(destination_x, destination_y):
    mouse_speed_min = MOUSE_SPEED_MIN
    mouse_speed_max = MOUSE_SPEED_MAX
    x_start,y_start = pyautogui.position() #current position
    x, y = pyautogui.position()  # current position
    angle_curve = ANGLE_CURVE * (1 if random.random() > 0.5 else -1)
    while x != destination_x and y != destination_y:
        angle = math.atan2(destination_x - x,destination_y - y) # angle randomizing:
        angle_random = random_range(-ANGLE_MAX_ERROR, ANGLE_MAX_ERROR)
        angle = angle + angle_random + angle_curve

        if mouse_speed_min > screen_size_x / 800:
            if distance(x, y, x_start, y_start) < distance(x, y, destination_x, destination_y):
                mouse_speed_min += screen_size_x / 1000
                mouse_speed_max += screen_size_x / 1000
            else:
                mouse_speed_min -= screen_size_x / 1000
                mouse_speed_max -= screen_size_x / 1000
        mouse_move = random_range(mouse_speed_min ,mouse_speed_max) # movement randomizing:

        x += int(math.sin(angle) * mouse_move)
        y += int(math.cos(angle) * mouse_move)
        pyautogui.moveTo(x, y, _pause=False) # moves with angle to Destination

        if(abs(destination_x - x) < ARRIVAL_DISTANCE and abs(destination_y - y) < ARRIVAL_DISTANCE): # jumps to the end when close:
            pyautogui.moveTo(destination_x, destination_y)
            x = destination_x
            y = destination_y

        mouse_pause = random_range(0.005, 0.02)
        time.sleep(mouse_pause)

mouse(1000, 1000)