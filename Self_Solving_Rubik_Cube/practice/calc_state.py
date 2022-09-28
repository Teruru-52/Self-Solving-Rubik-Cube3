# webcamから得た情報からstateを計算する

from shutil import move
from functools import lru_cache

class State:
    """
    ルービックキューブの状態を表すクラス
    """

    def __init__(self, cp, co, ep, eo):
        self.cp = cp
        self.co = co
        self.ep = ep
        self.eo = eo

    def apply_move(self, move):
        """
        操作を適用し、新しい状態を返す
        """
        new_cp = [self.cp[p] for p in move.cp]
        new_co = [(self.co[p] + move.co[i]) % 3 for i, p in enumerate(move.cp)]
        new_ep = [self.ep[p] for p in move.ep]
        new_eo = [(self.eo[p] + move.eo[i]) % 2 for i, p in enumerate(move.ep)]
        return State(new_cp, new_co, new_ep, new_eo)

# 完成状態を表すインスタンス
solved_state = State(
    [0, 1, 2, 3, 4, 5, 6, 7],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
)

# 18種類の1手操作を全部定義する
moves = {
    'U': State([3, 0, 1, 2, 4, 5, 6, 7],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 2, 3, 7, 4, 5, 6, 8, 9, 10, 11],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    'D': State([0, 1, 2, 3, 5, 6, 7, 4],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 8],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    'L': State([4, 1, 2, 0, 7, 5, 6, 3],
               [2, 0, 0, 1, 1, 0, 0, 2],
               [11, 1, 2, 7, 4, 5, 6, 0, 8, 9, 10, 3],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    'R': State([0, 2, 6, 3, 4, 1, 5, 7],
               [0, 1, 2, 0, 0, 2, 1, 0],
               [0, 5, 9, 3, 4, 2, 6, 7, 8, 1, 10, 11],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    'F': State([0, 1, 3, 7, 4, 5, 2, 6],
               [0, 0, 1, 2, 0, 0, 2, 1],
               [0, 1, 6, 10, 4, 5, 3, 7, 8, 9, 2, 11],
               [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0]),
    'B': State([1, 5, 2, 3, 0, 4, 6, 7],
               [1, 2, 0, 0, 2, 1, 0, 0],
               [4, 8, 2, 3, 1, 5, 6, 7, 0, 9, 10, 11],
               [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
               )}
move_names = []
faces = list(moves.keys())
for face_name in faces:
    move_names += [face_name, face_name + '2', face_name + '\'']
    moves[face_name + '2'] = moves[face_name].apply_move(moves[face_name])
    moves[face_name + '\''] = moves[face_name].apply_move(moves[face_name]).apply_move(moves[face_name])
# print(move_names)

def scamble2state(scramble):
    """
    スクランブル文字列適用したstateを返す
    """
    scrambled_state = solved_state
    for move_name in scramble.split(" "):
        move_state = moves[move_name]
        scrambled_state = scrambled_state.apply_move(move_state)
    return scrambled_state

"""main関数"""
if __name__ == '__main__':
    ramdom_scramble = "R2 D2 L D L' F2 U L F' R U2 R' D' B L D' B U2 B2 L2"
    state = scamble2state(ramdom_scramble)
    print("cp = ", state.cp)
    print("co = ", state.co)
    print("ep = ", state.ep)
    print("eo = ", state.eo)

    # 完成状態における色情報
    solved_cc = [['W','O','B'], ['W','B','R'], ['W','R','G'], ['W','G','O'], ['Y','B','O'], ['Y','R','B'], ['Y','G','R'], ['Y','O','G']]
    solved_ec = [['B','O'], ['B','R'], ['G','R'], ['G','O'], ['W','B'], ['W','R'], ['W','G'], ['W','O'], ['Y','B'], ['Y','R'], ['Y','G'], ['Y','O']]
    # stateにおける色情報
    cc = [['Y','B','O'], ['O','G','Y'], ['B','Y','R'], ['O','B','W'], ['W','B','R'], ['R','Y','G'], ['G','O','W'], ['G','W','R']]
    ec = [['G','W'], ['G','R'], ['B','O'], ['Y','R'], ['G','O'], ['Y','G'], ['B','R'], ['Y','B'], ['W','O'], ['R','W'], ['Y','O'], ['W','B']]
    
    for i in range(8):
        for j in range(8):
            if set(cc[i]) == set(solved_cc[j]):
                state.cp[i] = j
                if cc[i] == solved_cc[j]:
                    state.co[i] = 0
                else:
                    tmp = cc[i].pop(0)
                    cc[i].append(tmp)
                    if cc[i] == solved_cc[j]:
                        state.co[i] = 1
                    else:
                        state.co[i] = 2
                continue
    for i in range(12):
        for j in range(12):
            if set(ec[i]) == set(solved_ec[j]):
                state.ep[i] = j
                if ec[i] == solved_ec[j]:
                    state.eo[i] = 0
                else:
                    state.eo[i] = 1
                continue

    print("\n")
    print("cp = ", state.cp)
    print("co = ", state.co)
    print("ep = ", state.ep)
    print("eo = ", state.eo)