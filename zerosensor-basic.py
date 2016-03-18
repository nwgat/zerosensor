# A simple program to test the driver

import sys
import time
import datetime
import HTU21DF

while True:
	sys.stdout = open('data', 'w')
	temp = HTU21DF.read_temperature()
	time.sleep(1)
	hum = HTU21DF.read_humidity()
	dtime = datetime.datetime.now()
	ans_time = time.mktime(dtime.timetuple())
	print "%.2f,%.2F" % (temp, hum,) ,ans_time
	#time.sleep(60)
	time.sleep(1)

