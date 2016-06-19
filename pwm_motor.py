import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)

class Motor:

    def __init__(self, pinForward, pinBackward, pinControlStraight,pinLeft, pinRight, pinControlSteering):
        """ Initialize the motor with its control pins and start pulse-width
             modulation """

        self.pinForward = pinForward
        self.pinBackward = pinBackward
        self.pinControlStraight = pinControlStraight
        self.pinLeft = pinLeft
        self.pinRight = pinRight
        self.pinControlSteering = pinControlSteering
        GPIO.setup(self.pinForward, GPIO.OUT)
        GPIO.setup(self.pinBackward, GPIO.OUT)
        GPIO.setup(self.pinControlStraight, GPIO.OUT)

        GPIO.setup(self.pinLeft, GPIO.OUT)
        GPIO.setup(self.pinRight, GPIO.OUT)
        GPIO.setup(self.pinControlSteering, GPIO.OUT)

        self.pwm_forward = GPIO.PWM(self.pinForward, 100)
        self.pwm_backward = GPIO.PWM(self.pinBackward, 100)
        self.pwm_forward.start(0)
        self.pwm_backward.start(0)

        self.pwm_left = GPIO.PWM(self.pinLeft, 100)
        self.pwm_right = GPIO.PWM(self.pinRight, 100)
        self.pwm_left.start(0)
        self.pwm_right.start(0)

        GPIO.output(self.pinControlStraight,GPIO.HIGH) 
        GPIO.output(self.pinControlSteering,GPIO.HIGH) 

    def forward(self, speed):
        """ pinForward is the forward Pin, so we change its duty
             cycle according to speed. """
        self.pwm_backward.ChangeDutyCycle(0)
        self.pwm_forward.ChangeDutyCycle(speed)    

    def backward(self, speed):
        """ pinBackward is the forward Pin, so we change its duty
             cycle according to speed. """

        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(speed)


    def left(self, speed):
        """ pinForward is the forward Pin, so we change its duty
             cycle according to speed. """
        self.pwm_right.ChangeDutyCycle(0)
        self.pwm_left.ChangeDutyCycle(speed)  

    def right(self, speed):
        """ pinForward is the forward Pin, so we change its duty
             cycle according to speed. """
        self.pwm_left.ChangeDutyCycle(0)
        self.pwm_right.ChangeDutyCycle(speed)   

    def stop(self):
        """ Set the duty cycle of both control pins to zero to stop the motor. """

        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(0)

class SteeringMotor(Motor):

    def left(self,speed):
        self.forward(speed)

    def right(self,speed):
        self.backward(speed)

motor = Motor(16, 18, 22, 19, 21, 23)
motor.left(50)
motor.forward(50)
sleep(1)
motor.stop()

GPIO.cleanup()
