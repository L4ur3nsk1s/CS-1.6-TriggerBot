from ahk import AHK
import time
import pyautogui
from ahk.window import Window


ahk = AHK()

W, H = pyautogui.size()


center = (W/2, H/2)

centerx_m10, centery_m10 = (center[0] - 10, center[1] - 10)

centerx_p10, centery_p10 = (center[0] + 10, center[1] + 10)


up = (centerx_m10, centery_m10)
down = (centerx_p10, centery_p10)


color = ahk.pixel_search('0xe2c08d', upper_bound=up, lower_bound=down)

print(color, up, down, center)
