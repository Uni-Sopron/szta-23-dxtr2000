from Card import Card
import random

class DrawPile:
    """Represents the draw pile of the game.

    Attributes:
        cards (list): The list of cards in the draw pile.
    """

    def __init__(self):
        """
        Initializes a new instance of the DrawPile class.
        """
        self.cards = []
        self.generate_cards()
        self.shuffle()

    def generate_cards(self):
        """
        Generates the cards for the draw pile.
        """
        colors = ['red', 'green', 'blue', 'white', 'yellow']
        values = list(range(2, 11))
        for color in colors:
            for value in values:
                self.cards.append(Card(color, value))

    def shuffle(self):
        """
        Shuffles the cards in the draw pile.
        """
        random.shuffle(self.cards)

    def draw_card(self):
        """
        Draws a card from the draw pile.

        Returns:
            Card or None: The drawn card, or None if the draw pile is empty.
        """
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None