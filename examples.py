import time
import utytilities
import pyautogui

print("lefet")
print("lefet")

# Screen size
print(pyautogui.size())

# Mouse position
print(pyautogui.position())

# Finding a window and its location and wait until it's active
# window = []
# while len(window) == 0 or not window[0].isActive:
#     window = pyautogui.getWindowsWithTitle('Untitled - Notepad')
#     time.sleep(0.5)
# window = window[0]

# Moves to center of the notepad and types some texts
# pyautogui.moveTo(window.centerx, window.centery)
# time.sleep(0.5)
# pyautogui.click()
# time.sleep(0.5)
# pyautogui.typewrite("I AM TEXT BITCH")

# Now open calculator
pyautogui.keyDown('winleft')
pyautogui.press('r')
pyautogui.keyUp('winleft')
time.sleep(0.1)
pyautogui.typewrite("calc")
time.sleep(0.1)
pyautogui.press("enter")

time.sleep(3)

# Screenshot
six = pyautogui.locateCenterOnScreen("sex.png",)
utytilities.move_mouse(six.x, six.y)
time.sleep(0.5)
utytilities.mouse_click()
utytilities.mouse_click()
utytilities.mouse_click()