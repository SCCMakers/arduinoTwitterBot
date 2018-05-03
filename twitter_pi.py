#/usr/bin/env python

#twitterbot from www.makeuseof.com/tag/how-to-build-a-raspbery-pi-twitter-bot/

#serial from https://playground.arduino.cc/Interfacing/Python

#tweets to 
#SCC Maker Bot
#@sccmakerbot

try: #from https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    leftOut=15
    rightOut=16
    chan_list = [leftOut,rightOut]    # add as many channels as you want!
                           # you can tuples instead i.e.:
                           #   chan_list = (11,12)
    GPIO.setup(chan_list, GPIO.OUT)
    #state = GPIO.LOW
    #GPIO.output(channel, state) #set one pin to "state"
    #chan_list = [11,12]                             # also works with tuples
    GPIO.output(chan_list, GPIO.LOW)                # sets all to GPIO.LOW
    #GPIO.output(chan_list, (GPIO.HIGH, GPIO.LOW))   # sets first HIGH and second LOW
except:
    print "this is not a raspberry pi"
    
import sys
from twython import Twython
import serial
import time

CONSUMER_KEY=''
CONSUMER_SECRET=''#
ACCESS_KEY=''
ACCESS_SECRET=''

api=Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

ids=[]#

def robotDir(api):
    timeline=api.get_mentions_timeline()#gets all of my mentions
    #print timeline
    for tweet in timeline:
        if tweet['id'] in ids:
            print "already ran this"
            return False
        ids.append(tweet['id'])
        output = "thanks @"+tweet['user']['screen_name']+","
        words=tweet['text'].lower().split()
        if 'move' in words:
            GPIO.output(chan_list,GPIO.HIGH)
            output+= " i like to move it, move it"
        elif 'right' in words:
            GPIO.output(rightOut,GPIO.HIGH)
            output+= " you turn my head right round, right round"
        elif 'left' in words:
            GPIO.output(leftOut,GPIO.HIGH)
            output+= " heavens to mergatroid, exit stage left"
        elif 'stop' in words:
            GPIO.output(chan_list,GPIO.LOW)
            output+= " stop, in the name of love!"
        else:#not a command
            output+= " but that wasn't a command!"
        print output
        return output.encode('utf-8')#tweet['text'].encode('utf-8')

def readHashtag(api,tag):
    #searches all of twitter
    query=api.search(q=tag)#,result_type='recent')
    #print query
    for result in query['statuses']:
        return result['text'].encode('utf-8')
    return 'tweet to '+tag

def sendToArduino(string):
    #ser.write('testing')
    print len(string)
    for i in range(0,len(string),32):
        ser.write(string[i:i+32])#
        time.sleep(3)


#ser = serial.Serial('COM12', 9600)#windows
#ser = serial.Serial('/dev/tty.usbserial', 9600)#linux/mac
ser = serial.Serial('/dev/ttyACM0', 9600)#raspberryPi
time.sleep(2)#wait for arduino to reset

#api.update_status(status='Trying to become a real twitterbot #sccmakes')


while True:
#if True:
#for x in range(5):
    robotComm=robotDir(api)
    print ids
    if robotComm:
        sendToArduino(robotComm)
        api.update_status(status=robotComm)
    time.sleep(3)
    GPIO.output(chan_list,GPIO.LOW)
    sendToArduino(readHashtag(api,'#sccmakes'))
    time.sleep(8)
#sendToArduino('maximum number of characters is 140 I think, what do you think my friend? I think it is hard to write 140 characters sometimes. And yet we are almost there.')
#sendToArduino('arduino interface works!')

time.sleep(2)#wait for string to finish
ser.close()












#works
##timeline=api.get_home_timeline()
###print timeline
##for tweet in timeline:
##    mentions= tweet['entities']['user_mentions']
##    for mention in mentions:
##        print '@',mention['screen_name']
##    hashtags=tweet['entities'].get('hashtags')
##    for hashtag in hashtags:
##        print '#',hashtag['text']
##    #break


