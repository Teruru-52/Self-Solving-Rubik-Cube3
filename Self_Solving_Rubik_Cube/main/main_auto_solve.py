import random
from shutil import move
import time 
from time import sleep
import cv2
from hardware import motors
from algorithm import state
from algorithm import search
from algorithm import detect_color

"""main関数"""
if __name__ == '__main__':
  try:
    motor = motors.Motor()

    """完成状態の設定"""
    # vortexは未検証
    mode = 'normal'
    # mode = 'checker'
    # mode = 'checker2'
    # mode = 'H'
    # mode = 'vertical_stripe'
    # mode = 'heso'
    # mode = 'cubeincube'
    # mode = 'mini_cubeincube'
    # mode = 'T'

    """randomに回す場合"""
    # scramble_length = 40
    # random_scramble = state.Create_scramble(scramble_length)
    # print("random_scramble: ", random_scramble)
    # print('start scrambling')
    # motor.Solve(random_scramble)

    """Webcamで画像を撮影し, scrambled_stateを求める"""
    print('start detecting colors')
    detect_color.Detect_color_state(1)
    motor.Solve("R L")
    detect_color.Detect_color_state(2)
    motor.Solve("R' L' F B")
    detect_color.Detect_color_state(3)
    motor.Solve("F' B'")
    # color_state = detect_color.Get_color_state()
    # scrambled_state = state.Set_solved_state(mode, color_state)
    # print("scrambled_state: ", scrambled_state)

    """Phase2探索プログラムの動作確認"""
    # search2 = search.Search2(scrambled_state)
    # start = time.time()
    # solution = search2.start_search()
    # print(f"Phase1,2 Finished! ({time.time() - start:.5f} sec.)")
    # if solution:
    #   print(f'Solution: "{solution}"')
    # else:
    #   print("Solution not found.")

    # print("start solving")
    # start = time.time()
    # motor.Solve(solution)
    # print(f"Solving Finished! ({time.time() - start:.5f} sec.)")
    # sleep(0.5)

    motor.Cleanup()
    
  except KeyboardInterrupt:
    motor.Cleanup()