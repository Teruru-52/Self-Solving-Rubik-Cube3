import random
from shutil import move
import time 
from time import sleep
from hardware import motors
from algorithm import state

"""main関数"""
if __name__ == '__main__':
  try:
    motor = motors.Motor()

    """random"""
    scramble_length = 40
    random_scramble = state.Create_scramble(scramble_length)
    print("random_scramble: ", random_scramble)
    print('start scrambling')
    motor.Solve(random_scramble)

    motor.Cleanup()
    
  except KeyboardInterrupt:
    motor.Cleanup()