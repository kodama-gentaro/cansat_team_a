from machine import Pin
from utime import sleep
import cs_gps as gps
import cs_sdcard as sd
import cs_motor_driver as md
import cs_nine_axis_sensor as imu

md.init()
imu.init()
md.set_motor(1,1)
print(imu.get_eulervalue())







