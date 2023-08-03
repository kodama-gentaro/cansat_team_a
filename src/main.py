from machine import Pin
from utime import sleep
import cs_gps as gps
import cs_sdcard as sd
import cs_motor_driver as md
import cs_nine_axis_sensor as imu
import math

IN1 = Pin(10, Pin.IN,Pin.PULL_DOWN)
IN2 = Pin(11, Pin.OUT)
p7 = Pin(7, Pin.OUT)

IN2.value(1)
while True:
    #print(IN1.value())
    print(IN1.value())
    if IN1.value() == 0 :
        p7.value(1)
        sleep(8)
        p7.value(0)
        break
    else :
        print("A")
    sleep(0.5)

md.init()
imu.init()

md.set_motor(0, 0)

#x1=longtitude(経度）
#y1=latitude（緯度）
x2=39.717098      #本番の南側のポイントの経度
y2=140.129604      #南緯度                     ここは本番で入力
x3=39.717098      #カラーコーンの経度
y3=140.129604      #緯度
#x1_rad=math.radians(x1)
#y1_rad=math.radians(y1)
x2_rad=math.radians(x2)
y2_rad=math.radians(y2)
x3_rad=math.radians(x3)
y3_rad=math.radians(y3)

r=6378137

def distance_first(a,b):
    x1_rad=math.radians(a)
    y1_rad=math.radians(b)
    return r*math.acos(math.sin(y1_rad) * math.sin(y2_rad) + math.cos(y1_rad) * math.cos(y2_rad) * math.cos(x2_rad - x1_rad))#中間地点との距離算出

def th2nd(a,b):
    x1_rad=math.radians(a)
    y1_rad=math.radians(b)
    return 90 - math.degrees(math.atan(math.sin(x2_rad - x1_rad)/( math.cos(y1_rad) * math.tan(y2_rad) - math.sin(y1_rad) * math.cos(x2_rad - x1_rad))))#中間地点の方位算出

def distance_second(c,d):
    x1_rad=math.radians(c)
    y1_rad=math.radians(d)
    return r*math.acos(math.sin(y1_rad) * math.sin(y3_rad) + math.cos(y1_rad) * math.cos(y3_rad) * math.cos(x3_rad - x1_rad))#コーンとの距離算出

def th3rd(c,d):
    x1_rad=math.radians(c)
    y1_rad=math.radians(d)
    return 90 - math.degrees(math.atan2(math.sin(x3_rad - x1_rad)/(math.cos(y3_rad) * math.tan(y3_rad) - math.sin(y1_rad) * math.cos(x3_rad - x1_rad))))#コーンの方位算出


while True:
    print(imu.get_eulervalue())
    th1 = imu.get_eulervalue()[0]
    print(th1)
    
    x1,y1 = gps.get_coordinate()
    distance_1 = distance_first(x1,y1)
    th2 = th2nd(x1,y1)
    
    if distance_1 > 2:
     if th1 > th2:
        if th1 - th2 < 30:
            md.set_motor(1, 1)	
        else:
            if th1 - th2 <= 180:
                md.set_motor(0.6, 1)
            else:
                md.set_motor(1, 0.6)
     else:
         if th2 - th1 < 30:
             md.set_motor(1, 1)
         else:
             if th2 - th1 <= 180:
                 md.set_motor(1, 0.6)
             else:
                 md.set_motor(0.6, 1)
    else:
        break    #この時点でdes1に到着

while True:
    print(imu.get_eulervalue())
    th1 = imu.get_eulervalue()[0]
    print(th1)
    
    x1,y1 = gps.get_coordinate()
    distance_2 = distance_second(x1,y1)
    th3 = th3rd(x1,y1)
    
    if distance_2 >5:
     if th1 > th3:
        if th1 - th3 < 30:
            md.set_motor(1, 1)
        else:
            if th1 - th3 <= 180:
                md.set_motor(0.6, 1)
            else:
                md.set_motor(1, 0.6)
     else:
         if th3 - th1 < 5:
             md.set_motor(1, 1)
         else:
             if th3 - th1 <= 180:
                 md.set_motor(1, 0.6)
             else:
                 md.set_motor(0.6, 1)
    else:
        break    #この時点でdes2にのこり5m。ここからカメラ移行のプログラミングをつける

pinX = machine.pin(26,Pin.IN)
pinY = machine.pin(27,Pin.IN)

def go_destination(i):
    return i.value()

while True:
    X = go_destination(pinX)
    Y = go_destination(pinY)
    
    if X==Y==0:
        md.set_motor(1,1)
    
    
    elif X=1 and Y=0:
        md.set_motor(1,-1)
    
    elif X=0 and Y=1:
        md.set_motor(-1,1)
    
    else:
        md.set_motor(0,0)



"""while True:
    
    tandem=get_cameravalue()
    
    if tandem > 20:
        md.set_motor(1,-1)
    
    elif tandem < -20:
        md.set_motor(-1.1)
    
    else:
        md.set_motor(1.1)"""
