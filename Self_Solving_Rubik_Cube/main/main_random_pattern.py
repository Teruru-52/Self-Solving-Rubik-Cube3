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

    """`状態の設定"""
    cur_mode = 'normal'
    
    while True:
      # 6面同色状態から各modeの状態に遷移させる
      next_mode = state.Select_mode(cur_mode)
      scrambled_state = state.Set_next_state(cur_mode, next_mode)

      """Phase2探索プログラムの動作確認"""
      search2 = search.Search2(scrambled_state)
      start = time.time()
      solution = search2.start_search()
      print(f"Phase1,2 Finished! ({time.time() - start:.5f} sec.)")
      if solution:
        print(f'Solution: "{solution}"')
        print("solution_length: ", len(solution.split()))
      else:
        print("Solution not found.")

      print("start solving")
      start = time.time()
      motor.Solve(solution)
      print(f"Solving Finished! ({time.time() - start:.5f} sec.)\n")
      sleep(3.0)
      cur_mode = next_mode

    motor.Cleanup()
    
  except KeyboardInterrupt:
    motor.Cleanup()