import utytilities
import pyautogui
import time
import socket

computer_name = socket.gethostname()
print(computer_name)
images_folder = {
    "Rambo": "images/darvid/",
    "DESKTOP-N349C6N": "images/shlombif/",
    # SHLORMO and YOTAM add yours
}[computer_name]


def enter_game():
    create_window = False
    window = []
    while len(window) == 0 or not window[0].isActive:
        window = pyautogui.getWindowsWithTitle('Diablo II: Resurrected')
        time.sleep(0.5)
    window = window[0]

    create_button_pressed = pyautogui.locateCenterOnScreen(images_folder + "create_pressed.png")
    if create_button_pressed is not None:
        create_window = True

    while not create_window:
        creat_button_unpressed = pyautogui.locateCenterOnScreen(images_folder + "create_unpressed.png",)
        if creat_button_unpressed is not None:
            utytilities.move_mouse(creat_button_unpressed.x, creat_button_unpressed.y)
            time.sleep(0.2)
            utytilities.mouse_click()
            create_button_pressed = pyautogui.locateCenterOnScreen(images_folder + "create_pressed.png")
            if create_button_pressed is not None:
                create_window = True
        time.sleep(0.4)




enter_game()