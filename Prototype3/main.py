# Evan Kerr
# kerre10
# Thurs-42
# -----------------------------------------------------------

# REFINED CODE 3

from time import sleep
from text import start, cursor_selection
import serial

ser = serial.Serial('/dev/2022')
ser.flush_Input()

# Pyautogiu is a downloadable library that has access
# to cursor controls and commmands (ie. click, scroll, etc.)

# Serial is a common API ised to read serial outputs from a raspberry pi.

# ------------------------------------------------------------


start()

while True:
    try:
        # Reads line from serial output
        ser_bytes = ser.readline()

        # Puts this value into a reaedable format
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))

        cursor_selection(decoded_bytes)

        sleep(1)

    except RuntimeError as error:
        continue
