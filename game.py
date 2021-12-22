from random import choices, randint


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
