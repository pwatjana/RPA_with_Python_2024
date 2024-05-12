'''
Task
1.Open web browser'google'
2.search country infomation
3. capture screen and save to picture in to RPA_with_python_2024.

'''
import pyautogui as pg
import webbrowser
import pyperclip
import time

webbrowser.open_new('https://www.google.com')
time.sleep(2)

pyperclip.copy('เกาหลีใต้')
pg.hotkey('ctrl', 'v')
time.sleep(3)
pg.press('enter')
time.sleep(3)
pg.screenshot('south_korea.png')

for i in range(1,4):
    pg.scroll(-500 * i) #need to position mouse above website
    pg.screenshot('south_korea' +str(i) + '.png')
    time.sleep(3)