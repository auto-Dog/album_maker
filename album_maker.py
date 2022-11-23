import pyautogui
import time

pyautogui.confirm('Put mouse on where you click to roll the page.')
time.sleep(1)
currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
roll_loca = [currentMouseX, currentMouseY]

pyautogui.confirm('Now specify the screen shot region.\n\
(+)----  \n\
        \n\
 -----+ \n\
We need you first put mouse on left-top point ')
time.sleep(2)
currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
lt_loca = [currentMouseX, currentMouseY]

pyautogui.confirm('Now specify the screen shot region.\n\
+-----  \n\
        \n\
----(+) \n\
We need you then put mouse on right-bottom point ')
time.sleep(2)
currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
rb_loca = [currentMouseX, currentMouseY]

num_page = pyautogui.prompt('Input total clicks (e.g. 2)')
num_page = eval(num_page)

print(num_page)
time.sleep(0.5)
for i in range(num_page):
    im_test = pyautogui.screenshot(region=(lt_loca[0], lt_loca[1], rb_loca[0]-lt_loca[0], rb_loca[1]-lt_loca[1]))
    im_test.save('./image/'+ "{0:03d}".format(i)+'.png')
    pyautogui.click(x=roll_loca[0],y=roll_loca[1])
    time.sleep(1)
