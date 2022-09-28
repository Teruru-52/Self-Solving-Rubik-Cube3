import random
from shutil import move
import time 
from time import sleep
from hardware import motors
from algorithm import state
from algorithm import search

"""main関数"""
if __name__ == '__main__':
    """scrambleの生成"""
    scramble_length = 20
    random_scramble = state.Create_scramble(scramble_length)
    print("random_scramble = ", random_scramble)

    """モータ動作"""
    print('start scrambling')
    sleep(1)
    motor = motors.Motor()
    motor.Solve(random_scramble)

    # """Phase1探索プログラムの動作確認"""
    # scrambled_state = state.scamble2state(random_scramble)
    # search1 = search.Search1(scrambled_state)
    # start = time.time()
    # solution = search1.start_search()
    # print(f"Phase1 Finished! ({time.time() - start:.5f} sec.)")
    # if solution:
    #   print(f'Phase1 Solution: "{solution}"')
    # else:
    #   print("Solution not found.")

    """Phase2探索プログラムの動作確認"""
    scrambled_state = state.scamble2state(random_scramble)
    search2 = search.Search2(scrambled_state)
    start = time.time()
    solution = search2.start_search()
    print(f"Phase1,2 Finished! ({time.time() - start:.5f} sec.)")
    if solution:
      print(f'Solution: "{solution}"')
    else:
      print("Solution not found.")

    """モータ動作"""
    print("start solving")
    sleep(1)
    start = time.time()
    motor.Solve(solution)
    print(f"Solving Finished! ({time.time() - start:.5f} sec.)")
    motor.Cleanup()