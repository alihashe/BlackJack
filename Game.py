# import Player
import Deck
import Chip
# import Card
import pygame as pg
from sys import exit

class Game:

    def __init__(self, totalCash):
        self.totalCash = totalCash
        self.run_single_game()

    def run_single_game(self):

        # region Pygame Set-Up
        pg.init() # Initialize Pygame
        self.screen = pg.display.set_mode((1200,750)) # Set size of the window
        pg.display.set_caption('BlackJack') # Name the window
        pg.display.set_icon(pg.image.load('Images/Chips/red_chip.png').convert()) # Set Icon
        self.screen.fill('forestgreen') # Set Background Image
        self.frameSpeed = pg.time.Clock() # Framerate variable
        self.myFont = pg.font.Font(None, 35)  # <-- Do Later
        # endregion

        self.hand = 0 # The current total value of a players hand
        self.bet = 0 # The current amount of money riding on a turn.
        self.currCardVal = 0 # Value of a drawn card. Used when player hits.
        self.aDeck = pg.sprite.GroupSingle()
        self.aDeck.add(Deck.Deck(self.screen)) # Generate and shuffle a Deck

        # region Place Sprites and Text
        self.chipTypes = [] # Used to loop through the different types of poker chip rectangles
        betText = self.myFont.render('Please Choose The Amount You Would Like To Bet!', True, 'White')
        betAmountText = self.myFont.render('$' + str(self.bet), True, 'White')
        totalCashAmountText = self.myFont.render('$' + str(self.totalCash), True, 'White')
        self.whiteChip = pg.sprite.GroupSingle()
        self.whiteChip.add(Chip.Chip(1,'white','Images/Chips/white_chip.png',(self.screen.get_width() * 0.2),(self.screen.get_height() * 3) // 4)) # $1
        self.redChip = pg.sprite.GroupSingle()
        self.redChip.add(Chip.Chip(5,'red','Images/Chips/red_chip.png',(self.screen.get_width() * 0.35),(self.screen.get_height() * 2) // 4)) # $5
        self.blueChip = pg.sprite.GroupSingle()
        self.blueChip.add(Chip.Chip(10,'blue','Images/Chips/blue_chip.png',(self.screen.get_width() * 0.5),(self.screen.get_height() * 3) // 4)) # $10
        self.greenChip = pg.sprite.GroupSingle() 
        self.greenChip.add(Chip.Chip(25,'green','Images/Chips/green_chip.png',(self.screen.get_width() * 0.65),(self.screen.get_height() * 2) // 4)) # $25
        self.blackChip = pg.sprite.GroupSingle()
        self.blackChip.add(Chip.Chip(100,'black','Images/Chips/black_chip.png',(self.screen.get_width() * 0.8),(self.screen.get_height() * 3) // 4)) # $100

        betTextRect = betText.get_rect(center = (self.screen.get_width() // 2, 50))
        betAmountTextRect = betAmountText.get_rect(center = (self.screen.get_width() // 2, 100))
        totalCashAmountTextRect = totalCashAmountText.get_rect(center = (self.screen.get_width() - 75, self.screen.get_height() - 50))
        self.mouseRect = pg.draw.rect(self.screen, (0,0,0,0), pg.Rect(1, 1, 1, 1))
        self.chipTypes.append(self.whiteChip)
        self.chipTypes.append(self.redChip)
        self.chipTypes.append(self.blueChip)
        self.chipTypes.append(self.greenChip)
        self.chipTypes.append(self.blackChip)
        # endregion

        while(True):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

            self.aDeck.draw(self.screen)
            self.screen.blits([(betText, betTextRect),(betAmountText,betAmountTextRect),(totalCashAmountText,totalCashAmountTextRect)])
            for chip in self.chipTypes:
                chip.draw(self.screen)
            self.mouseRect.center = pg.mouse.get_pos()
            self.check_chips()

            pg.display.update()
            self.frameSpeed.tick(60)

    def check_chips(self):
        if self.mouseRect.colliderect(self.whiteChip.sprite):
            print("Touch white")
        else:
            pass
        #     self.whiteChip = pg.transform.smoothscale(self.whiteChip,(120,120))
        # if self.redChipRect.collidepoint(self.mousePos):
        #     self.redChip = pg.transform.smoothscale(self.redChip,(160,160))
        # else:
        #     self.redChip = pg.transform.smoothscale(self.redChip,(120,120))
        # if self.blueChipRect.collidepoint(self.mousePos):
        #     self.blueChip = pg.transform.smoothscale(self.blueChip,(160,160))
        # else:
        #     self.blueChip = pg.transform.smoothscale(self.blueChip,(120,120))
        # if self.greenChipRect.collidepoint(self.mousePos):
        #     self.greenChip = pg.transform.smoothscale(self.greenChip,(160,160))
        # else:
        #     self.greenChip = pg.transform.smoothscale(self.greenChip,(120,120))
        # if self.blackChipRect.collidepoint(self.mousePos):
        #     self.blackChip = pg.transform.smoothscale(self.blackChip,(160,160))
        # else:
        #     self.blackChip = pg.transform.smoothscale(self.blackChip,(120,120))

    def take_turn(self, playerName, betAmount):
        pass

newGame = Game(5000)