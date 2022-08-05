import random

import utytilities
import pyautogui
import time


def enter_game():
    create_window = False
    create_button_pressed = pyautogui.locateCenterOnScreen(utytilities.settings.images_folder + "create_pressed.png", )
    if create_button_pressed is not None:
        create_window = True

    while not create_window:
        create_button_unpressed = utytilities.wait_until_found("create_unpressed.png", confidence=0.9)
        utytilities.move_mouse(create_button_unpressed.x, create_button_unpressed.y)
        time.sleep(0.2)
        utytilities.mouse_click()
        create_window = True

    # write the game name: (starts with countess1 always)
    game_name = utytilities.wait_until_found("game_name.png", confidence=0.9)
    utytilities.move_mouse(game_name.x + utytilities.random_range(-2, 6),
                           game_name.y + 25 * utytilities.MOUSE_SPEED_ACCELERATION)
    utytilities.mouse_click()
    utytilities.backspace(10)
    utytilities.write_text(utytilities.count_run.generate_game_name())

    # add password if we want!!
    # add password if we want!!
    # add password if we want!!

    create_game_button = utytilities.wait_until_found("create_game_button.png", confidence=0.9)
    utytilities.move_mouse(create_game_button.x, create_game_button.y)
    utytilities.mouse_click()


def city():
    utytilities.wait_until_found("new_graphic_barrel.png", confidence=0.9)
    utytilities.write_text('g')  # old graphics

    utytilities.write_text('z')
    time.sleep(0.2)
    utytilities.mouse_click(is_right_click=True)
    time.sleep(0.2)
    utytilities.write_text('x')
    time.sleep(0.2)
    utytilities.mouse_click(is_right_click=True)
    time.sleep(0.2)
    utytilities.write_text('e')

    city_chest = utytilities.wait_until_found("city_chest.png", confidence=0.9)
    utytilities.move_mouse(city_chest.x, city_chest.y)
    utytilities.mouse_click()

    pyautogui.keyDown('esc')
    time.sleep(0.2)
    pyautogui.keyUp('esc')

    pyautogui.keyDown('tab')
    time.sleep(0.2)
    pyautogui.keyUp('tab')

    time.sleep(1)


# for i in range(100):
#     print(utytilities.create_run_name())

# tower_entrance = pyautogui.locateCenterOnScreen("tower_entrance.png", confidence = 0.9)
# utytilities.move_mouse(tower_entrance.x, tower_entrance.y)

def go_to_portal():
    wp_minimap = utytilities.find_wp_on_minimap()
    if wp_minimap is None:
        raise Exception("Shet no wp now we die")
    # centerx = count_run.window.left + count_run.window.width / 2
    # centery = count_run.window.top + (count_run.window.height - count_run.toolbar_height) / 2 + count_run.toolbar_height
    utytilities.move_mouse(wp_minimap.x, wp_minimap.y)
    utytilities.mouse_down()
    time.sleep(2 + random.random() * 0.1)
    utytilities.mouse_up()
    time.sleep(1 + random.random() * 0.1)  # Important cause he keeps running a bit after the mouse is release

    pyautogui.keyDown('tab')
    time.sleep(0.2)
    pyautogui.keyUp('tab')

    utytilities.find_and_click("wp.png", confidence=0.9)
    time.sleep(0.5 + random.random() * 0.1)
    utytilities.find_and_click("black_marsh_wp.png", confidence=0.9)

    pyautogui.keyDown('tab')
    time.sleep(0.2)
    pyautogui.keyUp('tab')


count_run = utytilities.count_run
count_run.wait_for_diablo_window()

enter_game()
city()
go_to_portal()

# enter_game()
# city()

# charsi_name = utytilities.wait_until_found("charsi_name.png", confidence = 0.8)
# utytilities.mouse_click()
