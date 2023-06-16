from machine import Pin
from time import sleep

relay = Pin(32, Pin.OUT)

while True:
    relay.value(1)
    sleep(1)
    relay.value(0)
    sleep(1)