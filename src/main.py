from machine import Pin
from utime import sleep
import cs_gps as gps
import cs_sdcard as sd
import cs_motor_driver as md
import cs_nine_axis_sensor as imu

md.init()
imu.init()

md.set_motor(0, 0)

while True:
    break
    print(imu.get_eulervalue())
    th1 = imu.get_eulervalue()[0]
    th2 = 40
    print(th1)
    if th1 > th2:
        if th1 - th2 < 5:
            md.set_motor(1, 1)
        else:
            if th1 - th2 <= 180:
                md.set_motor(-1, 1)
            else:
                md.set_motor(1, -1)
    else:
        if th2 - th1 < 5:
            md.set_motor(1, 1)
        else:
            if th2 - th1 <= 180:
                md.set_motor(1, -1)
            else:
                md.set_motor(-1, 1)
