from games.guess_number import GuessNumber
from games.dice_roll import DiceRoll
from games.rps import RPS
from games.game import Game

def select_game() -> tuple[str, Game] | None:
    game_names : list[str] = [
        "Guess the Number",
        "Dice Roll",
        "Rock Paper Scissors"
    ]

    game_instances : list[Game] = [
        GuessNumber(),
        DiceRoll(),
        RPS()
    ]

    # Ensure the game names and their respective instances match
    game_options : list[tuple[str, Game]] = [(name, instance) for name, instance in zip(game_names, game_instances)]


    while True:
        try:
            selected_option: str = input(
            f"\nGames Available:\n"
              f"1. {game_names[0]}\n"
              f"2. {game_names[1]}\n"
              f"3. {game_names[2]}\n"
              f"Pick Game Number or (q) to quit: ")
            
            if (selected_option.lower() == "q"):
                return None

            selected_no : int = int(selected_option)
            if (selected_no < 1 or selected_no > len(game_names)):
                print("Invalid Option Chosen")
                continue

            return game_options[selected_no-1]

        except ValueError:
            print("Invalid input. Enter a valid number.")