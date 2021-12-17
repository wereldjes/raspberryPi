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

        #Check of button 1 is ingedrukt
        if buttonState6 == GPIO.HIGH:
            #Huidige tijd - laatste knippertijd moet groter dan of gelijk aan de knippertijd zijn
            if currentTime - lastBlinkTime >= blinkTime[0]:
                lastBlinkTime = currentTime
                #Zet de led aan als deze op uit staat, als hij aan staat zet hem dan uit
                ledStatus[0] = GPIO.HIGH if ledStatus[0] == GPIO.LOW else GPIO.LOW
        else:
            ledStatus[0] = GPIO.LOW

        #Check of button 2 is ingedrukt
        if buttonState13 == GPIO.HIGH:
            # Huidige tijd - laatste knippertijd moet groter dan of gelijk aan de knippertijd zijn
            if currentTime - lastBlinkTime >= blinkTime[1]:
                lastBlinkTime = currentTime
                # Zet de led aan als deze op uit staat, als hij aan staat zet hem dan uit
                ledStatus[1] = GPIO.HIGH if ledStatus[1] == GPIO.LOW else GPIO.LOW
        else:
            ledStatus[1] = GPIO.LOW
finally:
    GPIO.cleanup()
