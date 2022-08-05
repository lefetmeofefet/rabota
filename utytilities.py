import time
import math
import random
import pyautogui

import socket

computer_name = socket.gethostname()
print(computer_name)


class Settings:
    def __init__(self, images_folder, wp_mirror_pixel_distance, window_title_height):
        self.images_folder = images_folder
        self.wp_mirror_pixel_distance = wp_mirror_pixel_distance
        self.window_title_height = window_title_height


settings = {
    "Rambo": Settings(
        images_folder="images/darvid/",
        wp_mirror_pixel_distance=9,
        window_title_height=38
    ),
    "DESKTOP-N349C6N": Settings(
        images_folder="images/shlombif/",
        wp_mirror_pixel_distance=17,
        window_title_height=0,
    ),
}[computer_name]

COUNTESS_NAMES = ["countess", "count", "county", "countnum", "countrun"]
COUNTESS_MIN_RUNS = 10
COUNTESS_MAX_RUNS = 20

SCREEN_SIZE_X, SCREEN_SIZE_Y = pyautogui.size()
ARRIVAL_DISTANCE = 10
ANGLE_MAX_ERROR = 0.4
ANGLE_OVERALL_CURVE = 0.15
MOUSE_SPEED_RANDOM_MIN = SCREEN_SIZE_X * 0.005
MOUSE_SPEED_RANDOM_MAX = SCREEN_SIZE_X * 0.006
MOUSE_SPEED_ACCELERATION = SCREEN_SIZE_X * 0.0005
MOUSE_SPEED_MIN = SCREEN_SIZE_X * 0.00125


class CountRun:
    count_num = 1
    count_name = 0
    toolbar_height = settings.window_title_height

    def __init__(self):
        self.window = None

    def wait_for_diablo_window(self):
        window = []
        while len(window) == 0 or not window[0].isActive:
            window = pyautogui.getWindowsWithTitle('Diablo II: Resurrected')
            time.sleep(0.5)
        self.window = window[0]

    def generate_game_name(self):
        count_num = self.count_num
        count_name = COUNTESS_NAMES[self.count_name]
        run_name = count_name + str(count_num)

        if count_num == COUNTESS_MAX_RUNS:
            self.count_num = 1
            temp_num = self.count_name
            while temp_num == self.count_name:
                self.count_name = int(random_range(0, 4))
        elif count_num >= COUNTESS_MIN_RUNS and int(random_range(1, 10)) == 10:
            self.count_num = 1
            temp_num = self.count_name
            while temp_num == self.count_name:
                self.count_name = int(random_range(0, 4))
        else:
            self.count_num += 1

        return run_name


count_run = CountRun()


def wait_until_found(image_name, confidence=1):
    image = None
    while image is None:
        image = pyautogui.locateCenterOnScreen(settings.images_folder + image_name, confidence=confidence)
        if image is not None:
            return image
        time.sleep(0.5)


def find_and_click(image_name, confidence=1):
    wp = wait_until_found(image_name, confidence)
    move_mouse(wp.x, wp.y)
    time.sleep(0.2 + random.random() * 0.1)
    mouse_click()


def random_range(minimum, maximum):
    num1 = random.random()
    num1 += minimum
    num1 *= (maximum - minimum)
    return num1


def backspace(num):
    for i in range(num):
        pyautogui.keyDown('backspace', _pause=False)
        time.sleep(random_range(0.05, 0.2))
        pyautogui.keyUp('backspace', _pause=False)
        time.sleep(random_range(0.05, 0.2))


def write_text(text):
    for letter in text:
        pyautogui.keyDown(letter, _pause=False)
        time.sleep(random_range(0.1, 0.4))
        pyautogui.keyUp(letter, _pause=False)
        time_to_sleep = random_range(0.1, 0.3)
        time.sleep(time_to_sleep * time_to_sleep)


def mouse_click(is_right_click=False):
    time_to_sleep = random_range(0.05, 0.2)
    pyautogui.mouseDown(_pause=False, button=pyautogui.SECONDARY if is_right_click else pyautogui.PRIMARY)
    time.sleep(time_to_sleep)
    pyautogui.mouseUp(_pause=False, button=pyautogui.SECONDARY if is_right_click else pyautogui.PRIMARY)


def mouse_down(is_right_click=False):
    pyautogui.mouseDown(_pause=False, button=pyautogui.SECONDARY if is_right_click else pyautogui.PRIMARY)


def mouse_up(is_right_click=False):
    pyautogui.mouseUp(_pause=False, button=pyautogui.SECONDARY if is_right_click else pyautogui.PRIMARY)


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def move_mouse(destination_x, destination_y):
    mouse_speed_min = MOUSE_SPEED_RANDOM_MIN
    mouse_speed_max = MOUSE_SPEED_RANDOM_MAX
    x_start, y_start = pyautogui.position()  # current position
    x, y = pyautogui.position()  # current position
    angle_curve = ANGLE_OVERALL_CURVE * (1 if random.random() > 0.5 else -1)
    while x != destination_x and y != destination_y:
        angle = math.atan2(destination_x - x, destination_y - y)  # angle randomizing:
        angle_random = random_range(-ANGLE_MAX_ERROR, ANGLE_MAX_ERROR)
        angle += angle_random + angle_curve

        if mouse_speed_min > MOUSE_SPEED_MIN:
            if distance(x, y, x_start, y_start) < distance(x, y, destination_x, destination_y):
                mouse_speed_min += MOUSE_SPEED_ACCELERATION
                mouse_speed_max += MOUSE_SPEED_ACCELERATION
            else:
                mouse_speed_min -= MOUSE_SPEED_ACCELERATION
                mouse_speed_max -= MOUSE_SPEED_ACCELERATION
        mouse_move = random_range(mouse_speed_min, mouse_speed_max)  # movement randomizing:

        x += int(math.sin(angle) * mouse_move)
        y += int(math.cos(angle) * mouse_move)
        pyautogui.moveTo(x, y, _pause=False)  # moves with angle to Destination

        if abs(destination_x - x) < ARRIVAL_DISTANCE and abs(
                destination_y - y) < ARRIVAL_DISTANCE:  # jumps to the end when close:
            pyautogui.moveTo(destination_x, destination_y)
            x = destination_x
            y = destination_y

        mouse_pause = random_range(0.005, 0.02)
        time.sleep(mouse_pause)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def find_wp_on_minimap():
    screenshot = pyautogui.screenshot()

    portal_teal = (178, 235, 255)
    portal_white = (212, 255, 255)
    portal_blue = (33, 111, 255)
    parallel_pixel_distance = settings.wp_mirror_pixel_distance

    for x in range(screenshot.width - parallel_pixel_distance):
        for y in range(screenshot.height - 3):
            current_pixel = screenshot.getpixel((x, y))
            portal_height = 0
            if current_pixel == portal_teal:
                is_portal = True
                teals_count = 0
                blues_count = 0
                whites_count = 0
                while current_pixel in [portal_blue, portal_teal, portal_white]:
                    if current_pixel == portal_white:
                        whites_count += 1
                    if current_pixel == portal_blue:
                        blues_count += 1
                    if current_pixel == portal_teal:
                        teals_count += 1
                    portal_height += 1
                    current_pixel = screenshot.getpixel((x, y + portal_height))
                if portal_height < 3 or teals_count == 0 or blues_count == 0 or whites_count == 0:
                    continue
                for height_index in range(portal_height):
                    current_pixel = screenshot.getpixel((x, y + height_index))
                    right_mirror_pixel = screenshot.getpixel((x + parallel_pixel_distance, y + height_index))
                    if current_pixel != right_mirror_pixel:
                        is_portal = False
                        break
                if is_portal:
                    return Point(x + parallel_pixel_distance // 2, y + 2)
