#/usr/bin/env python

#twitterbot from www.makeuseof.com/tag/how-to-build-a-raspbery-pi-twitter-bot/

#serial from https://playground.arduino.cc/Interfacing/Python

#tweets to 
#SCC Maker Bot
#@sccmakerbot

import sys
from twython import Twython
import serial

CONSUMER_KEY='key here'
CONSUMER_SECRET='secret here'
ACCESS_KEY='key here'
ACCESS_SECRET='secret here'

api=Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#api.update_status(status='fourth python tweet! #sccmakes') 

#ser = serial.Serial('COM3', 9600)#windows check com port in arduino software
#ser = serial.Serial('/dev/tty.usbserial', 9600)#linux/mac
ser = serial.Serial('/dev/ttyACM0', 9600)#raspberryPi

while True:
    print ser.readline()

