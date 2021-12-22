from operator import attrgetter
from random import choices, randint, shuffle


class Game:
    """
        Game object contains game number, turns played, list of players and the board.

        Args:
            number  (int):  the game identification

        Attributes:
            number  (int):  game id
            turns   (int):  number of turns played
            board   (list): game board (Property)
            players (list): list of player (Player)
    """

    def __init__(self, number):
        self.turns = 0
        self.number = number
        self.board = [Property() for _ in range(20)]

        # Shuffle players list
        self.players = [Player(i) for i in range(4)]
        shuffle(self.players)

    def clear_properties(self, player):
        """
            Removes players properties.

            Args:
                player (int): The player that lost the game
        """

        for tile in self.board:
            if tile.owner == player:
                tile.owner = None

    def finish(self):
        """
            Finishes a game and returns the results.

            Returns:
                number: game identification
                turns: number of turns played
                winner: player that won the game
        """

        if len(self.players) == 1:
            return self.number, self.turns, self.players[0].strategy
        else:
            winner = max(self.players, key=attrgetter("balance"))
            return self.number, self.turns, winner.strategy


class Property:
    """
        Property object that contains it's price, rent and owner.

        Attributes:
            owner (int): player that owns the property
            rent  (int): renting price
            price (int): property price
    """

    def __init__(self):
        self.owner = None
        self.rent = randint(100, 100000)
        self.price = randint(100, 100000)


class Player:
    """
        Player object with it's defined strategy, balance and current position.

        Args:
            strategy (int): player's buying strategy number

        Attributes:
            strategy (int): buying strategy
            balance  (int): current balance
            position (int): current position in board
    """

    def __init__(self, strategy):
        self.strategy = strategy
        self.balance = 300
        self.position = 0

    def move(self):
        """
            Moves player on the game board.
        """

        # Roll dice
        roll = randint(1, 6)

        # Calculate new position
        new_pos = self.position + roll

        # Completed board run
        if new_pos > 19:
            self.position = new_pos - 20
            self.balance += 300
        else:
            self.position = new_pos

    def negotiate(self, price, rent):
        """
            Buys a property based on the player's strategy.

            Args:
                price (int): property price
                rent  (int): renting price

            Returns:
                sold: true if property was bought, false otherwise
        """

        # Player cannot afford the property
        if self.balance < price:
            return False
        else:
            # Impulsive player
            if self.strategy == 0:
                self.balance -= price
            # Demanding player
            elif self.strategy == 1 and rent > 50:
                self.balance -= price
            # Careful player
            elif self.strategy == 2 and (self.balance - price) >= 80:
                self.balance -= price
            # Random player (50/50)
            elif self.strategy == 3 and choices([0, 1])[0] == 1:
                self.balance -= price
            else:
                return False

            return True

    def pay(self, value):
        """
            Pays rent, updating the player's balance.

            Args:
                value (int): value to be subtracted from balance
        """

        self.balance -= value

    def collect(self, value):
        """
            Collects rent, updating the player's balance.

            Args:
                value (int): value to be added to balance
        """

        self.balance += value

    def lost(self):
        """
            Checks if the player lost the game.

            Returns:
                lost: true if balance is less than zero, false otherwise
        """

        return self.balance < 0
