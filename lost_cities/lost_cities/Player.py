from Card import Card
from DrawPile import DrawPile
from DiscardPile import DiscardPile
from Board import Board

class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand_cards = []
        self.points = 0
        self.board = Board()
    
    def draw_card(self, draw_pile: DrawPile):
        self.hand_cards.append(draw_pile.draw_card())
    
    def play_card(self, card_index: int, board: Board):
        card = self.hand_cards[card_index - 1]
        self.hand_cards.pop(card_index - 1)
        board.expeditions[board.get_expedition(card.color)].add_card(card)
        self.points += card.value
    
    def discard_card(self, card_index: int, discard_pile: DiscardPile):
        card = self.hand_cards[card_index - 1]
        discard_pile.add_card(card)
        self.hand_cards.pop(card_index - 1)