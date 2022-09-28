import time 
from algorithm import state

from tables import co_table
from tables import eo_table
from tables import e_table
from tables import cp_table
from tables import e_ep_table
from tables import ud_ep_table
from tables import co_eec_table
from tables import cp_eep_table
from tables import eo_eec_table
from tables import udep_eep_table

move_names = state.move_names

"""COのindex化"""
def co_to_index(co):
    index = 0
    for co_i in co[:-1]:
        index *= 3
        index += co_i
    return index

def index_to_co(index):
    co = [0] * 8
    sum_co = 0
    for i in range(6, -1, -1):
        co[i] = index % 3
        index //= 3
        sum_co += co[i]
    co[-1] = (3 - sum_co % 3) % 3
    return co

"""EOのindex化"""
def eo_to_index(eo):
    index = 0
    for eo_i in eo[:-1]:
        index *= 2
        index += eo_i
    return index


def index_to_eo(index):
    eo = [0] * 12
    sum_eo = 0
    for i in range(10, -1, -1):
        eo[i] = index % 2
        index //= 2
        sum_eo += eo[i]
    eo[-1] = (2 - sum_eo % 2) % 2
    return eo

def calc_combination(n, r):
    """nCrの計算"""
    ret = 1
    for i in range(r):
        ret *= n - i
    for i in range(r):
        ret //= r - i
    return ret

def e_combination_to_index(comb):
    index = 0
    r = 4
    for i in range(12 - 1, -1, -1):
        if comb[i]:
            index += calc_combination(i, r)
            r -= 1
    return index

def index_to_e_combination(index):
    combination = [0] * 12
    r = 4
    for i in range(12 - 1, -1, -1):
        if index >= calc_combination(i, r):
            combination[i] = 1
            index -= calc_combination(i, r)
            r -= 1
    return combination

"""CPのindex化"""
def cp_to_index(cp):
    index = 0
    for i, cp_i in enumerate(cp):
        index *= 8 - i
        for j in range(i + 1, 8):
            if cp[i] > cp[j]:
                index += 1
    return index

def index_to_cp(index):
    cp = [0] * 8
    for i in range(6, -1, -1):
        cp[i] = index % (8 - i)
        index //= 8 - i
        for j in range(i + 1, 8):
            if cp[j] >= cp[i]:
                cp[j] += 1
    return cp

"""UD面のEPのindex化"""
def ud_ep_to_index(ep):
    index = 0
    for i, ep_i in enumerate(ep):
        index *= 8 - i
        for j in range(i + 1, 8):
            if ep[i] > ep[j]:
                index += 1
    return index


def index_to_ud_ep(index):
    ep = [0] * 8
    for i in range(6, -1, -1):
        ep[i] = index % (8 - i)
        index //= 8 - i
        for j in range(i + 1, 8):
            if ep[j] >= ep[i]:
                ep[j] += 1
    return ep

"""E列のEPのindex化"""
def e_ep_to_index(eep):
    index = 0
    for i, eep_i in enumerate(eep):
        index *= 4 - i
        for j in range(i + 1, 4):
            if eep[i] > eep[j]:
                index += 1
    return index


def index_to_e_ep(index):
    eep = [0] * 4
    for i in range(4 - 2, -1, -1):
        eep[i] = index % (4 - i)
        index //= 4 - i
        for j in range(i + 1, 4):
            if eep[j] >= eep[i]:
                eep[j] += 1
    return eep

move_names_ph2 = ["U", "U2", "U'", "D", "D2", "D'", "L2", "R2", "F2", "B2"]
move_names_to_index = {move_name: i for i, move_name in enumerate(move_names)}

class Search1:
    def __init__(self, state):
        self.initial_state = state
        self.current_solution_ph1 = []

    def depth_limited_search_ph1(self, co_index, eo_index, e_comb_index, depth):
        if depth == 0 and co_index == 0 and eo_index == 0 and e_comb_index == 0:
            return True
        if depth == 0:
            return False

        # 枝刈り
        if max(co_eec_table.co_eec_prune_table[co_index][e_comb_index], eo_eec_table.eo_eec_prune_table[eo_index][e_comb_index]) > depth:
            return False

        prev_move = self.current_solution_ph1[-1] if self.current_solution_ph1 else None
        for move_name in move_names:
            if not state.is_move_available(prev_move, move_name):
                continue
            self.current_solution_ph1.append(move_name)
            move_index = move_names_to_index[move_name]
            next_co_index = co_table.co_move_table[co_index][move_index]
            next_eo_index = eo_table.eo_move_table[eo_index][move_index]
            next_e_comb_index = e_table.e_combination_table[e_comb_index][move_index]
            if self.depth_limited_search_ph1(next_co_index, next_eo_index, next_e_comb_index, depth - 1):
                return True
            self.current_solution_ph1.pop()

    def start_search(self, max_length=20):
        co_index = co_to_index(self.initial_state.co)
        eo_index = eo_to_index(self.initial_state.eo)
        e_combination = [1 if e in (0, 1, 2, 3) else 0 for e in self.initial_state.ep]
        e_comb_index = e_combination_to_index(e_combination)
        depth = 0
        while depth <= max_length:
            # print(f"# Start searching phase 1 length {depth}")
            if self.depth_limited_search_ph1(co_index, eo_index, e_comb_index, depth):
                return " ".join(self.current_solution_ph1)
            depth += 1
        return None

move_names_to_index_ph2 = {move_name: i for i, move_name in enumerate(move_names_ph2)}

class Search2:
    def __init__(self, states):
        self.initial_state = states
        self.current_solution_ph1 = []
        self.current_solution_ph2 = []
        self.max_solution_length = 9999
        self.start = 0

    def depth_limited_search_ph1(self, co_index, eo_index, e_comb_index, depth):
        if depth == 0 and co_index == 0 and eo_index == 0 and e_comb_index == 0:
            states = self.initial_state
            for move_name in self.current_solution_ph1:
                states = states.apply_move(state.moves[move_name])
            return self.start_phase2(states)

        if depth == 0:
            return False

        # 枝刈り
        if max(co_eec_table.co_eec_prune_table[co_index][e_comb_index], eo_eec_table.eo_eec_prune_table[eo_index][e_comb_index]) > depth:
            return False

        prev_move = self.current_solution_ph1[-1] if self.current_solution_ph1 else None
        for move_name in move_names:
            if not state.is_move_available(prev_move, move_name):
                continue
            self.current_solution_ph1.append(move_name)
            move_index = move_names_to_index[move_name]
            next_co_index = co_table.co_move_table[co_index][move_index]
            next_eo_index = eo_table.eo_move_table[eo_index][move_index]
            next_e_comb_index = e_table.e_combination_table[e_comb_index][move_index]
            if self.depth_limited_search_ph1(next_co_index, next_eo_index, next_e_comb_index, depth - 1):
                return True
            self.current_solution_ph1.pop()

    def depth_limited_search_ph2(self, cp_index, udep_index, eep_index, depth):
        if depth == 0 and cp_index == 0 and udep_index == 0 and eep_index == 0:
            return True
        if depth == 0:
            return False

        # 枝刈り
        if max(cp_eep_table.cp_eep_prune_table[cp_index][eep_index], udep_eep_table.udep_eep_prune_table[udep_index][eep_index]) > depth:
            return False

        if self.current_solution_ph2:
            prev_move = self.current_solution_ph2[-1]
        elif self.current_solution_ph1:
            prev_move = self.current_solution_ph1[-1]
        else:
            prev_move = None

        for move_name in move_names_ph2:
            if not state.is_move_available(prev_move, move_name):
                continue
            self.current_solution_ph2.append(move_name)
            move_index = move_names_to_index_ph2[move_name]
            next_cp_index = cp_table.cp_move_table[cp_index][move_index]
            next_udep_index = ud_ep_table.ud_ep_move_table[udep_index][move_index]
            next_eep_index = e_ep_table.e_ep_move_table[eep_index][move_index]
            if self.depth_limited_search_ph2(next_cp_index, next_udep_index, next_eep_index, depth - 1):
                return True
            self.current_solution_ph2.pop()

    def start_search(self, max_length=30):
        self.start = time.time()
        self.max_solution_length = max_length
        co_index = co_to_index(self.initial_state.co)
        eo_index = eo_to_index(self.initial_state.eo)
        e_combination = [1 if e in (0, 1, 2, 3) else 0 for e in self.initial_state.ep]
        e_comb_index = e_combination_to_index(e_combination)

        depth = 0
        while depth <= self.max_solution_length:
            # print(f"# Start searching phase 2 length {depth}")
            if self.depth_limited_search_ph1(co_index, eo_index, e_comb_index, depth):
                return " ".join(self.current_solution_ph1) + " " + " ".join(self.current_solution_ph2)
            depth += 1
        return None

    def start_phase2(self, state):
        cp_index = cp_to_index(state.cp)
        udep_index = ud_ep_to_index(state.ep[4:])
        eep_index = e_ep_to_index(state.ep[:4])
        depth = 0
        while depth <= self.max_solution_length - len(self.current_solution_ph1):
            if self.depth_limited_search_ph2(cp_index, udep_index, eep_index, depth):
                return True
            depth += 1