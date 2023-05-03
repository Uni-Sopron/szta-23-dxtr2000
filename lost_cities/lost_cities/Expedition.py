from Card import Card
from DiscardPile import DiscardPile

class Expedition:
    def __init__(self, color: str):
        self.color = color
        self.cards = []
        self.discard_pile = DiscardPile()
        self.started = False

    def add_card(self, card):
        if not self.started:
            self.started = True
        self.cards.append(card)

    def get_points(self):
        if len(self.cards) == 0:
            return 0
        elif len(self.cards) < 8:
            return sum(card.value for card in self.cards) - 20
        else:
            return sum(card.value for card in self.cards) + 20
    
    def __repr__(self):
        return self.color