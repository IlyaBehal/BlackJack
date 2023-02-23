from random import shuffle


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


class Deck(object):
    def __init__(self):
        ranks = "23456789TJQKA"
        suits = "DCHS"
        self.cards = [Card(r, s) for r in ranks for s in suits]  # list generator is creating full deck
        shuffle(self.cards)  # shuffle the deck

    def deal_card(self):
        return self.cards.pop()


def new_game():
    d = Deck()
    player_hand = Hand("Player")
    dealer_hand = Hand("Dealer")
    player_hand.add_card(d.deal_card())  # give two cards to player
    player_hand.add_card(d.deal_card())
    dealer_hand.add_card(d.deal_card())  # give one card to dealer
    print(dealer_hand)
    print("="*20)
    print(player_hand)
    in_game = True  # flag for check
    while player_hand.get_value() < 21:
        ans = input("Hit or stand? (h/s) ")
        if ans == "h":
            player_hand.add_card(d.deal_card())
            print(player_hand)
            if player_hand.get_value() > 21:  # if player has 21+ point - he lose
                print("You lose")
                in_game = False
        else:
            print("You stand!")
            break
    print("=" * 20)
    if in_game:
        while dealer_hand.get_value() < 17:  # rules game
            dealer_hand.add_card(d.deal_card())
            print(dealer_hand)
            if dealer_hand.get_value() > 21:  # if dealer has 21+ point - he lose
                print("Dealer bust")
                in_game = False
    if in_game:
        if player_hand.get_value() > dealer_hand.get_value():
            print("You win")
        else:
            print("Dealer win")


if __name__ == '__main__':
    new_game()
