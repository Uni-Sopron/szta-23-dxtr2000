from Card import Card

class Expedition:
    """
    A class representing an expedition in the game.

    Attributes:
        color (str): The color of the expedition, represented as a string.
        cards (list): A list containing instances of the Card class representing the cards in the
            expedition.

    Methods:
        __init__(color: str): Initializes a new instance of the Expedition class with the given color and
            an empty cards list.
        
        add_card(card: Card): Adds the given Card instance to the expedition.

    Parameters:
        card (Card): The Card instance to be added to the expedition.

    """
    def __init__(self, color: str):
        self.color = color
        self.cards = []

    def add_card(self, card: Card):
        pass