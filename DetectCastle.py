from turtle import Screen
import pyautogui
import keyboard
import cv2
import numpy as np
import mss

monitor_size = pyautogui.size()

scale_amount = min(monitor_size[0] / 800, monitor_size[1] / 600)
game_window_size = (int(800 * scale_amount), int(600 * scale_amount))
game_window_start = (monitor_size.width // 2 -
                     game_window_size[0] // 2, monitor_size.height // 2 - game_window_size[1] // 2)

entrance_purple_color = np.array([122, 29, 133])


def detect_purple_blob(frame, tolerance):

    frame = cv2.GaussianBlur(frame, (7, 7), 0)
    lower_purple = entrance_purple_color - \
        np.array([tolerance, tolerance, tolerance])
    upper_purple = entrance_purple_color + \
        np.array([tolerance, tolerance, tolerance])
    mask = cv2.inRange(frame, lower_purple, upper_purple)
    return mask


def get_castle_entrance_mask(frame, tolerance):
    purple_mask = detect_purple_blob(frame, tolerance)
    entrances, _ = cv2.findContours(
        purple_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # draw entrances
    for entrance in entrances:
        cv2.drawContours(frame, [entrance], -1, (0, 255, 0), 2)

    return purple_mask


def get_castle_entrance_position(frame, tolerance):
    purple_mask = get_castle_entrance_mask(frame, tolerance)
    entrances, _ = cv2.findContours(
        purple_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # there should only be one contour
    contour = entrances[0]
    return contour


start_pressed = False
while not start_pressed:
    start_pressed = keyboard.is_pressed('x')

with mss.mss() as sct:
    monitor = {"top": game_window_start[1], "left": game_window_start[0],
               "width": game_window_size[0], "height": game_window_size[1]}

    screen = np.array(sct.grab(monitor))
    screen = cv2.cvtColor(screen, cv2.COLOR_RGBA2RGB)
    entrance = get_castle_entrance_mask(screen, 10)

    psoition = get_castle_entrance_position(screen, 10)
    qwer = cv2.drawContours(screen, [psoition], -1, (0, 255, 0), 2)

    cv2.imshow('entrance', qwer)
    cv2.waitKey(0)
