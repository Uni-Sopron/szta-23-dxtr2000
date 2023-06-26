from Board import Board
from DiscardPile import DiscardPile
from DrawPile import DrawPile

class Player:
    """Represents a player in the game.

    Attributes:
        name (str): The name of the player.
        hand_cards (list): The list of cards in the player's hand.
        points (int): The total points earned by the player.
        board (Board): The player's game board.
    """

    def __init__(self, name: str):
        """
        Initializes a new instance of the Player class.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.hand_cards = []
        self.points = 0
        self.board = Board()

    def draw_card(self, draw_pile: DrawPile):
        """
        Draws a card from the draw pile and adds it to the player's hand.

        Args:
            draw_pile (DrawPile): The draw pile from which to draw the card.
        """
        self.hand_cards.append(draw_pile.draw_card())

    def play_card(self, card_index: int, board: Board):
        """
        Plays a card from the player's hand onto the game board.

        Args:
            card_index (int): The index of the card in the player's hand.
            board (Board): The game board on which to play the card.
        """
        card = self.hand_cards[card_index - 1]
        self.hand_cards.pop(card_index - 1)
        board.expeditions[board.get_expedition(card.color)].add_card(card)
        self.points += card.value

    def discard_card(self, card_index: int, discard_pile: DiscardPile):
        """
        Discards a card from the player's hand into the discard pile.

        Args:
            card_index (int): The index of the card in the player's hand.
            discard_pile (DiscardPile): The discard pile to which the card is discarded.
        """
        card = self.hand_cards[card_index - 1]
        discard_pile.add_card(card)
        self.hand_cards.pop(card_index - 1)
