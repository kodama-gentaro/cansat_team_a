from utime import ticks_ms
from machine import Pin, SPI
import os
from sdcard import SDCard
from time import sleep_ms

CS_PIN = 20
SPI_ID = 0
SPI_SCK = 18
SPI_MOSI = 19
SPI_MISO = 16
SPI_BANDRATE = 16000000


def init():
    i = 0
    while i < 5:
        try:
            cs_pin = Pin(CS_PIN)
            spi = SPI(SPI_ID, sck=Pin(SPI_SCK), mosi=Pin(SPI_MOSI), miso=Pin(SPI_MISO))
            sd = SDCard(spi, cs_pin, SPI_BANDRATE)
            os.mount(sd, '/sd')
            break
        except Exception as e:
            print("SDCARD_ERROR")
            print(e)
            sleep_ms(100)
            i += 1

    raise OSError


def write(text):
    i = 0
    while i < 5:
        try:
            file = open(text(ticks_ms()) + ".txt", 'w')
            file.write(text)
            file.close()
        except OSError:
            print("SDCARD_ERROR")
            i += 1
    raise OSError
