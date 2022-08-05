import pyautogui
import time


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


time.sleep(1)
wp = find_wp_on_minimap()
if wp is None:
    print("Shit")
if wp is not None:
    print(wp.x, wp.y)
    pyautogui.moveTo(wp.x, wp.y)
