import RPi.GPIO as GPIO
import wifi_signal_strength as wifi_ss

def show_signal_strength(red_pin, blue_pin, green_pin):
    net_strengths = wifi_ss.get_wifi_strengths()
    
    for network in net_strengths:
        if network['Name'] == 'MPO':
            sig_str = network['Strength']
    
    print(sig_str)
            
    if sig_str == 0:
        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(blue_pin, GPIO.LOW)
        GPIO.output(green_pin, GPIO.LOW)
        
    elif 0 < sig_str <= 25:
        GPIO.output(red_pin, GPIO.HIGH)
        GPIO.output(blue_pin, GPIO.LOW)
        GPIO.output(green_pin, GPIO.LOW)
    
    elif 25 < sig_str <= 50:
        GPIO.output(red_pin, GPIO.HIGH)
        GPIO.output(blue_pin, GPIO.LOW)
        GPIO.output(green_pin, GPIO.HIGH)
    
    elif 50 < sig_str <= 75:
        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(blue_pin, GPIO.LOW)
        GPIO.output(green_pin, GPIO.HIGH)

    elif 75 < sig_str <= 100:
        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(blue_pin, GPIO.HIGH)
        GPIO.output(green_pin, GPIO.LOW)
         
            
def turn_off_led(red_pin, blue_pin, green_pin):
    GPIO.output(red_pin, GPIO.LOW)
    GPIO.output(blue_pin, GPIO.LOW)
    GPIO.output(green_pin, GPIO.LOW)