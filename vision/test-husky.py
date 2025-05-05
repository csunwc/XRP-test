# test the huskylens driver 
# qwiic_huskylens.py in the lib directory
# https://github.com/sparkfun/qwiic_huskylens_py
# test color recognizer algorithm
# https://wiki.dfrobot.com/HUSKYLENS_V1.0_SKU_SEN0305_SEN0336

import qwiic_huskylens
import qwiic_i2c
import sys
import time

def runExample():
    # get i2c driver: QwiicHuskylens( I2C address, i2c_driver )
    husky_addr = 0x32
    i2c_driver = qwiic_i2c.get_i2c_driver(sda=4, scl=5, freq=100000)
    ping = i2c_driver.ping(husky_addr)
    print("Husky ping:", ping )
    if ping==False :
        return  

    # get husky driver
    myHuskylens = qwiic_huskylens.QwiicHuskylens(husky_addr,i2c_driver)
    connected = myHuskylens.is_connected()
    print("Husky connected? ",  connected)
    if connected==False :
        return      

    # set detection algorithm - color
    myHuskylens.set_algorithm(myHuskylens.kAlgorithmColorRecognition)

    # read results
    nScans = 0
    while True:
        # This function will return a list of objects of interest that the device sees
        # In color recognition mode, these objects will be squares around matches to the colors we have learned
        myColors = myHuskylens.get_objects_of_interest()
        if len(myColors) == 0:
            print("No colors found")
        else:
            print("--New Colors Scan #{}--".format(nScans))
            for i, color in enumerate(myColors):
                print ("Color ID: " + str(color.id))
                print ("Color X: " + str(color.xCenter))
                print ("Color Y: " + str(color.yCenter))
                print ("Color Width: " + str(color.width))
                print ("Color Height: " + str(color.height))
                print("\n")
                nScans += 1
        time.sleep(2)  # sleep 2 sec


runExample()
