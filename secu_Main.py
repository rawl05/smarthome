from time import sleep
import RPi.GPIO as GPIO

powerled=35
alertled=37
indoorled=31
outdoorled=33
modeButton=38
alertButton=40
autoButton=36




class secu_Class(object):
       
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(powerled,GPIO.OUT)
        GPIO.setup(alertled,GPIO.OUT)
        GPIO.setup(indoorled,GPIO.OUT)
        GPIO.setup(outdoorled,GPIO.OUT)
        GPIO.setup(alertButton,GPIO.IN,pull_up_down=GPIO.PUD_UP)
        GPIO.setup(modeButton,GPIO.IN)
        GPIO.setup(autoButton,GPIO.IN,pull_up_down=GPIO.PUD_UP)
        
        

    def set_powerled(self,value):
            GPIO.output(powerled,value)

    def set_indoorled(self,value):
        GPIO.output(indoorled,value)

    def set_outdoorled(self,value):
        GPIO.output(outdoorled,value)

    def set_alertled(self,value):
        GPIO.output(alertled,value)

    def get_profile(self):
        sleep(0.1)
        return GPIO.input(modeButton)


    
            
           

    
