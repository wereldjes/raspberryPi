import RPi.GPIO as GPIO
import time

LED_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

#Zet pin 26 aan en uit met een snelheid van 0.1 seconde
while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.1)
