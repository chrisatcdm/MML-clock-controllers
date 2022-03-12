# **[MML-clock-controllers](https://github.com/chrisatcdm/MML-clock-controllers)**

# Repository for the two and four button clock controllers, including adafruit_hid library

The included code has been designed to run on a Raspberry Pi Pico microcontroller running [CircuitPython](https://circuitpython.org/). The **[code.py](http://code.py/)** and the **lib** can be dropped onto a mounted Pico and the device will mount as a human interface device (HID).

There are two variations to the boxes (two-button and four-button) but the same code runs on both.

# Buttons

The buttons for the controllers are 24mm arcade-style buttons that are normally open, momentary switches. They consist of three main components - The coloured house, the micro-switch, and the tail.

## **The coloured hosing**

The coloured housing is made up of two parts that clip together using plastic tags on opposing sides of the housing.

To disassemble the coloured housing (to gain access to the micro-switch) simply depress the plastic tags and the button will release from out the front of the housing.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4d05922d-eb1a-4075-b24b-b37e4702d692/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/955be2cd-905d-4b96-847b-61872068406d/Untitled.png)

## **The micro-switch**

is a sealed unit and is retained in the back of the coloured housing with opposing plastic tags.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e4d88e1a-d5b5-44d7-ae70-11f66f97911f/Untitled.png)

**To remove the micro-switch** you must first remove the button and depress the plastic tags, and push the micro-switch towards the front of the button.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fc601fe1-af69-49c2-85da-57520bb1d1ba/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/69b4654a-8419-4db5-bd73-8acf5a1b15ae/Untitled.png)

## “The Tail”

The tail is two wires (black and red) soldered to the micro-switch and are terminated with a JST 2.0 PH 2 Femail Pin Connector for connection to the Raspberry Pi Pico. Each control box has a spare micro-switch, with a pre-soldered tail taped inside the box.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cd9ce176-2a26-4837-a8a8-506801e045cd/Untitled.png)

# Button Connections

The buttons should be connected to GPIO0, GPIO1, GPIO2, and GPIO3 and ground on the Raspberry Pi Pico. GPIO mapping can of course be changed in the code. The opposite ends of the button connections are terminated with JST 2.0 PH 2 Male Pin Connectors and are marked with black permanent marker to indicate the button numbers.

The buttons are numbered 1-4 (or 1-2 in the case of the two-button boxes) and should be read from top to bottom, left to right.

The top-left button is “1” the top right button is “2”, the bottom left is “3” and the bottom right is “4”.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/63e185f1-774a-4163-ad5f-4210a5d66d9a/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fa404d6a-21cb-4385-bb69-49ed547bdfff/Untitled.png)

# Key Mapping

The two buttons for starting and stopping the clock are mapped to the same key (”A”). They cannot be pressed more than once at a time and must be reset by the opposing button. In other words, you cannot stop the clock twice, you must start it before you can stop it again.

The 24 & 14-second reset buttons are mapped to keys "B" and "C" respectively and can be pressed as many times as required. They do not latch. In other words, if you hold the button down, it will only fire once.

# USB Port

The control boxes connect to a PC via a Straight, XLR Panel Mount, Socket Type A to A 2.0 USB Connector located at the rear. Retained in a 24mm hole by two counter-sunk SS hex head screws (M3x12mm) and SS full nuts (Loctite applied).

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d8d21e8d-e991-49a7-9a36-1d1796697769/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f5696ce0-1d9b-4c3a-98dc-319ff3a3ebbe/Untitled.png)

Internally a short micro-USB cable connected the external USB socket to the Raspberry Pi Pico.
