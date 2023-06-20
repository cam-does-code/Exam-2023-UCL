import time
import board
import adafruit_dht
import psutil
import sqlite3 as lite

conn = lite.connect("sensorData.db")
c = conn.cursor()
#c.execute("CREATE TABLE Dht (Temp FLOAT, Humidity FLOAT)")
# We first check if a libgpiod process is running. If yes, we kill it!
for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()
sensor = adafruit_dht.DHT11(board.D23)
while True:
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        c.execute('INSERT INTO Dht VALUES(?,?)',(temp, humidity))
        print(c.execute("SELECT * FROM Dht WHERE temp").fetchall())
        print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
    time.sleep(2.0)
