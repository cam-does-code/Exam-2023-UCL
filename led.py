import machine 

import time 



# Pin number for the LED 

led_pin = 23 

 

# Set up the LED pin as an output 

led = machine.Pin(led_pin, machine.Pin.OUT) 

 

# Function to toggle the LED state 

def toggle_led(): 

    led.value(not led.value()) 

 

# Blink the LED 

while True: 

    toggle_led() 

    time.sleep(1) 