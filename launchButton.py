import RPi.GPIO as GPIO
import time
import subprocess
from subprocess import call
import os
import random


GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.OUT)
#GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(14, GPIO.IN)
GPIO.setup(24, GPIO.OUT)

GPIO.output(21, GPIO.LOW)
GPIO.output(24, GPIO.LOW)

while True:
        try:
                input_state = GPIO.input(15)
                if (GPIO.input(14) == 1):
                        GPIO.output(24, GPIO.HIGH)
                        if input_state == True:
                                print 'party started'
                                GPIO.output(21, GPIO.HIGH)
                                song =  random.choice(os.listdir('/home/pi/scripts/songs/'))
                                #call(['/usr/bin/cvlc', '--play-and-exit','/home/pi/scripts/songs/' +song])
                                call(['/usr/bin/cvlc', '-Z','/home/pi/scripts/playlist.xspf'])
                else:
                        GPIO.output(24, GPIO.LOW)

                if input_state == False:
                        GPIO.output(21, GPIO.LOW)

        except KeyboardInterrupt:
                GPIO.output(21, GPIO.LOW)
                GPIO.output(24, GPIO.LOW)
                break

};