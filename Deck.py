import Card

class Deck:

    def __init__(self):
        self.size = 52
        self.deckSize = 0
        self.deckList = {}

    def generate_num_cards(self, suit, col, image):
        numOfNumCards = 10
        i = 2
        while i <= numOfNumCards:
            self.deckList[self.deckSize] = Card(i, suit, col, image)
            self.deckSize += 1
            i += 1

    def generate_face_cards(self, suit, col, image):
        numOfFaceCards = 3
        i = 1
        while i <= numOfFaceCards:
            self.deckList[self.deckSize] = Card(10, suit, col, image)
            self.deckSize += 1
            i += 1

    def generate_aces(self, suit, col, image):
        self.deckList[self.deckSize] = Card(1, suit, col, image)
        self.deckSize += 1

    def generate_reds(self, image):
        pass

    def generate_blacks(self):
        pass

    def generate_deck(self):
        pass
