# **[MML-clock-controllers](https://github.com/chrisatcdm/MML-clock-controllers)**

# Repository for the two and four button clock controllers, including adafruit_hid library

The included code has been designed to run on a Raspberry Pi Pico microcontroller running [CircuitPython](https://circuitpython.org/). The **[code.py](http://code.py/)** and the **lib** can be dropped onto a mounted Pico and the device will mount as a human interface device (HID).

There are two variations to the boxes (two-button and four-button) but the same code runs on both.

# Buttons

The buttons for the controllers are 24mm arcade-style buttons that are normally open, momentary switches. They consist of three main components - The coloured house, the micro-switch, and the tail.

## **The coloured hosing**

The coloured housing is made up of two parts that clip together using plastic tags on opposing sides of the housing.

To disassemble the coloured housing (to gain access to the micro-switch) simply depress the plastic tags and the button will release from out the front of the housing.

![Untitled](https://tulip-actress-fdd.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F4d05922d-eb1a-4075-b24b-b37e4702d692%2FUntitled.png?table=block&id=fcd75b41-7728-4b9f-abb2-e2876046f4a4&spaceId=556b476a-35e6-4053-976b-1f2853a5ec64&width=960&userId=&cache=v2)

![Untitled](https://tulip-actress-fdd.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F955be2cd-905d-4b96-847b-61872068406d%2FUntitled.png?table=block&id=0b1a7780-7953-4c84-a32d-506c520f2a16&spaceId=556b476a-35e6-4053-976b-1f2853a5ec64&width=2000&userId=&cache=v2)

## **The micro-switch**

is a sealed unit and is retained in the back of the coloured housing with opposing plastic tags.

![Untitled](https://tulip-actress-fdd.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fe4d88e1a-d5b5-44d7-ae70-11f66f97911f%2FUntitled.png?table=block&id=cb0cb9e2-6b24-4588-938d-9d45d3c7bf48&spaceId=556b476a-35e6-4053-976b-1f2853a5ec64&width=2000&userId=&cache=v2)

**To remove the micro-switch** you must first remove the button and depress the plastic tags, and push the micro-switch towards the front of the button.

![Untitled](https://tulip-actress-fdd.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ffc601fe1-af69-49c2-85da-57520bb1d1ba%2FUntitled.png?table=block&id=1e4df75f-d049-49c7-971a-995e4d2eaff2&spaceId=556b476a-35e6-4053-976b-1f2853a5ec64&width=670&userId=&cache=v2)

![Untitled](https://tulip-actress-fdd.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F69b4654a-8419-4db5-bd73-8acf5a1b15ae%2FUntitled.png?table=block&id=d8534019-2a8a-415b-8682-cc24a0d56459&spaceId=556b476a-35e6-4053-976b-1f2853a5ec64&width=2000&userId=&cache=v2)

## “The Tail”

The tail is two wires (black and red) soldered to the micro-switch and are terminated with a JST 2.0 PH 2 Femail Pin Connector for connection to the Raspberry Pi Pico. Each control box has a spare micro-switch, with a pre-soldered tail taped inside the box.

![Untitled](https://tulip-actress-fdd.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fcd9ce176-2a26-4837-a8a8-506801e045cd%2FUntitled.png?table=block&id=b552d624-54dd-487e-9935-00686b143daf&spaceId=556b476a-35e6-4053-976b-1f2853a5ec64&width=580&userId=&cache=v2)

# Button Connections

The buttons should be connected to GPIO0, GPIO1, GPIO2, and GPIO3 and ground on the Raspberry Pi Pico. GPIO mapping can of course be changed in the code. The opposite ends of the button connections are terminated with JST 2.0 PH 2 Male Pin Connectors and are marked with black permanent marker to indicate the button numbers.

The buttons are numbered 1-4 (or 1-2 in the case of the two-button boxes) and should be read from top to bottom, left to right.

The top-left button is “1” the top right button is “2”, the bottom left is “3” and the bottom right is “4”.

![Untitled](https://tulip-actress-fdd.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F63e185f1-774a-4163-ad5f-4210a5d66d9a%2FUntitled.png?table=block&id=9af40635-a363-4352-ae33-27316205b386&spaceId=556b476a-35e6-4053-976b-1f2853a5ec64&width=2000&userId=&cache=v2)

![Untitled](https://tulip-actress-fdd.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ffa404d6a-21cb-4385-bb69-49ed547bdfff%2FUntitled.png?table=block&id=f6060423-96fe-4564-b207-6f3d30b2c729&spaceId=556b476a-35e6-4053-976b-1f2853a5ec64&width=2000&userId=&cache=v2)

# Key Mapping

The two buttons for starting and stopping the clock are mapped to the same key (”A”). They cannot be pressed more than once at a time and must be reset by the opposing button. In other words, you cannot stop the clock twice, you must start it before you can stop it again.

The 24 & 14-second reset buttons are mapped to keys "B" and "C" respectively and can be pressed as many times as required. They do not latch. In other words, if you hold the button down, it will only fire once.

# USB Port

The control boxes connect to a PC via a Straight, XLR Panel Mount, Socket Type A to A 2.0 USB Connector located at the rear. Retained in a 24mm hole by two counter-sunk SS hex head screws (M3x12mm) and SS full nuts (Loctite applied).

![Untitled](https://tulip-actress-fdd.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fd8d21e8d-e991-49a7-9a36-1d1796697769%2FUntitled.png?table=block&id=602dd298-9846-420c-a493-9dca2693a5c6&spaceId=556b476a-35e6-4053-976b-1f2853a5ec64&width=1880&userId=&cache=v2)

![Untitled](https://tulip-actress-fdd.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff5696ce0-1d9b-4c3a-98dc-319ff3a3ebbe%2FUntitled.png?table=block&id=c1718551-9ba0-4140-95d8-d7e787759833&spaceId=556b476a-35e6-4053-976b-1f2853a5ec64&width=670&userId=&cache=v2)

Internally a short micro-USB cable connects the external USB socket to the Raspberry Pi Pico.

# Service notes

27/04/2023

Controller B: As found, no signs of life - MCU didn't register when plugged in. USB had come unplugged from MCU. All plug connectors had been replaced by a 3rd-party with chocolate block-style connectors. As left, reconnected the USB plug, added Loctite to both ends and removed all chocolate block style connectors and hard soldered/heat-shrunk joins. Screwed the faceplate on. Tested OK. Code notes were updated and added to the git repository.

Controller C: As found, TR and BR buttons are not working. All plug connectors had been replaced by a 3rd-party with chocolate block-style connectors. Two solder joins had broken at MCU. The faceplate is loose. As left, re-soldered MCU joins, removed all chocolate block style connectors, and hard soldered/heat-shrunk joins. Added Loctite to both ends of the USB plug and screwed the faceplate on. Tested OK. Code notes were updated and added to the git repository.

Controller D: As found, no signs of life - MCU didn't register when plugged in, face plate was not secured to the main body. The rear USB connector was unplugged. One plug had a broken solder joint at the button end, and another had a plug that had come apart. As left, hard soldered both buttons to MCU added Loctite to both ends of the USB plug, and screwed the faceplate. Tested OK. Code notes were updated and added to the git repository.
