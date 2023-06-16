import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
relay_GPIO = 17
GPIO.setup(relay_GPIO, GPIO.OUT) # GPIO Assign mode

try:
    while True:
        GPIO.output(relay_GPIO, GPIO.HIGH) # on
        sleep(1)
        GPIO.output(relay_GPIO, GPIO.LOW) # off
        sleep(1)
except KeyboardInterrupt:
    print('stopped')
