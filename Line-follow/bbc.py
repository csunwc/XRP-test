# 5/2/25 - line follow with bang-bang control -Charles Sun

from XRPLib.defaults import *
import time


def line_track():
    base_effort = 0.3 # min speed to get moving, dependent on battery voltage
    while True:
        error = reflectance.get_left() - reflectance.get_right() 
        # determine which side the robot is off the line
        if error < 0:
            # robot is off to the left, turn right
            drivetrain.set_effort(base_effort, 0)
        elif error > 0:
            # robot is off to the right, turn left
            drivetrain.set_effort(0, base_effort)
        else:
            # robot is on the line, go straight
            drivetrain.set_effort(base_effort, base_effort)
        # adjustment freq    
        #time.sleep(0.01)    
        # stop if path blocked
        if rangefinder.distance() < 10 :  # detect 10 cm
            drivetrain.stop()   
            break   
    

line_track()

    