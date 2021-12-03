import RPi.GPIO as GPIO
import time

LED_PIN_26 = 26
LED_PIN_19 = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_26, GPIO.OUT)
GPIO.setup(LED_PIN_19, GPIO.OUT)

while True:
    #Zet pin 26 aan voor 1.3 seconde en zet hem uit voor 0.7 seconde
    GPIO.output(LED_PIN_26, GPIO.HIGH)
    time.sleep(1.3)
    GPIO.output(LED_PIN_26, GPIO.LOW)
    time.sleep(0.7)
    #Zet pin 19 aan voor 0.8 seconde en zet hem uit voor 1.7 seconde
    GPIO.output(LED_PIN_19, GPIO.HIGH)
    time.sleep(0.8)
    GPIO.output(LED_PIN_19, GPIO.LOW)
    time.sleep(1.7)
