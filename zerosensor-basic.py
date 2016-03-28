# zerosensor
# http://nwgat.ninja

import sys
import arrow
import time
import HTU21DF

while True:
	# output to file
	sys.stdout = open('html/data', 'a')

	# sensor reading
	temp = HTU21DF.read_temperature()
	time.sleep(1)
	hum = HTU21DF.read_humidity()

	# arrow on time
	local = arrow.now()

	# keeping time (standard)
	st = arrow.now()

        # keeping time (unix time)
        ut = local.timestamp

	# format in unix time
	#print "%.2f,%.2F,"% (temp, hum,), ut 

	# format in standard time
	#print "%0.2f, %0.2F,"% (temp, hum),st

	# display as temp,humidity only
	print "%.2f, %.2F"%(temp, hum)

	# time delay for reading from sensors
	#time.sleep(60)
	time.sleep(4)

