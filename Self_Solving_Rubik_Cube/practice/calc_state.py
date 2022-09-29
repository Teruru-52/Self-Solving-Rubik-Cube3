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

# 完成状態における色情報
solved_cc = [['W','O','B'], ['W','B','R'], ['W','R','G'], ['W','G','O'], ['Y','B','O'], ['Y','R','B'], ['Y','G','R'], ['Y','O','G']]
solved_ec = [['B','O'], ['B','R'], ['G','R'], ['G','O'], ['W','B'], ['W','R'], ['W','G'], ['W','O'], ['Y','B'], ['Y','R'], ['Y','G'], ['Y','O']]

def color2state(state, cc, ec):
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
    print("cp =", state.cp)
    print("co =", state.co)
    print("ep =", state.ep)
    print("eo =", state.eo)

def random2state():
    random_scramble = "R2 D2 L D L' F2 U L F' R U2 R' D' B L D' B U2 B2 L2"
    state = scamble2state(random_scramble)
    print("cp =", state.cp)
    print("co =", state.co)
    print("ep =", state.ep)
    print("eo =", state.eo)

    # stateにおける色情報
    cc = [['Y','B','O'], ['O','G','Y'], ['B','Y','R'], ['O','B','W'], ['W','B','R'], ['R','Y','G'], ['G','O','W'], ['G','W','R']]
    ec = [['G','W'], ['G','R'], ['B','O'], ['Y','R'], ['G','O'], ['Y','G'], ['B','R'], ['Y','B'], ['W','O'], ['R','W'], ['Y','O'], ['W','B']]

    color2state(state, cc, ec)

def checker2state():
    # 適当なインスタンスを代入しておく
    state = solved_state

    # checker（全面）における色情報
    checker_cc = solved_cc
    checker_ec = [['G','R'], ['G','O'], ['B','O'], ['B','R'], ['Y','G'], ['Y','O'], ['Y','B'], ['Y','R'], ['W','G'], ['W','O'], ['W','B'], ['W','R']]

    color2state(state, checker_cc, checker_ec)

def checker2state2():
    # 適当なインスタンスを代入しておく
    state = solved_state

    # checker2（4面）における色情報
    checker2_cc = [['Y','O','G'], ['Y','G','R'], ['Y','R','B'], ['Y','B','O'], ['W','G','O'], ['W','R','G'], ['W','B','R'], ['W','O','B']]
    checker2_ec = solved_ec

    color2state(state, checker2_cc, checker2_ec)

def heso2state():
    # 適当なインスタンスを代入しておく
    state = solved_state

    # hesoにおける色情報
    heso_cc = [['R','B','Y'], ['R','Y','G'], ['R','G','W'], ['R','W','B'], ['O','Y','B'], ['O','G','Y'], ['O','W','G'], ['O','B','W']]
    heso_ec = [['Y','B'], ['Y','G'], ['W','G'], ['W','B'], ['R','Y'], ['R','G'], ['R','W'], ['R','B'], ['O','Y'], ['O','G'], ['O','W'], ['O','B']]

    color2state(state, heso_cc, heso_ec)

def H2state():
    # 適当なインスタンスを代入しておく
    state = solved_state

    # 6面Hにおける色情報
    H_cc = [['W','O','B'], ['W','B','R'], ['W','R','G'], ['W','G','O'], ['Y','B','O'], ['Y','R','B'], ['Y','G','R'], ['Y','O','G']]
    H_ec = [['B','R'], ['B','O'], ['G','O'], ['G','R'], ['W','G'], ['Y','R'], ['W','B'], ['Y','O'], ['Y','G'], ['W','R'], ['Y','B'], ['W','O']]

    color2state(state, H_cc, H_ec)

def T2state():
    # 適当なインスタンスを代入しておく
    state = solved_state

    # 6面Tにおける色情報
    T_cc = [['Y','R','B'], ['Y','G','R'], ['W','R','G'], ['W','B','R'], ['Y','B','O'], ['Y','O','G'], ['W','G','O'], ['W','O','B']]
    T_ec = [['B','R'], ['B','O'], ['G','O'], ['G','R'], ['W','G'], ['Y','R'], ['W','B'], ['Y','O'], ['Y','G'], ['W','R'], ['Y','B'], ['W','O']]

    color2state(state, T_cc, T_ec)

def cubeincube2state():
    # 適当なインスタンスを代入しておく
    state = solved_state

    # 6面Tにおける色情報
    cubeincube_cc = [['R','G','W'], ['W','B','R'], ['R','B','Y'], ['R','Y','G'], ['O','W','G'], ['O','B','W'], ['O','Y','B'], ['Y','O','G']]
    cubeincube_ec = [['W','G'], ['B','R'], ['Y','B'], ['G','O'], ['W','B'], ['W','R'], ['R','Y'], ['R','G'], ['O','W'], ['O','B'], ['Y','G'], ['Y','O']]

    color2state(state, cubeincube_cc, cubeincube_ec)

def mini_cubeincube2state():
    # 適当なインスタンスを代入しておく
    state = solved_state

    # 6面Tにおける色情報
    mini_cubeincube_cc = [['W','O','B'], ['R','W','B'], ['W','R','G'], ['W','G','O'], ['Y','B','O'], ['Y','R','B'], ['Y','G','R'], ['O','G','Y']]
    mini_cubeincube_ec = solved_ec

    color2state(state, mini_cubeincube_cc, mini_cubeincube_ec)

def vortex2state():
    # 適当なインスタンスを代入しておく
    state = solved_state

    # 6面Tにおける色情報
    vortex_cc = [['R','G','W'], ['W','B','R'], ['R','B','Y'], ['R','Y','G'], ['O','W','G'], ['O','B','W'], ['O','Y','B'], ['Y','O','G']]
    vortex_ec = [['W','G'], ['W','R'], ['Y','B'], ['Y','O'], ['R','B'], ['W','B'], ['R','Y'], ['R','G'], ['O','W'], ['O','B'], ['O','G'], ['Y','O']]

    color2state(state, vortex_cc, vortex_ec)

def vertical_stripe2state():
    # 適当なインスタンスを代入しておく
    state = solved_state

    # 6面Tにおける色情報
    vertical_stripe_cc = [['W','B','R'], ['W','O','B'], ['W','G','O'], ['W','R','G'], ['Y','R','B'], ['Y','B','O'], ['Y','O','G'], ['Y','G','R']]
    vertical_stripe_ec = [['R','B'], ['O','B'], ['O','G'], ['R','G'], ['W','B'], ['W','R'], ['W','G'], ['W','O'], ['Y','B'], ['Y','R'], ['Y','G'], ['Y','O']]

    color2state(state, vertical_stripe_cc, vertical_stripe_ec)

"""main関数"""
if __name__ == '__main__':
    # random2state()
    # checker2state()
    # checker2state2()
    # heso2state()
    # H2state()
    # T2state()
    # cubeincube2state()
    # mini_cubeincube2state()
    # vortex2state()
    vertical_stripe2state()