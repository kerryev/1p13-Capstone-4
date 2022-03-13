import pyautogui
import datetime


def menu():
    pyautogui.alert(
        'Hello! These are the commands used to control your cursor:' '\
    1 - Cursor Up' '\
    2 - Cursor Down' '\
    3 - Cursor Right' '\
    4 - Cursor Left' '\
    5 - Click')


def get_date():

    print('Accessed:', datetime.datetime.now())  # Finds date/time
    print('')
