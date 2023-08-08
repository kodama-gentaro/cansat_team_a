from machine import Pin, UART, lightsleep
import utime, time

from micropyGPS import MicropyGPS

import math


def init():
    global gps_module
    gps_module = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

    global TIMEZONE
    TIMEZONE = 9

    global my_gps
    my_gps = MicropyGPS(TIMEZONE)


# 緯度(latitude)と経度(longitude)を取得する関数を作って方向を±180で表示
def get_coordinate():
    latitude = 0.0
    longitude = 0.0
    for i in range(8):
        try:
            length = gps_module.any()
            if length > 0:
                b = gps_module.read(length)
                for x in b:
                    msg = my_gps.update(chr(x))
            # _________________________________________________
            latitude = convert(my_gps.latitude)
            longitude = convert(my_gps.longitude)
            # _________________________________________________
            if type(latitude) == str:
                latitude = float(latitude)
            if type(longitude) == str:
                longitude = float(longitude)


            # _________________________________________________
            #print('Lat:', latitude)
            #print('Lng:', longitude)
            #print(type(latitude))
            break

        except Exception as E:
            pass
    return longitude, latitude

##########################################################
def convert(parts):
    if (parts[0] == 0):
        return None

    data = parts[0] + (parts[1] / 60.0)

    if (parts[2] == 'S'):
        data = -data
    if (parts[2] == 'W'):
        data = -data

    data = '{0:.6f}'.format(data)  # to 6 decimal places
    return str(data)


##########################################################



