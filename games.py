from games.game import Game
from games.game_selection import select_game
from games.result_table import display_results


def main() -> None:
    player : str = "Ahmed"
    
    session : int = 1

    game_records: list[tuple[str, int]] = []

    while True:

        print(f"\n== Session {session} ==")

        selected_option : tuple[str, Game] | None = select_game() 
        
        if (selected_option == None):
            print("\n=== FINAL RESULTS ===")
            display_results(game_records)
            return
        
        name, game = selected_option

        points: int = game.play()

        game_records.append((name, points))

        print("\n=== RESULTS ===")
        display_results(game_records)

        session += 1


if "__main__" == __name__:
    main()

