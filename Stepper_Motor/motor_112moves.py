import motors
import RPi.GPIO as GPIO
from time import sleep

if __name__ == '__main__':
    motor = motors.Motor()

    scramble = "R U R' D'"

    try:
        for _ in range(28):
            motor.Solve(scramble)

    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        motor.Cleanup()
        print("\nexit program")