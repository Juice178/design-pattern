from strategy import Strategy
from hand import Hand
import numpy as np

class WinningStrategy(Strategy):
    def __init__(self, seed):
        self._random = np.random.seed(seed)
        self._won = False
        self._prev_hand = None
    
    def next_hand(self):
        if not self._won:
            self._prev_hand = Hand.get_hand(np.random.randint(3))
        return self._prev_hand
    
    def study(self, win):
        self._won = win
