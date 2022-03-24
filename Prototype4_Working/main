# Evan Kerr
# kerre10
# Thurs-42
# -----------------------------------------------------------

# REFINED CODE 3

from alert import start, cursor_selection
import serial
from serial import Serial

ser = serial.Serial('COM3', 9600)

# Pyautogiu is a downloadable library that has access
# to cursor controls and commmands (ie. click, scroll, etc.)

# Serial is a common API ised to read serial outputs from an arduino.

# ------------------------------------------------------------


start()

while True:
    try:
        # Reads line from serial output
        ser_bytes = str(ser.readline(1000))
        # Puts this value into a reaedable format
        cursor_selection(ser_bytes)

    except RuntimeError as error:
        continue
