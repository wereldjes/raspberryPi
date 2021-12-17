import RPi.GPIO as GPIO
import time

LED_PIN_26 = 26
LED_PIN_19 = 19
BUTTON_PIN_13 = 13
ledStatus = [GPIO.LOW, GPIO.LOW]
blinkTime = [1000, 1300, 700]

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_26, GPIO.OUT)
GPIO.setup(LED_PIN_19, GPIO.OUT)
GPIO.setup(BUTTON_PIN_13, GPIO.IN, GPIO.PUD_DOWN)

#Geeft huidige tijd in seconden sinds "epoch"
def millis():
    return time.time() * 1000

#Zet laatste blink time gelijk aan millis() (dit is basically 0 bij het opstarten van de software)
lastBlinkTime = millis()

try:
    while True:
        currentTime = millis()
        buttonState13 = GPIO.input(BUTTON_PIN_13)
        GPIO.output(LED_PIN_19, ledStatus[0])
        GPIO.output(LED_PIN_26, ledStatus[1])

        if buttonState13 == GPIO.HIGH:
            if currentTime - lastBlinkTime >= blinkTime[0]:
                lastBlinkTime = currentTime
                ledStatus[0] = GPIO.HIGH if ledStatus[0] == GPIO.LOW else GPIO.LOW
                ledStatus[1] = GPIO.LOW if ledStatus[0] == GPIO.HIGH else GPIO.HIGH
        else:
            if currentTime - lastBlinkTime >= blinkTime[1]:
                lastBlinkTime = currentTime
                ledStatus[0] = GPIO.HIGH
                ledStatus[1] = GPIO.LOW
            elif ledStatus[1] == GPIO.LOW and currentTime - lastBlinkTime >= blinkTime[2]:
                ledStatus[1] = GPIO.HIGH
                ledStatus[0] = GPIO.LOW

finally:
    GPIO.cleanup()
