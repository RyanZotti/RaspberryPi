import RPi.GPIO as GPIO
import time

# So that I can refer to pin names. At least that's what the book says
GPIO.setmode(GPIO.BCM)

led_pin = 18
GPIO.setup(led_pin,GPIO.OUT)
try:
    for i in range(10):
    	print("On")
        GPIO.output(led_pin,True) # LED on
        time.sleep(0.5) # delay for 0.5 seconds
        print("Off")
        GPIO.output(led_pin, False) # LED off
        time.sleep(0.5)  # delay for 0.5 seconds
finally:
    print("Cleaning up.")
    GPIO.cleanup()
    print("Finished.")
