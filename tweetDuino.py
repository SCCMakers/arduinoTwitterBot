#/usr/bin/env python

#twitterbot from www.makeuseof.com/tag/how-to-build-a-raspbery-pi-twitter-bot/

#serial from https://playground.arduino.cc/Interfacing/Python

#tweets to 
#SCC Maker Bot
#@sccmakerbot

import sys
from twython import Twython
import serial

CONSUMER_KEY='tu95NAQI6enOYyFL5tjxmCIag'
CONSUMER_SECRET='VAqhyDSLAwHGanBPxPmA28HCoNc6V1dZLt23ML5xQLuQDpFkj1'
ACCESS_KEY='933492700216561664-0kcjfYbiAVmg3B2FkljWJpqz15k5bw8'
ACCESS_SECRET='V3ApGModi1oE3odhSUEZ0Me3xJdiP8nbeV1MLSW9G1KmR'

api=Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#api.update_status(status='fourth python tweet! #sccmakes') 

#ser = serial.Serial('COM3', 9600)#windows check com port in arduino software
#ser = serial.Serial('/dev/tty.usbserial', 9600)#linux/mac
ser = serial.Serial('/dev/ttyACM0', 9600)#raspberryPi

while True:
    print ser.readline()

