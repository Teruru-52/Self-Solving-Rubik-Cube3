import motors
import RPi.GPIO as GPIO
from time import sleep


if __name__ == '__main__':
    motor = motors.Motor()

    try:
        for _ in range(4):
            motor.Solve("R")
            sleep(0.3)
        for _ in range(4):
            motor.Solve("R'")
            sleep(0.3)
        for _ in range(2):
            motor.Solve("R2")
            sleep(0.3)

        sleep(0.5)
        
        for _ in range(4):
            motor.Solve("L")
            sleep(0.3)
        for _ in range(4):
            motor.Solve("L'")
            sleep(0.3)
        for _ in range(2):
            motor.Solve("L2")
            sleep(0.3)

        sleep(0.5)
        
        for _ in range(4):
            motor.Solve("F")
            sleep(0.3)
        for _ in range(4):
            motor.Solve("F'")
            sleep(0.3)
        for _ in range(2):
            motor.Solve("F2")
            sleep(0.3)

        sleep(0.5)
        
        for _ in range(4):
            motor.Solve("B")
            sleep(0.3)
        for _ in range(4):
            motor.Solve("B'")
            sleep(0.3)
        for _ in range(2):
            motor.Solve("B2")
            sleep(0.3)

        sleep(0.5)
        
        for _ in range(4):
            motor.Solve("U")
            sleep(0.3)
        for _ in range(4):
            motor.Solve("U'")
            sleep(0.3)
        for _ in range(2):
            motor.Solve("U2")
            sleep(0.3)

        sleep(0.5)
        
        for _ in range(4):
            motor.Solve("D")
            sleep(0.3)
        for _ in range(4):
            motor.Solve("D'")
            sleep(0.3)
        for _ in range(2):
            motor.Solve("D2")
            sleep(0.3)

    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        motor.Cleanup()
        print("\nexit program")