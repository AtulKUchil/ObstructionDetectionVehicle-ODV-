import serial
import wiringpi as wp
import RPi.GPIO as GPIO
import time

wp.wiringPiSetupGpio()

wp.pinMode(2,1)
wp.pinMode(3,1)
wp.pinMode(4,1)
wp.pinMode(17,1)

uart_channel = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout = 2)
data1 = ""
data = ''
uart_channel.write("Ready for requests")

GPIO.setmode(GPIO.BOARD)

PIN_TRIGGER = 13
PIN_ECHO = 15

GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

GPIO.output(PIN_TRIGGER, GPIO.LOW)

print "Waiting for sensor to settle"

time.sleep(2)

print "Calculating distance"

GPIO.output(PIN_TRIGGER, GPIO.HIGH)
time.sleep(0.00001)
GPIO.output(PIN_TRIGGER, GPIO.LOW)
while GPIO.input(PIN_ECHO)==0:
    pulse_start_time = time.time()
while GPIO.input(PIN_ECHO)==1:
    pulse_end_time = time.time()

pulse_duration = pulse_end_time - pulse_start_time
distance = round(pulse_duration * 17150, 2)
#print(distance)

while True:

    data = uart_channel.read(1)
    data1=data.decode('utf-8')
    print(data1)    

    if(data1 == 'a'):
        wp.digitalWrite(2,0)
        wp.digitalWrite(3,1)
        wp.digitalWrite(4,0)
        wp.digitalWrite(17,1)
    if(data1 == 'b'):
        wp.digitalWrite(2,1)
        wp.digitalWrite(3,0)
        wp.digitalWrite(4,1)
        wp.digitalWrite(17,0)
    if(data1 == 'c'):
        wp.digitalWrite(2,0)
        wp.digitalWrite(3,1)
        wp.digitalWrite(4,1)
        wp.digitalWrite(17,0)
    if(data1 == 'd'):
        wp.digitalWrite(2,1)
        wp.digitalWrite(3,0)
        wp.digitalWrite(4,0)
        wp.digitalWrite(17,1)
    if(data1 == 'e'):
        wp.digitalWrite(2,0)
        wp.digitalWrite(3,0)
        wp.digitalWrite(4,0)
        wp.digitalWrite(17,0)

    uart_channel.flush()
    data = ""
    data1 = ""

    GPIO.output(PIN_TRIGGER, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    while GPIO.input(PIN_ECHO)==0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO)==1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    #uart_channel.write(distance)
    print "Distance:",distance,"cm"
    if(distance<60):
        wp.digitalWrite(2,0)
        wp.digitalWrite(3,0)
        wp.digitalWrite(4,0)
        wp.digitalWrite(17,0)
