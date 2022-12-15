import RPi.GPIO as GPIO
import time

LED_PIN = [2, 3]
blinkTime = [1000, 3000]
ledStatus = [GPIO.LOW, GPIO.LOW]

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN[0], GPIO.OUT)
GPIO.setup(LED_PIN[1], GPIO.OUT)


def millis():
    return time.time() * 1000


lastBlinkTime = [millis(), millis()]


try:
    while True:
        currentTime = millis()
        GPIO.output(LED_PIN[0], ledStatus[0])
        GPIO.output(LED_PIN[1], ledStatus[1])

        if currentTime - lastBlinkTime[0] >= blinkTime[0]:
            lastBlinkTime[0] = currentTime
            ledStatus[0] = GPIO.HIGH if ledStatus[0] == GPIO.LOW else GPIO.LOW

        if currentTime - lastBlinkTime[1] >= blinkTime[1]:
            lastBlinkTime[1] = currentTime
            ledStatus[1] = GPIO.HIGH if ledStatus[1] == GPIO.LOW else GPIO.LOW
finally:
    GPIO.cleanup()
