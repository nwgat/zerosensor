# A simple program to test the driver

import sys
import time
import datetime
import HTU21DF

while True:
	temp hum ans_time = open('tmphum.txt', 'a')
	temp = HTU21DF.read_temperature()
	time.sleep(1)
	hum = HTU21DF.read_humidity()
	dtime = datetime.datetime.now()
	ans_time = time.mktime(dtime.timetuple())
	#print "%.2f,%.2F," % (temp, hum),dt
	#print "%.2f,%.2F" % (temp, hum)
	print "%.2f,%.2F" % (temp, hum,) ,ans_time
	#time.sleep(60)
	time.sleep(1)


import SimpleHTTPServer
import SocketServer

# minimal web server.  serves files relative to the
# current directory.

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()

