#!/usr/bin/python
import time
import RPi.GPIO as GPIO

from . PCA9685 import PCA9685
#from . TSL2581 import TSL2581

def main(args=None):
    try:
        print ("Testing WaveShare Pan-Tilt_HAT")
        pwm = PCA9685()
        pwm.setPWMFreq(50)
        #pwm.setServoPulse(1,500) 
        pwm.setRotationAngle(0, 90)
        pwm.setRotationAngle(1, 90)
        
        time.sleep(1)

        #light = TSL2581(0X39, debug=False)
        #id = light.Read_ID() & 0xf0
        #print('ID = %#x'%id)
        #light.Init_TSL2581()

        for i in range(0,1,1):
            # setServoPulse(2,2500)
            for i in range(20,160,1): 
                pwm.setRotationAngle(1, i)
                time.sleep(0.1)

            pwm.setRotationAngle(1, 90)
            time.sleep(1)

            for i in range(140,30,-1): 
                pwm.setRotationAngle(0, i)
                time.sleep(0.1)
    
            pwm.setRotationAngle(0, 90)
            time.sleep(1)

            #lux  =  light.calculate_Lux()
            #print("lux = ", lux)
            #time.sleep(1)

        pwm.exit_PCA9685()
        print("\nTest finished")
        exit()


    except:
        pwm.exit_PCA9685()
        # GPIO.cleanup()
        print("\nProgram error")
        exit()


if __name__ == '__main__':
    main()