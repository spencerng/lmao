#!/usr/bin/python
import time
from threading import Thread
import RPi.GPIO as GPIO

# Ultrasonic time settings [s]
FULL_TIME_THRESH = 3.0  # time until a section is detected as full
REFRESH_TIME = 0.5  # frequency of polling the ultrasonic sensor

GPIO.setmode(GPIO.BCM)


class Ultrasonic:

    def __init__(self, trigPin, echoPin):
        self.trigPin = trigPin
        self.echoPin = echoPin
        GPIO.setup(self.trigPin, GPIO.OUT)
        GPIO.setup(self.echoPin, GPIO.IN)
        self.topTimeElapsed = 0.0
        self.bottomTimeElapsed = 0.0
        self.threads = []
        self.terminate = {'topTimer': False, 'bottomTimer': False}

    def timeTop(self):
        while True:
            if self.minTopDist <= self.distance() <= self.maxTopDist:
                self.topTimeElapsed += REFRESH_TIME
            else:
                self.topTimeElapsed = 0.0

            time.sleep(REFRESH_TIME)

            if self.terminate['topTimer']:
                return

    def timeBottom(self):
        while True:
            if self.minBottomDist <= self.distance() <= self.maxBottomDist or 1000 <= self.distance() <= 5000:
                self.bottomTimeElapsed += REFRESH_TIME
            else:
                self.bottomTimeElapsed = 0.0

            time.sleep(REFRESH_TIME)

            if self.terminate['bottomTimer']:
                return

    def killThread(self, threadName):
        for thread in self.threads:
            if thread.getName() == threadName:
                self.terminate[threadName] = True
                thread.join()
                self.terminate[threadName] = False
                self.threads.remove(thread)

    def setupTopTimer(self, minDist, maxDist):
        self.topTimeElapsed = 0.0
        self.minTopDist = minDist
        self.maxTopDist = maxDist

        self.killThread('topTimer')

        timer = Thread(target=self.timeTop, name='topTimer')
        self.threads.append(timer)
        timer.start()

    def setupBottomTimer(self, minDist, maxDist):
        self.bottomTimeElapsed = 0.0
        self.minBottomDist = minDist
        self.maxBottomDist = maxDist

        self.killThread('bottomTimer')

        timer = Thread(target=self.timeBottom, name='bottomTimer')
        self.threads.append(timer)
        timer.start()

    def getTopTimerReached(self):
        return self.topTimeElapsed >= FULL_TIME_THRESH

    def getBottomTimerReached(self):
        return self.bottomTimeElapsed >= FULL_TIME_THRESH

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
        distance = timeElapsed * 34300 / 2
        return distance
