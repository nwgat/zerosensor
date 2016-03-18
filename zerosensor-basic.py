# zerosensor
# http://nwgat.ninja

import sys
import time
import datetime
import HTU21DF

while True:
	# output to file
	sys.stdout = open('data', 'a')

	temp = HTU21DF.read_temperature()
	time.sleep(1)
	hum = HTU21DF.read_humidity()

	# keeping time (unix time)
	#dtime = datetime.datetime.now()
	#ans_time = time.mktime(dtime.timetuple())

	# keeping time (standard)
	td = datetime.datetime.utcnow()

	# display
	#print "%.2f,%.2F" % (temp, hum,) ,ans_time
	print "%0.2f,%0.2F," % (temp, hum), td
	#print "%.2f,%.2F" % (temp, hum,)

	# sleep
	#time.sleep(60)
	time.sleep(1)

