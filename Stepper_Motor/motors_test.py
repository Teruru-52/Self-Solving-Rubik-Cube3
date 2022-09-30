import motors
import RPi.GPIO as GPIO
from time import sleep


if __name__ == '__main__':
    motor = motors.Motor()

    random_scramble = "R2 D2 L D L' F2 U L F' R U2 R' D' B L D' B U2 B2 L2"
    solution = "U L2 U F' R2 U2 L D' L2 B U2 B2 U B2 D' R2 U' F2 U R2 D'"

    try:
        motor.Solve(random_scramble)
        sleep(2)
        motor.Solve(solution)

    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        motor.Cleanup()
        print("\nexit program")