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
    mode = 'normal'
    # 2回繰り返すと元に戻る
    # mode = 'checker'
    # mode = 'checker2'
    # mode = 'H'
    # mode = 'vertical_stripe'
    # 3回繰り返すと元に戻る
    # mode = 'heso'
    mode = 'checker3'
    # mode = 'cubeincube'
    # mode = 'mini_cubeincube'
    # mode = 'cubeincubeincube'
    # 6回繰り返すと元に戻る
    # mode = 'T'
    # mode = 'vortex'
    
    # mode = 'angel_fish'
    # mode = 'convex'
    # mode = 'ring'

    """scrambled_stateの生成"""
    """1. 完成状態からrandomに回してstateを求める場合"""
    # state.Set_next_state('normal', mode)
    # scramble_length = 20
    # random_scramble = state.Create_scramble(scramble_length)
    # print("random_scramble: ", random_scramble)
    # print('start scrambling')
    # motor.Solve(random_scramble)
    # scrambled_state = state.scamble2state(random_scramble)

    """2.1 6面同色状態から模様の状態にする"""
    # scrambled_state = state.Set_next_state('normal', mode)

    """2.2 模様の状態から6面同色状態に戻す"""
    scrambled_state = state.Set_next_state(mode, 'normal')

    """3. Webcamで画像を撮影し, stateを求める場合"""
    # detect_color.Take_pictures()
    # color_state = detect_color.Get_color_state()
    # scrambled_state = state.Set_solved_state(mode, color_state)
    # print("scrambled_state: ", scrambled_state)

    """Phase2探索プログラムの動作確認"""
    search2 = search.Search2(scrambled_state)
    start = time.time()
    solution = search2.start_search()
    print(f"Phase1,2 Finished! ({time.time() - start:.5f} sec.)")
    if solution:
      print(f'Solution: "{solution}"')
    else:
      print("Solution not found.")

    print("start solving")
    start = time.time()
    motor.Solve(solution)
    print(f"Solving Finished! ({time.time() - start:.5f} sec.)")
    motor.Cleanup()
    
  except KeyboardInterrupt:
    motor.Cleanup()