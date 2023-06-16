from machine import Pin, ADC
import time
pot_pin = 32
pot = ADC(Pin(pot_pin))
pot.atten(ADC.ATTN_11DB) # Kalibrering til korrekte målinger
pot.width(ADC.WIDTH_10BIT) # Fra 0 - 4095 range til 0 - 1023 range 

while True:
    print('Pot value:',pot.read())
    time.sleep(0.5)
