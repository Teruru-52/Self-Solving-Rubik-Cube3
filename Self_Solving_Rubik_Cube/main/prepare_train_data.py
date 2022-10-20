from time import sleep

from hardware import motors
from algorithm import detect_color

"""main関数"""
if __name__ == '__main__':
    try:
        motor = motors.Motor()

        detect_color.Train_data('train', 1)
        motor.Solve("R L")
        detect_color.Train_data('train', 2)
        motor.Solve("R' L'")

        detect_color.Print_train_data()

        motor.Cleanup()

    except KeyboardInterrupt:
        motor.Cleanup()
