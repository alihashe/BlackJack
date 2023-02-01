import Deck
import Button
# import Card
import pygame as pg
from sys import exit

class Game:

    def __init__(self, totalCash):
        self.totalCash = totalCash
        self.hand = 0 # The current total value of a players hand
        self.bet = 0 # The current amount of money riding on a turn.
        self.currCardVal = 0 # Value of a drawn card. Used when player hits.

    def startBetting(self):
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
        while(True):
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
                        print("begin game")
                        return self.bet
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
        # region Pygame Set-Up
        pg.init() # Initialize Pygame
        self.screen = pg.display.set_mode((1200,750)) # Set size of the window
        self.screen.fill('forestgreen') # Set Background Image
        pg.display.set_caption('BlackJack') # Name the window
        pg.display.set_icon(pg.image.load('Images/Chips/red_chip.png').convert()) # Set Icon
        self.frameSpeed = pg.time.Clock() # Framerate variable
        self.uiFont = pg.font.Font(None, 35)  # <-- Do Later
        # endregion
        while (True):
            self.mousePos = pg.mouse.get_pos()
            self.aDeck = Deck.Deck(image=pg.image.load('Images/card_back_black.png').convert_alpha(),pos=(self.screen.get_width() * 0.5,self.screen.get_height() * 0.25),text_input='HIT',font=self.chipFont,base_color='white',hovering_color='yellow')
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
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.aDeck.checkForInput(self.mousePos):
                        self.newCard = self.aDeck.pull_card()
                        self.currCardVal = self.newCard.get_value()
                        if self.newCard.get_value() == 1:
                            self.confirm_ace()
                        self.newCard.draw(self.screen,self.screen.get_width() * 0.5,self.screen.get_height() * 0.75)
                        self.hand += self.currCardVal
                    if self.stayButton.checkForInput(self.mousePos):
                        print('On Stay')
            if self.hand > 21:
                self.bet = 0
                pg.time.wait(3000)
                self.end_round("You Lose!")
            elif self.hand == 21:
                self.black_jack()
            pg.display.update()
            pg.display.flip()
            self.frameSpeed.tick(60)

    def end_round(self, resultText):
        self.hand = 0
        self.bet = 0
        while True:
            pg.display.set_caption(resultText) # Name the window
            pg.display.set_icon(pg.image.load('Images/Chips/white_chip.png').convert()) # Set Icon
            self.mousePos = pg.mouse.get_pos()
            self.screen.fill('forestgreen') # Set Background Image
            self.lossText = self.chipFont.render(resultText, True, 'White','forestgreen')
            self.lossTextRect = self.lossText.get_rect(center = (self.screen.get_width() * 0.5, self.screen.get_height() * 0.25))
            self.screen.blit(self.lossText,self.lossTextRect)
            self.newBetButton = Button.Button(image=pg.image.load('Images/default_button_1.png'),pos=((self.screen.get_width() * 0.35),(self.screen.get_height() * 0.75)),text_input='Bet Again',font=self.uiFont,base_color='white',hovering_color='yellow')
            self.exitButton = Button.Button(image=pg.image.load('Images/default_button_1.png'),pos=((self.screen.get_width() * 0.65),(self.screen.get_height() * 0.75)),text_input='Leave',font=self.uiFont,base_color='white',hovering_color='yellow')
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
                        exit
            pg.display.update()
            pg.display.flip()
            self.frameSpeed.tick(60)

    def black_jack(self):
        pass

    def confirm_ace(self):
        while (True):
            pg.display.set_caption('Confirmation') # Name the window
            pg.display.set_icon(pg.image.load('Images/Chips/blue_chip.png').convert()) # Set Icon
            self.mousePos = pg.mouse.get_pos()
            self.screen.fill('forestgreen')
            self.newCard.draw(self.screen,self.screen.get_width() * 0.5,self.screen.get_height() * 0.75)
            self.confirmText = self.chipFont.render('Choose the value...', True, 'White','forestgreen')
            self.confirmTextRect = self.confirmText.get_rect(center = (self.screen.get_width() * 0.5, self.screen.get_height() * 0.25))
            self.screen.blit(self.confirmText,self.confirmTextRect)
            if (self.hand + 11 > 21):
                self.elevenButton = Button.Button(image=pg.image.load('Images/default_button_1.png'),pos=((self.screen.get_width() * 0.35),(self.screen.get_height() * 0.75)),text_input='11',font=self.uiFont,base_color='white',hovering_color='yellow')
                self.elevenButton.changeColor(self.mousePos)
                self.elevenButton.resize(160,160)
                self.elevenButton.update(self.screen)
            if (self.hand + 1 > 21):
                self.oneButton = Button.Button(image=pg.image.load('Images/default_button_1.png'),pos=((self.screen.get_width() * 0.65),(self.screen.get_height() * 0.75)),text_input='1',font=self.uiFont,base_color='white',hovering_color='yellow')
                self.oneButton.changeColor(self.mousePos)
                self.oneButton.resize(160,160)
                self.oneButton.update(self.screen)
            else:
                self.currCardVal = 1
                self.screen.fill('forestgreen')
                return
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.elevenButton.checkForInput(self.mousePos):
                        self.currCardVal = 11
                        self.screen.fill('forestgreen')
                        return
                    if self.oneButton.checkForInput(self.mousePos):
                        self.currCardVal = 1
                        self.screen.fill('forestgreen')
                        return
            pg.display.update()
            pg.display.flip()
            self.frameSpeed.tick(60)

newGame = Game(5000)
newBet = newGame.startBetting()
newGame.take_turn()