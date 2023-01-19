import RPi.GPIO as GPIO
import time

LED_PIN = [2, 3, 4, 17]
ARDUINO_PIN = [5, 6, 13, 19]
BLINK_SPEED = [100, 250, 500, 1000]
last_blink_time = [0, 0]
blinking_led = [[LED_PIN[0], BLINK_SPEED[2]], [LED_PIN[1], BLINK_SPEED[2]]]
temp_led = []

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN[0], GPIO.OUT)
GPIO.setup(LED_PIN[1], GPIO.OUT)
GPIO.setup(LED_PIN[2], GPIO.OUT)
GPIO.setup(LED_PIN[3], GPIO.OUT)
GPIO.output(LED_PIN[0], GPIO.LOW)
GPIO.output(LED_PIN[1], GPIO.LOW)
GPIO.output(LED_PIN[2], GPIO.LOW)
GPIO.output(LED_PIN[3], GPIO.LOW)
GPIO.setup(ARDUINO_PIN[0], GPIO.OUT)
GPIO.setup(ARDUINO_PIN[1], GPIO.OUT)
GPIO.setup(ARDUINO_PIN[2], GPIO.OUT)
GPIO.setup(ARDUINO_PIN[3], GPIO.OUT)


def millis():
    return time.time() * 1000



def blink(led_list, current_time):
    global last_blink_time

    if current_time - last_blink_time[0] >= led_list[0][1]:
        last_blink_time[0] = current_time
        GPIO.output(led_list[0][0], GPIO.HIGH) if GPIO.input(led_list[0][0]) == GPIO.LOW else GPIO.output(led_list[0][0], GPIO.LOW)

    if current_time - last_blink_time[1] >= led_list[1][1]:
        last_blink_time[1] = current_time
        GPIO.output(led_list[1][0], GPIO.HIGH) if GPIO.input(led_list[1][0]) == GPIO.LOW else GPIO.output(led_list[1][0], GPIO.LOW)


try:
    while True:
        currentTime = millis()

        if len(temp_led) == 0:
            if GPIO.input(ARDUINO_PIN[3]) == GPIO.HIGH:
                temp_led.append(LED_PIN[0])
            elif GPIO.input(ARDUINO_PIN[2]) == GPIO.HIGH:
                temp_led.append(LED_PIN[1])
            elif GPIO.input(ARDUINO_PIN[1]) == GPIO.HIGH:
                temp_led.append(LED_PIN[2])
            elif GPIO.input(ARDUINO_PIN[0]) == GPIO.HIGH:
                temp_led.append(LED_PIN[3])
        elif len(temp_led) == 1:
            if GPIO.input(ARDUINO_PIN[3]) == GPIO.HIGH:
                temp_led.append(BLINK_SPEED[0])
            elif GPIO.input(ARDUINO_PIN[2]) == GPIO.HIGH:
                temp_led.append(BLINK_SPEED[1])
            elif GPIO.input(ARDUINO_PIN[1]) == GPIO.HIGH:
                temp_led.append(BLINK_SPEED[2])
            elif GPIO.input(ARDUINO_PIN[0]) == GPIO.HIGH:
                temp_led.append(BLINK_SPEED[3])
        elif len(temp_led) == 2:
            x = [temp_led[0], temp_led[1]]
            blinking_led.insert(0, x)
            blinking_led.pop()
            temp_led.clear()
            GPIO.output(LED_PIN[0], GPIO.LOW)
            GPIO.output(LED_PIN[1], GPIO.LOW)
            GPIO.output(LED_PIN[2], GPIO.LOW)
            GPIO.output(LED_PIN[3], GPIO.LOW)

        time.sleep(0.5)
        print(blinking_led)
        blink(blinking_led, currentTime)

finally:
    GPIO.cleanup()
