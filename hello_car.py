import RPi.GPIO as GPIO
from time import sleep 
import show_wifi_strength

enA=18
enB=13
in1=17
in2=27
in3=22
in4=25
red_pin = 21
green_pin = 20
blue_pin = 16

GPIO.setmode(GPIO.BCM)

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p_left=GPIO.PWM(enA,1000)
p_right = GPIO.PWM(enB,1000)

p_left.start(25)
p_right.start(25)

print("To control the car, type forward, back, left, right, stop.")
print("\n")

while(1):
    x = raw_input()

    show_wifi_strength.show_signal_strength(red_pin, blue_pin, green_pin)

    if x == 'forward':
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        p_left.ChangeDutyCycle(75)
        p_right.ChangeDutyCycle(75)
        x = 'wait'

    elif x == 'stop':
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        p_left.ChangeDutyCycle(25)
        p_right.ChangeDutyCycle(25)
        x = 'wait'

    elif x == 'left':
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        p_left.ChangeDutyCycle(100)
        p_right.ChangeDutyCycle(25)
        x = 'wait'
    
    elif x == 'right':
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        p_left.ChangeDutyCycle(25)
        p_right.ChangeDutyCycle(100)
        x = 'wait'

    elif x == 'back':
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        p_left.ChangeDutyCycle(75)
        p_right.ChangeDutyCycle(75)
        x = 'wait'

    elif x == 'exit':
        GPIO.cleanup()
        break

    else:
        print('wrong command, type go or stop.')
