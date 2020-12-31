from strategy import Strategy

class Player:
    def __init__(self, name, strategy):
        self._name = name 
        self._strategy = strategy
        self._wincount = 0
        self._losecount = 0
        self._gamecount = 0

    def next_hand(self):
        return self._strategy.next_hand()
    
    def win(self):
        self._strategy.study(True)
        self._wincount += 1
        self._gamecount += 1

    def lose(self):
        self._strategy.study(False)
        self._losecount += 1
        self._gamecount += 1

    def even(self):
        self._gamecount += 1

    def to_string(self):
        return f"[{self._name} : {self._gamecount} games, {self._wincount} win, {self._losecount} lose]"