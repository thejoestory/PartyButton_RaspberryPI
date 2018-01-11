
import subprocess
from subprocess import call
import RPi.GPIO as GPIO
import time
import sys


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#relay
GPIO.setup(21, GPIO.OUT)

#led light on green button
GPIO.setup(24, GPIO.OUT)


while True:
        if (GPIO.input(23) == True):
                print "kill switch pushed"
                call(['pkill', '-9','-f','vlc'])
                call(['pkill','-9','-f','launchButton.py'])
                call(['pkill', '-9','-f','vlc'])
                GPIO.output(24, GPIO.LOW)
                GPIO.output(21, GPIO.LOW)
                sys.exit()
        else:
                time.sleep(1)



};