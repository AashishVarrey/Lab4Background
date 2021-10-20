#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import json

redled = 19
yellowled = 16
blueled = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(redled, GPIO.OUT)
GPIO.setup(yellowled, GPIO.OUT)
GPIO.setup(blueled, GPIO.OUT)

pwmr = GPIO.PWM(redled, 100)
pwmy = GPIO.PWM(yellowled, 100)
pwmb = GPIO.PWM(blueled, 100)

pwmr.start(0)
pwmy.start(0)
pwmb.start(0)

try: 
  while True:
    with open("Lab4.txt", 'r') as f:
      data = json.load(f)
    dutycycle = float(data['ledvalue'])
    if data['option'] == "red":
      pwmr.start(0)
      pwmr.ChangeDutyCycle(dutycycle)
      pwmy.stop()
      pwmb.stop()
    elif data['option'] == "yellow":
      pwmy.start(0)
      pwmy.ChangeDutyCycle(dutycycle)
      pwmr.stop()
      pwmb.stop()
    else:
      pwmb.start(0)
      pwmb.ChangeDutyCycle(dutycycle)
      pwmr.stop()
      pwmy.stop()      
    time.sleep(0.1)
except KeyboardInterrupt:
  pwmr.stop()
  pwmy.stop()
  pwmb.stop()
  GPIO.cleanup()



