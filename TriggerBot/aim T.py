from ahk import AHK
import time
import pyautogui
from ahk.window import Window

ahk = AHK()
colors_t = ['0xA40A04', '0x950804', '0x730404', '0x870404', '0x510504', '0x760404',
            '0x660404',
            '0x370404',
            '0x280404',
            '0x530404']


W, H = pyautogui.size()

top_left = (679, 380)
bottom_right = (687, 388)

win = ahk.active_window

mouse_position = ahk.mouse_position

center = (W/2, H/2)

centerx = center[0]
centery = center[1]

pixel_search = ahk.pixel_search(
    colors_t, upper_bound=top_left, lower_bound=bottom_right)

pixel_get_color_center = ahk.pixel_get_color(center[0], center[1])

pixel_get_mouse_color = ahk.pixel_get_color(
    mouse_position[0], mouse_position[1])
i = 10

currentMouseX, currentMouseY = pyautogui.position()
# win = ahk.find_window(title=b'Counter-Strike') # Find the opened window
# win.activate()

while 10 > 0:
    i = i - 1
    pixel_get_color_center = ahk.pixel_get_color(center[0], center[1])
    print(win)
    pixel_search = ahk.pixel_search(
        colors_t, upper_bound=top_left, lower_bound=bottom_right)
if pixel_search == colors_t:
    print(pixel_get_color_center)

    ahk.sound_beep(frequency=880, duration=100)
    ahk.click()
