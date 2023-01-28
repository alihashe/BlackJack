from random import shuffle
import Card
import pygame as pg

class Deck(pg.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.size = 52
        self.deckList = []
        self.generate_deck()
        self.image = pg.image.load('Images/card_back_black.png').convert_alpha()
        self.image = pg.transform.scale(self.image,(176,250))
        self.rect = self.image.get_rect(center = (screen.get_width() // 2,250))

    # region Generate Card Value Types

    def generate_num_cards(self, suit, col, image):
        numOfNumCards = 10
        i = 2
        while i <= numOfNumCards:
            self.deckList.append(Card.Card(i, suit, col, str(i) + image))
            i += 1

    def generate_face_cards(self, suit, col):
        self.deckList.append(Card.Card(10, suit, col, "jack_of_" + suit + ".png"))
        self.deckList.append(Card.Card(10, suit, col, "king_of_" + suit + ".png"))
        self.deckList.append(Card.Card(10, suit, col, "queen_of_" + suit + ".png"))

    def generate_ace(self, suit, col, image):
        self.deckList.append(Card.Card(1, suit, col, image))

    # endregion

    # region Generate Suit Types

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

    # endregion

    def generate_deck(self):
        self.generate_clubs()
        self.generate_diamonds()
        self.generate_hearts()
        self.generate_spades()
        self.shuffleDeck()
        if (len(self.deckList) != self.size):
            raise Exception("Deck has incorrect number of cards. Check Deck class.")

    def shuffleDeck(self):
        shuffle(self.deckList)

    def pull_card(self):
        if not self.deckList:
            self.generate_deck()
            return self.deckList.pop()
        else:
            return self.deckList.pop()


# region For Testing

# newDeck = Deck()
# i = 0
# for c in newDeck.deckList:
#     i+=1
#     print(c.get_value())
#     print(c.get_suit())
#     print(c.get_color())
#     print(c.get_image())
# print(i)
# newDeck.shuffleDeck()
# for c in newDeck.deckList:
#     print(c.get_value())
#     print(c.get_suit())
#     print(c.get_color())
#     print(c.get_image())

# endregion