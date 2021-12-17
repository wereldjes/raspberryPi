import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib as rpi

MOTOR_PINS = [13, 6, 5, 0]
BUTTON_PIN_26 = 26
BUTTON_PIN_19 = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN_26, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(BUTTON_PIN_19, GPIO.IN, GPIO.PUD_DOWN)
motor = rpi.BYJMotor("motor", "28BYJ")

try:
    while True:
        buttonState19 = GPIO.input(BUTTON_PIN_19)
        buttonState26 = GPIO.input(BUTTON_PIN_26)

        if buttonState19 == GPIO.HIGH:
            motor.motor_run(MOTOR_PINS, .001, 1, False, False, "half", 0)

        if buttonState26 == GPIO.HIGH:
            motor.motor_run(MOTOR_PINS, .002, 1, True, False, "half", 0)
finally:
    GPIO.cleanup()

