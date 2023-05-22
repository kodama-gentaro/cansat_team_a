from machine import Pin
from utime import sleep

import test
t = test.test()
while True:
    print(t.cst())
    sleep(2)

