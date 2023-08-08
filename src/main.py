from machine import Pin
from utime import sleep, ticks_ms
import cs_gps as gps
import cs_sdcard as sd
import cs_motor_driver as md
import cs_nine_axis_sensor as imu
import math
import ujson as json

IN1 = Pin(17, Pin.IN, Pin.PULL_UP)
IN2 = Pin(11, Pin.OUT)
p6 = Pin(6, Pin.OUT)

IN2.value(1)
dict = {}
md.init()
md.set_motor(0, 0)
while True:
    # print(IN1.value())
    print(IN1.value())
    if IN1.value() == 1:
        p6.value(1)
        sleep(0)
        p6.value(0)
        print("para_deprecated")
        break
    else:
        print("A")
    sleep(0.5)

md.init()
imu.init()
gps.init()
#sd.init()
#sd.write('para_deprecated')
sleep(1)
md.set_motor(0, 0)
dict[f'{ticks_ms()}'] = "start"
# x1=longtitude(経度）
# y1=latitude（緯度）
x2 = 130.21753  # 本番の南側のポイントの経度
y2 = 33.59507  # 南緯度                     ここは本番で入力
x3 = 130.21753 # カラーコーンの経度
y3 = 33.59507  # 緯度
# x1_rad=math.radians(x1)
# y1_rad=math.radians(y1)
x2_rad = math.radians(x2)
y2_rad = math.radians(y2)
x3_rad = math.radians(x3)
y3_rad = math.radians(y3)

r = 6378137


def distance_first(a, b):
    x1_rad = math.radians(a)
    y1_rad = math.radians(b)
    #print(f"{x1_rad} {y1_rad} {x2_rad} {y2_rad}")
    M = 6334834 / math.sqrt((1-0.0066744*math.sin((y1_rad + y2_rad) / 2.0)**2.0)**3.0)
    N = 6377397 / math.sqrt(1-0.0066744*math.sin((y1_rad + y2_rad) / 2.0)**2.0)
    dist = ((M*(y1_rad - y2_rad)) ** 2 + (N*(x1_rad - x2_rad)*math.cos((y1_rad + y2_rad) / 2.0)) ** 2.0) ** 0.5
    #print(dist)
    return dist

def th2nd(a, b):
    x1_rad = math.radians(a)
    y1_rad = math.radians(b)
    #print(f"{x1_rad} {y1_rad} {x2_rad} {y2_rad}")
    return math.degrees(math.pi / 2 - math.atan2((
                math.cos(y1_rad) * math.tan(y2_rad) - math.sin(y1_rad) * math.cos(x2_rad - x1_rad)),math.sin(x2_rad - x1_rad)))  # 中間地点の方位算出


def distance_second(c, d):
    x1_rad = math.radians(c)
    y1_rad = math.radians(d)
    # print(f"{x1_rad} {y1_rad} {x2_rad} {y2_rad}")
    M = 6334834 / math.sqrt((1 - 0.0066744 * math.sin((y1_rad + y3_rad) / 2.0) ** 2.0) ** 3.0)
    N = 6377397 / math.sqrt(1 - 0.0066744 * math.sin((y1_rad + y3_rad) / 2.0) ** 2.0)
    dist = ((M * (y1_rad - y3_rad)) ** 2 + (N * (x1_rad - x3_rad) * math.cos((y1_rad + y3_rad) / 2.0)) ** 2.0) ** 0.5
    # print(dist)
    return dist


def th3rd(c, d):
    x1_rad = math.radians(c)
    y1_rad = math.radians(d)
    return 90 - math.degrees(math.atan2( (
                math.cos(y1_rad) * math.tan(y3_rad) - math.sin(y1_rad) * math.cos(x3_rad - x1_rad)),math.sin(x3_rad - x1_rad)))  # コーンの方位算出


dict[f'{ticks_ms()}'] = "start"
pinX = Pin(26, Pin.IN)
pinY = Pin(27, Pin.IN)
sleep(30000)
md.set_motor(0.5, 0.5)
sleep(1)
while True:
    th1 = imu.get_eulervalue()[0]
    #print(imu.get_magvalue()[0])
    x1, y1 = gps.get_coordinate()
    
    if x1 is None or x2 is None:
        continue
    distance_1 = distance_first(x1, y1)
    th2 = th2nd(x1, y1)
    th1 = th1
    th2 = th2 if th2 > 0 else 360 + th2

    print(f'{x1} {y1} {distance_1} {th1} {th2}')
    #sd.write(f'{x1} {y1} {distance_1} {th1} {th2}')

    # dict[f'{ticks_ms()}'] = f"{th1} {th2}"
    if distance_1 > 5:

        if th1 > th2:
            if th1 - th2 < 10:
                md.set_motor(1, 1)
                print('s')
            else:
                if th1 - th2 <= 180:
                    md.set_motor(0.4, 1)
                    print('l')
                else:
                    md.set_motor(1, 0.4)
                    print('r')
        else:
            if th2 - th1 < 10:
                md.set_motor(1, 1)
                print('s')
            else:
                if th2 - th1 <= 180:
                    md.set_motor(1, 0.4)
                    print('r')
                else:
                    md.set_motor(0.4, 1)
                    print('l')
    else:
        break  # この時点でdes1に到着

md.set_motor(0.5, 0.5)
sleep(1)
while True:
    print(imu.get_eulervalue())
    th1 = imu.get_eulervalue()[0]
    print(th1)
    
    x1,y1 = gps.get_coordinate()
    if x1 is None or x2 is None:
        continue
    distance_2 = distance_second(x1,y1)
    th3 = th3rd(x1,y1)
    #sd.write(f'{x1} {y1} {distance_2} {th1} {th3}')
    if distance_2 >5:
     if th1 > th3:
        if th1 - th3 < 5:
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



md.set_motor(0.5, 0.5)
sleep(1)
while True:
    X = pinX.value()
    Y = pinY.value()
    #sd.write(f'{X} {Y}')
    if X == Y == 0:
        md.set_motor(0.6, 0.7)
    elif X == 1 and Y == 0:
        md.set_motor(0.4, 0.2)
    elif X == 0 and Y == 1:
        md.set_motor(0.2, 0.4)
    else:
        md.set_motor(0.3, 0.2)
    sleep(0.5)
    md.set_motor(0, 0)
    sleep(0.5)
    if IN1.value() == 0:
        break

"""while True:
    
    tandem=get_cameravalue()
    
    if tandem > 20:
        md.set_motor(1,-1)
    
    elif tandem < -20:
        md.set_motor(-1.1)
    
    else:
        md.set_motor(1.1)"""
