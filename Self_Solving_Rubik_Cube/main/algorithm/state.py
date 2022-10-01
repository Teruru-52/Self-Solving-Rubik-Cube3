import random
from shutil import move
from functools import lru_cache
from algorithm import detect_color

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
initial_state = State(
    [0, 1, 2, 3, 4, 5, 6, 7],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
)

# 完成状態の変更 (random_scrambleにのみ適用)
# 各modeを完成状態としたときの6面同色状態を記述
def Set_initial_state(mode):
    print("mode: ", mode)
    if mode == 'checker':
        initial_state.ep = [2, 3, 0, 1, 10, 11, 8, 9, 6, 7, 4, 5]
    elif mode == 'checker2':
        initial_state.cp = [7, 6, 5, 4, 3, 2, 1, 0]
    elif mode == 'heso':
        initial_state.cp = [7, 3, 2, 6, 4, 0, 1, 5]
        initial_state.co = [1, 2, 1, 2, 2, 1, 2, 1]
        initial_state.ep = [11, 7, 5, 9, 3, 6, 2, 10, 0, 4, 1, 8]
        initial_state.eo = [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    elif mode == 'H':
        initial_state.ep = [1, 0, 3, 2, 6, 9, 4, 11, 10, 5, 8, 7]
    elif mode == 'T':
        initial_state.cp = [7, 3, 2, 6, 4, 0, 1, 5]
        initial_state.ep = [1, 0, 3, 2, 6, 9, 4, 11, 10, 5, 8, 7]
    elif mode == 'cubeincube':
        initial_state.cp = [5, 1, 0, 4, 6, 2, 3, 7]
        initial_state.co = [1, 0, 1, 2, 2, 1, 2, 0]
        initial_state.ep = [9, 1, 7, 3, 4, 5, 0, 8, 2, 6, 10, 11]
        initial_state.eo = [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]
    elif mode == 'mini_cubeincube':
        initial_state.co = [0, 2, 0, 0, 0, 0, 0, 1]
    elif mode == 'vortex': 
        initial_state.cp = [5, 1, 0, 4, 6, 2, 3, 7]
        initial_state.co = [1, 0, 1, 2, 2, 1, 2, 0]
        initial_state.ep = [9, 4, 7, 10, 5, 1, 0, 8, 2, 6, 10, 11]
        initial_state.eo = [1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0]
    elif mode == 'vertical_stripe':
        initial_state.cp = [1, 0, 3, 2, 5, 4, 7, 6]
        initial_state.ep = [1, 0, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11]
        initial_state.eo = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]

# 6面同色状態完成状態としたときの各modeを記述
def Reset_normal_state(mode):
    print("mode: ", mode)
    if mode == 'checker':
        initial_state.ep = [2, 3, 0, 1, 10, 11, 8, 9, 6, 7, 4, 5]
    elif mode == 'checker2':
        initial_state.cp = [7, 6, 5, 4, 3, 2, 1, 0]
    elif mode == 'heso':
        initial_state.cp = [5, 6, 2, 1, 4, 7, 3, 0]
        initial_state.co = [2, 1, 2, 1, 1, 2, 1, 2]
        initial_state.ep = [8, 10, 6, 4, 9, 2, 5, 1, 11, 3, 7, 0]
        initial_state.eo = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    elif mode == 'H':
        initial_state.ep = [1, 0, 3, 2, 6, 9, 4, 11, 10, 5, 8, 7]
    elif mode == 'T':
        initial_state.cp = [5, 6, 2, 1, 4, 7, 3, 0]
        initial_state.ep = [1, 0, 3, 2, 6, 9, 4, 11, 10, 5, 8, 7]
    elif mode == 'cubeincube':
        initial_state.cp = [2, 1, 5, 6, 3, 0, 4, 7]
        initial_state.co = [2, 0, 2, 1, 1, 2, 1, 0]
        initial_state.ep = [6, 1, 8, 3, 4, 5, 9, 2, 7, 0, 10, 11]
        initial_state.eo = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0]
    elif mode == 'mini_cubeincube':
        initial_state.co = [0, 1, 0, 0, 0, 0, 0, 2]
    elif mode == 'vortex': 
        initial_state.cp = [2, 1, 5, 6, 3, 0, 4, 7]
        initial_state.co = [2, 0, 2, 1, 1, 2, 1, 0]
        initial_state.ep = [6, 5, 8, 11, 1, 4, 9, 2, 7, 0, 3, 11]
        initial_state.eo = [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0]
    elif mode == 'vertical_stripe':
        initial_state.cp = [1, 0, 3, 2, 5, 4, 7, 6]
        initial_state.ep = [1, 0, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11]
        initial_state.eo = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    return initial_state


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
    scrambled_state = initial_state
    for move_name in scramble.split(" "):
        move_state = moves[move_name]
        scrambled_state = scrambled_state.apply_move(move_state)
    return scrambled_state

# 対面を引くdict
inv_face = {
    "U": "D",
    "D": "U",
    "L": "R",
    "R": "L",
    "F": "B",
    "B": "F"
}

@lru_cache(maxsize=400)
def is_move_available(prev_move, move):
    """
    前の1手を考慮して次の1手として使える操作であるかを判定する
    - 同じ面は連続して回さない (e.g. R' R2 は不可)
    - 対面を回すときは順序を固定する (e.g. D Uは良いが、U Dは不可)
    """
    if prev_move is None:
        return True  # 最初の1手はどの操作も可
    prev_face = prev_move[0]  # 1手前で回した面
    if prev_face == move[0]:
        return False # 同一面は不可
    if inv_face[prev_face] == move[0]:
        return prev_face < move[0] # 対面のときは、辞書順なら可
    return True

def Create_scramble(scramble_length):
    move_names = "U U' U2 D D' D2 L L' L2 R R' R2 F F' F2 B B' B2"
    random_scramble = ""
    prev_move = None
    for _ in range(scramble_length):
        flag = True
        while flag is True:
            move_name = random.choice(move_names.split())
            if is_move_available(prev_move, move_name):
                random_scramble += move_name + " "
                prev_move = move_name
                flag = False
    return random_scramble.strip()

def color2state(color_state):
    initial_state = State(
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    )

    solved_cc = [['W','O','B'], ['W','B','R'], ['W','R','G'], ['W','G','O'], ['Y','B','O'], ['Y','R','B'], ['Y','G','R'], ['Y','O','G']]
    solved_ec = [['B','O'], ['B','R'], ['G','R'], ['G','O'], ['W','B'], ['W','R'], ['W','G'], ['W','O'], ['Y','B'], ['Y','R'], ['Y','G'], ['Y','O']]
    solved_color_state = ColorState(solved_cc, solved_ec)

    for i in range(8):
        for j in range(8):
            if set(color_state.cc[i]) == set(solved_color_state.cc[j]):
                initial_state.cp[i] = j
                if color_state.cc[i] == solved_color_state.cc[j]:
                    initial_state.co[i] = 0
                else:
                    tmp = color_state.cc[i].pop(0)
                    color_state.cc[i].append(tmp)
                    if color_state.cc[i] == solved_color_state.cc[j]:
                        initial_state.co[i] = 1
                    else:
                        initial_state.co[i] = 2
                continue
    for i in range(12):
        for j in range(12):
            if set(color_state.ec[i]) == set(solved_color_state.ec[j]):
                initial_state.ep[i] = j
                if color_state.ec[i] == solved_color_state.ec[j]:
                    initial_state.eo[i] = 0
                else:
                    initial_state.eo[i] = 1
                continue
    return initial_state