from machine import UART, Pin


def init():
    global uart_zero
    uart_zero = UART(1, 9600, tx=Pin(8), rx=Pin(9))


def write(str: str):
    uart_zero.write(str + "\r\n")
