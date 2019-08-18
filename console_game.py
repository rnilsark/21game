from deck import Deck
from computer import Computer
from hand import Hand
from player import Player
from rule_set import RuleSet


def player_stops():
    return str(input("Draw [Y, N]? ")).lower() == "n"


def run():
    pile = Deck.standard_deck()
    pile.shuffle()

    player_hand = Hand("Player")
    computer_hand = Hand("Computer")

    player = Player()
    computer = Computer()

    while not player.stopped:

        if player_stops():
            player.stop()
        else:
            player.draw(player_hand, pile)

        print(player_hand)

        if RuleSet.sums_to_21(player_hand) or RuleSet.is_bust(player_hand):
            break

        print("---------")
        print("Total: {0}".format(player_hand.sum()))

    computer.play(computer_hand, pile, player_hand)

    print("\n=== WINNER ===")
    print("---------")
    winning_hand = RuleSet().determine_winner(computer_hand, player_hand)

    if RuleSet.sums_to_21(winning_hand):
        print("{0} got 21".format(winning_hand.holder))
    else:
        print("{0} won ({1})".format(winning_hand.holder, winning_hand.sum()))


run()
