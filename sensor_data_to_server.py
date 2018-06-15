import sys
import serial
from serial import Serial
import time
import requests
import re


while True:
    time.sleep(2)
    s = serial.Serial(port='/dev/cu.usbmodem1411', baudrate=9600)
    try:
        temperature = str(s.readline(), 'ascii')
        humidity = str(s.readline(), 'ascii')

        time.sleep(2)

        temperature = re.sub("[^0-9]", "", temperature.split('.')[0])
        humidity = re.sub("[^0-9]", "", humidity.split('.')[0])
        print(temperature)
        print(humidity)
        print('Values have been read...')

        temperature_post = "https://marindelija.com/db/ddownr.com/index.php?request=add_temp&temp=" + str(temperature) + "&sensorid=1"
        requests.get(temperature_post)

        humidity_post = "https://marindelija.com/db/ddownr.com/index.php?request=add_hum&hum=" + str(humidity) + "&sensorid=1"
        requests.get(humidity_post)
    except:
        print("Unexpected Error:", sys.exc_info()[0])
