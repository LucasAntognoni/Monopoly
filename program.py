import sys

from game import Game


def run(number, max_turns):
    """
        Runs the main game loop.

        Args:
            number    (int): the game identification
            max_turns (int): maximum number of turns

        Returns:
            number: game identification
            turns: number of turns played
            winner: player that won the game
    """

    game = Game(number)

    while True:

        for i, player in enumerate(game.players):

            # Player turn
            player.move()

            # No owner
            if game.board[player.position].owner is None:

                # Buy property?
                if player.negotiate(game.board[player.position].price, game.board[player.position].rent):
                    game.board[player.position].owner = player.strategy

            # Has owner
            else:
                # Pay rent
                game.players[i].pay(game.board[player.position].rent)

                # Collect rent
                for j, p in enumerate(game.players):
                    if game.board[player.position].owner == p.strategy:
                        game.players[j].collect(game.board[player.position].rent)
                        break

            if player.lost():
                game.players.pop(i)
                game.clear_properties(player.strategy)

            # Increment turn counter
            game.turns += 1

            if game.turns == max_turns:
                return game.finish()

        if len(game.players) == 1:
            return game.finish()


def main():
    """
        Main function.
    """

    # Set default values
    max_number_of_turns = 1000
    number_of_simulations = 300

    # Check for input parameters
    try:
        if len(sys.argv) == 3:
            number_of_simulations = int(sys.argv[1])
            max_number_of_turns = int(sys.argv[2])
    except Exception as e:
        print(f"Error reading input parameters!\nException: {e}.")
        exit(0)

    # Validate parameters
    if number_of_simulations <= 0 or max_number_of_turns < 4:
        print("Invalid input parameters!")
        exit(0)

    results = list()

    for simulation in range(number_of_simulations):
        results.append(run(simulation, max_number_of_turns))


if __name__ == '__main__':
    main()
