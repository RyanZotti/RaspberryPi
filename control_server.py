import tornado.ioloop
import tornado.web
import RPi.GPIO as GPIO
from time import sleep



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class PostHandler(tornado.web.RequestHandler):
    def post(self):
    	data_json = tornado.escape.json_decode(self.request.body)
    	command = data_json['command']
    	print(command)
    	if command['type'] == 'speed':
            speed = command['value']
            if speed == '1':
                motor.backward(25)
            elif speed == '2':
                motor.backward(50)
            elif speed == '3':
                motor.backward(75)
            elif speed == '4':
                motor.backward(100)
            elif speed == '5':
                motor.stop()
                GPIO.cleanup()
            elif speed == '6':
                motor.forward(25)
            elif speed == '7':
                motor.forward(50)
            elif speed == '8':
                motor.forward(75)
            elif speed == '9':
                motor.forward(100)
                print(speed)
        elif command['type'] == 'turn':
            turn = command['value']
            if turn == 'h':
                steering_motor.left(50)
                sleep(0.5)
                steering_motor.stop()
            elif turn == 'l':
                steering_motor.right(50)
                sleep(0.5)
                steering_motor.stop()
                print(turn)
        else:
            print('bad command')

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),(r"/post", PostHandler)
    ])

class Motor:

    def __init__(self, pinForward, pinBackward, pinControl):
        """ Initialize the motor with its control pins and start pulse-width
             modulation """

        self.pinForward = pinForward
        self.pinBackward = pinBackward
        self.pinControl = pinControl
        GPIO.setup(self.pinForward, GPIO.OUT)
        GPIO.setup(self.pinBackward, GPIO.OUT)
        GPIO.setup(self.pinControl, GPIO.OUT)
        self.pwm_forward = GPIO.PWM(self.pinForward, 100)
        self.pwm_backward = GPIO.PWM(self.pinBackward, 100)
        self.pwm_forward.start(0)
        self.pwm_backward.start(0)
        GPIO.output(self.pinControl,GPIO.HIGH) 

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

    def stop(self):
        """ Set the duty cycle of both control pins to zero to stop the motor. """

        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(0)

class SteeringMotor(Motor):

    def left(self,speed):
        self.forward(speed)

    def right(self,speed):
        self.backward(speed)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    GPIO.setmode(GPIO.BOARD)
    motor = Motor(16, 18, 22)
    steering_motor = SteeringMotor(19, 21, 23)
