from Card import Card

class DiscardPile:
    """
    A class representing the discard pile in the game.

    Attributes:
        cards (list): A list containing instances of the Card class representing the cards in the
            discard pile.

    Methods:
        __init__(): Initializes a new instance of the DiscardPile class with an empty cards list.
        
        add_card(card: Card): Adds the given Card instance to the discard pile.

    Parameters:
        card (Card): The Card instance to be added to the discard pile.
    """
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        pass