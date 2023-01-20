import RPi.GPIO as GPIO

LED_ONE = 2
LED_TWO = 3
ARDUINO_CONNECTOR = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_ONE, GPIO.OUT)
GPIO.setup(LED_TWO, GPIO.OUT)
GPIO.setup(ARDUINO_CONNECTOR, GPIO.OUT)

try:
    while True:
        if GPIO.input(ARDUINO_CONNECTOR) == GPIO.HIGH:
            print("test1")
            GPIO.output(LED_ONE, GPIO.HIGH)
            GPIO.output(LED_TWO, GPIO.LOW)
        elif GPIO.input(ARDUINO_CONNECTOR) == GPIO.LOW:
            print("test2")
            GPIO.output(LED_ONE, GPIO.LOW)
            GPIO.output(LED_TWO, GPIO.HIGH)
finally:
    GPIO.cleanup()
