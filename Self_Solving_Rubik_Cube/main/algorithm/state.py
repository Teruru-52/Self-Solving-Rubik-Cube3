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

# 6面同色状態を表すインスタンス
initial_state = State(
    [0, 1, 2, 3, 4, 5, 6, 7],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
)

normal_color_state = detect_color.ColorState(
    [['W','O','B'], ['W','B','R'], ['W','R','G'], ['W','G','O'], ['Y','B','O'], ['Y','R','B'], ['Y','G','R'], ['Y','O','G']],
    [['B','O'], ['B','R'], ['G','R'], ['G','O'], ['W','B'], ['W','R'], ['W','G'], ['W','O'], ['Y','B'], ['Y','R'], ['Y','G'], ['Y','O']]
)
checker_color_state = detect_color.ColorState(
    normal_color_state.cc,
    [['G','R'], ['G','O'], ['B','O'], ['B','R'], ['Y','G'], ['Y','O'], ['Y','B'], ['Y','R'], ['W','G'], ['W','O'], ['W','B'], ['W','R']]
)
checker2_color_state = detect_color.ColorState(
    [['Y','O','G'], ['Y','G','R'], ['Y','R','B'], ['Y','B','O'], ['W','G','O'], ['W','R','G'], ['W','B','R'], ['W','O','B']],
    normal_color_state.ec
)
heso_color_state = detect_color.ColorState(
    [['R','B','Y'], ['R','Y','G'], ['R','G','W'], ['R','W','B'], ['O','Y','B'], ['O','G','Y'], ['O','W','G'], ['O','B','W']],
    [['Y','B'], ['Y','G'], ['W','G'], ['W','B'], ['R','Y'], ['R','G'], ['R','W'], ['R','B'], ['O','Y'], ['O','G'], ['O','W'], ['O','B']]
)
H_color_state = detect_color.ColorState(
    [['W','O','B'], ['W','B','R'], ['W','R','G'], ['W','G','O'], ['Y','B','O'], ['Y','R','B'], ['Y','G','R'], ['Y','O','G']],
    [['B','R'], ['B','O'], ['G','O'], ['G','R'], ['W','G'], ['Y','R'], ['W','B'], ['Y','O'], ['Y','G'], ['W','R'], ['Y','B'], ['W','O']]
)
T_color_state = detect_color.ColorState(
    [['Y','R','B'], ['Y','G','R'], ['W','R','G'], ['W','B','R'], ['Y','B','O'], ['Y','O','G'], ['W','G','O'], ['W','O','B']],
    [['B','R'], ['B','O'], ['G','O'], ['G','R'], ['W','G'], ['Y','R'], ['W','B'], ['Y','O'], ['Y','G'], ['W','R'], ['Y','B'], ['W','O']]
)
cubeincube_color_state = detect_color.ColorState(
    [['R','G','W'], ['W','B','R'], ['R','B','Y'], ['R','Y','G'], ['O','W','G'], ['O','B','W'], ['O','Y','B'], ['Y','O','G']],
    [['W','G'], ['B','R'], ['Y','B'], ['G','O'], ['W','B'], ['W','R'], ['R','Y'], ['R','G'], ['O','W'], ['O','B'], ['Y','G'], ['Y','O']]
)
mini_cubeincube_color_state = detect_color.ColorState(
    [['W','O','B'], ['R','W','B'], ['W','R','G'], ['W','G','O'], ['Y','B','O'], ['Y','R','B'], ['Y','G','R'], ['O','G','Y']],
    normal_color_state.ec
)
vortex_color_state = detect_color.ColorState(
    [['R','G','W'], ['W','B','R'], ['R','B','Y'], ['R','Y','G'], ['O','W','G'], ['O','B','W'], ['O','Y','B'], ['Y','O','G']],
    [['W','G'], ['W','R'], ['Y','B'], ['Y','O'], ['R','B'], ['W','B'], ['R','Y'], ['R','G'], ['O','W'], ['O','B'], ['O','G'], ['Y','O']]
)
vertical_stripe_color_state = detect_color.ColorState(
    [['W','B','R'], ['W','O','B'], ['W','G','O'], ['W','R','G'], ['Y','R','B'], ['Y','B','O'], ['Y','O','G'], ['Y','G','R']],
    [['R','B'], ['O','B'], ['O','G'], ['R','G'], ['W','B'], ['W','R'], ['W','G'], ['W','O'], ['Y','B'], ['Y','R'], ['Y','G'], ['Y','O']]
)
solved_color_state = normal_color_state

def Set_state(mode): 
    if mode == 'normal':
        color_state = normal_color_state
    elif mode == 'checker':
        color_state = checker_color_state
    elif mode == 'checker2':
        color_state = checker2_color_state
    elif mode == 'heso':
        color_state = heso_color_state
    elif mode == 'H':
        color_state = H_color_state
    elif mode == 'T':
        color_state = T_color_state
    elif mode == 'cubeincube':
        color_state = cubeincube_color_state
    elif mode == 'mini_cubeincube':
        color_state = mini_cubeincube_color_state
    elif mode == 'vortex': 
        color_state = vortex_color_state
    elif mode == 'vertical_stripe':
        color_state = vertical_stripe_color_state
    return color_state

# 次の状態を完成状態としたときの各modeの状態を求める
def Set_next_state(cur_mode, next_mode):
    print("mode: ", next_mode)
    current_color_state = Set_state(cur_mode)
    next_color_state = Set_state(next_mode)
    initial_state = color2state(current_color_state, next_color_state)
    return initial_state

# 画像からの色状態と各modeの色状態から，各modeの状態を求める
def Set_solved_state(mode, current_color_state):
    print("mode: ", mode)
    solved_color_state = Set_state(mode)
    initial_state = color2state(current_color_state, solved_color_state)
    print("cp =", initial_state.cp)
    print("co =", initial_state.co)
    print("ep =", initial_state.ep)
    print("eo =", initial_state.eo)
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

def color2state(current_color_state, solved_color_state):
    for i in range(8):
        for j in range(8):
            if set(current_color_state.cc[i]) == set(solved_color_state.cc[j]):
                initial_state.cp[i] = j
                if current_color_state.cc[i] == solved_color_state.cc[j]:
                    initial_state.co[i] = 0
                else:
                    tmp = current_color_state.cc[i].pop(0)
                    current_color_state.cc[i].append(tmp)
                    if current_color_state.cc[i] == solved_color_state.cc[j]:
                        initial_state.co[i] = 1
                    else:
                        initial_state.co[i] = 2
                continue
    for i in range(12):
        for j in range(12):
            if set(current_color_state.ec[i]) == set(solved_color_state.ec[j]):
                initial_state.ep[i] = j
                if current_color_state.ec[i] == solved_color_state.ec[j]:
                    initial_state.eo[i] = 0
                else:
                    initial_state.eo[i] = 1
                continue
    return initial_state