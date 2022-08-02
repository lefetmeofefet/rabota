import pyautogui
import keyboard

start_pressed = False
while not start_pressed:
    start_pressed = keyboard.is_pressed('x')

monitor_size = pyautogui.size()

scale_amount = min(monitor_size[0] / 800, monitor_size[1] / 600)
game_window_size = (int(800 * scale_amount), int(600 * scale_amount))

pyautogui.moveTo(monitor_size.width // 2 -
                 game_window_size[0] // 2, monitor_size.height // 2 - game_window_size[1] // 2)
