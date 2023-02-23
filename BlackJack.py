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