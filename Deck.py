import random
import Card
from Card import *

class Deck:

    def __init__(self):
        self.size = 52
        self.deckList = []

    def generate_num_cards(self, suit, col, image):
        numOfNumCards = 10
        i = 2
        while i <= numOfNumCards:
            self.deckList.append(Card(i, suit, col, str(i) + image))
            i += 1

    def generate_face_cards(self, suit, col):
        self.deckList.append(Card(10, suit, col, "jack_of_" + suit + ".png"))
        self.deckList.append(Card(10, suit, col, "king_of_" + suit + ".png"))
        self.deckList.append(Card(10, suit, col, "queen_of_" + suit + ".png"))

    def generate_ace(self, suit, col, image):
        self.deckList.append(Card(1, suit, col, image))

    def generate_clubs(self):
        self.generate_ace("clubs", "black", "ace_of_clubs.png")
        self.generate_num_cards("clubs", "black", "_of_clubs.png")
        self.generate_face_cards("clubs", "black")

    def generate_diamonds(self):
        self.generate_ace("diamonds", "red", "ace_of_diamonds.png")
        self.generate_num_cards("diamonds", "red", "_of_diamonds.png")
        self.generate_face_cards("diamonds", "red")

    def generate_hearts(self):
        self.generate_ace("hearts", "red", "ace_of_hearts.png")
        self.generate_num_cards("hearts", "red", "_of_hearts.png")
        self.generate_face_cards("hearts", "red")

    def generate_spades(self):
        self.generate_ace("spades", "black", "ace_of_spades.png")
        self.generate_num_cards("spades", "black", "_of_spades.png")
        self.generate_face_cards("spades", "black")

    def generate_deck(self):
        self.generate_clubs()
        self.generate_diamonds()
        self.generate_hearts()
        self.generate_spades()
        self.shuffleDeck()

    def shuffleDeck(self):
        random.shuffle(self.deckList)

    def pull_card(self):
        if not self.deckList:
            self.generate_deck()
            return self.deckList.pop()
        else:
            return self.deckList.pop()


# For Testing

# newDeck = Deck()
# newDeck.generate_deck()
# for c in newDeck.deckList:
#     print(c.get_value())
#     print(c.get_suit())
#     print(c.get_color())
#     print(c.get_image())
# newDeck.shuffleDeck()
# for c in newDeck.deckList:
#     print(c.get_value())
#     print(c.get_suit())
#     print(c.get_color())
#     print(c.get_image())
