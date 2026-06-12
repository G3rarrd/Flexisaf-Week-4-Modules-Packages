def display_results(
    game_records: list[tuple[str, int]]
) -> None:

    COLUMN_TITLES: list[str] = [
        "Session",
        "Game",
        "Points"
    ]

    if len(game_records) == 0:

        print("N/A")

        return

    # Dynamic column widths
    session_len = max(len(COLUMN_TITLES[0]),len(str(len(game_records))))

    game_len = max(len(COLUMN_TITLES[1]),max(len(name) for name, _ in game_records))

    points_len = max(len(COLUMN_TITLES[2]),
        max(len(str(points))for _, points in game_records)
    )

    total_width = (session_len + game_len + points_len + 10)

    print("\n" + "=" * total_width)

    print(
        f"{COLUMN_TITLES[0]:<{session_len}} | "
        f"{COLUMN_TITLES[1]:<{game_len}} | "
        f"{COLUMN_TITLES[2]:<{points_len}}"
    )

    print("-" * total_width)

    total_points = 0

    for i, (game_name, points) in enumerate(game_records, start=1):

        total_points += points

        print(
            f"{i:<{session_len}} | "
            f"{game_name:<{game_len}} | "
            f"{points:<{points_len}}"
        )

    print("-" * total_width)

    print(f"Total Points: {total_points}")

    print("=" * total_width)
