from machine import Pin, SoftI2C
import utime

from bno055 import BNO055

def init():
    global i2c
    i2c = SoftI2C(scl=Pin(4), sda=Pin(5), freq=10000)
    global sensor
    sensor = BNO055(i2c)
    global offset
    offset = (0, 0, 0, #加速度(x,y,z)のキャリブレーション
              0, 0, 0, #角速度(x,y,z)のキャリブレーション
              0, 0, 0, #地磁気(x,y,z)のキャリブレーション
              0, 0, -35) #オイラー角(x,y,z)のキャリブレーション

def get_accvalue():
    a=5
    count=0
    while True:
        a-=1
        count+=1
        if a>0:
            try:
                acc_x = sensor.accel()[0] - offset[0]
                acc_y = sensor.accel()[1] - offset[1]
                acc_z = sensor.accel()[2] - offset[2]
                
                if acc_x == 0.0 and acc_y == 0.0 and acc_z == 0.0:
                    raise OSError
                
                #加速度
                return acc_x,acc_y,acc_z
                
            except OSError as e:
                print(e)
        else:
            break
    raise OSError


def get_gyrvalue():
    a=5
    count=0
    while True:
        a-=1
        count+=1
        if a>0:
            try:
                gyr_x = sensor.gyro()[0] - offset[3]
                gyr_y = sensor.gyro()[1] - offset[4]
                gyr_z = sensor.gyro()[2] - offset[5]
                
                if gyr_x == 0.0 and gyr_y == 0.0 and gyr_z == 0.0:
                    raise OSError
                
                #角速度
                return gyr_x,gyr_y,gyr_z
                
            except OSError as e:
                print(e)
        else:
            break
    raise OSError


def get_magvalue():
    a=5
    count=0
    while True:
        a-=1
        count+=1
        if a>0:
            try:
                mag_x = sensor.mag()[0] - offset[6]
                mag_y = sensor.mag()[1] - offset[7]
                mag_z = sensor.mag()[2] - offset[8]
                
                if mag_x == 0.0 and mag_y == 0.0 and mag_z == 0.0:
                    raise OSError
                
                #地磁気
                return mag_x,mag_y,mag_z
                
            except OSError as e:
                print(e)
        else:
            break
    raise OSError
       

def get_eulervalue():
    a=50
    count=0
    while True:
        a-=1
        count+=1
        if a>0:
            try:
                euler_x = sensor.euler()[0] - offset[9]
                euler_y = sensor.euler()[1] - offset[10]
                euler_z = sensor.euler()[2] - offset[11]
        
                if euler_x == 0.0 and euler_y == 0.0 and euler_z == 0.0:
                    raise OSError
                
                #オイラー角
                return euler_x,euler_y,euler_z
            
            except OSError as e:
                print(e)
        else:
            break
    raise OSError


