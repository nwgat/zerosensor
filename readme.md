this web app is based on @dalexgray and @randymxj awesome example code 

this has been tested with a Pi Zero, Raspbian and Sparkfun HTU21 Sensor

# go to home
cd /home/pi/

# install pigpio

`git clone https://github.com/joan2937/pigpio && cd pigpio`
`make && make install`
`sudo pigpiod`

# install dalexgray's htu21 libary

`git clone https://github.com/dalexgray/RaspberryPI_HTU21DF`
`cd RaspberryPI_HTU21DF && python HTU21DF.py install`

# install zerosensor

`git clone https://github.com/nwgat/zerosensor``
`python zerosensor-basic.py` (basicly logs to data file with format `temp,sensor,unixtime`
`python zerosensor-db.py` (logs to mongodb`
`python zerosensor-serve-py` (logs to file, http server with zingchart)
