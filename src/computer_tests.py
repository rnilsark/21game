import unittest
from computer import Computer
from deck import Card, Deck
from hand import Hand


class MyTestCase(unittest.TestCase):
    def test_computer_stops_at_21(self):
        player_hand = Hand("")
        player_hand.add(Card("spades", 13))
        player_hand.add(Card("clubs", 8))

        cards = [Card("hearts", 1), Card("hearts", 7), Card("hearts", 13)]
        pile = Deck(cards)

        computer_hand = Hand("")
        Computer().play(computer_hand, pile, player_hand)
        self.assertEqual(computer_hand.sum(), 21)

    def test_computer_stops_when_player_is_bust(self):
        player_hand = Hand("")
        player_hand.add(Card("spades", 13))
        player_hand.add(Card("clubs", 13))

        cards = [Card("hearts", 1), Card("hearts", 7), Card("hearts", 13)]
        pile = Deck(cards)

        computer_hand = Hand("")
        Computer().play(computer_hand, pile, player_hand)
        self.assertEqual(computer_hand.sum(), 0)

    def test_computer_always_tries_to_get_higher_total_than_player(self):
        player_hand = Hand("")
        player_hand.add(Card("spades", 13))
        player_hand.add(Card("clubs", 7))

        cards = [Card("hearts", 3), Card("hearts", 6), Card("hearts", 13)]
        deck = Deck(cards)

        computer_hand = Hand("")
        Computer().play(computer_hand, deck, player_hand)
        self.assertTrue(computer_hand.sum() > 21)


if __name__ == '__main__':
    unittest.main()
