from strategy import Strategy
from hand import Hand 
import numpy as np

class ProbStrategy(Strategy):
    def __init__(self, seed):
        self._random = np.random.seed(seed)
        self._prev_hand_value = 0
        self._current_hand_value = 0
        self._history = [[1,1,1], [1,1,1], [1,1,1]]

    def next_hand(self):
        bet = np.random.randint(self.get_sum(self._current_hand_value))
        hand_value = 0
        if bet < self._history[self._current_hand_value][0]:
            hand_value = 0
        elif (bet < self._history[self._current_hand_value][0] + self._history[self._current_hand_value][1]):
            hand_value = 1
        else:
            hand_value = 2

        self._prev_hand_value = self._current_hand_value
        self._current_hand_value = hand_value
        return Hand.get_hand(hand_value)

    def get_sum(self, hv):
        sum_int = 0
        for i in range(3):
            sum_int += self._history[hv][i]
        return sum_int
    
    def study(self, win):
        if win:
            self._history[self._prev_hand_value][self._current_hand_value] += 1
        else:
            self._history[self._prev_hand_value][(self._current_hand_value + 1) % 3] += 1
            self._history[self._prev_hand_value][(self._current_hand_value + 2) % 3] += 1

