##################################################
# Controller C
# 4 arcade style buttons
# each button sends a single keypress, and holding down a button 
# does not repeat the keypress, or prevent another button from being pressed.
# 
# Button mapping:
# TL: E
# TR: F
# BL: G
# BR: H



import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

# keymaps
start_key = Keycode.E
stop_key = Keycode.F
reset_24_key = Keycode.G
reset_14_key = Keycode.H

# pin setups
start = digitalio.DigitalInOut(board.GP0)
start.direction = digitalio.Direction.INPUT
start.pull = digitalio.Pull.UP
start_switch_state = 0

stop = digitalio.DigitalInOut(board.GP1)
stop.direction = digitalio.Direction.INPUT
stop.pull = digitalio.Pull.UP
stop_switch_state = 0


reset_24 = digitalio.DigitalInOut(board.GP2)
reset_24.direction = digitalio.Direction.INPUT
reset_24.pull = digitalio.Pull.UP
reset_24_switch_state = 0

reset_14 = digitalio.DigitalInOut(board.GP3)
reset_14.direction = digitalio.Direction.INPUT
reset_14.pull = digitalio.Pull.UP
reset_14_switch_state = 0

# initial status for start/stop keys
start_status = 0
stop_status = 0

# the loop
while True:
    # if start_status == 0:
    #     if not start.value:
    #         kbd.send(start_key)
    #         #print("timer started")
    #         start_status = 1
    #         stop_status = 0
    if start_switch_state == 0:
        if not start.value:
            kbd.press(start_key)
            kbd.release(start_key)
            start_switch_state = 1

    if start_switch_state == 1:
        if start.value:
            kbd.release(start_key)
            start_switch_state = 0

    # if stop_status == 0:
    #     if not stop.value:
    #         kbd.send(stop_key)
    #         #print("timer stopped")
    #         stop_status = 1
    #         start_status = 0
    if stop_switch_state == 0:
        if not stop.value:
            kbd.press(stop_key)
            kbd.release(stop_key)
            stop_switch_state = 1

    if stop_switch_state == 1:
        if stop.value:
            kbd.release(stop_key)
            stop_switch_state = 0

    # reset_24
    if reset_24_switch_state == 0:
        if not reset_24.value:
            kbd.press(reset_24_key)
            kbd.release(reset_24_key)
            reset_24_switch_state = 1

    if reset_24_switch_state == 1:
        if reset_24.value:
            kbd.release(reset_24_key)
            reset_24_switch_state = 0

    # reset_14
    if reset_14_switch_state == 0:
        if not reset_14.value:
            kbd.press(reset_14_key)
            kbd.release(reset_14_key)
            reset_14_switch_state = 1

    if reset_14_switch_state == 1:
        if reset_14.value:
            kbd.release(reset_14_key)
            reset_14_switch_state = 0

    # debounce
    time.sleep(0.01)
