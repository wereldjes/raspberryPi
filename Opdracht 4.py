import RPi.GPIO as GPIO
import time

LED_PIN_26 = 26
LED_PIN_19 = 19
BUTTON_PIN_13 = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_26, GPIO.OUT)
GPIO.setup(LED_PIN_19, GPIO.OUT)
GPIO.setup(BUTTON_PIN_13, GPIO.IN, GPIO.PUD_DOWN)

while True:
    buttonState = GPIO.input(BUTTON_PIN_13)

    #Als button ingedrukt is, voer deze code uit
    if buttonState == GPIO.HIGH:
        #Led 19 gaat uit, Led 26 gaat aan voor 1.3 seconde en uit voor 0.7 seconde
        GPIO.output(LED_PIN_19, GPIO.LOW)
        GPIO.output(LED_PIN_26, GPIO.HIGH)
        time.sleep(1.3)
        GPIO.output(LED_PIN_26, GPIO.LOW)
        time.sleep(0.7)
    else:
        #Als de button net is ingedrukt, zet led 19 dan aan en 26 uit
        GPIO.output(LED_PIN_26, GPIO.LOW)
        GPIO.output(LED_PIN_19, GPIO.HIGH)
