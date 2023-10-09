import utytilities
import pyautogui


def enter_game():
    create_window = False
    create_button_pressed = pyautogui.locateCenterOnScreen(
        utytilities.settings.images_folder + "create_pressed.png", )
    if create_button_pressed is not None:
        create_window = True

    while not create_window:
        create_button_unpressed = utytilities.wait_until_found("create_unpressed.png", confidence=0.9)
        utytilities.move_mouse(create_button_unpressed.x, create_button_unpressed.y)
        utytilities.sleep(0.2)
        utytilities.mouse_click()
        create_window = True

    # write the game name: (starts with countess1 always)
    game_name = utytilities.wait_until_found("game_name.png", confidence=0.9)

    utytilities.move_mouse(game_name.x + utytilities.random_range(-2, 6),
                           game_name.y + 25 * utytilities.MOUSE_SPEED_ACCELERATION)
    utytilities.mouse_click()
    utytilities.backspace(10)
    utytilities.write_text(utytilities.count_run.generate_game_name())

    # Password, comment this if you dont want it
    password = utytilities.wait_until_found("password.png", confidence=0.9, time_wait=4)
    utytilities.move_mouse(password.x + utytilities.random_range(-2, 6),
                           password.y + 25 * utytilities.MOUSE_SPEED_ACCELERATION)
    utytilities.mouse_click()
    utytilities.backspace(4)
    utytilities.write_text("1234")

    create_game_button = utytilities.wait_until_found("create_game_button.png", confidence=0.9)
    utytilities.move_mouse(create_game_button.x, create_game_button.y)
    utytilities.mouse_click()


def city():
    utytilities.wait_until_found("new_graphic_barrel.png", confidence=0.9)
    utytilities.write_text('g')  # old graphics

    cast_skills()

    city_chest = utytilities.wait_until_found("city_chest.png", confidence=0.9)
    utytilities.move_mouse(city_chest.x, city_chest.y)
    utytilities.mouse_click()
    utytilities.sleep(3)

    pyautogui.keyDown('esc')
    utytilities.sleep(0.2)
    pyautogui.keyUp('esc')
    utytilities.sleep(0.2)
    pyautogui.keyDown('tab')
    utytilities.sleep(0.2)
    pyautogui.keyUp('tab')


def cast_skills():
    utytilities.write_text('z')
    utytilities.sleep(0.2)
    utytilities.mouse_click(is_right_click=True)
    utytilities.sleep(0.2)
    utytilities.write_text('x')
    utytilities.sleep(0.2)
    utytilities.mouse_click(is_right_click=True)
    utytilities.sleep(0.2)
    utytilities.write_text('e')


def walk_to_portal(walk_duration=2.0):
    utytilities.sleep(0.1)
    utytilities.write_text('g')
    utytilities.sleep(0.2)
    wp_minimap = utytilities.wait_until_found("wp_minimap.png", confidence=0.9)
    # wp_minimap = utytilities.find_wp_on_minimap()
    if wp_minimap is None:
        raise Exception("Shet no wp now we die")
    # centerx = count_run.window.left + count_run.window.width / 2
    # centery = count_run.window.top + (count_run.window.height - count_run.toolbar_height) / 2 + count_run.toolbar_height
    # distance_on_map = utytilities.distance(wp_minimap.x, centerx, wp_minimap.y, centery)
    utytilities.move_mouse(wp_minimap.x, wp_minimap.y)
    utytilities.mouse_down()
    utytilities.sleep(walk_duration)
    # utytilities.sleep(distance_on_map / (400 * utytilities.MOUSE_SPEED_ACCELERATION))
    utytilities.mouse_up()
    utytilities.sleep(1)  # Important cause he keeps running a bit after the mouse is release

    utytilities.sleep(0.1)
    utytilities.write_text('g')
    utytilities.sleep(0.2)


def go_to_portal_and_enter_black_marsh():
    walk_to_portal()

    pyautogui.keyDown('tab')
    utytilities.sleep(0.2)
    pyautogui.keyUp('tab')

    found_wp = utytilities.find_and_click("wp.png", confidence=0.7, timeout_seconds=4)
    if not found_wp:
        walk_to_portal(0.3)
        utytilities.find_and_click("wp.png", confidence=0.7, timeout_seconds=4)
    utytilities.sleep(0.5)
    utytilities.find_and_click("black_marsh_wp.png", confidence=0.9)
    utytilities.sleep(3)
    pyautogui.keyDown('tab')
    utytilities.sleep(0.2)
    pyautogui.keyUp('tab')


def find_tower_entrance_and_enter():
    entered_tower = False
    while not entered_tower:
        tower_entrance_minimap = utytilities.wait_until_found("tower_entrance_minimap.png", confidence=0.9)
        tower_entrance = utytilities.convert_minimap_coordinates_to_game(tower_entrance_minimap, True)

        utytilities.move_mouse(tower_entrance.x, tower_entrance.y)
        utytilities.sleep(0.2)
        utytilities.mouse_click(is_right_click=True)
        utytilities.sleep(0.4)

        entered_tower = utytilities.find_and_click("to_the_forgotten_tower.png", confidence=0.7, timeout_seconds=0.3)


def check_for_runes():
    """ check for runes on the ground and picks them up
    """
    utytilities.show_items()
    rune = utytilities.wait_until_found("rune1.png", confidence=0.8, time_wait=2)
    while rune is not None:
        print(rune.x)
        print(rune.y)
        utytilities.move_mouse(rune.x, rune.y)
        utytilities.mouse_click()
        utytilities.sleep(0.5)
        rune = utytilities.wait_until_found("rune1.png", confidence=0.8, time_wait=2)


def exit_game():
    pyautogui.keyDown('esc')
    utytilities.sleep(0.2)
    pyautogui.keyUp('esc')
    utytilities.sleep(0.2)
    pyautogui.keyDown('enter')
    utytilities.sleep(0.2)
    pyautogui.keyUp('enter')
    utytilities.sleep(0.2)


count_run = utytilities.count_run
count_run.wait_for_diablo_window()

# for i in range(4):
#     enter_game()
#     city()
#     go_to_portal_and_enter_black_marsh()
#     exit_game()

find_tower_entrance_and_enter()

# enter_game()
# city()
# go_to_portal()
# exit_game()


# check_for_runes()

# tower_entrance = pyautogui.locateCenterOnScreen("tower_entrance.png", confidence = 0.9)
# utytilities.move_mouse(tower_entrance.x, tower_entrance.y)
