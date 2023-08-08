import machine
import utime
from machine import PWM
WAIT = 2/65536
def init():
    global Motor1
    global Motor2
    global Motor3
    global Motor4
    Motor1 = PWM(machine.Pin(13, machine.Pin.OUT))
    Motor2 = PWM(machine.Pin(12, machine.Pin.OUT))
    Motor3 = PWM(machine.Pin(15, machine.Pin.OUT))
    Motor4 = PWM(machine.Pin(14, machine.Pin.OUT))

    #IN1.value(0)
    #IN2.value(1)
    Motor1.freq(5000)
    Motor2.freq(5000)
    Motor3.freq(5000)
    Motor4.freq(5000)
    Motor1.duty_u16(0)
    Motor2.duty_u16(0)
    Motor3.duty_u16(0)
    Motor4.duty_u16(0)
def set_motor(r,l):
    x = 0
    if r>0 :
        x = 65536*r
        x = int(x)
        for i in range(x):
             Motor1.duty_u16(x)
             utime.sleep(WAIT)
        Motor2.duty_u16(0)
        
        
    else :
        x = 65536*(-r)
        x = int(x)
        Motor1.duty_u16(0)
        for i in range(x):
             Motor2.duty_u16(x)
             utime.sleep(WAIT)

    
    if l>0 :
        x = 65536*l
        x = int(x)
        for i in range(x):
             Motor3.duty_u16(x)
             utime.sleep(WAIT)
        Motor4.duty_u16(0)
        
        
    else :
        x = 65536*(-l)
        x = int(x)
        Motor3.duty_u16(0)
        for i in range(x):
             Motor4.duty_u16(x)
             utime.sleep(WAIT)

init()
print("start")

