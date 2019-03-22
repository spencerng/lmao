import RPi.GPIO as GPIO
import time
 
# Ultrasonic time settings [s]
FULL_TIME_THRESH = 10.0
REFRESH_TIME = 0.1

GPIO.setmode(GPIO.BCM)

class Ultrasonic:
    def __init__(self, trigPin, echoPin):
        self.trigPin = trigPin
        self.echoPin = echoPin
        GPIO.setup(self.trigPin, GPIO.OUT)
        GPIO.setup(self.echoPin, GPIO.IN)

    def setupTopTimer(self, minDist, maxDist):
        self.topTimeElapsed = 0.0
        # use threading library here
        # create timer that increments once in range
        # resets once out of range
        # if time threshold is exceeded, set the appropriate flag to True
        # deletes old thread on previous call

    def setupBottomTimer(self, minDist, maxDist):
        self.bottomTimeElapsed = 0.0

    def getTopTimerReached(self):
        return False

    def getBottomTimerReached(self):
        return False

    def distance(self):
        GPIO.output(self.trigPin, True)
 
        time.sleep(0.00001)
        GPIO.output(self.trigPin, False)
 
        startTime = time.time()
        stopTime = time.time()
     
        while GPIO.input(self.echoPin) == 0:
            startTime = time.time()
     
        while GPIO.input(self.echoPin) == 1:
            stopTime = time.time()
     
     
        timeElapsed = stopTime - startTime
        
        # function of ultrasonic wave speed
        distance = (timeElapsed * 34300) / 2
     
        return distance