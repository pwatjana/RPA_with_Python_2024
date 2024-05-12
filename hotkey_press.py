#pyautogui - cap location on object in to x , y
'''https://pyautogui.readthedocs.io/en/latest/'''
'''
Tasks
1. find positon of notepad file 1 and 2.
2. click to notepad file 1 then type message
3. click to notepad file 2 
4. copy mesaage to clipboard.
5. hit key ctrl+v
'''

'''
Find positon of notepad file 1 and 2.
Open IDLE 
    import pyautogui as pg
    pg.position()
        Result position of file 1 >> Point(x=1550, y=308)
    pg.position()
        Result position of file 2 >> Point(x=1385, y=106)

'''

import pyautogui as pg
import time #to delay program 
import pyperclip 

time.sleep(3) # stall program in second
pg.click('notepad1.png') #click as screen capture but need to install packlage pillow. and picture file need to locate within same folder of .py
time.sleep(3)
pg.move(150,100) # move mouse by fix x,y pixel from current location.
#pg.click(1550 , 308) # click on position as file 1, after run cursor will appear on selected (x,y)
time.sleep(0.5)
pg.write('Hello world\n', interval=0.25)#to write in english need to select language bar=english.


#Cannot use pg.write with other languages
#To type in Thai language,use pyperclip to copy thai text and use .hotkey() to apply ctrl+v key to paste value instead.
pyperclip.copy('สวัสดี')
pg.click(1385 , 106)
pg.hotkey('ctrl','v')
pg.press('enter')

'''
add new line can apply '\n' like file 1 or pg.press('enter') in file 2
pyautogui need to be careful on screen resolution, need to check or set environment.
'''