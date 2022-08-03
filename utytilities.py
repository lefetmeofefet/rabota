import time
import math
import random
import pyautogui

COUNTESS_NAMES = ["coutess", "count", "county", "countnumber", "countrun"]
COUNTESS_MIN_RUNS = 10
COUNTESS_MAX_RUNS = 20

class count_run:
    count_num = 1
    count_name = 0

def create_run_name():
    count_num = count_run.count_num
    count_name = COUNTESS_NAMES[count_run.count_name]
    run_name = count_name + str(count_num)

    if count_num == COUNTESS_MAX_RUNS:
        count_run.count_num = 1
        temp_num = count_run.count_name
        while temp_num == count_run.count_name:
            count_run.count_name = int(random_range(0, 4))
    elif count_num >= COUNTESS_MIN_RUNS and int(random_range(1, 10)) == 10:
        count_run.count_num = 1
        temp_num = count_run.count_name
        while temp_num == count_run.count_name:
            count_run.count_name = int(random_range(0, 4))
    else:
        count_run.count_num += 1

    return run_name


def random_range(minimum, maximum):
    num1 = random.random()
    num1 += minimum
    num1 *= (maximum - minimum)
    return num1


def write_text(text):
    for letter in text:
        pyautogui.typewrite(letter, _pause=False)
        time_to_sleep = random_range(0.1, 0.6)
        time.sleep(time_to_sleep * time_to_sleep)


def mouse_click(is_right_click=False):
    time_to_sleep = random_range(0.05, 0.2)
    pyautogui.mouseDown(_pause=False, button=pyautogui.SECONDARY if is_right_click else pyautogui.PRIMARY)
    time.sleep(time_to_sleep)
    pyautogui.mouseUp(_pause=False, button=pyautogui.SECONDARY if is_right_click else pyautogui.PRIMARY)


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


def move_mouse(destination_x, destination_y):
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
