import machine
import utime
from machine import Pin

IN1 = machine.Pin(10, machine.Pin.IN,Pin.PULL_DOWN)
IN2 = machine.Pin(11,machine.Pin.OUT)
p7 = machine.Pin(7, machine.Pin.OUT)

IN2.value(1)

while True:
    print(IN1.value())
    if IN1.value() == 0:
        p7.value(1)
        utime.sleep(8)
        p7.value(0)
        break
    else:
        print("A")
    utime.sleep(0.5)