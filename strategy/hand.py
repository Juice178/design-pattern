import sys

class Hand:
    HANDVALUE_ROCK = 0
    HANDVALUE_PAPER = 1
    HANDVAUE_SCISSORS = 2
    hand = []
    name = ["Rock", "Paper", "scissors"]

    def __init__(self, handvalue):
        self._handvalue = handvalue
    
    @classmethod
    def append_hands(cls):
        cls.hand.append(Hand(cls.HANDVALUE_ROCK))
        cls.hand.append(Hand(cls.HANDVALUE_PAPER))
        cls.hand.append(Hand(cls.HANDVAUE_SCISSORS))

    @classmethod
    def get_hand(cls, handvalue):
        cls.append_hands()
        return cls.hand[handvalue]

    def is_stronger_than(self, h):
        return self.fight(h) == 1

    def is_weaker_than(self, h):
        return self.fight(h) == -1

    def fight(self, h):
        if (self == h):
            return 0 
        elif (self._handvalue + 1) % 3 == h._handvalue:
            return 1
        else:
            return -1

    def to_string(self):
        return self.name[self._handvalue]

    

    