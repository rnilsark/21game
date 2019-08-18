from hand import Hand


class RuleSet(object):

    # Console game rule set
    @staticmethod
    def determine_winner(computer_hand: Hand, player_hand: Hand):

        if RuleSet.sums_to_21(player_hand):
            return player_hand
        elif RuleSet.sums_to_21(computer_hand):
            return computer_hand
        elif RuleSet.is_bust(computer_hand):
            return player_hand
        elif RuleSet.is_bust(player_hand):
            return computer_hand
        elif computer_hand.sum() >= player_hand.sum():
            return computer_hand
        elif player_hand.sum() > computer_hand.sum():
            return player_hand

    # TODO move into hand
    @staticmethod
    def sums_to_21(hand):
        return hand.sum() == 21

    # TODO move into hand
    @staticmethod
    def is_bust(hand):
        if hand.sum() > 21:
            return True

        return False
