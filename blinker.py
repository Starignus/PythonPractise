#!/usr/bin/env python


# External module imports GPIO
import RPi.GPIO as GPIO
# Library to slow or give a rest to the script
import time


# Pin definiton using Broadcom scheme
# PWM ("Analog")
pwmPin = 18  # Broadcom pin 18 (P1 pin 12)
# Led
ledPin = 23  # Broadcom pin 23 (P1 pin 16)
# Button
butPin = 17  # Broadcom pin 17 (P1 pin 11)

dc = 95  # duty cycle (0 i.e 0%/LOW and 100 ie.e 100%/HIGH) for PWM pin


# Pin Setup:
GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme
GPIO.setup(ledPin, GPIO.OUT)  # LED pin set as output
GPIO.setup(pwmPin, GPIO.OUT)  # PWM pin set as output
# PWM ("Analog") Output
pwm = GPIO.PWM(pwmPin, 50)  # Initialize PWM on pwmPin 100Hz frequency
# Button pin set as input w/ pull-up resistors
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# Initial state for LEDs:
GPIO.output(ledPin, GPIO.LOW)
# This function set an initial value of the frequency
pwm.start(dc)


print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        # The input() function will return either a True or False
        # indicating whether the pin is HIGH or LOW.
        if GPIO.input(butPin):  # button is released
            pwm.ChangeDutyCycle(dc)  # Adjust the value of the PWM output
            GPIO.output(ledPin, GPIO.LOW)
        else:  # button is pressed:
            pwm.ChangeDutyCycle(100-dc)
            GPIO.output(ledPin, GPIO.HIGH)
            # Delay of 75 milliseconds
            time.sleep(0.075)
            GPIO.output(ledPin, GPIO.LOW)
            # Delay of 75 milliseconds
            time.sleep(0.075)
except KeyboardInterrupt:  # If CTRL+C is pressed, exit cleanly:
    pwm.stop()  # stop PWM
    GPIO.cleanup()  # cleanup all GPIO
