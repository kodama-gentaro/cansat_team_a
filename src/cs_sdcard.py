from machine import Pin, SPI
import os
from sdcard import  SDCard
from time import sleep_ms
CS_PIN = 17  #回路作ってから多分変える
SPI_ID = 0
SPI_SCK = 18
SPI_MOSI = 19
SPI_MISO = 16
SPI_BANDRATE = 32000000
FILE_TITLE = "starrail"

class SDcard:
    def __init__(self):
        i = 0
        while i < 5:
            try:
                self.cs_pin = Pin(CS_PIN)
                self.spi = SPI(SPI_ID,  sck=Pin(SPI_SCK), mosi=Pin(SPI_MOSI), miso=Pin(SPI_MISO))
                self.sd = SDCard(self.spi , self.cs_pin, SPI_BANDRATE)
                os.mount(self.sd, '/sd')
            except Exception as e:
                print("SDCARD_ERROR")
                print(e)
                sleep_ms(100)
                i += 1
                break







