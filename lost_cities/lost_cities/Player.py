from Hand import Hand
from DrawPile import DrawPile
from DiscardPile import DiscardPile
from Board import Board

class Player:
    """
    A class representing a player in the game.

    Attributes:
        name (str): A string representing the player's name.
        hand (Hand): An instance of the Hand class representing the player's hand of cards.
        points (int): An integer representing the player's score.

    Methods:
        __init__(name: str): Initializes a new instance of the Player class with the given name, creating an empty hand
            and setting the player's score to 0.

        draw_card(draw_pile: DrawPile): Draws a card from the given DrawPile instance and adds it to the player's hand.

        play_card(card_index: int, board: Board): Plays the card at the given index in the player's hand on the given Board
            instance, removing the card from the player's hand and adding it to an Expedition on the board.

        discard_card(card_index: int, discard_pile: DiscardPile): Discards the card at the given index in the player's hand,
            removing the card from the player's hand and adding it to the given DiscardPile instance.

    Parameters:
        draw_pile (DrawPile): The DrawPile instance to draw a card from.
        card_index (int): The index of the card to be played or discarded in the player's hand.
        board (Board): The Board instance on which the card is to be played.
        discard_pile (DiscardPile): The DiscardPile instance to discard a card to.
    """
    def __init__(self, name: str):
        self.name = name
        self.hand = Hand()
        self.points = 0
    
    def draw_card(self, draw_pile: DrawPile):
        pass
    def play_card(self, card_index: int, board: Board):
        pass
    def discard_card(self, card_index: int, discard_pile: DiscardPile):
        pass