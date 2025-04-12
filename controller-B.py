##################################################
# Controller B
# 4 arcade style buttons
# each button sends a single keypress, and holding down a button 
# does not repeat the keypress, or prevent another button from being pressed.
# 
# Button mapping:
# TL: X
# TR: Y
# BL: V
# BR: Z

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

print("---Pico Pad Keyboard---")

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = True

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

# list of pins to use (skipping GP15 on Pico because it's funky)
pins = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
]

MEDIA = 1
KEY = 2

keymap = {
    (0): (KEY, [Keycode.X]),
    (1): (KEY, [Keycode.Y]),
    (2): (KEY, [Keycode.V]),
    (3): (KEY, [Keycode.Z]),
    (4): (KEY, [Keycode.D]),

}
switches = [0, 1, 2, 3, 4]

for i in range(5):
    switches[i] = DigitalInOut(pins[i])
    switches[i].direction = Direction.INPUT
    switches[i].pull = Pull.UP

switch_state = [0, 0, 0, 0, 0]

while True:
    for button in range(5):
        if switch_state[button] == 0:
            if not switches[button].value:
                try:
                    if keymap[button][0] == KEY:
                        kbd.press(*keymap[button][1])
                        kbd.release(*keymap[button][1])
                    else:
                        cc.send(keymap[button][1])
                except ValueError:  # deals w six key limit
                    pass
                switch_state[button] = 1

        if switch_state[button] == 1:
            if switches[button].value:
                try:
                    if keymap[button][0] == KEY:
                        kbd.release(*keymap[button][1])

                except ValueError:
                    pass
                switch_state[button] = 0

    time.sleep(0.01)  # debounce
