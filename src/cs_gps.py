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
def get_coordinate(parts):
    if (parts[0] == 0):
        return None
        
    data = parts[0]+(parts[1]/60.0)
    
    if (parts[2] == 'S'):
        data = -data
    if (parts[2] == 'W'):
        data = -data

    data = '{0:.6f}'.format(data) # to 6 decimal places
    return str(data)
##########################################################

##########################################################
while True:
    
    length = gps_module.any()
    if length>0:
        b = gps_module.read(length)
        for x in b:
            msg = my_gps.update(chr(x))
    #_________________________________________________
    latitude = convert(my_gps.latitude)
    longitude = convert(my_gps.longitude)
    #_________________________________________________
    if type(latitude) == str:
        latitude = float(latitude)
    
    
    #_________________________________________________
    print('Lat:', latitude)
    print('Lng:', longitude)
    print(type(latitude))
    
    
    lightsleep(5000)
    
    lat1 = ('Lat:') # Current latitude
    lon1 = ('Lng:')# Current longitude
    lat2 = 33.597608# Destination latitude
    lon2 = 130.224240 # Destination longitude

# Define bearing function
def bearing(lat1, lon1, lat2, lon2):
    # Convert degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Calculate longitude and latitude differences
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Calculate bearing
    bearing = math.atan2(math.sin(dlon) * math.cos(lat2),
                         math.cos(lat1) * math.sin(lat2) -
                         math.sin(lat1) * math.cos(lat2) * math.cos(dlon))

    # Adjust bearing to be in range of 0 to 360 degrees
    if bearing < 0:
        bearing += 2 * math.pi

    # Convert radians to degrees
    bearing = math.degrees(bearing)

    return bearing

    # Calculate and print bearing
    bearing = bearing(lat1, lon1, lat2, lon2)
    print("Bearing:", bearing)
    return 
