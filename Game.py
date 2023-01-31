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
        self.myFont = pg.font.Font(None, 35)  # <-- Do Later
        # endregion
        while(True):
            self.mousePos = pg.mouse.get_pos()
            self.betText = self.myFont.render('Please Choose The Amount You Would Like To Bet!', True, 'White','forestgreen')
            self.betAmountText = self.myFont.render('$' + str(self.bet), True, 'White', 'forestgreen')
            self.totalCashAmountText = self.myFont.render('$' + str(self.totalCash), True, 'White', 'forestgreen')
            self.betButton = Button.Button(image=pg.image.load('Images/default_button_1.png'),pos=((self.screen.get_width() * 0.35),(self.screen.get_height() * 0.25)),text_input='Make Bet',font=self.myFont,base_color='white',hovering_color='yellow')
            self.resetButton = Button.Button(image=pg.image.load('Images/default_button_1.png'),pos=((self.screen.get_width() * 0.65),(self.screen.get_height() * 0.25)),text_input='Reset',font=self.myFont,base_color='white',hovering_color='yellow')

            self.betTextRect = self.betText.get_rect(center = (self.screen.get_width() // 2, 50))
            self.betAmountTextRect = self.betAmountText.get_rect(center = (self.screen.get_width() // 2, 100))
            self.totalCashAmountTextRect = self.totalCashAmountText.get_rect(center = (self.screen.get_width() - 75, self.screen.get_height() - 50))
            self.whiteChipButton = Button.Button(image=pg.image.load('Images/Chips/white_chip.png'),pos=((self.screen.get_width() * 0.2),(self.screen.get_height() * 0.75)),text_input="1$",font=self.myFont,base_color='green',hovering_color='yellow')
            self.redChipButton = Button.Button(image=pg.image.load('Images/Chips/red_chip.png'),pos=((self.screen.get_width() * 0.35),(self.screen.get_height() * 0.5)),text_input="5$",font=self.myFont,base_color='green',hovering_color='yellow')
            self.blueChipButton = Button.Button(image=pg.image.load('Images/Chips/blue_chip.png'),pos=((self.screen.get_width() * 0.5),(self.screen.get_height() * 0.75)),text_input="10$",font=self.myFont,base_color='green',hovering_color='yellow')
            self.greenChipButton = Button.Button(image=pg.image.load('Images/Chips/green_chip.png'),pos=((self.screen.get_width() * 0.65),(self.screen.get_height() * 0.5)),text_input="25$",font=self.myFont,base_color='green',hovering_color='yellow')
            self.blackChipButton = Button.Button(image=pg.image.load('Images/Chips/black_chip.png'),pos=((self.screen.get_width() * 0.8),(self.screen.get_height() * 0.75)),text_input="100$",font=self.myFont,base_color='green',hovering_color='yellow')
        

            self.screen.blits([(self.betText,self.betTextRect),(self.betAmountText,self.betAmountTextRect),(self.totalCashAmountText,self.totalCashAmountTextRect)])

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

                    if self.betButton.checkForInput(self.mousePos):
                        print("begin game")
                        return self.bet
                    if self.resetButton.checkForInput(self.mousePos):
                        self.totalCash += self.bet
                        self.bet -= self.bet
                        self.updateCosts()

            pg.display.update()
            pg.display.flip()
            self.frameSpeed.tick(60)

    def updateCosts(self):
        self.screen.fill('forestgreen')
        self.betAmountText = self.myFont.render('$' + str(self.bet), True, 'White', 'forestgreen')
        self.totalCashAmountText = self.myFont.render('$' + str(self.totalCash), True, 'White', 'forestgreen')

    def take_turn(self, betAmount):
        # region Pygame Set-Up
        pg.init() # Initialize Pygame
        self.screen = pg.display.set_mode((1200,750)) # Set size of the window
        self.screen.fill('forestgreen') # Set Background Image
        pg.display.set_caption('BlackJack') # Name the window
        pg.display.set_icon(pg.image.load('Images/Chips/red_chip.png').convert()) # Set Icon
        self.frameSpeed = pg.time.Clock() # Framerate variable
        self.myFont = pg.font.Font(None, 35)  # <-- Do Later
        # endregion
        while (True):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
            pg.display.update()
            pg.display.flip()
            self.frameSpeed.tick(60)

newGame = Game(5000)
newBet = newGame.startBetting()
newGame.take_turn(newBet)