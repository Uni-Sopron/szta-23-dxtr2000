from Card import Card
from DiscardPile import DiscardPile

class Expedition:
    """Represents an expedition of cards of a specific color.

    Attributes:
        color (str): The color of the expedition.
        cards (list): The cards in the expedition.
        discard_pile (DiscardPile): The discard pile associated with the expedition.
        started (bool): Indicates if the expedition has been started.
    """

    def __init__(self, color: str):
        """
        Initializes a new instance of the Expedition class.

        Args:
            color (str): The color of the expedition.
        """
        self.color = color
        self.cards = []
        self.discard_pile = DiscardPile()
        self.started = False

    def add_card(self, card):
        """
        Adds a card to the expedition.

        Args:
            card (Card): The card to be added to the expedition.
        """
        if not self.started:
            self.started = True
        self.cards.append(card)

    def get_points(self):
        """
        Calculates the points earned by the expedition.

        Returns:
            int: The points earned by the expedition.
        """
        if len(self.cards) == 0:
            return 0
        elif len(self.cards) < 8:
            return sum(card.value for card in self.cards) - 20
        else:
            return sum(card.value for card in self.cards) + 20

    def __repr__(self):
        """
        Returns a string representation of the expedition.

        Returns:
            str: The string representation of the expedition.
        """
        return self.color
