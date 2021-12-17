import RPi.GPIO as GPIO
import time

BUTTON_PIN_26 = 26
BUTTON_PIN_19 = 19
SERVO_PIN_13 = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN_13, GPIO.OUT)
GPIO.setup(BUTTON_PIN_26, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN_19, GPIO.IN, GPIO.PUD_DOWN)
PWM = GPIO.PWM(SERVO_PIN_13, 50)
PWM.start(1)


def setAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(SERVO_PIN_13, True)
    print(duty)
    PWM.ChangeDutyCycle(duty)
    time.sleep(0.05)
    GPIO.output(SERVO_PIN_13, False)
    PWM.ChangeDutyCycle(0)


try:
    while True:
        buttonState19 = GPIO.input(BUTTON_PIN_19)
        buttonState26 = GPIO.input(BUTTON_PIN_26)

        if buttonState19 == GPIO.HIGH:
            for i in range(0, 120, 8):
                setAngle(i)

            for i in range(120, 0, -8):
                setAngle(i)

        if buttonState26 == GPIO.HIGH:
            for i in range(0, 120, 16):
                setAngle(i)

            for i in range(120, 0, -16):
                setAngle(i)
finally:
    GPIO.cleanup()
