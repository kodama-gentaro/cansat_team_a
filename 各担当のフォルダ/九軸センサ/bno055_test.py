from machine import Pin, I2C
import utime

from bno055 import BNO055

i2c = I2C(1, scl=Pin(7), sda=Pin(6))

sensor = BNO055(i2c)

acc_x = float

offset = (0, 0, 0, #加速度(x,y,z)のキャリブレーション
          0, 0, 0, #角速度(x,y,z)のキャリブレーション
          0, 0, 0) #地磁気(x,y,z)のキャリブレーション

while True:
    acc_x = sensor.accel()[0] - offset[0]
    acc_y = sensor.accel()[1] - offset[1]
    acc_z = sensor.accel()[2] - offset[2]

    gyr_x = sensor.gyro()[0] - offset[3]
    gyr_y = sensor.gyro()[1] - offset[4]
    gyr_z = sensor.gyro()[2] - offset[5]

    mag_x = sensor.mag()[0] - offset[6]
    mag_y = sensor.mag()[1] - offset[7]
    mag_z = sensor.mag()[2] - offset[8]
    
    print('加速度:',acc_x,acc_y,acc_z)
    print('角速度:',gyr_x,gyr_y,gyr_z)
    print('地磁気:',mag_x,mag_y,mag_z)
    print('------------------------------')
    utime.sleep(2)