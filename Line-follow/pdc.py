# 5/2/25 - PD line follow with rangefinder stop
# note white surface reading ~=0, black surface reading ~=1
# thus on black line...
# if error <0, bot is too far left & need to turn right (left_m > right_m)
# same logic goes for delta-error (error - last error)
# -Charles Sun

from XRPLib.defaults import *
import time

# white: lower ret val ,  black: higher ret val
def check_sensor():
    while True:
        L = reflectance.get_left()
        R = reflectance.get_right()
        print( L , R , L-R)
        time.sleep(0.5)  # adjustment freq
    
    
def line_track():
    base_effort = 0.2 # original 0.6
    max_effort = 0.5 # max speed of motors
    min_effort = 0 # min allowed speed per wheel
    KP = 0.6  # proportional const - original 0.6
    KD = 0.1  # derivative const 
    last_error = 0; # for derivative term
    while True:
        # take the difference of the sensors, drift left means neg error 
        error = reflectance.get_left() - reflectance.get_right() 
        # compute effort
        effortL =  base_effort -(error * KP) - (error - last_error) * KD
        effortR = base_effort + (error * KP) + (error - last_error) * KD
        # constrain effort to be within limits but less than base_effort 
        # is okay to stop 1 wheel to allow sharp turn
        effortL = constrain(effortL, min_effort, max_effort)
        effortR = constrain(effortR, min_effort, max_effort)
        # drive motor (L,R)
        print(error, effortL, effortR)
        drivetrain.set_effort(effortL, effortR)
        #time.sleep(0.001)  # adjustment freq
        last_error = error # save last error for derivative term
        # stop if path blocked
        if rangefinder.distance() < 10 :  # detect 10 cm
            drivetrain.stop
            break


# limit range of output val
def constrain(val, min_val, max_val):
    if val < min_val: return min_val
    if val > max_val: return max_val
    return val


#check_sensor()
line_track()

