from machine import Pin
from utime import sleep
import cs_gps as gps
import cs_sdcard as sd
import cs_motor_driver as md
import cs_nine_axis_sensor as imu
import math as m

IN1 = machine.Pin(10, machine.Pin.IN,Pin.PULL_DOWN)
IN2 = machine.Pin(11, machine.Pin.OUT)
p7 = machine.Pin(7, machine.Pin.OUT)

IN2.value(1)
while True:
    #print(IN1.value())
    print(IN1.value())
    if IN1.value() == 0 :
        p7.value(1)
        utime.sleep(8)
        p7.value(0)
        break
    else :
        print("A")
    utime.sleep(0.5)

md.init()
imu.init()

md.set_motor(0, 0)

x1=latitude
y1=longtitude
x2=#本番の南側のポイントの緯度
y2=#南経度                     ここは本番で入力
x3=#カラーコーンの緯度
y3=#経度
x1_rad=math.radians(x1)
y1_rad=math.radians(y1)
x2_rad=math.radians(x2)
y2_rad=math.radians(y2)
x3_rad=math.radians(x3)
y3_rad=math.radians(y3)

r=6378137
distance_first=r*math.acos(math.sin(y1_rad) * math.sin(y2_rad) + math.cos(y1_rad) * math.cos(y2_rad) * math.cos(x2_rad - x1_rad))#中間地点との距離算出
th2= 90 - math.degrees(math.atan2(math.sin(x2_rad - x1_rad), math.cos(y1_rad) * math.tan(y2_rad) - math.sin(y1_rad) * math.cos(x2_rad - x1_rad)))#中間地点の方位算出

distance_second=r*math.acos(math.sin(y1_rad) * math.sin(y3_rad) + math.cos(y1_rad) * math.cos(y3_rad) * math.cos(x3_rad - x1_rad))#コーンとの距離算出
th3= 90 - math.degrees(math.atan2(math.sin(x3_rad - x1_rad), math.cos(y3_rad) * math.tan(y3_rad) - math.sin(y1_rad) * math.cos(x3_rad - x1_rad)))#コーンの方位算出


while True:
    print(imu.get_eulervalue())
    th1 = imu.get_eulervalue()[0]
    print(th1)
    if distance_first > 2:
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
    else:
        break    #この時点でdes1に到着

while True:
    print(imu.get_eulervalue())
    th1 = imu.get_eulervalue()[0]
    print(th1)
    if distance_second >5:
     if th1 > th3:
        if th1 - th3 < 5:
            md.set_motor(1, 1)
        else:
            if th1 - th3 <= 180:
                md.set_motor(-1, 1)
            else:
                md.set_motor(1, -1)
     else:
         if th3 - th1 < 5:
             md.set_motor(1, 1)
         else:
             if th3 - th1 <= 180:
                 md.set_motor(1, -1)
             else:
                 md.set_motor(-1, 1)
    else:
        break    #この時点でdes2にのこり5m。ここからカメラ移行のプログラミングをつける
