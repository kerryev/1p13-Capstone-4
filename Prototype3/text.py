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
    if i == 0:
        pyautogui.moveRel(0, -100)  # Cursor moves up1
    elif i == 1:
        pyautogui.moveRel(0, 100)  # Cursor moves down
    elif i == 2:
        pyautogui.moveRel(100, 0)  # Cursor moves right
    elif i == 3:
        pyautogui.moveRel(-100, 0)  # Cursor moves left
    elif i == 4:
        pyautogui.click()  # Click
    else:
        print('No possible movement')

    get_date()
