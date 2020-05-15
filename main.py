from ahk import AHK
import time
import pyautogui
from ahk.window import Window

ahk = AHK()
colors_t = [0xFC0404, 0xFC0C04, 0xE10404, 0xCE0404, 0xEC0404, ]
colors_ct = [0x040494, 0x04047F, 0x04044E, 0x040460, 0x040443]

W, H = pyautogui.size()

top_left = (679, 380)
bottom_right = (687, 388)

win = ahk.active_window

mouse_position = ahk.mouse_position

center = (W/2, H/2)

centerx = center[0]
centery = center[1]

win = ahk.find_window(title=b'Condition Zero')
win.activate()

team = 1  # Search for Terrorist colors
# team = 0 #Search for Counter Terrorist colors

pixel_search = ahk.pixel_search(
    colors_t, upper_bound=top_left, lower_bound=bottom_right)

pixel_get_color_center = ahk.pixel_get_color(center[0], center[1])

while team is 0:
    pixel_get_color_center = ahk.pixel_get_color(center[0], center[1])
    pixel_search = ahk.pixel_search(
        colors_t, upper_bound=top_left, lower_bound=bottom_right)
    if pixel_search == colors_t:
        print(pixel_get_color_center)
        ahk.sound_beep(frequency=880, duration=100)
        ahk.click()
