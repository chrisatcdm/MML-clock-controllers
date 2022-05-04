import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

# keymaps
start_key = Keycode.A
stop_key = Keycode.A
reset_24_key = Keycode.B
reset_14_key = Keycode.C
horn_key = Keycode.D

# pin setups
start = digitalio.DigitalInOut(board.GP0)
start.direction = digitalio.Direction.INPUT
start.pull = digitalio.Pull.UP

stop = digitalio.DigitalInOut(board.GP1)
stop.direction = digitalio.Direction.INPUT
stop.pull = digitalio.Pull.UP

reset_24 = digitalio.DigitalInOut(board.GP2)
reset_24.direction = digitalio.Direction.INPUT
reset_24.pull = digitalio.Pull.UP
reset_24_switch_state = 0

reset_14 = digitalio.DigitalInOut(board.GP3)
reset_14.direction = digitalio.Direction.INPUT
reset_14.pull = digitalio.Pull.UP
reset_14_switch_state = 0

horn = digitalio.DigitalInOut(board.GP4)
horn.direction = digitalio.Direction.INPUT
horn.pull = digitalio.Pull.UP
horn_state = 0


# initial status for start/stop keys
start_status = 0
stop_status = 0

# the loop
while True:
    if start_status == 0:
        if not start.value:
            kbd.send(start_key)
            #print("timer started")
            start_status = 1
            stop_status = 0

    if stop_status == 0:
        if not stop.value:
            kbd.send(stop_key)
            #print("timer stopped")
            stop_status = 1
            start_status = 0

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

    # horn
    if horn_state == 0:
        if not horn.value:
            kbd.press(horn_key)
            kbd.release(horn_key)
            horn_state = 1

    if horn_state == 1:
        if horn.value:
            kbd.release(horn_key)
            horn_state = 0

    # debounce
    time.sleep(0.01)
