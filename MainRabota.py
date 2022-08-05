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
    create_button_pressed = pyautogui.locateCenterOnScreen(images_folder + "create_pressed.png")
    if create_button_pressed is not None:
        create_window = True

    while not create_window:
        create_button_unpressed = utytilities.wait_until_found(images_folder + "create_unpressed.png", )
        utytilities.move_mouse(create_button_unpressed.x, create_button_unpressed.y)
        time.sleep(0.2)
        utytilities.mouse_click()
        create_window = True

    # write the game name: (starts with countess1 always)
    game_name = utytilities.wait_until_found(images_folder + "game_name.png")
    utytilities.move_mouse(game_name.x + utytilities.random_range(-2, 6),
                           game_name.y + 25 * utytilities.MOUSE_SPEED_ACCELERATION)
    utytilities.mouse_click()
    utytilities.backspace(10)
    utytilities.write_text(utytilities.get_game_name())

    # add password if we want!!
    # add password if we want!!
    # add password if we want!!

    create_game_button = utytilities.wait_until_found(images_folder + "create_game_button.png")
    utytilities.move_mouse(create_game_button.x, create_game_button.y)
    utytilities.mouse_click()


def city():
    utytilities.wait_until_found(images_folder + "new_graphic_barrel.png", confidence=0.9)
    utytilities.write_text('g')  # old graphics

    city_chest = utytilities.wait_until_found(images_folder + "city_chest.png", confidence=0.9)
    utytilities.move_mouse(city_chest.x, city_chest.y)
    utytilities.mouse_click()


# for i in range(100):
#     print(utytilities.create_run_name())

# tower_entrance = pyautogui.locateCenterOnScreen(images_folder + "tower_entrance.png", confidence = 0.9)
# utytilities.move_mouse(tower_entrance.x, tower_entrance.y)


enter_game()
city()
