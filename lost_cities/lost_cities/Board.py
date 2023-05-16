from Expedition import Expedition
from Card import Card

class Board:
    """Represents the game board.

    Attributes:
        expeditions (list): The list of expeditions on the board.
    """

    def __init__(self):
        """
        Initializes a new instance of the Board class.
        Creates expeditions for each color.

        """
        self.expeditions = [Expedition(color) for color in ['yellow', 'green', 'blue', 'white', 'red']]
    
    def add_card(self, card: Card):
        """
        Adds a card to the corresponding expedition.

        Args:
            card (Card): The card to add.
        """
        color = card.color.lower()
        self.expeditions[self.get_expedition(color)].add_card(card)

    def get_expedition(self, color: str):
        """
        Returns the index of the expedition based on the color.

        Args:
            color (str): The color of the expedition.

        Returns:
            int: The index of the expedition.

        Raises:
            ValueError: If the color is invalid.
        """
        colors = ['yellow', 'green', 'blue', 'white', 'red']
        if color not in colors:
            raise ValueError("Invalid color")
        return colors.index(color)

    def __str__(self):
        """
        Returns the string representation of the board.

        Returns:
            str: The string representation of the board, displaying each expedition.
        """
        return '\n'.join([str(expedition) for expedition in self.expeditions])