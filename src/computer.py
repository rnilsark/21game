from deck import Deck
from hand import Hand
from rule_set import RuleSet


class Computer(object):
    @staticmethod
    def play(hand: Hand, deck: Deck, player_hand: Hand):

        if RuleSet.is_bust(player_hand):
            # No need to do anything
            return

        while deck.count() > 0:
            hand.add(deck.draw())

            if RuleSet.sums_to_21(hand) or RuleSet.is_bust(hand) or hand.sum() >= player_hand.sum():
                # Computer is cheating looking at player cards
                return
