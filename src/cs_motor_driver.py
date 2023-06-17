from machine import Pin


class Motor:
    def __init__(self, pin_1_A:Pin, pin_1_B:Pin, pin_2_A:Pin, pin_2_B:Pin):
        self.pin_1_A = pin_1_A
        self.pin_1_B = pin_1_B
        self.pin_2_A = pin_2_A
        self.pin_2_B = pin_2_B

    #左右のタイヤの速度を、最大１、最小ー１の実数で設定できる関数
    def set_speed(self, left, right):
        #ここに処理を書く

    def stop(self):
        self.set_speed(0, 0)