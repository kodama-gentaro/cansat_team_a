import machine
from utime import sleep


p7 = machine.Pin(0, machine.Pin.OUT)


p7.value(1)
sleep(5)
p7.value(0)