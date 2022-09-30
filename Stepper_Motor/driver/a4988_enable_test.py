import RPi.GPIO as GPIO
from time import sleep

enable_D = 20
enable_L = 21
enable_U = 16
enable_R = 1
enable_B = 7
enable_F = 8

GPIO.setmode(GPIO.BCM)

GPIO.setup(enable_D, GPIO.OUT)
GPIO.setup(enable_L, GPIO.OUT)
GPIO.setup(enable_U, GPIO.OUT)
GPIO.setup(enable_F, GPIO.OUT)
GPIO.setup(enable_B, GPIO.OUT)
GPIO.setup(enable_R, GPIO.OUT)

if __name__ == '__main__':
    try:
        while True:
            GPIO.output(enable_D, 1)
            GPIO.output(enable_L, 1)
            GPIO.output(enable_U, 1)
            GPIO.output(enable_F, 1)
            GPIO.output(enable_B, 1)
            GPIO.output(enable_R, 1)

    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        GPIO.cleanup()
        print("\nexit program")