import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
 

TRIG_LEFT = 23
ECHO_LEFT = 24

TRIG_RIGHT = 17
ECHO_RIGHT = 27


def setupUltrasonic(trigPin, echoPin):
	GPIO.setup(trigPin, GPIO.OUT)
	GPIO.setup(echoPin, GPIO.IN)
 
def distance(trigPin, echoPin):
    GPIO.output(trigPin, True)
 
    time.sleep(0.00001)
    GPIO.output(trigPin, False)
 
    startTime = time.time()
    stopTime = time.time()
 
    while GPIO.input(echoPin) == 0:
        startTime = time.time()
 
    while GPIO.input(echoPin) == 1:
        stopTime = time.time()
 
 
    timeElapsed = stopTime - startTime
    
    # function of ultrasonic wave speed
    distance = (timeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
    	setupUltrasonic(TRIG_LEFT, ECHO_LEFT)
    	setupUltrasonic(TRIG_RIGHT, ECHO_RIGHT)

        while True:
            leftDist = distance(TRIG_LEFT, ECHO_LEFT)
            print ("Measured Left Distance = %.1f cm" % leftDist)
            rightDist = distance(TRIG_RIGHT, ECHO_RIGHT)
            print ("Measured Right Distance = %.1f cm" % rightDist)
            time.sleep(1)
 
    except KeyboardInterrupt:
        GPIO.cleanup()