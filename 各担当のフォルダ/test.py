import utime
from machine import Pin, PWM

IN1 = PWM(Pin(17, Pin.OUT))
IN2 = Pin(18, Pin.OUT)
IN1.freq(1000)

while True:
    IN1.duty_u16(52429)
    IN2.value(0)
    utime.sleep(2)
    """
    IN1.value(0)
    IN2.value(1)
    utime.sleep(2)
    IN1.value(0)
    IN1.value(0)
    utime.sleep_ms(100)
    IN1.value(1)
    IN2.value(0)
    utime.sleep(2)
    """
