#!/usr/bin/python

# zerosensor
# http://nwgat.ninja

import HTU21DF
import time
import traceback
import pymongo
import datetime

import sys

# Connection to Mongo DB
conn=pymongo.MongoClient()
db = conn.HTU21
data = db.sensor
		
while True:
	temp = HTU21DF.read_temperature()
	hum = HTU21DF.read_humidity()
	
	# keeping time (unix time)
        dtime = datetime.datetime.now()
        ans_time = time.mktime(dtime.timetuple())
	
	# Write to DB
	doc = {"Date": datetime.datetime.utcnow(),
	       "Timestamp": ans_time,
	       "Temperature": temp,
	       "Humidity": hum}
	data.insert(doc)
	conn.close()

	# time delay for reading
	#time.sleep(60)
	time.sleep(1)
