import RPi.GPIO as GPIO
from time import sleep

hall  =3
lobby =5
room1 =7
room2 =11
loo   =13
tank  =19
garage=15
ac=21
allswitch=40

class auto_Class(object):

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(allswitch,GPIO.IN)
        GPIO.setup(hall,GPIO.OUT)
        GPIO.setup(lobby,GPIO.OUT)
        GPIO.setup(room1,GPIO.OUT)
        GPIO.setup(room2,GPIO.OUT)
        GPIO.setup(loo,GPIO.OUT)
        GPIO.setup(garage,GPIO.OUT)
        GPIO.setup(tank,GPIO.OUT)
        GPIO.setup(ac,GPIO.OUT)
        sleep(1)
        GPIO.output(hall,1)
        GPIO.output(lobby,1)
        GPIO.output(room1,1)
        GPIO.output(room2,1)
        GPIO.output(loo,1)
        GPIO.output(garage,1)
        GPIO.output(tank,1)
        GPIO.output(ac,1)

    def read_allswitch(self):
        return GPIO.input(allswitch)

    def set_hall(self, value):
        GPIO.output(hall,value)

    def set_lobby(self, value):
        GPIO.output(lobby,value)

    def set_room1(self, value):
        GPIO.output(room1,value)

    def set_room2(self, value):
        GPIO.output(room2,value)

    def set_loo(self, value):
        GPIO.output(loo,value)

    def set_garage(self, value):
        GPIO.output(garage,value)

    def set_tank(self, value):
        GPIO.output(tank,value)

    def set_ac(self, value):
        GPIO.output(ac,value)
