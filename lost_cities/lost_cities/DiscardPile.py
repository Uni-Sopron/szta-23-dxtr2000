from Card import Card

class DiscardPile:
    """Represents the discard pile of the game.

    Attributes:
        cards (list): The list of cards in the discard pile.
    """

    def __init__(self):
        """
        Initializes a new instance of the DiscardPile class.
        """
        self.cards = []

    def add_card(self, card: Card):
        """
        Adds a card to the discard pile.

        Args:
            card (Card): The card to be added.
        """
        self.cards.append(card)

    def get_top_card(self):
        """
        Retrieves the top card from the discard pile.

        Returns:
            Card or None: The top card, or None if the discard pile is empty.
        """
        if len(self.cards) > 0:
            return self.cards[-1]
        else:
            return None

    def is_empty(self):
        """
        Checks if the discard pile is empty.

        Returns:
            bool: True if the discard pile is empty, False otherwise.
        """
        return len(self.cards) == 0

    def reset(self):
        """
        Resets the discard pile by removing all cards.
        """
        self.cards = []
