import RPi.GPIO as GPIO
from time import sleep

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT)
    p=GPIO.PWM(en,1000)
    p.start(25)

def reverse(sec):
    init()
    GPIO.output(17, True)
    GPIO.output(22, True)
    GPIO.output(23, True)
    GPIO.output(24, False)
    sleep(sec)
    GPIO.cleanup()

def forward(sec):
    init()
    GPIO.output(17, True)
    GPIO.output(22, True)
    GPIO.output(23, False)
    GPIO.output(24, True)
    sleep(sec)
    GPIO.cleanup()

def left(sec):
    init()
    GPIO.output(17, False)
    GPIO.output(22, True)
    GPIO.output(23, True)
    GPIO.output(24, True)
    sleep(sec)
    GPIO.cleanup()
def right(sec):
    init()
    GPIO.output(17, True)
    GPIO.output(22, False)
    GPIO.output(23, True)
    GPIO.output(24, True)
    sleep(sec)
    GPIO.cleanup()
def rightfor(sec):
    init()
    GPIO.output(17, True)
    GPIO.output(22, False)
    GPIO.output(23, False)
    GPIO.output(24, True)
    sleep(sec)
    GPIO.cleanup()
    
rightfor(0.5)
