import RPi.GPIO as GPIO
from time import sleep

class A4988:
    def __init__(self, Pin_dir, Pin_step, Pin_enable):
        self.mPin_dir = Pin_dir
        self.mPin_step = Pin_step
        self.mPin_enable = Pin_enable

        self.SetWaitTime(0.001)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.mPin_dir, GPIO.OUT)
        GPIO.setup(self.mPin_step, GPIO.OUT)
        GPIO.setup(self.mPin_enable, GPIO.OUT)

        GPIO.output(self.mPin_enable, GPIO.HIGH)

    def SetWaitTime(self, wait):
        self.mStep_wait = wait

    def Step_CW(self, step_count):
        GPIO.output(self.mPin_enable, GPIO.LOW)
        GPIO.output(self.mPin_dir, GPIO.LOW)
        for i in range(step_count):
            GPIO.output(self.mPin_step, GPIO.HIGH)
            sleep(self.mStep_wait)
            GPIO.output(self.mPin_step, GPIO.LOW)
            sleep(self.mStep_wait)
        GPIO.output(self.mPin_enable, GPIO.HIGH)

    def Step_CCW(self, step_count):
        GPIO.output(self.mPin_enable, GPIO.LOW)
        GPIO.output(self.mPin_dir, GPIO.HIGH)
        for i in range(step_count):
            GPIO.output(self.mPin_step, GPIO.HIGH)
            sleep(self.mStep_wait)
            GPIO.output(self.mPin_step, GPIO.LOW)
            sleep(self.mStep_wait)
        GPIO.output(self.mPin_enable, GPIO.HIGH)

    # def Velocity_Control(self):


    # def Cleanup(self):
    #     GPIO.cleanup()

if __name__ == '__main__':
    motor_L = A4988(Pin_dir=26, Pin_step=19, Pin_enable = 20)
    motor_D = A4988(Pin_dir=6, Pin_step=13, Pin_enable = 21)
    motor_U = A4988(Pin_dir=0, Pin_step=5, Pin_enable = 16)
    motor_R = A4988(Pin_dir=27, Pin_step=17, Pin_enable = 1)
    motor_F = A4988(Pin_dir=10, Pin_step=22, Pin_enable = 7)
    motor_B = A4988(Pin_dir=9, Pin_step=11, Pin_enable = 8)

    try:
        motor_F.Step_CW(50)
        motor_F.Step_CCW(50)
        motor_B.Step_CW(50)
        motor_B.Step_CCW(50)
        motor_U.Step_CW(50)
        motor_U.Step_CCW(50)
        motor_D.Step_CW(50)
        motor_D.Step_CCW(50)
        motor_R.Step_CW(50)
        motor_R.Step_CCW(50)
        motor_L.Step_CW(50)
        motor_L.Step_CCW(50)

    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        GPIO.cleanup()
        print("\nexit program")