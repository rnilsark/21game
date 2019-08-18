class Hand(object):
    def __init__(self, holder):
        self.holder = holder
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def __str__(self):
        hand_str = ""
        for card in self.cards:
            hand_str = hand_str + "\n" + card.__str__()
        return hand_str

    def sum(self):
        total = 0
        aces = []  # Aces ranks 1 or 14

        for card in self.cards:
            if card.rank == 1:
                aces.append(card)
            else:
                total = total + card.rank

        for index in range(0, len(aces)):
            if 21 - total - len(aces) + index + 1 >= 14:
                total = total + 14
            else:
                total = total + 1

        return total

