class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        if self.rank in "TJQK":
            # По 10 за десятку, валета, даму та короля
            return 10
        else:
            # Повертає потрібну кількість очок за будь-яку іншу карту
            # Туз спочатку дає одне очко.
            return "A23456789".index(self.rank)

    def get_rank(self):
        return self.rank

    def __str__(self):
        return f"{self.rank}{self.suit}"


class Hand(object):
    def __init__(self, name):
        self.name = name  # player name
        self.cards = []  # emtpy hand

    def add_card(self, card):  # add card on hand
        self.cards.append(card)

    def get_value(self):  # method getting the points
        result = 0
        aces = 0  # count of A in hand
        for card in self.cards:
            result += card.card_value()
            if card.get_rank() == "A":  # if A on hand - aces ++
                aces += 1
        if result + aces * 10 <= 21:  # deciding T = 1 point ot T = 11 point
            result += aces * 10
        return result

    def __str__(self):
        text = f"{self.name}'s contains:\n"
        for card in self.cards:
            text += str(card) + " "
        text += f"\nHand value: {self.get_value()}"
        return text

