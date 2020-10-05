import RPi.GPIO as GPIO

class Robert:
    def __init__(self):
        self.enA = 18
        self.enB = 13
        self.in1 = 17
        self.in2 = 27
        self.in3 = 22
        self.in4 = 25
        self.red_pin = 21
        self.green_pin = 20
        self.blue_pin = 16
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.setup(self.blue_pin, GPIO.OUT)
        GPIO.setup(self.green_pin, GPIO.OUT)

        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(self.in3,GPIO.OUT)
        GPIO.setup(self.in4,GPIO.OUT)
        GPIO.setup(self.enA,GPIO.OUT)
        GPIO.setup(self.enB,GPIO.OUT)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.LOW)
        self.p_left = GPIO.PWM(self.enA,1000)
        self.p_right = GPIO.PWM(self.enB,1000)    
        self.p_left.start(25)
        self.p_right.start(25)
        print("pins initialised")
            


    def forward(self):
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.HIGH)
        GPIO.output(self.in4,GPIO.LOW)
        self.p_left.ChangeDutyCycle(75)
        self.p_right.ChangeDutyCycle(75)


    def stop(self):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.LOW)
        self.p_left.ChangeDutyCycle(25)
        self.p_right.ChangeDutyCycle(25)

    def exit(self):
        GPIO.cleanup()
        print("pins cleaned")

    def left(self):
        self.p_left.ChangeDutyCycle(100)
        self.p_right.ChangeDutyCycle(25)
    
    def right(self):
        self.p_left.ChangeDutyCycle(25)
        self.p_right.ChangeDutyCycle(100)

    def backward(self):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)
        self.p_left.ChangeDutyCycle(75)
        self.p_right.ChangeDutyCycle(75)

