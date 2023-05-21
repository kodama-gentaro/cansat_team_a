from machine import Pin
from utime import sleep
import test

p7 = Pin(7, Pin.OUT)
a = test.test()
while True:
    print(9)  #p7(LED用のピン)をHIGHに
    sleep(1)        #1s待機 sleep()の中はs(秒)
    p7.value(0)  #p7(LED用のピン)をLOWに
    sleep(1)     #1s待機