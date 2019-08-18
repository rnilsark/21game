import unittest
from deck import Deck
from deck import Card


class DeckTests(unittest.TestCase):
    def test_draws_the_top_card(self):
        cards = [Card("diamond", 2), Card("diamond", 3)]
        deck = Deck(cards)

        card = deck.draw()
        self.assertEqual(card.rank, 3)
        self.assertEqual(deck.count(), 1)


if __name__ == '__main__':
    unittest.main()
