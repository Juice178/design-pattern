import sys
from player import Player
from winning_strategy import WinningStrategy
from prob_strategy import ProbStrategy

def main(*args):
    print(args)
    seed1 = int(args[1])
    seed2 = int(args[2])
    player1 = Player("Taro", WinningStrategy(seed1))
    player2 = Player("Hana", ProbStrategy(seed2))
    for _ in range(1000):
        next_hand1 = player1.next_hand()
        next_hand2 = player2.next_hand()
        if next_hand1.is_stronger_than(next_hand2):
            print(f"Winner: {player1.to_string()}")
            player1.win()
            player2.lose()
        elif next_hand2.is_stronger_than(next_hand1):
            print(f"Winner: {player2.to_string()}")
            player1.lose()
            player2.win()
        else:
            print("Even ...")
            player1.even()
            player2.even()
    print("Total result:")
    print(player1.to_string())
    print(player2.to_string())

if __name__ == "__main__":
    main(*sys.argv)
