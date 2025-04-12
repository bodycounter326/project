#!/usr/bin/env python

import sys
import time
# Add the path to the VL53L0X module
sys.path.insert(0, '/home/bak32/final-project/VL53L0X/python')

# Import VL53L0X module
import VL53L0X

def main():
    # Create a VL53L0X sensor object
    tof = VL53L0X.VL53L0X(i2c_bus=1,i2c_address=0x29)
    tof.open()
    # Start ranging
    tof.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)

    timing = tof.get_timing()
    if timing < 10000:
        timing = 10000
    print("Timing %d ms" % (timing/1000))

    while(True):
        distance = tof.get_distance()
        if distance > 0:
            print("%d mm, %d cm" % (distance, (distance/10)))
        time.sleep(timing/100000.00)

    tof.stop_ranging()
    tof.close()


if __name__ == "__main__":
    main()