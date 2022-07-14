import time

import pyautogui

# Screen size
print(pyautogui.size())

# Mouse position
print(pyautogui.position())

# Finding a window and its location and wait until it's active
window = []
while len(window) == 0 or not window[0].isActive:
    window = pyautogui.getWindowsWithTitle('Untitled - Notepad')
    time.sleep(0.5)
window = window[0]

# Moves to center of the notepad and types some texts
pyautogui.moveTo(window.centerx, window.centery)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.typewrite("I AM TEXT BITCH")

