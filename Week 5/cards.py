# #Set the class card = Card
# #Same line we pass the suit and rank
#
# card = Card("Spades", "8")
# card = Card("Clubs", "Ace")
# card.print_card()
#
# card.suit = "Hearts"
# card.print_card()
#
# my_card = Card("Hearts", "7")
# print(my_card.is_valid())
#
# second_draw = Card("Spades", "Joker")
# print(second_draw.is_valid())
#
# card = Card("Hearts", "7")
# print(card.get_value())
#
# card_two = Card("Spades", "Jack")
# print(card_two.get_value())

class Card():
    def __init__(self, suit, rank, next = None):
        self.suit = suit
        self.rank = rank
        self.next = next

    def print_card(self):
        print(f"{self.rank} of {self.suit}")

    def is_valid(self):
        if self.suit in ["Hearts", "Spades", "Clubs", "Diamonds"]:
            if self.rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]:
                return True
        return False

    def get_value(self):
        if not self.is_valid():
            return None
        if self.rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            return int(self.rank)
        if self.rank == "Ace":
            return 1
        if self.rank == "Jack":
            return 11
        if self.rank == "Queen":
            return 12
        if self.rank == "King":
            return 13

class Hand():
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)


card_one = Card("Hearts", "3")
card_two = Card("Spades", "8")

player1_hand = Hand()
# cards = []

player1_hand.add_card(card_one)
# cards = [card_one]

player1_hand.add_card(card_two)
# cards = [card_one, card_two]

player1_hand.remove_card(card_one)
# cards = [card_two]

def sum_hand(hand):
    sum = 0
    for card in hand.cards:
        if not card.is_valid():
            return None
        sum += card.get_value()
    return sum

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "Jack")
card_three = Card("Spades", "3")

hand = Hand()
hand.add_card(card_one)
hand.add_card(card_two)
hand.add_card(card_three)

sum = sum_hand(hand)
print(sum)

def print_hand(starting_card):
    x = []
    current_card = starting_card
    while current_card is not None:
        x.append(current_card)
        current_card = current_card.next
    print(x)

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "King")

card_one.next = card_two
card_two.next = card_three

print_hand(card_one)