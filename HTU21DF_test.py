# A simple program to test the driver

import time
import HTU21DF
import sys

sys.stdout=open("test.txt","w")

while True:
	print("sending reset...")
	HTU21DF.htu_reset
	temperature = HTU21DF.read_temperature()
	time.sleep(1)
	humidity = HTU21DF.read_humidity()
	print("The temperature is %f C." % temperature)
	print("The humidity is %F percent." % humidity)
	print time.strftime("%Y-%m-%d %H:%M")
	time.sleep(1)
