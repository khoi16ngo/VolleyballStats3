from models.player import Player

def askForPlayers() -> list:    
    """
    Prompt the user for the number of players and their names.
    Returns list of Player objects.
    """

    players = []
    while True:
        print("How many players are on the team?")
        number_players = input("Number players: ")
        if number_players == "":
            print("No player number entered. Please try again.")
        elif not number_players.isnumeric():
            print("Invalid player number entered. Please try again.")
        else:
            number_players = int(number_players)
            break
    
    print("Please enter the names and numbers of the players on the team.")
    for i in range(number_players):
        players = _get_player_from_user(players)
    
    # Ask if there are more players
    while True:
        exit = input("Are there more players? (y/n): ").strip().lower()
        if exit == "y":
            players = _get_player_from_user(players)
        elif exit == "n":
            return players
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def _get_player_from_user(players: list[Player]) -> list[Player]:
    while True:
        # Get player name
        playerName = input("Enter player name: ").strip().title()
        if playerName == "":
            print("No player name entered. Please try again.")
            continue

        # Get player number
        playerNumber = input("Enter player number: ").strip()
        if playerNumber == "":
            print("No player number entered. Please try again.")
            continue
        elif not playerNumber.isnumeric():
            print("Invalid player number entered. Please try again.")
            continue
        elif int(playerNumber) >= 100 or int(playerNumber) < 0:
            print("Invalid player number entered. Must be between 0 and 100. Please try again.")
            continue
        
        # Add player to list
        print(f"Adding player ... {playerName} ({playerNumber})")
        players.append(Player(playerName, int(playerNumber)))
        break
    
    return players