import unittest
from deck import Card
from hand import Hand


class GameTests(unittest.TestCase):
    def test_hand_sums_according_to_rank(self):
        hand = Hand("")
        hand.add(Card("diamond", 7))
        hand.add(Card("diamond", 10))
        hand.add(Card("diamond", 2))
        self.assertEqual(hand.sum(), 19)

    def test_ace_ranks_14(self):
        hand = Hand("")
        hand.add(Card("diamond", 1))
        self.assertEqual(hand.sum(), 14)

    def test_ace_ranks_1_when_hand_getting_bust(self):
        hand = Hand("")
        hand.add(Card("diamond", 5))
        hand.add(Card("diamond", 1))
        hand.add(Card("clubs", 1))
        hand.add(Card("hearts", 1))
        self.assertEqual(hand.sum(), 21)


if __name__ == '__main__':
    unittest.main()
