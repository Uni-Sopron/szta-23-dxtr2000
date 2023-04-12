from Card import Card

class Hand:
    """
    A class representing a player's hand of cards in the game.

    Attributes:
        cards (list): A list containing instances of the Card class representing the cards in the player's hand.

    Methods:
        __init__(): Initializes a new instance of the Hand class with an empty cards list.

        add_card(card: Card): Adds the given Card instance to the player's hand.

        remove_card(card: Card): Removes the given Card instance from the player's hand.

    Parameters:
        card (Card): The Card instance to be added or removed from the player's hand.
    """
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        pass
    
    def remove_card(self, card: Card):
        pass