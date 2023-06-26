import unittest

from Card import Card
from DrawPile import DrawPile


class TestDrawPile(unittest.TestCase):
    def setUp(self):
        self.draw_pile = DrawPile()

    def test_generate_cards(self):
        self.assertEqual(len(self.draw_pile.cards), 45)

    def test_shuffle(self):
        initial_cards = self.draw_pile.cards[:]
        self.draw_pile.shuffle()
        self.assertNotEqual(self.draw_pile.cards, initial_cards)
        self.assertEqual(len(self.draw_pile.cards), len(initial_cards))

    def test_draw_card(self):
        card = Card("red", 5)
        self.draw_pile.cards = [card]
        drawn_card = self.draw_pile.draw_card()
        self.assertEqual(drawn_card, card)
        self.assertEqual(len(self.draw_pile.cards), 0)


if __name__ == "__main__":
    unittest.main()
