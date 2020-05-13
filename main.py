from ahk import AHK
import time
import pyautogui
from ahk.window import Window

ahk = AHK()
colors_t = ['new colors']
colors_ct = ['new colors']

W, H = pyautogui.size()

top_left = (679, 380)
bottom_right = (687, 388)

win = ahk.active_window

mouse_position = ahk.mouse_position

center = (W/2, H/2)

centerx = center[0]
centery = center[1]

team = 1  # Search for Terrorist colors
# team = 0 #Search for Counter Terrorist colors

pixel_search = ahk.pixel_search(
    colors_t, upper_bound=top_left, lower_bound=bottom_right)

pixel_get_color_center = ahk.pixel_get_color(center[0], center[1])


currentMouseX, currentMouseY = pyautogui.position()

# Using while 10 to not get infinite loop
i = 10
while 10 > 0:
    i = i - 1
    pixel_get_color_center = ahk.pixel_get_color(center[0], center[1])
    pixel_search = ahk.pixel_search(
        colors_t, upper_bound=top_left, lower_bound=bottom_right)
if pixel_search == colors_t:
    print(pixel_get_color_center)
    ahk.sound_beep(frequency=880, duration=100)
    ahk.click()
