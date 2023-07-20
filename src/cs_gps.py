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

#緯度(latitude)と経度(longitude)を取得する関数を作って方向を±180で表示
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
            lat_str = convert(my_gps.latitude)
            long_str = convert(my_gps.longitude)

            # _________________________________________________
            if type(lat_str) == str:
                latitude = float(lat_str)
            if type(long_str) == str:
                longitude = float(long_str)
        except:
            print("gps_warning")
    return latitude, longitude


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
init()
while True:
    print(get_coordinate())
    lightsleep(1000)


# Define be
