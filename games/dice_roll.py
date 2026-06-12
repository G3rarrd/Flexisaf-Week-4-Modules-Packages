from games.game import Game

import random

class DiceRoll(Game):
    def play(self) -> int:
        print("\n === Dice Roll ===")
        point : int = random.randint(1, 6)
        
        print(f"You rolled: {point}.")

        print(f"Points Gained: {point}")

        return point