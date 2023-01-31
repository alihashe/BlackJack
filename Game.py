# import Player
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
        # region Pygame Set-Up
        pg.init() # Initialize Pygame
        self.screen = pg.display.set_mode((1200,750)) # Set size of the window
        pg.display.set_caption('BlackJack') # Name the window
        pg.display.set_icon(pg.image.load('Images/Chips/red_chip.png').convert()) # Set Icon
        self.frameSpeed = pg.time.Clock() # Framerate variable
        self.myFont = pg.font.Font(None, 35)  # <-- Do Later
        self.mouseRect = pg.draw.rect(self.screen, (0,0,0,0), pg.Rect(1, 1, 1, 1))
        # endregion
        self.run_single_game()

    def run_single_game(self):
        self.screen.fill('forestgreen') # Set Background Image
        self.aDeck = Deck.Deck(self.screen) # Generate and shuffle a Deck
        self.startBetting()

    def startBetting(self):
        self.betText = self.myFont.render('Please Choose The Amount You Would Like To Bet!', True, 'White','forestgreen')
        self.betAmountText = self.myFont.render('$' + str(self.bet), True, 'White', 'forestgreen')
        self.totalCashAmountText = self.myFont.render('$' + str(self.totalCash), True, 'White', 'forestgreen')

        self.betTextRect = self.betText.get_rect(center = (self.screen.get_width() // 2, 50))
        self.betAmountTextRect = self.betAmountText.get_rect(center = (self.screen.get_width() // 2, 100))
        self.totalCashAmountTextRect = self.totalCashAmountText.get_rect(center = (self.screen.get_width() - 75, self.screen.get_height() - 50))
        while(True):
            self.mousePos = pg.mouse.get_pos()
            self.whiteChipButton = Button.Button(image=pg.image.load('Images/Chips/white_chip.png'),pos=((self.screen.get_width() * 0.2),(self.screen.get_height() * 0.75)),text_input="1$",font=self.myFont,base_color='yellow',hovering_color='green')
            self.redChipButton = Button.Button(image=pg.image.load('Images/Chips/red_chip.png'),pos=((self.screen.get_width() * 0.35),(self.screen.get_height() * 0.5)),text_input="5$",font=self.myFont,base_color='yellow',hovering_color='green')
            self.blueChipButton = Button.Button(image=pg.image.load('Images/Chips/blue_chip.png'),pos=((self.screen.get_width() * 0.5),(self.screen.get_height() * 0.75)),text_input="10$",font=self.myFont,base_color='yellow',hovering_color='green')
            self.greenChipButton = Button.Button(image=pg.image.load('Images/Chips/green_chip.png'),pos=((self.screen.get_width() * 0.65),(self.screen.get_height() * 0.5)),text_input="25$",font=self.myFont,base_color='yellow',hovering_color='green')
            self.blackChipButton = Button.Button(image=pg.image.load('Images/Chips/black_chip.png'),pos=((self.screen.get_width() * 0.8),(self.screen.get_height() * 0.75)),text_input="100$",font=self.myFont,base_color='yellow',hovering_color='green')
        

            self.screen.blits([(self.betText,self.betTextRect),(self.betAmountText,self.betAmountTextRect),(self.totalCashAmountText,self.totalCashAmountTextRect)])

            for button in [self.whiteChipButton, self.redChipButton, self.blueChipButton, self.greenChipButton, self.blackChipButton]:
                button.changeColor(self.mousePos)
                button.resize(160,160)
                button.update(self.screen)

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

            pg.display.update()
            pg.display.flip()
            self.frameSpeed.tick(60)

    def updateCosts(self):
        self.screen.fill('forestgreen')
        self.betAmountText = self.myFont.render('$' + str(self.bet), True, 'White', 'forestgreen')
        self.totalCashAmountText = self.myFont.render('$' + str(self.totalCash), True, 'White', 'forestgreen')

    def take_turn(self, playerName, betAmount):
        pass

newGame = Game(5000)