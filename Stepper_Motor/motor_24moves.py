import a4988
import RPi.GPIO as GPIO
from time import sleep

class Motor:
    def __init__(self):
        self.motor_L = a4988.A4988(Pin_dir=26, Pin_step=19, Pin_enable = 20)
        self.motor_D = a4988.A4988(Pin_dir=6, Pin_step=13, Pin_enable = 21)
        self.motor_U = a4988.A4988(Pin_dir=0, Pin_step=5, Pin_enable = 16)
        self.motor_R = a4988.A4988(Pin_dir=27, Pin_step=17, Pin_enable = 1)
        self.motor_F = a4988.A4988(Pin_dir=10, Pin_step=22, Pin_enable = 7)
        self.motor_B = a4988.A4988(Pin_dir=9, Pin_step=11, Pin_enable = 8)

    def Solve(self, scramble):
        for move_name in scramble.split(" "):
            if move_name == "U":
                # print("U")
                self.motor_U.Step_CW(50)
            elif move_name == "U'":
                # print("U'")
                self.motor_U.Step_CCW(50)
            elif move_name == "U2":
                # print("U2")
                self.motor_U.Step_CW(100)

            elif move_name == "D":
                # print("D")
                self.motor_D.Step_CW(50)
            elif move_name == "D'":
                # print("D'")
                self.motor_D.Step_CCW(50)
            elif move_name == "D2":
                # print("D2")
                self.motor_D.Step_CW(100)

            elif move_name == "L":
                # print("L")
                self.motor_L.Step_CW(50)
            elif move_name == "L'":
                # print("L'")
                self.motor_L.Step_CCW(50)
            elif move_name == "L2":
                # print("L2")
                self.motor_L.Step_CW(100)

            elif move_name == "R":
                # print("R")
                self.motor_R.Step_CW(50)
            elif move_name == "R'":
                # print("R'")
                self.motor_R.Step_CCW(50)
            elif move_name == "R2":
                # print("R2")
                self.motor_R.Step_CW(100)

            elif move_name == "F":
                # print("F")
                self.motor_F.Step_CW(50)
            elif move_name == "F'":
                # print("F'")
                self.motor_F.Step_CCW(50)
            elif move_name == "F2":
                # print("F2")
                self.motor_F.Step_CW(100)

            elif move_name == "B":
                # print("B")
                self.motor_B.Step_CW(50)
            elif move_name == "B'":
                # print("B'")
                self.motor_B.Step_CCW(50)
            elif move_name == "B2":
                # print("B2")
                self.motor_B.Step_CW(100)

            else:
                print("no move_name")
            # sleep(0.1)

    def Cleanup(self):
        GPIO.cleanup()

if __name__ == '__main__':
    motors = Motor()

    ramdom_scramble = "B' R B U'"

    try:
        for _ in range(6):
            motors.Solve(ramdom_scramble)

    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        motors.Cleanup()
        print("\nexit program")