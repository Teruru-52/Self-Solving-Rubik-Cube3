from time import sleep

from hardware import motors
from algorithm import detect_color

"""main関数"""
if __name__ == '__main__':
    motor = motors.Motor()

    scramble = "D2 B U' R F' R D' F' L2 D' L R' B F2 R U R B L' B2"
    motor.Solve(scramble)
    # detect_color.Take_pictures()
    # detect_color.Set_train_data(1)

    scramble = "F2 L2 D' L2 U L U' R B2 U' L2 R2 D2 F' U F' D' B' D2 B'"
    motor.Solve(scramble)
    # detect_color.Take_pictures()
    # detect_color.Set_train_data(2)

    solution = "U2 F D' L F R2 D' B2 R U2 L2 F2 U L2 D' L2 F2 D' L2 F2 U' F2 D2"
    motor.Solve(solution)

    # Print_train_data()
