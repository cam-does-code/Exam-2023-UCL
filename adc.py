# https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/python-circuitpython

# import necessary modules and initialize the I2C bus
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)

# import the module for the board you are using. For the ADS1015, use:
import adafruit_ads1x15.ads1015 as ADS
# The final import needed is for the ADS1x15 library's version of AnalogIn
from adafruit_ads1x15.analog_in import AnalogIn

# create the ADC object. For the ADS1015, use:
ads = ADS.ADS1015(i2c)

# For single ended mode we use AnalogIn to create the analog input channel, 
# providing the ADC object and the pin to which the signal is attached. 
# Here, we use pin 0:
chan = AnalogIn(ads, ADS.P0)

# Now you can read the raw value and voltage of the channel 
# using either the the value or voltage property.
print(chan.value, chan.voltage)
