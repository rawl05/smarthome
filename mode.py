from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
modeButton=38
powerLed=35
alertButton=40
autoButton=36
alertLed=37
indoorLed=31
outdoorLed=33
GPIO.setup(powerLed,GPIO.OUT)
GPIO.setup(alertLed,GPIO.OUT)
GPIO.setup(indoorLed,GPIO.OUT)
GPIO.setup(outdoorLed,GPIO.OUT)
GPIO.setup(alertButton,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(modeButton,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(autoButton,GPIO.IN,pull_up_down=GPIO.PUD_UP)
flag=0
try:
        
        while(1):
                GPIO.output(powerLed,1)
                if GPIO.input(modeButton)==0:
                        #sleep(0.7)
                        if flag==0:
                                print"Outdoor Profile Activated"
                		GPIO.output(outdoorLed,1)
                		GPIO.output(indoorLed,0)
                                sleep(0.5)
                		flag=1
                		while(GPIO.input(modeButton)!=0):
                                        if GPIO.input(autoButton)==0:
                                                sleep(0.5)
                                                print"Alarm Triggered"
                                                print"High Proximity Alert Activated!"
                                                blink=10
                                                sleep(2)
                                                if GPIO.input(modeButton)==0:
                                                        sleep(0.5)
                                                        print"Alarm Deactivated "
                                                        break
                                                sleep(2)
                                                if GPIO.input(modeButton)==0:
                                                        sleep(0.5)
                                                        print"Alarm Deactivated "
                                                        break
                                                sleep(2)
                                                if GPIO.input(modeButton)==0:
                                                        sleep(0.5)
                                                        print"Alarm Deactivated "
                                                        break
                                                sleep(2)
                                                if GPIO.input(modeButton)==0:
                                                        sleep(0.5)
                                                        print"Alarm Deactivated "
                                                        break
                                                sleep(2)
                                                if GPIO.input(modeButton)==0:
                                                        sleep(0.5)
                                                        print"Alarm Deactivated "
                                                        break
                                                sleep(2)
                                                if GPIO.input(modeButton)==0:
                                                        sleep(0.5)
                                                        print"Alarm Deactivated "
                                                        break      
                                                while(blink!=0):
                                                        GPIO.output(alertLed,1)
                                                        sleep(0.5)
                                                        GPIO.output(alertLed,0)
                                                        sleep(0.5)
                                                        blink=blink-1
                	else:
                        	count=0
                        	flag=0
        			print"Indoor Profile Activated"
                		GPIO.output(indoorLed,1)
                		GPIO.output(outdoorLed,0)
                		sleep(0.5)
                		while(GPIO.input(modeButton)!=0):
                                        if GPIO.input(alertButton)==0:
                                        	count=count+1
                                        	print"Alert Pressed: ",count
                                        	sleep(0.5)
                                        if count==3:
                                        	count=0
                                                blink=10
                                                print"High Proximity Alert Activated!"
                                        	while(blink!=0):
                                                	GPIO.output(alertLed,1)
                                                        sleep(0.5)
                                                        GPIO.output(alertLed,0)
                                                        sleep(0.5)
                                                        blink=blink-1
except KeyboardInterrupt:
        print"System Reset"
        GPIO.cleanup()
