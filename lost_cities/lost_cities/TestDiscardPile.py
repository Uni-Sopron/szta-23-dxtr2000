import unittest
from unittest.mock import patch

from Card import Card
from DiscardPile import DiscardPile


class TestDiscardPile(unittest.TestCase):
    def setUp(self):
        self.discard_pile = DiscardPile()

    def test_add_card(self):
        card = Card("red", 5)
        self.discard_pile.add_card(card)
        self.assertIn(card, self.discard_pile.cards)
        self.assertEqual(len(self.discard_pile.cards), 1)

    def test_get_top_card(self):
        card1 = Card("blue", 3)
        card2 = Card("green", 2)
        self.discard_pile.cards = [card1, card2]
        top_card = self.discard_pile.get_top_card()
        self.assertEqual(top_card, card2)

        self.discard_pile.cards = []
        top_card = self.discard_pile.get_top_card()
        self.assertIsNone(top_card)

    def test_is_empty(self):
        self.assertTrue(self.discard_pile.is_empty())

        card = Card("yellow", 1)
        self.discard_pile.cards.append(card)
        self.assertFalse(self.discard_pile.is_empty())

    def test_reset(self):
        self.discard_pile.cards = [Card("red", 4), Card("green", 5)]
        self.discard_pile.reset()
        self.assertEqual(len(self.discard_pile.cards), 0)


if __name__ == "__main__":
    unittest.main()
