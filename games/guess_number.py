from games.game import Game

import random

class GuessNumber(Game):
    MIN_NUMBER : int = 1
    MAX_NUMBER : int = 10
    MAX_POINT : int = 3

    def play(self) -> int:
        print("\n === Guess The Number ===")
        
        guessed_number : int = self.__get_guess()
        actual_number : int = random.randint(self.MIN_NUMBER, self.MAX_NUMBER)
        diff : int = abs(guessed_number-actual_number)
        self.__display_reusult(guessed_number, actual_number, diff)
        points : int = max(self.MAX_POINT-diff, 0)

        print(f"Points Gained: {points}")

        return points
    
    def __display_reusult(self, guessed_number : int, actual_number : int, difference : int) -> None:
        if guessed_number == actual_number:
            print("You guessed the right number!!")
        else:
            print(f"The actual number was {actual_number}. Off by {difference} number(s)")

    
    def __get_guess(self) -> int:
        while True:

            try:

                guessed_number: int = int(input(f"\nGuess a number from {self.MIN_NUMBER} to {self.MAX_NUMBER}: "))

                if guessed_number < self.MIN_NUMBER or guessed_number > self.MAX_NUMBER:
                    print("Number is out of range")
                    continue
                
                return guessed_number

            except ValueError:
                print("Invalid input. Enter a valid number.")


