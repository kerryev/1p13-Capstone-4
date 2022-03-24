import pyautogui
import datetime


def start():
    pyautogui.alert(
        'Hello! These are the commands used to control your cursor:' '\
    1: Cursor Up.' '\
    2: Cursor Down.' '\
    3: Cursor Right.' '\
    4: Cursor Left.' '\
    5: Click.')


def get_date():

    print('Accessed:', datetime.datetime.now())  # Finds date/time
    print('')


def cursor_selection(i):
    up = str(b'BUTTON 1 WAS PRESSED\r\n')
    down = str(b'BUTTON 2 WAS PRESSED\r\n')
    right = str(b'BUTTON 3 WAS PRESSED\r\n')
    left = str(b'BUTTON 4 WAS PRESSED\r\n')
    click = str(b'BUTTON 5 WAS PRESSED\r\n')
    if i == up:
        pyautogui.moveRel(0, -25)  # Cursor Moves up
    elif i == down:
        pyautogui.moveRel(0, 25)  # Cursor moves down
    elif i == right:
        pyautogui.moveRel(25, 0)  # Cursor moves right
    elif i == left:
        pyautogui.moveRel(-25, 0)  # Cursor moves left
    elif i == click:
        pyautogui.click()  # Click
    else:
        print('No possible movement')
    get_date()
