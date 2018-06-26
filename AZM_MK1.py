#!/usr/bin/python
import sys
import Adafruit_DHT

from time import sleep, strftime, time

def write_temp(temp, humi):
    with open("temp.csv", "a") as log:
        log.write("{0},{1},{2}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)[:4],str(humi)[:4]))
while True:
	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
	write_temp(temperature, humidity)
	sleep(45)
