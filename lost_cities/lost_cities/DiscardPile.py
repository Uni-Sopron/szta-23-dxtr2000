from Card import Card

class DiscardPile:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def get_top_card(self):
        if len(self.cards) > 0:
            return self.cards[-1]
        else:
            return None
    def is_empty(self):
        return len(self.cards) == 0

    def reset(self):
        self.cards = []