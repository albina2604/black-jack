# Модуль cards
# Набор базовых классов для карточной игры

import easygui as gui


class Card:
    """ Одна игральная карта. """
    RANKS = ["Т", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "В", "Д", "K"]
    SUITS = [u'\u2660', u'\u2663', u'\u2665', u'\u2666']  # ♠ ♣ ♥ ♦
    SUITS_STR = ''.join(SUITS)
    SUITS_NAMES = 'schd'

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Unprintable_Card(Card):
    """ Карта, номинал и масть которой не могут быть выведены на экран. """

    def __str__(self):
        return "<нельзя напечатать>"


class Positionable_Card(Card):
    """ Карта, которую можно положить лицом или рубашкой вверх. """

    def __init__(self, rank, suit, face_up=True):
        super().__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super().__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


class Hand:
    """ Рука: набор карт на руках у одного игрока. """

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<пусто>"
        return rep

    def card_images(self):
        rep = []
        if self.cards:
            for card in self.cards:
                card_name = str(card)
                if card_name == 'XX':
                    filename = 'back.png'
                else:
                    table = card_name.maketrans(
                        Card.SUITS_STR, Card.SUITS_NAMES)
                    card_name = card_name.translate(table)
                    filename = f'{card_name[-1]}{(Card.RANKS.index(card_name[:-1]) + 1):0>2}.png'
                rep.append('assets/' + filename)
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """ Колода игральных карт. """

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    gui.msgbox("Не могу больше сдавать: карты закончились!")


if __name__ == "__main__":
    gui.msgbox("Вы запустили модуль cards, а не импортировали его (import cards).")
