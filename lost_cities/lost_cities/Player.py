from Hand import Hand
from DrawPile import DrawPile
from DiscardPile import DiscardPile
from Board import Board

class Player:
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