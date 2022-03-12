# **[MML-clock-controllers](https://github.com/chrisatcdm/MML-clock-controllers)**

# Repository for the two and four button clock controllers, including adafruit_hid library

This code has been designed to run on a Raspberry Pi Pico microcontroller running [CircuitPython](https://circuitpython.org/). The **code.py** and the **lib** can be dropped onto a mounted Pico and the device will mount as a human interface device (HID).

There are two variations to the boxes, but the same code runs on both.

## Button Connections

Normally open-circuit should be connected to GPIO0, GPIO1, GPIO2, and GPIO3 and ground. GPIO mapping can of course be changed in the code.

## Key Mapping

The two buttons for starting and stopping the clock are mapped to the same key (”A”). They cannot be pressed more than once at a time and must be reset by the opposing button. In other words, you cannot stop the clock twice, you must start it before you can stop it again.

The 24 & 14-second reset buttons can be pressed as many times as required. They do not latch. In other words, if you hold the button down, it will only fire once.
