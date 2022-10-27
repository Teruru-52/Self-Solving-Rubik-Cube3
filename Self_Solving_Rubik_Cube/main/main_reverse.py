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

    """scrambled_stateの生成"""
    """1. 完成状態からrandomに回してstateを求める場合"""
    random_scramble = "L D2 U2 B2 F2 R U B2 U2 L2 D L2 R2 U' F2 D2 R2 D' F2 R2"
    scrambled_state = state.scamble2state(random_scramble)

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