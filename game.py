import random

from cards import Cards

class MemoryGame:
    def __init__(self):
        self.cards = []
        self.score = 0
        self.moves = 0

        self.create_cards()

    def create_cards(self, num_pairs=6):

        values = [
            "🍎", "🍎",
            "🌟", "🌟",
            "❤️", "❤️",
            "🎵", "🎵",
            "🐶", "🐶",
            "🦋", "🦋",


        ]

        random.shuffle(values)

        for value in values:
            card = Cards(value)
            self.cards.append(card)
