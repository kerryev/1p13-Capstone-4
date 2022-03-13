import pyautogui
# pyautogiu is a downloadable library that has access to cursor controls and commmands
from alert import menu


def cursor_selection(i):
    if i == '1':
        print(pyautogui.moveRel(0, -100))  # Up
    elif i == '2':
        pyautogui.moveRel(0, 100)  # Down
    elif i == '3':
        pyautogui.moveRel(100, 0)  # Right
    elif i == '4':
        pyautogui.moveRel(-100, 0)  # Left
    elif i == '5':
        pyautogui.click()  # Click
    elif i == '6':
        pyautogui.scroll(700)  # Scroll up
    elif i == '7':
        pyautogui.scroll(-700)  # Scroll down
    elif i == '8':
        menu()

    else:
        return('No possible movement')


while True:
    try:
        button_ID = input('Select Button: ')
        print(cursor_selection(button_ID))
    except RuntimeError as error:
        print(error.args[0])
        continue
    except Exception as error:
        raise error
