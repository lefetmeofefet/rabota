import pyautogui
import keyboard
import cv2
import numpy as np

# start_pressed = False
# while not start_pressed:
#     start_pressed = keyboard.is_pressed('x')

# monitor_size = pyautogui.size()

# scale_amount = min(monitor_size[0] / 800, monitor_size[1] / 600)
# game_window_size = (int(800 * scale_amount), int(600 * scale_amount))

# pyautogui.moveTo(monitor_size.width // 2 -
#                  game_window_size[0] // 2, monitor_size.height // 2 - game_window_size[1] // 2)

entrance_purple_color = np.array([122, 29, 133])


def detect_purple_blob(frame):
    lower_purple = entrance_purple_color - np.array([10, 10, 10])
    upper_purple = entrance_purple_color + np.array([10, 10, 10])
    mask = cv2.inRange(frame, lower_purple, upper_purple)
    return mask


# save tower.PNG into a frame
frame = cv2.imread('tower.PNG')
frame = detect_purple_blob(frame)


cv2.imshow('frame', frame)
cv2.waitKey(0)
