from Card import Card
import random

class DrawPile:
    def __init__(self):
        self.cards = []
        self.generate_cards()
        self.shuffle()

    def generate_cards(self):
        colors = ['red', 'green', 'blue', 'white', 'yellow']
        values = list(range(2, 11)) + [1] * 10
        for color in colors:
            for value in values:
                self.cards.append(Card(color, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None