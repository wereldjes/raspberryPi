import RPi.GPIO as GPIO
import time

LED_PIN_26 = 26
LED_PIN_19 = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_26, GPIO.OUT)
GPIO.setup(LED_PIN_19, GPIO.OUT)

while True:
    GPIO.output(LED_PIN_26, GPIO.HIGH)
    time.sleep(1.3)
    GPIO.output(LED_PIN_26, GPIO.LOW)
    time.sleep(0.7)
    GPIO.output(LED_PIN_19, GPIO.HIGH)
    time.sleep(0.8)
    GPIO.output(LED_PIN_19, GPIO.LOW)
    time.sleep(1.7)
