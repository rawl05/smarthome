import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
ldr=12
flag=0


while KeyboardInterrupt:
    count=0
    GPIO.setup(ldr,GPIO.OUT)
    GPIO.output(ldr,GPIO.LOW)
    sleep(1)
    GPIO.setup(ldr,GPIO.IN)
    while(GPIO.input(ldr)==GPIO.LOW):
        count=count+1
    print count
    sleep(0.5)
    if(count>4000):
        if(flag==0):
            print"ON"
        flag=1
        
    else:
        if(flag==1):
            print"OFF"
        flag=0
