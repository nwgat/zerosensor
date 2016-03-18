# A simple program to test the driver

import sys
import time


from datetime import datetime
import HTU21DF

i = datetime.now()

while True:
	sys.stdout = open('/var/www/html/tmphum.txt', 'a')
	temperature = HTU21DF.read_temperature()
	time.sleep(1)
	humidity = HTU21DF.read_humidity()
	print "%f|%F" % (temperature, humidity)
#	print i.strftime('%Y/%m/%d %H:%M:%S')
	time.sleep(1)

