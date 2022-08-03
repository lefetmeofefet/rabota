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
        create_button_unpressed = pyautogui.locateCenterOnScreen(images_folder + "create_unpressed.png",)
        if create_button_unpressed is not None:
            utytilities.move_mouse(create_button_unpressed.x, create_button_unpressed.y)
            time.sleep(0.2)
            utytilities.mouse_click()
            create_button_pressed = pyautogui.locateCenterOnScreen(images_folder + "create_pressed.png")
            if create_button_pressed is not None:
                create_window = True
        time.sleep(0.4)

    #write the game name:z
    game_name = pyautogui.locateCenterOnScreen(images_folder + "game_name.png")
    utytilities.move_mouse(game_name.x + utytilities.random_range(-2, 6), game_name.y + 25 * utytilities.MOUSE_SPEED_ACCELERATION)
    utytilities.mouse_click()
    utytilities.backspace(utytilities.random_range(10, 13))
    utytilities.mouse_click(utytilities.write_text(utytilities.create_run_name()))

    #add password if we want!!

    create_game_button = pyautogui.locateCenterOnScreen(images_folder + "create_game_button.png")
    utytilities.move_mouse(create_game_button.x, create_game_button.y)
    utytilities.mouse_click()
# for i in range(100):
#     print(utytilities.create_run_name())

# tower_entrance = pyautogui.locateCenterOnScreen(images_folder + "tower_entrance.png", confidence = 0.9)
# utytilities.move_mouse(tower_entrance.x, tower_entrance.y)
enter_game()