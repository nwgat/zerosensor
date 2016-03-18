this web app is based on @dalexgray and @randymxj awesome example code 
its been tested on a Pi Zero, Raspbian and Sparkfun HTU21 Sensor

**go to home**
* `cd /home/pi/`

**Install pigpio**

* `git clone https://github.com/joan2937/pigpio && cd pigpio`
* `make && make install`
* `sudo pigpiod`

* **Install dalexgray's htu21 libary and get zerosensor**
* `git clone https://github.com/nwgat/zerosensor``
* `git clone https://github.com/dalexgray/RaspberryPI_HTU21DF`
* `cp RaspberryPI_HTU21DF/HTU21DF.py zerosensor/`
* `cd zerosensor && python HTU21DF.py install`

**Run zerosensor**
* `cd $home/zerosensor`
* `python zerosensor-basic.py &` (basicly logs to data file with format `temp,sensor,unixtime`
* `python zerosensor-db.py &` (logs to mongodb)


**Start a web server**
* `cd html`
* `python -m SimpleHTTPServer 80`
