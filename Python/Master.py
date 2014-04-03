from threading import Thread    ## import
import time, os

pi = 0 # 1 = running on pi, 0 = running in test mode
if os.path.exists("/dev/i2c-0"): # Am I runnin on a pi?
    pi = 1
    import smbus

if pi = 1:
    print "[INFO] Detected I2C. Running normally"
else
    print "[INFO] Did not detect I2C. Running in simulation mode"


class IOThread(Thread):
    def __init__(self):  ## to pass a variable to the class add here
        Thread.__init__(self)
        self.count = 0
        self.pressure = 0
        self.distance = 0
        self.LED = 1
    def pollpress():
        return pressure
    def setled(LED):
        
    def getdist():
        return distance
    def run(self):  ## dont need it here
        error = 0
        loopNum = 0
        while error == 0:  ## Main thread program using passed variable
            pollpress()
            getdist()
            print("Pressure",pressure)
            time.sleep(.005)
            while (count < 5):
                pollpress()
                setled(LED)
                count =+ 1
                LED = LED + 1
                print("LED",LED)
                print("distance",distance)
                time.sleep(.0057)
            count = 0
            LED = 1
            


tclass = IOThread() ## create instance
tclass.start() ## start class running










