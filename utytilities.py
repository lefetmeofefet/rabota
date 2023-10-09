import math
import random
import socket
import time

import pyautogui

computer_name = socket.gethostname()
print(computer_name)


class Settings:
    def __init__(self, images_folder, wp_mirror_pixel_distance, window_title_height, life_pixels):
        self.images_folder = images_folder
        self.wp_mirror_pixel_distance = wp_mirror_pixel_distance
        self.window_title_height = window_title_height
        self.life_pixels = life_pixels


settings = {
    "Rambo": Settings(
        images_folder="images/darvid/",
        wp_mirror_pixel_distance=9,
        window_title_height=38,
        life_pixels=[(x, 847) for x in range(570, 630)]
    ),
    "HACKT": Settings(
        images_folder="images/shlombif/",
        wp_mirror_pixel_distance=17,
        window_title_height=0,
        life_pixels=[(x, 1320) for x in range(600, 661)]
    ),
}[computer_name]

COUNTESS_NAMES = ["countess", "count", "county", "countnum", "countrun", "keyss", "lefet"]
COUNTESS_MIN_RUNS = 10
COUNTESS_MAX_RUNS = 25

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


def calculate_new_coordinates(x, y, angle_rad, distance):
    new_x = x + distance * math.cos(angle_rad)
    new_y = y + distance * math.sin(angle_rad)
    return new_x, new_y


def convert_minimap_coordinates_to_game(point, should_limit_to_window=False):
    my_location = count_run.window.center
    minimap_distance_multiplier = 10  # Approx lol
    half_character_height = count_run.window.height * 0.05
    left_offset = count_run.window.width * 0.03
    game_coordinates = Point(
        my_location.x + (point.x - my_location.x) * minimap_distance_multiplier - left_offset,
        my_location.y + (point.y - my_location.y) * minimap_distance_multiplier - half_character_height
    )

    # Limit teleport destination so it won't be out of the diablo window
    if should_limit_to_window:
        max_radius = count_run.window.height * 0.4  # Tweak this maybe
        diffx = (game_coordinates.x - my_location.x)
        diffy = (game_coordinates.y - my_location.y)
        if diffx * diffx + diffy * diffy > max_radius * max_radius:
            angle = math.atan2(diffy, diffx)
            game_coordinates = Point(
                my_location.x + max_radius * math.cos(angle),
                my_location.y + max_radius * math.sin(angle)
            )
    return game_coordinates


def is_shade_of_red_or_green(color):
    # Define threshold values for red, green, and blue components
    red_threshold_red = 80  # You can adjust this value based on your requirement
    green_threshold_red = 10  # You can adjust this value based on your requirement
    blue_threshold_red = 10  # You can adjust this value based on your requirement

    red_threshold_green = 35  # You can adjust this value based on your requirement
    green_threshold_green = 90  # You can adjust this value based on your requirement
    blue_threshold_green = 10  # You can adjust this value based on your requirement

    # Extract RGB components from the color tuple
    red, green, blue = color

    # Check if the color is a shade of red based on thresholds
    if red > red_threshold_red and green < green_threshold_red and blue < blue_threshold_red or \
            red < red_threshold_green and green > green_threshold_green and blue < blue_threshold_green:
        return True
    else:
        return False


def check_life():
    screenshot = pyautogui.screenshot()
    sum_red = 0
    sum_green = 0
    sum_blue = 0
    for life_pixel in settings.life_pixels:
        pixel_color = screenshot.getpixel(life_pixel)
        sum_red += pixel_color[0]
        sum_green += pixel_color[1]
        sum_blue += pixel_color[2]
        # print(pixel_color)
    length = len(settings.life_pixels)
    color = (sum_red / length, sum_green / length, sum_blue / length)
    return is_shade_of_red_or_green(color)


def wait_until_found(image_name, confidence=1, timeout_seconds=None, check_interval=0.5):
    print(f"Looking for {image_name}")
    total_seconds = 0
    while timeout_seconds is None or total_seconds < timeout_seconds or timeout_seconds == 0:
        location = pyautogui.locateCenterOnScreen(settings.images_folder + image_name, confidence=confidence)
        if location is not None:
            print(f"Found {image_name} at {location}")
            return location
        if timeout_seconds == 0:
            break
        time.sleep(check_interval)
        total_seconds += check_interval
    print(f"Didn't find {image_name}")


def find_and_click(image_name, confidence=1, timeout_seconds=None, check_interval=0.5):
    if timeout_seconds == 0:
        location = pyautogui.locateCenterOnScreen(settings.images_folder + image_name, confidence=confidence)
    else:
        location = wait_until_found(image_name, confidence, timeout_seconds, check_interval)
    if location is None:
        return
    move_mouse(location.x, location.y)
    sleep(0.1)
    mouse_click()
    return True


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


def show_items():
    pyautogui.keyDown('alt', _pause=False)
    time.sleep(random_range(0.05, 0.2))
    pyautogui.keyUp('alt', _pause=False)
    time.sleep(random_range(0.05, 0.2))


def write_text(text):
    for letter in text:
        pyautogui.keyDown(letter, _pause=False)
        time.sleep(random_range(0.1, 0.4))
        pyautogui.keyUp(letter, _pause=False)
        time_to_sleep = random_range(0.1, 0.3)
        time.sleep(time_to_sleep * time_to_sleep)


def mouse_click(location=None, is_right_click=False):
    if location is not None:
        move_mouse(location.x, location.y)
    time_to_sleep = random_range(0.01, 0.05)
    pyautogui.mouseDown(_pause=False, button=pyautogui.SECONDARY if is_right_click else pyautogui.PRIMARY)
    time.sleep(time_to_sleep)
    pyautogui.mouseUp(_pause=False, button=pyautogui.SECONDARY if is_right_click else pyautogui.PRIMARY)


def mouse_down(is_right_click=False):
    pyautogui.mouseDown(_pause=False, button=pyautogui.SECONDARY if is_right_click else pyautogui.PRIMARY)


def mouse_up(is_right_click=False):
    pyautogui.mouseUp(_pause=False, button=pyautogui.SECONDARY if is_right_click else pyautogui.PRIMARY)


def sleep(sleepy_time, random_min=0.05, random_max=0.15):
    time.sleep(sleepy_time + random_range(random_min, random_max))


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

        mouse_pause = random_range(0.005, 0.01)
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
