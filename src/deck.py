import random


class Card(object):
    def __init__(self, suite: str, rank: int):
        self.rank = rank
        self.suite = suite

    def __get_rank_str(self):
        if self.rank == 11:
            return "jack"
        elif self.rank == 12:
            return "queen"
        elif self.rank == 13:
            return "king"
        elif self.rank == 1:
            return "ace"
        else:
            return str(self.rank)

    def __str__(self):
        return self.suite + " " + self.__get_rank_str()

    @staticmethod
    def get_suit(suite):
        for rank in range(1, 13):
            yield Card(suite, rank)


class Deck(object):
    def __init__(self, cards: Card):
        self.cards = cards

    @classmethod
    def standard_deck(cls):
        cards = []
        cards.extend(Card.get_suit("hearts"))
        cards.extend(Card.get_suit("spades"))
        cards.extend(Card.get_suit("diamonds"))
        cards.extend(Card.get_suit("clubs"))

        return Deck(cards)

    def draw(self):
        assert self.count() > 0
        return self.cards.pop()

    def count(self):
        return len(self.cards)

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            j = random.randint(0, i + 1)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]