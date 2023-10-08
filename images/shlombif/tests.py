import pyautogui
import time


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y



def test():
    screenshot = pyautogui.screenshot()

    wall_colors1 = [
        (100, 100, 100),
        (100, 90, 79),
        (66, 61, 48),
    ]
    # wall_colors2 = [
    #     (66, 61, 48),
    #
    # ]

    # Maybe for crossroads indicator (11, 1, 0),
    # Maybe (74, 68, 63),

    # screenshot.remap_palette()
    for x in range(screenshot.width):
        for y in range(screenshot.height):
            pixel = screenshot.getpixel((x, y))
            if pixel in wall_colors1:
                screenshot.putpixel((x, y), (255, 255, 255))
            # elif pixel in wall_colors2:
            #     screenshot.putpixel((x, y), (0, 255, 0))
            else:
                screenshot.putpixel((x, y), (0, 0, 0))
                # screenshot.putpixel((x, y), (pixel[0] // 4, pixel[1] // 4, pixel[2] // 4))
    screenshot.save("test.png")



time.sleep(1)
test()