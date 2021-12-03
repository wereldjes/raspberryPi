import RPi.GPIO as GPIO
import time

LED_PIN_26 = 26
LED_PIN_19 = 19
BUTTON_PIN_13 = 13
BUTTON_PIN_6 = 6
blinkTime = [1000, 700]             #Zet 2 verschillende knippertijden (1 en 0.7 seconden)
ledStatus = [GPIO.LOW, GPIO.LOW]    #Zet LEDs op uit

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_26, GPIO.OUT)
GPIO.setup(LED_PIN_19, GPIO.OUT)
GPIO.setup(BUTTON_PIN_13, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN_6, GPIO.IN, GPIO.PUD_DOWN)

#Geeft huidige tijd in seconden sinds "epoch"
def millis():
    return time.time() * 1000

#Zet laatste blink time gelijk aan millis() (dit is basically 0 bij het opstarten van de software)
lastBlinkTime = millis()


try:
    while True:
        currentTime = millis()

        buttonState13 = GPIO.input(BUTTON_PIN_13)
        buttonState6 = GPIO.input(BUTTON_PIN_6)
        GPIO.output(LED_PIN_19, ledStatus[0])
        GPIO.output(LED_PIN_26, ledStatus[1])

        if buttonState6 == GPIO.HIGH:
            if currentTime - lastBlinkTime >= blinkTime[0]:
                lastBlinkTime = currentTime
                ledStatus[0] = GPIO.HIGH if ledStatus[0] == GPIO.LOW else GPIO.LOW
        else:
            ledStatus[0] = GPIO.LOW

        if buttonState13 == GPIO.HIGH:
            if currentTime - lastBlinkTime >= blinkTime[1]:
                lastBlinkTime = currentTime
                ledStatus[1] = GPIO.HIGH if ledStatus[1] == GPIO.LOW else GPIO.LOW
        else:
            ledStatus[1] = GPIO.LOW
finally:
    GPIO.cleanup()
