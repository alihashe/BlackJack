from random import shuffle
import Card
import Button
import pygame as pg

class Deck(Button.Button):

    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        super().__init__(image, pos, text_input, font, base_color, hovering_color)
        self.size = 52
        self.deckList = []
        self.generate_deck()
        

    # region Generate Card Value Types

    def generate_num_cards(self, suit, col, image):
        numOfNumCards = 10
        i = 2
        while i <= numOfNumCards:
            self.deckList.append(Card.Card(i, suit, col, "Images/Front/" + str(i) + image))
            i += 1

    def generate_face_cards(self, suit, col):
        self.deckList.append(Card.Card(10, suit, col, "Images/Front/jack_of_" + suit + ".png"))
        self.deckList.append(Card.Card(10, suit, col, "Images/Front/king_of_" + suit + ".png"))
        self.deckList.append(Card.Card(10, suit, col, "Images/Front/queen_of_" + suit + ".png"))

    def generate_ace(self, suit, col, image):
        self.deckList.append(Card.Card(1, suit, col, image))

    # endregion

    # region Generate Suit Types

    def generate_clubs(self):
        self.generate_ace("clubs", "black", "Images/Front/ace_of_clubs.png")
        self.generate_num_cards("clubs", "black", "_of_clubs.png")
        self.generate_face_cards("clubs", "black")

    def generate_diamonds(self):
        self.generate_ace("diamonds", "red", "Images/Front/ace_of_diamonds.png")
        self.generate_num_cards("diamonds", "red", "_of_diamonds.png")
        self.generate_face_cards("diamonds", "red")

    def generate_hearts(self):
        self.generate_ace("hearts", "red", "Images/Front/ace_of_hearts.png")
        self.generate_num_cards("hearts", "red", "_of_hearts.png")
        self.generate_face_cards("hearts", "red")

    def generate_spades(self):
        self.generate_ace("spades", "black", "Images/Front/ace_of_spades.png")
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

    def animate_shuffle(self, screen, initialPos):
        index = 0
        while(index < self.size):
            while initialPos[0] not in range(self.rect.left, self.rect.right) and initialPos[1] not in range(self.rect.top, self.rect.bottom):
                screen.blit(self.image, self.image.get_rect(center=(initialPos[0], initialPos[1])))
                initialPos[0] += 0.1
                initialPos[1] += 0.1
                screen.fill('forestgreen')
            index += 1

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