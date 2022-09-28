import RPi.GPIO as GPIO
from time import sleep

# motor_D(yellow)
direction = 6
step = 13
enable_D = 20
# motor_L(orenge)
# direction = 26
# step = 19
enable_L = 21
# motor_U(white)
# direction = 0
# step = 5
enable_U = 16
# motor_R(red)
# direction = 27
# step = 17
enable_R = 1

# direction = 10
# step = 22

enable_B = 8
enable_F = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(direction, GPIO.OUT)
GPIO.setup(step, GPIO.OUT)
GPIO.setup(enable_D, GPIO.OUT)
GPIO.setup(enable_L, GPIO.OUT)
GPIO.setup(enable_U, GPIO.OUT)
GPIO.setup(enable_F, GPIO.OUT)
GPIO.setup(enable_B, GPIO.OUT)
GPIO.setup(enable_R, GPIO.OUT)
GPIO.output(direction, 1)
GPIO.output(enable_D, 0)
GPIO.output(enable_L, 1)
GPIO.output(enable_U, 1)
GPIO.output(enable_F, 1)
GPIO.output(enable_B, 1)
GPIO.output(enable_R, 1)

delay = .001

for x in range(50):
    GPIO.output(step, GPIO.HIGH)
    sleep(delay)
    GPIO.output(step, GPIO.LOW)
    sleep(delay)

GPIO.output(enable_D, 1)
sleep(.5)
GPIO.output(direction, 0)
GPIO.output(enable_D, 0)

for x in range(50):
    GPIO.output(step, GPIO.HIGH)
    sleep(delay)
    GPIO.output(step, GPIO.LOW)
    sleep(delay)

GPIO.output(enable_D, 1)
GPIO.cleanup()