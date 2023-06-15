from machine import Pin, ADC
import time

# Set up ADC (Analog to Digital Converter)
adc = ADC(Pin(34))  # ADC pin 34 on ESP32

while True:
    ldr_value = adc.read()  # Read the LDR value from ADC
    print("LDR Value:", ldr_value)
    # Add your desired logic here based on the LDR value

    # Optional delay
    time.sleep(1)  # Delay for 1 second before reading again
