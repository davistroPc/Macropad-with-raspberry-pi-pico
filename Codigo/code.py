import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio


btn1_pin = board.GP0
btn2_pin = board.GP1
btn3_pin = board.GP2
btn4_pin = board.GP3
btn5_pin = board.GP4
btn6_pin = board.GP5
btn7_pin = board.GP18
btn8_pin = board.GP19
btn9_pin = board.GP20 

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN

btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN

btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN

keyboard = Keyboard(usb_hid.devices)

while True:
    if btn1.value:
        keyboard.send(Keycode.F13)
        time.sleep(0.1)
    if btn2.value:
        keyboard.send(Keycode.F14)
        time.sleep(0.1)
    if btn3.value:
        keyboard.send(Keycode.F15)
        time.sleep(0.1)
    if btn4.value:
        keyboard.send(Keycode.F16)
        time.sleep(0.1)
    if btn5.value:
        keyboard.send(Keycode.F17)
        time.sleep(0.1)
    if btn6.value:
        keyboard.send(Keycode.F18)
        time.sleep(0.1)
    if btn7.value:
        keyboard.send(Keycode.F19)
        time.sleep(0.1)
    if btn8.value:
        keyboard.send(Keycode.F20)
        time.sleep(0.1)
    if btn9.value:
        keyboard.send(Keycode.F21)
        time.sleep(0.1)

    time.sleep(0.1)
