import motors
import RPi.GPIO as GPIO
from time import sleep

if __name__ == '__main__':
    motor = motors.Motor()
    try:
        while True:
            move = input()
            if move == 'r':
                motor.Solve("R")
            elif move == 't':
                motor.Solve("R2")
            elif move == 'e':
                motor.Solve("R'")
            elif move == 'l':
                motor.Solve("L")
            elif move == ';':
                motor.Solve("L2")
            elif move == 'k':
                motor.Solve("L'")
            elif move == 'f':
                motor.Solve("F")
            elif move == 'g':
                motor.Solve("F2")
            elif move == 'h':
                motor.Solve("F'")
            elif move == 'b':
                motor.Solve("B")
            elif move == 'n':
                motor.Solve("B2")
            elif move == 'v':
                motor.Solve("B'")
            elif move == 'u':
                motor.Solve("U")
            elif move == 'i':
                motor.Solve("U2")
            elif move == 'y':
                motor.Solve("U'")
            elif move == 's':
                motor.Solve("D")
            elif move == 'd':
                motor.Solve("D2")
            elif move == 'a':
                motor.Solve("D'")

    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    finally:
        motor.Cleanup()
        print("\nexit program")