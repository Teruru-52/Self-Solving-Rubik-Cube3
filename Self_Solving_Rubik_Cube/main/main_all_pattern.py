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
    mode_scramble = []
    mode_scramble += ['normal']
    mode_scramble += ['H']
    mode_scramble += ['T']
    mode_scramble += ['checker']
    mode_scramble += ['vertical_stripe']
    mode_scramble += ['vortex']
    mode_scramble += ['heso']
    mode_scramble += ['checker2']
    mode_scramble += ['cubeincube']
    mode_scramble += ['mini_cubeincube']
    mode_scramble += ['cubeincubeincube']
    mode_scramble += ['angel_fish']
    mode_scramble += ['convex']
    mode_scramble += ['ring']
    mode_scramble += ['checker3']
    mode_scramble += ['normal']
    print(mode_scramble)

    for i in range(len(mode_scramble) - 1):
      # 6面同色状態から各modeの状態に遷移させる
      scrambled_state = state.Set_next_state(mode_scramble[i], mode_scramble[i + 1])

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
      sleep(1.5)

    motor.Cleanup()
    
  except KeyboardInterrupt:
    motor.Cleanup()