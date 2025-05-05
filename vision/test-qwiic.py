# test qwiic lib
# https://github.com/sparkfun/Qwiic_I2C_Py

import qwiic_i2c

# get I2C bus driver
my_bus = qwiic_i2c.get_i2c_driver(sda=4, scl=5, freq=100000)

# Perform scan of I2C bus
devices = my_bus.scan()
print("Bus scan:", devices)

# check if Husky w/ ID=50 is connected
print("Husky ping:", my_bus.ping(50))

