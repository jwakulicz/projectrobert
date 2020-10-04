import RPi.GPIO as GPIO
import wifi_signal_strength as wifi_ss

def show_signal_strength(red_pin, blue_pin, green_pin):
    net_strengths = wifi_ss.get_wifi_signal_strength()
    
    for network in net_strengths:
        if network['Name'] == 'MPO':
            sig_str = network['Strength']
            
    if sig_str == 0:
        GPIO.output(red_pin, GPIO.HIGH)
        GPIO.output(blue_pin, GPIO.LOW)
        GPIO.output(green_pin, GPIO.LOW)
        
    elif 0 < sig_str <= 33:
        GPIO.output(red_pin, GPIO.HIGH)
        GPIO.output(blue_pin, GPIO.LOW)
        GPIO.output(green_pin, GPIO.HIGH)
    
    elif 33 < sig_str <= 66:
        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(blue_pin, GPIO.HIGH)
        GPIO.output(green_pin, GPIO.LOW)
    
    elif 66 < sig_str <= 100:
        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(blue_pin, GPIO.LOW)
        GPIO.output(green_pin, GPIO.HIGH)
         
            