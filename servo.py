#!/usr/bin/python

import RPi.GPIO as GPIO
import time

class Servo():
    
    def start(self, pos):
        GPIO.setup(11,GPIO.OUT)
        self.pwm=GPIO.PWM(11,50)
        self.pwm.start(pos)
        time.sleep(0.5)

    def stop(self):
        self.pwm.stop()
        GPIO.cleanup()

    def full_left(self):
        self.set_pos(self.MAX_LEFT)

    def full_right(self):
        self.set_pos(self.MAX_RIGHT)

    def neutral(self):
        self.set_pos(self.NEUTRAL)

    def neutral_right(self):
        self.set_pos(self.NEUTRAL_RIGHT)

    def neutral_left(self):
        self.set_pos(self.NEUTRAL_LEFT)

    def set_pos(self, pos):
        self.start(pos)
        #self.pwm.ChangeDutyCycle(pos)
        #time.sleep(0.3)
        self.stop()
        time.sleep(0.5)

class y3009(Servo):
     def __init__(self):
        self.MAX_LEFT = 14.5
        self.MAX_RIGHT = 2.5
        self.MIDDLE = (self.MAX_LEFT-self.MAX_RIGHT)/2
        GPIO.setmode(GPIO.BOARD)

class HS475HB(Servo):    
    def __init__(self):
        self.MAX_LEFT = 1.5
        self.MAX_RIGHT = 17
        self.NEUTRAL = 9.5 
        self.NEUTRAL_RIGHT = self.NEUTRAL + 3 
        self.NEUTRAL_LEFT = self.NEUTRAL - 3
        self.MIDDLE = abs(self.MAX_LEFT-self.MAX_RIGHT)/2
        GPIO.setmode(GPIO.BOARD)

       


if __name__ == "__main__":
    
    def servo_test():
        servo = HS475HB()
        servo.full_right()
        servo.full_left()
    
    def card_test():
        #servo = y3009()
        servo = HS475HB()
        servo.neutral()
        servo.neutral_right()
        servo.neutral()
        servo.neutral_left()
        servo.neutral()

    #servo_test()
    card_test()
