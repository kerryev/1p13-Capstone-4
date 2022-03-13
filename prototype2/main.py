# Evan Kerr
# kerre10
# Thurs-42
# -----------------------------------------------------------

import pyautogui
from time import sleep
from alert import menu, get_date
# from RPi.GPIO as GPIO

# Pyautogiu is a downloadable library that has access
# to cursor controls and commmands (ie. click, scroll, etc.)

# Link to follow:
# https://www.google.com/search?q=python+program+which+returns+what+pin+is+located+on+a+button&rlz=1C1CHBF_enCA919CA91
# 9&oq=python+program+which+returns+what+pin+is+located+on+a+button&aqs=chrome..69i57.14562j0j7&sourceid=chrome&ie=UTF-8#kpvalbx=_3F8tYsbtG-TptQbnlL-gBQ54

# ------------------------------------------------------------


def get_input(inputs):  # Input from pins

    #button1 = 25
    #button2 = 20
    #button3 = 15
    #button4 = 10
    #button5 = 5

    #GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    #GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_UP)

    #input1 = GPIO.input(button1)
    # inputs.append(input1)

    #input2 = GPIO.input(button2)
    # inputs.append(input2)

    #input3 = GPIO.input(button3)
    # inputs.append(input3)

    #input4 = GPIO.input(button4)
    # inputs.append(input4)

    #input5 = GPIO.input(button5)
    # inputs.append(input5)

    return inputs


def check_input(inputs):
    for i in inputs:
        if i == 0:
            return (inputs.index(i) + 1)
        else:
            continue


def cursor_selection(i):
    if i == 1:
        pyautogui.moveRel(0, -100)  # Cursor moves up
    elif i == 2:
        pyautogui.moveRel(0, 100)  # Cursor moves down
    elif i == 3:
        pyautogui.moveRel(100, 0)  # Cursor moves right
    elif i == 4:
        pyautogui.moveRel(-100, 0)  # Cursor moves left
    elif i == 5:
        pyautogui.click()  # Click
    else:
        print('No possible movement')

    get_date()


def main():

    menu()

    while True:

        inputs = [0, 1, 1, 1, 1]

        try:
            get_input(inputs)
            button_ID = check_input(inputs)
            cursor_selection(button_ID)

            sleep(1)

        except RuntimeError as error:

            continue


main()
