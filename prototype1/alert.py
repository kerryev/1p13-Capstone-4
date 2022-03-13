import pyautogui

def menu():
    pyautogui.alert(
        'Hello! These are the commands used to control your cursor:' '\
    1 - Cursor Up' '\
    2 - Cursor Down' '\
    3 - Cursor Right' '\
    4 - Cursor Left' '\
    5 - Click' '\
    6 - Scroll Up' '\
    7 - Scroll Down')
