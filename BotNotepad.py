#pyautogui - cap location on object in to x , y
'''
1. find positon of notepad file 1 and 2.
2. click to notepad file 1 then type message
3. click to notepad file 2 
4. copy mesaage to clipboard.
5. hit key ctrl+v
'''

'''
1. Find positon of notepad file 1 and 2.
Open IDLE 
    import pyautogui as pg
    pg.position()
        Result position of file 1 >> Point(x=1550, y=308)
    pg.position()
        Result position of file 2 >> Point(x=1385, y=106)

'''

import pyautogui as pg
import time #to delay program 

time.sleep(5) # stall program in second
pg.click(1550 , 308) # click on position as file 1