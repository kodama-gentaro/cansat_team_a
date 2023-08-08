import utime
import time
from machine import Pin


def init():
    global pin1_c
    global pin2_c
    pin1_c = Pin(27, Pin.IN, Pin.PULL_DOWN)
    pin2_c = Pin(26, Pin.IN, Pin.PULL_DOWN)
    pin2_c.value()
    pin1_c.value()


def read():
    i = pin1_c.value()
    l = pin2_c.value()
    return i, l