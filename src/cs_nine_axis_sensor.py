from machine import I2C


class NineAxisSensor:
    def __init__(self, i2c:I2C):
        self.i2c = i2c
    # x,y,zそれぞれの加速度を返す関数
    def get_accel(self):
        return x, y, z

    # x,y,zそれぞれのジャイロの値（角速度）を返す関数
    def get_gyro(self):
        return x, y, z
    # x,y,zそれぞれの地磁気の値(角度)を返す関数
    def get_mag(self):
        return x, y, z

    # x,y,zそれぞれの角度を返す関数
    def get_angle(self):
        return x, y, z

get_accel()

