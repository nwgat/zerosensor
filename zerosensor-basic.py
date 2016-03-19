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

	# display
	print "%.2f,%.2F,"% (temp, hum,), ut # unix time
	#print "%0.2f, %0.2F,"% (temp, hum),st # standard time
	#print "%.2f, %.2F"%(temp, hum)

	# time delay for reading
	#time.sleep(60)
	time.sleep(4)

