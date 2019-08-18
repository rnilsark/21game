from deck import Deck
from hand import Hand


class Player(object):
    def __init__(self):
        self.stopped = False

    @staticmethod
    def draw(hand: Hand, deck: Deck):
        hand.add(deck.draw())

    def stop(self):
        self.stopped = True
