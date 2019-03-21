import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
    

class Ultrasonic:
    def __init__(self, trigPin, echoPin):
        self.trigPin = trigPin
        self.echoPin = echoPin
        GPIO.setup(self.trigPin, GPIO.OUT)
        GPIO.setup(self.echoPin, GPIO.IN)

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