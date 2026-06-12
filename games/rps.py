import random

from games.game import Game

class RPS(Game):
    CHOICES: list[str] = [
        "rock",
        "paper",
        "scissors"
    ]

    WIN_POINT: int = 3
    DRAW_POINT: int = 1
    LOSE_POINT: int = 0
    def play(self) -> int:
        print("\n=== Rock paper Scissors ===" )

        user_choice: str = self.__get_choice()
        computer_choice : str = random.choice(self.CHOICES)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        points : int = self.__get_result(user_choice, computer_choice)
        
        self.__display_result(points)

        print(f"Points Gained: {points}")
        return points

    
    def __get_choice(self) -> str:
        while True:

            choice: str = input("\nChoose rock, paper, or scissors: ").lower().strip()

            if choice in self.CHOICES:
                return choice

            print(
                f"'{choice}' is invalid.\n"
                f"Valid options are: "
                f"rock, paper, scissors."
            )
            
    def __get_result(self, user_choice : str, computer_choice : str) -> int:
        if user_choice == computer_choice:
            return self.DRAW_POINT
        
        if ((user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")):
            return self.WIN_POINT
        
        return self.LOSE_POINT
    
    def __display_result(self, points : int) -> None:
        if (points == self.DRAW_POINT):
            print("It's a Draw")

        elif(points == self.WIN_POINT):
            print("You Won!")

        elif(points == self.LOSE_POINT):
            print("You Lose!")


