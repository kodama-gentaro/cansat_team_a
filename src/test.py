import machine
import utime

uart = machine.UART(0, baudrate=9600)

while True:
    byte = uart.read(1)
    if byte != None:
        print(byte)
    utime.sleep(1)
          