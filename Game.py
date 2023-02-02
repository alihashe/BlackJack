import Deck
import Button
import pygame as pg
from time import sleep
from sys import exit

class Game:

    def __init__(self, totalCash):
        self.totalCash = totalCash

    def startBetting(self):
        self.hand = 0 # The current total value of a players hand
        self.dealerHand = 0 # The current total value of a dealers hand
        self.bet = 0 # The current amount of money riding on a turn.
        self.currCardVal = 0 # Value of a drawn card. Used when player hits.
        self.usedPlayerCards = [] # The used player cards are stored here so they can be drawn
        self.usedDealerCards = [] # The used dealer cards are stored here so they can be drawn
        # region Pygame Set-Up
        pg.init() # Initialize Pygame
        self.screen = pg.display.set_mode((1200,750)) # Set size of the window
        self.screen.fill('forestgreen') # Set Background Image
        pg.display.set_caption('BlackJack') # Name the window
        pg.display.set_icon(pg.image.load('Images/Chips/red_chip.png').convert()) # Set Icon
        self.frameSpeed = pg.time.Clock() # Framerate variable
        self.uiFont = pg.font.Font(None, 35)  # <-- Do Later
        self.chipFont = pg.font.Font(None, 60)  # <-- Do Later
        # endregion
        while True:
            self.mousePos = pg.mouse.get_pos()
            # region Text and Button Init
            self.betText = self.uiFont.render('Please Choose The Amount You Would Like To Bet!', True, 'White','forestgreen')
            self.betAmountText = self.uiFont.render('$' + str(self.bet), True, 'White', 'forestgreen')
            self.totalCashAmountText = self.uiFont.render('$' + str(self.totalCash), True, 'White', 'forestgreen')
            self.betButton = Button.Button(image=pg.image.load('Images/default_button_1.png'),pos=((self.screen.get_width() * 0.35),(self.screen.get_height() * 0.25)),text_input='Make Bet',font=self.uiFont,base_color='white',hovering_color='yellow')
            self.resetButton = Button.Button(image=pg.image.load('Images/default_button_1.png'),pos=((self.screen.get_width() * 0.65),(self.screen.get_height() * 0.25)),text_input='Reset',font=self.uiFont,base_color='white',hovering_color='yellow')

            self.betTextRect = self.betText.get_rect(center = (self.screen.get_width() // 2, 50))
            self.betAmountTextRect = self.betAmountText.get_rect(center = (self.screen.get_width() // 2, 100))
            self.totalCashAmountTextRect = self.totalCashAmountText.get_rect(center = (self.screen.get_width() - 75, self.screen.get_height() - 50))
            self.whiteChipButton = Button.Button(image=pg.image.load('Images/Chips/white_chip.png'),pos=((self.screen.get_width() * 0.2),(self.screen.get_height() * 0.75)),text_input="1$",font=self.chipFont,base_color='white',hovering_color='yellow')
            self.redChipButton = Button.Button(image=pg.image.load('Images/Chips/red_chip.png'),pos=((self.screen.get_width() * 0.35),(self.screen.get_height() * 0.5)),text_input="5$",font=self.chipFont,base_color='white',hovering_color='yellow')
            self.blueChipButton = Button.Button(image=pg.image.load('Images/Chips/blue_chip.png'),pos=((self.screen.get_width() * 0.5),(self.screen.get_height() * 0.75)),text_input="10$",font=self.chipFont,base_color='white',hovering_color='yellow')
            self.greenChipButton = Button.Button(image=pg.image.load('Images/Chips/green_chip.png'),pos=((self.screen.get_width() * 0.65),(self.screen.get_height() * 0.5)),text_input="25$",font=self.chipFont,base_color='white',hovering_color='yellow')
            self.blackChipButton = Button.Button(image=pg.image.load('Images/Chips/black_chip.png'),pos=((self.screen.get_width() * 0.8),(self.screen.get_height() * 0.75)),text_input="100$",font=self.chipFont,base_color='white',hovering_color='yellow')
        
            self.screen.blits([(self.betText,self.betTextRect),(self.betAmountText,self.betAmountTextRect),(self.totalCashAmountText,self.totalCashAmountTextRect)])
            # endregion
            for button in [self.whiteChipButton, self.redChipButton, self.blueChipButton, self.greenChipButton, self.blackChipButton]:
                button.changeColor(self.mousePos)
                button.resize(160,160)
                newNumber = ''.join(x for x in button.text_input if x.isdigit())
                if self.totalCash >= int(newNumber):
                    button.update(self.screen)

            if self.bet > 0:
                self.betButton.changeColor(self.mousePos)
                self.betButton.resize(150, 90)
                self.betButton.update(self.screen)
                self.resetButton.changeColor(self.mousePos)
                self.resetButton.resize(150, 90)
                self.resetButton.update(self.screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.whiteChipButton.checkForInput(self.mousePos) and self.totalCash - 1 >= 0:
                        self.totalCash -= 1
                        self.bet += 1
                        self.updateCosts()
                    elif self.redChipButton.checkForInput(self.mousePos) and self.totalCash - 5 >= 0:
                        self.totalCash -= 5
                        self.bet += 5
                        self.updateCosts()
                    elif self.blueChipButton.checkForInput(self.mousePos) and self.totalCash - 10 >= 0:
                        self.totalCash -= 10
                        self.bet += 10
                        self.updateCosts()
                    elif self.greenChipButton.checkForInput(self.mousePos) and self.totalCash - 25 >= 0:
                        self.totalCash -= 25
                        self.bet += 25
                        self.updateCosts()
                    elif self.blackChipButton.checkForInput(self.mousePos) and self.totalCash - 100 >= 0:
                        self.totalCash -= 100
                        self.bet += 100
                        self.updateCosts()

                    if self.betButton.checkForInput(self.mousePos) and self.bet > 0:
                        self.take_turn()
                    if self.resetButton.checkForInput(self.mousePos) and self.bet > 0:
                        self.totalCash += self.bet
                        self.bet -= self.bet
                        self.updateCosts()

            pg.display.update()
            pg.display.flip()
            self.frameSpeed.tick(60)

    def updateCosts(self):
        self.screen.fill('forestgreen')
        self.betAmountText = self.uiFont.render('$' + str(self.bet), True, 'White', 'forestgreen')
        self.totalCashAmountText = self.uiFont.render('$' + str(self.totalCash), True, 'White', 'forestgreen')

    def take_turn(self):
        self.screen.fill('forestgreen') # Set Background Image
        pg.display.set_caption('BlackJack') # Name the window
        pg.display.set_icon(pg.image.load('Images/Chips/red_chip.png').convert()) # Set Icon
        self.aDeck = Deck.Deck(image=pg.image.load('Images/card_back_black.png').convert_alpha(),pos=(self.screen.get_width() * 0.5,self.screen.get_height() * 0.25),text_input='HIT',font=self.chipFont,base_color='white',hovering_color='yellow')
        self.cardPos_X = self.screen.get_width() * 0.45
        self.aceCheck = 0
        self.dealer_first_draw()
        while True:
            self.mousePos = pg.mouse.get_pos()
            # self.aDeck = Deck.Deck(image=pg.image.load('Images/card_back_black.png').convert_alpha(),pos=(self.screen.get_width() * 0.5,self.screen.get_height() * 0.25),text_input='HIT',font=self.chipFont,base_color='white',hovering_color='yellow')
            # Put shuffle animation here later
            self.aDeck.changeColor(self.mousePos)
            self.aDeck.resize(176,250)
            self.aDeck.update(self.screen)
            self.stayButton = Button.Button(image=pg.image.load('Images/default_button_1.png').convert_alpha(),pos=(self.screen.get_width() * 0.85,self.screen.get_height() * 0.2),text_input='HOLD',font=self.uiFont,base_color='white',hovering_color='yellow')
            if self.currCardVal > 0:
                self.stayButton.changeColor(self.mousePos)
                self.stayButton.resize(150, 90)
                self.stayButton.update(self.screen)
            self.betAmountText = self.uiFont.render('BET: $' + str(self.bet), True, 'White', 'darkred')
            self.betAmountTextRect = self.betAmountText.get_rect(center = (self.screen.get_width() * 0.85, self.screen.get_height() * 0.85))
            self.screen.blit(self.betAmountText,self.betAmountTextRect)
            self.cardValText = self.uiFont.render('HAND: ' + str(self.hand), True, 'White', 'darkred')
            self.cardValTextRect = self.cardValText.get_rect(center = (self.screen.get_width() * 0.15, self.screen.get_height() * 0.85))
            self.screen.blit(self.cardValText,self.cardValTextRect)
            self.dealerCardValText = self.uiFont.render("DEALER'S HAND: " + str(self.dealerHand), True, 'White', 'darkred')
            self.dealerCardValTextRect = self.dealerCardValText.get_rect(center = (self.screen.get_width() * 0.15, self.screen.get_height() * 0.75))
            self.screen.blit(self.dealerCardValText,self.dealerCardValTextRect)
            self.draw_dealers_first_hand()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.aDeck.checkForInput(self.mousePos) and not self.hand == 21:
                        self.add_a_card(self.usedPlayerCards)
                        self.currCardVal = self.newCard.get_value()
                        # if self.newCard.get_value() == 1:
                        #     self.confirm_ace()
                        self.draw_player_hand()
                        self.hand += self.currCardVal
                    if self.stayButton.checkForInput(self.mousePos):
                        self.start_dealers_turn()
            if self.hand > 21:
                if self.check_ace(self.usedPlayerCards) > self.aceCheck:
                    self.hand -= 10
                    self.aceCheck += 1
                else:
                    self.dealer_second_draw()
                    self.end_round("Dealer Wins","Bet Lost: $","darkred")
            elif self.hand == 21:
                self.black_jack()
            pg.display.update()
            pg.display.flip()
            self.frameSpeed.tick(60)

    def start_dealers_turn(self):
        self.screen.fill('forestgreen') # Set Background Image
        self.aceCheck = 0
        while True:
            self.aDeck.resize(176,250)
            self.aDeck.update(self.screen)
            self.betAmountText = self.uiFont.render('BET: $' + str(self.bet), True, 'White', 'darkred')
            self.betAmountTextRect = self.betAmountText.get_rect(center = (self.screen.get_width() * 0.85, self.screen.get_height() * 0.85))
            self.screen.blit(self.betAmountText,self.betAmountTextRect)
            self.cardValText = self.uiFont.render('HAND: ' + str(self.hand), True, 'White', 'darkred')
            self.cardValTextRect = self.cardValText.get_rect(center = (self.screen.get_width() * 0.15, self.screen.get_height() * 0.85))
            self.screen.blit(self.cardValText,self.cardValTextRect)
            self.dealerCardValText = self.uiFont.render("DEALER'S HAND: " + str(self.dealerHand), True, 'White', 'darkred')
            self.dealerCardValTextRect = self.dealerCardValText.get_rect(center = (self.screen.get_width() * 0.15, self.screen.get_height() * 0.75))
            self.screen.blit(self.dealerCardValText,self.dealerCardValTextRect)
            self.draw_player_hand()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
            # self.dealer_second_draw()
            if self.dealerHand < self.hand:
                if self.dealerHand < 21:
                    self.dealer_second_draw()
                if self.dealerHand > 21:
                    if self.check_ace(self.usedDealerCards) > self.aceCheck:
                        self.dealerHand -= 10
                        self.aceCheck += 1
                    else:
                        self.totalCash += (self.bet * 2)
                        self.end_round("Player Wins","Bet Won: $","yellow")
                if self.dealerHand == 21 and self.hand == 21:
                    self.totalCash += self.bet
                    self.end_round("Tie","Bet Returned: $","white")
            else:
                self.end_round("Dealer Wins","Bet Lost: $","darkred")

            pg.display.update()
            pg.display.flip()
            self.frameSpeed.tick(60)

    # region Card Drawing and Management

    def add_a_card(self, usedCards):
        self.newCard = self.aDeck.pull_card()
        usedCards.append(self.newCard)

    def dealer_first_draw(self):
        self.add_a_card(self.usedDealerCards)
        self.currCardVal = self.newCard.get_value()
        self.draw_dealers_first_hand()
        self.dealerHand += self.currCardVal

    def dealer_second_draw(self):
        self.add_a_card(self.usedDealerCards)
        self.currCardVal = self.newCard.get_value()
        self.draw_dealers_second_hand()
        self.dealerHand += self.currCardVal

    def draw_dealers_first_hand(self):
        self.cardBack = pg.image.load('Images/card_back_black.png')
        self.cardBack = pg.transform.smoothscale(self.cardBack,(88,125))
        for crd in self.usedDealerCards:
            crd.draw(self.screen,self.cardPos_X + (self.usedDealerCards.index(crd) * 25),self.screen.get_height() * 0.55)
        newRect = self.cardBack.get_rect(center = (self.cardPos_X + 25,self.screen.get_height() * 0.55))
        self.screen.blit(self.cardBack,newRect)

    def draw_dealers_second_hand(self):
        for crd in self.usedDealerCards:
            crd.draw(self.screen,self.cardPos_X + (self.usedDealerCards.index(crd) * 25),self.screen.get_height() * 0.55)

    def draw_player_hand(self):
        for crd in self.usedPlayerCards:
            crd.draw(self.screen,self.cardPos_X + (self.usedPlayerCards.index(crd) * 25),self.screen.get_height() * 0.75)

    # endregion

    def end_round(self, resultTitle, resultBet, textColor):
        while True:
            pg.display.set_caption(resultTitle) # Name the window
            pg.display.set_icon(pg.image.load('Images/Chips/white_chip.png').convert()) # Set Icon
            self.mousePos = pg.mouse.get_pos()
            self.screen.fill('forestgreen') # Set Background Image
            self.lossText = self.chipFont.render(resultTitle, True, textColor,'forestgreen')
            self.lossTextRect = self.lossText.get_rect(center = (self.screen.get_width() * 0.5, self.screen.get_height() * 0.1))
            self.screen.blit(self.lossText,self.lossTextRect)
            self.finalHandText = self.chipFont.render("Hand: " + str(self.hand), True, 'White','forestgreen')
            self.finalHandTextRect = self.finalHandText.get_rect(center = (self.screen.get_width() * 0.5, self.screen.get_height() * 0.2))
            self.screen.blit(self.finalHandText,self.finalHandTextRect)
            self.finalDealerHandText = self.chipFont.render("Dealer's Hand: " + str(self.dealerHand), True, 'White','forestgreen')
            self.finalDealerHandTextRect = self.finalDealerHandText.get_rect(center = (self.screen.get_width() * 0.5, self.screen.get_height() * 0.275))
            self.screen.blit(self.finalDealerHandText,self.finalDealerHandTextRect)
            self.finalBetResultText = self.chipFont.render(resultBet + str(self.bet), True, 'White','forestgreen')
            self.finalBetResultTextRect = self.finalBetResultText.get_rect(center = (self.screen.get_width() * 0.5, self.screen.get_height() * 0.35))
            self.screen.blit(self.finalBetResultText,self.finalBetResultTextRect)
            self.draw_player_hand()
            self.draw_dealers_second_hand()
            self.newBetButton = Button.Button(image=pg.image.load('Images/default_button_1.png'),pos=((self.screen.get_width() * 0.25),(self.screen.get_height() * 0.75)),text_input='Bet Again',font=self.uiFont,base_color='white',hovering_color='yellow')
            self.exitButton = Button.Button(image=pg.image.load('Images/default_button_1.png'),pos=((self.screen.get_width() * 0.75),(self.screen.get_height() * 0.75)),text_input='Leave',font=self.uiFont,base_color='white',hovering_color='yellow')
            for button in [self.newBetButton,self.exitButton]:
                button.changeColor(self.mousePos)
                button.resize(160,160)
                button.update(self.screen)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.newBetButton.checkForInput(self.mousePos):
                        self.startBetting()
                    if self.exitButton.checkForInput(self.mousePos):
                        pg.quit()
                        exit()
            pg.display.update()
            pg.display.flip()
            self.frameSpeed.tick(60)

    def black_jack(self):
        pass

    def check_ace(self, usedCards):
        numberOfAces = 0
        for crd in usedCards:
            if crd.get_value() == 11:
                numberOfAces += 1
        return numberOfAces


newGame = Game(5000)
newBet = newGame.startBetting()