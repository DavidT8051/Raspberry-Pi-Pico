#Edgar David Trujillo Vergara
#Blinking

from machine import Pin
import utime

led = Pin(25, Pin.OUT)

while True:
    led.value(1)
    utime.sleep_ms(500)
    led.value(0)
    utime.sleep_ms(500)
    