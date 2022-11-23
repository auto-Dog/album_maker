import pyautogui
import time

num_page = pyautogui.prompt('Input total clicks (e.g. 2)')
num_page = eval(num_page)

print(num_page)
time.sleep(0.5)
im_test = pyautogui.screenshot()
im_test.save('./image/1.png')