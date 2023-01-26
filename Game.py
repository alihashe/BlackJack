import Player
from Card import *
from Deck import *
from GUI import *

class Game:

    def __init__(self, totalCash):
        self.hand = 0
        self.bet = 0
        self.currCardVal = 0
        self.totalCash = totalCash
        self.playerNames = []

    def run_single_game(self):
        while(True):
            playerOneName = input("Please enter the name of the player --> ")
            play1 = Player(playerOneName, 5000)
            self.playerNames.append(play1)
            print(playerOneName + ", you will begin with $" + str(self.totalCash) + ".\n")
            aDeck = Deck()
            aDeck.generate_deck()
            aDeck.shuffleDeck()
            newCard = aDeck.pull_card()

    def take_turn(self, playerName, betAmount):
        self.take_bet()
    
    def take_bet(self):
        """Collects the bet amount from the player."""
        self.bet = input("Please enter the amount you would like to bet --> ")
        while self.bet > self.totalCash:
            self.bet = input("Insufficient Funds. Please enter the amount you would like to bet --> ")

    def get_hand(self):
        """Returns the value of the cards in hand"""
        return self.hand

    def hit(self, cardVal):
        """Adds a new card to the player hand"""
        self.hand += cardVal

    def bust(self):
        """Player goes over 21 and loses immediately"""
        self.bet = 0
