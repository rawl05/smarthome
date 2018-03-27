#Import libraries and respective class from the python files.
from flask import *
from auto_Main import auto_Class
from secu_Main import secu_Class
from ldr_input import ldr_Class
from time import sleep
import RPi.GPIO as GPIO
import random


#Set the Board Mode for GPIO.
GPIO.setmode(GPIO.BOARD)
ldr=12
state=0


#Create class objects
auto_Pi = auto_Class()
secu_Pi = secu_Class()
ldr_Pi = ldr_Class()

#Flask Web Framework
app = Flask(__name__)
@app.route("/")
def index():
        return render_template('index.html')

@app.route("/hall/<int:hall_state>", methods=['POST'])
def hall(hall_state):
        if hall_state == 0:
                auto_Pi.set_hall(1)
                hall_flag=0
        else :
                hall_flag=1
                auto_Pi.set_hall(0)


        return render_template('index.html')


@app.route("/lobby/<int:lobby_state>", methods=['POST'])
def lobby(lobby_state):
        if lobby_state == 0:
                auto_Pi.set_lobby(1)
                lobby_flag=0
        else :
                auto_Pi.set_lobby(0)
                lobby_flag=1
                
	return render_template('index.html')

@app.route("/room1/<int:room1_state>", methods=['POST'])
def room1(room1_state):
        if room1_state == 0:
                auto_Pi.set_room1(1)
                room1_flag=0
        else :
                auto_Pi.set_room1(0)
                room1_flag=1
                
	return render_template('index.html')

@app.route("/room2/<int:room2_state>", methods=['POST'])
def room2(room2_state):
        if room2_state == 0:
                auto_Pi.set_room2(1)
                room2_flag=0
        else :
                auto_Pi.set_room2(0)
                room2_flag=1
                
	return render_template('index.html')

@app.route("/loo/<int:loo_state>", methods=['POST'])
def loo(loo_state):
        if loo_state == 0:
                auto_Pi.set_loo(1)
                loo_flag=0
        else :
                auto_Pi.set_loo(0)
                loo_flag=1
                
	return render_template('index.html')

@app.route("/garage/<int:garage_state>", methods=['POST'])
def garage(garage_state):
        if garage_state == 0:
                auto_Pi.set_garage(1)
                garage_flag=0
        else :
                auto_Pi.set_garage(0)
                garage_flag=1
                
	return render_template('index.html')

@app.route("/tank/<int:tank_state>", methods=['POST'])
def tank(tank_state):
        if tank_state == 0:
                auto_Pi.set_tank(1)
                tank_flag=0
        else :
                auto_Pi.set_tank(0)
                tank_flag=1
                
	return render_template('index.html')

@app.route("/ac/<int:ac_state>", methods=['POST'])
def ac(ac_state):
        if ac_state == 0:
                auto_Pi.set_ac(1)
                ac_flag=0
        else :
                auto_Pi.set_ac(0)
                ac_flag=1
                
	return render_template('index.html')

@app.route("/all/<int:all_state>", methods=['POST'])
def all(all_state):
        if all_state == 0:
                auto_Pi.set_hall(1)
                auto_Pi.set_room1(1)
                auto_Pi.set_room2(1)
                auto_Pi.set_lobby(1)
                auto_Pi.set_loo(1)
                auto_Pi.set_garage(1)
        else :
                auto_Pi.set_hall(0)
                auto_Pi.set_room1(0)
                auto_Pi.set_room2(0)
                auto_Pi.set_lobby(0)
                auto_Pi.set_loo(0)
                auto_Pi.set_garage(0)
                
	return render_template('index.html')

@app.route("/alertin/<int:alertIndoor_state>", methods=['POST'])
def indoor(alertIndoor_state):
        if alertIndoor_state == 1:
                secu_Pi.set_alertled(1)
                
	return render_template('index.html')

@app.route('/profile')
def profile():
        def get_profile_values():
                while True:
                        profile = secu_Pi.get_profile()
                        yield('data: {0}\n\n'.format(profile))
                        sleep(0.05)
        return Response(get_profile_values(), mimetype='text/event-stream')

@app.route("/reset/<int:reset_state>", methods=['POST'])
def reset(reset_state):
        if reset_state == 1:
                auto_Pi.set_hall(1)
                auto_Pi.set_room1(1)
                auto_Pi.set_room2(1)
                auto_Pi.set_lobby(1)
                auto_Pi.set_loo(1)
                auto_Pi.set_garage(1)
                auto_Pi.set_tank(1)
                secu_Pi.set_alertled(0)
                
	return render_template('index.html')




			
			
