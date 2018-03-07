from card import Card

class Hand():
    def __init__(self, cards_list = None):
        if cards_list == None:
            self.cards = []
        elif all(isinstance(x, Card) for x in cards_list):
            self.cards = cards_list
        elif all(isinstance(x, str) for x in cards_list):
            rank_dict = {
                '2':2,
                '3':3,
                '4':4,
                '5':5,
                '6':6,
                '7':7,
                '8':8,
                '9':9,
                'T':10,
                'J':11,
                'Q':12,
                'K':13,
                'A':14,
            }
            self.cards = [Card(card[1], rank_dict[card[0]]) for card in cards_list]
        else:
            self.cards = []

    def __str__(self):
        if len(self.cards) > 0:
            output = ""
            for card in self.cards:
                output = output + str(card) + "  "
        else:
            output = "none"

        return output

    def add_card(self, card):
        if type(card) == Card:
            self.cards.append(card)
        if type(card) == list:
            for item in card:
                self.cards.append(item)

    def contains_ace(self):
        rank_list = [card.rank for card in self.cards]
        if 14 in rank_list:
            return True
        else:
            return False

    def discard(self, pos):
        self.cards.pop(pos)

    def draw_card(self, deck):
        self.cards.append(deck.draw_card())

    def empty_hand(self):
        self.cards = []

    def get_cards_with_rank(self, rank):
        return [card for card in self.cards if card.rank == rank]

    def get_cards_with_suit(self, suit):
        return [card for card in self.cards if card.suit == suit]

    def get_max_rank(self):
        rank_list = [card.rank for card in self.cards]
        return max(rank_list)

    def get_min_rank(self):
        rank_list = [card.rank for card in self.cards]
        return min(rank_list)
