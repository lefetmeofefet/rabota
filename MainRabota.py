import time
import math
import random
import pyautogui


def random_range(minimum, maximum):
    num1 = random.random()
    num1 += minimum
    num1 *= (maximum - minimum)
    return num1


MIN_WRITE_DELAY = 0.1
MAX_WRITE_DELAY = 0.6


def write_text(text):
    for letter in text:
        pyautogui.typewrite(letter, _pause=False)
        time_to_sleep = random_range(MIN_WRITE_DELAY, MAX_WRITE_DELAY)
        time.sleep(time_to_sleep * time_to_sleep)


def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))


SCREEN_SIZE_X, SCREEN_SIZE_Y = pyautogui.size()
ARRIVAL_DISTANCE = 10
ANGLE_MAX_ERROR = 0.4
ANGLE_OVERALL_CURVE = 0.15
MOUSE_SPEED_RANDOM_MIN = SCREEN_SIZE_X * 0.005
MOUSE_SPEED_RANDOM_MAX = SCREEN_SIZE_X * 0.006
MOUSE_SPEED_ACCELERATION = SCREEN_SIZE_X * 0.0005
MOUSE_SPEED_MIN = SCREEN_SIZE_X * 0.00125


def mouse(destination_x, destination_y):
    mouse_speed_min = MOUSE_SPEED_RANDOM_MIN
    mouse_speed_max = MOUSE_SPEED_RANDOM_MAX
    x_start,y_start = pyautogui.position()  # current position
    x, y = pyautogui.position()  # current position
    angle_curve = ANGLE_OVERALL_CURVE * (1 if random.random() > 0.5 else -1)
    while x != destination_x and y != destination_y:
        angle = math.atan2(destination_x - x, destination_y - y) # angle randomizing:
        angle_random = random_range(-ANGLE_MAX_ERROR, ANGLE_MAX_ERROR)
        angle += angle_random + angle_curve

        if mouse_speed_min > MOUSE_SPEED_MIN:
            if distance(x, y, x_start, y_start) < distance(x, y, destination_x, destination_y):
                mouse_speed_min += MOUSE_SPEED_ACCELERATION
                mouse_speed_max += MOUSE_SPEED_ACCELERATION
            else:
                mouse_speed_min -= MOUSE_SPEED_ACCELERATION
                mouse_speed_max -= MOUSE_SPEED_ACCELERATION
        mouse_move = random_range(mouse_speed_min, mouse_speed_max) # movement randomizing:

        x += int(math.sin(angle) * mouse_move)
        y += int(math.cos(angle) * mouse_move)
        pyautogui.moveTo(x, y, _pause=False) # moves with angle to Destination

        if abs(destination_x - x) < ARRIVAL_DISTANCE and abs(destination_y - y) < ARRIVAL_DISTANCE:  # jumps to the end when close:
            pyautogui.moveTo(destination_x, destination_y)
            x = destination_x
            y = destination_y

        mouse_pause = random_range(0.005, 0.02)
        time.sleep(mouse_pause)

mouse(1000, 1000)