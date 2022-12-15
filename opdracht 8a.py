import RPi.GPIO as GPIO
import time

ARDUINO_LED_PIN_TWO = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(ARDUINO_LED_PIN_TWO, GPIO.OUT)


def ledBlink():
    GPIO.output(ARDUINO_LED_PIN_TWO, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(ARDUINO_LED_PIN_TWO, GPIO.LOW)
    time.sleep(1)


try:
    while True:
        ledBlink()
finally:
    GPIO.cleanup()
