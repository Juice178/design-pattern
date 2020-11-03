from abc import ABC, abstractmethod

class Strategy:
    @abstractmethod
    def next_hand(self):
        pass
    @abstractmethod
    def study(self, win):
        pass