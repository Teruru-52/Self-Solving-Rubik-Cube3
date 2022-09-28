import random

# 対面を引くdict
inv_face = {
    "U": "D",
    "D": "U",
    "L": "R",
    "R": "L",
    "F": "B",
    "B": "F"
}

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

    # random_scramble = " ".join(random.choices(move_names.split(), k=scramble_length))
    # return random_scramble

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

if __name__ == '__main__':
    random_scramble = Create_scramble(20)
    print("random_scramble = ", random_scramble)
    print("length = ", len(random_scramble.split()))