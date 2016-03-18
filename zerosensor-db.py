#!/usr/bin/python

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
	
#	print "Temperature: %F C, Humidity: %f" % (temp, hum)
	
	# Write to DB
	doc = {"date": datetime.datetime.utcnow(),
	       "Temperature": temp,
	       "Humidity": hum}
	data.insert(doc)
	conn.close()
	time.sleep(60)
