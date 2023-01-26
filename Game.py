# import Player
import Deck
# import Card
import pygame as pg
from sys import exit

class Game:

    def __init__(self, totalCash):
        self.hand = 0
        self.bet = 0
        self.currCardVal = 0
        self.totalCash = totalCash
        self.playerNames = []
        self.aDeck = Deck.Deck()
        pg.init()
        self.screen = pg.display.set_mode((800,600))
        pg.display.set_caption('BlackJack')
        pg.display.set_icon(pg.image.load('Images/Chips/red_chip.png').convert())
        self.screen.fill('forestgreen')
        self.frameSpeed = pg.time.Clock()
        self.myFont = pg.font.Font(None, 35)  # <-- Do Later
        self.run_single_game()

    def run_single_game(self):
        betText = self.myFont.render('Please Choose The Amount You Would Like To Bet!', True, 'White')
        # region Load Chip Images
        whiteChip = pg.image.load('Images/Chips/white_chip.png').convert_alpha() # $1
        whiteChip = pg.transform.scale(whiteChip,(120,120))
        redChip = pg.image.load('Images/Chips/red_chip.png').convert_alpha() # $5
        redChip = pg.transform.scale(redChip,(120,120))
        blueChip = pg.image.load('Images/Chips/blue_chip.png').convert_alpha() # $10
        blueChip = pg.transform.scale(blueChip,(120,120))
        greenChip = pg.image.load('Images/Chips/green_chip.png').convert_alpha() # $25
        greenChip = pg.transform.scale(greenChip,(120,120))
        blackChip = pg.image.load('Images/Chips/black_chip.png').convert_alpha() # $100
        blackChip = pg.transform.scale(blackChip,(120,120))

        betTextRect = betText.get_rect(center = (self.screen.get_width() // 2, 50))
        whiteChipRect = whiteChip.get_rect(center = (130, (self.screen.get_height()) * 3 // 4))
        redChipRect = redChip.get_rect(center = (260, (self.screen.get_height()) * 2 // 4))
        blueChipRect = blueChip.get_rect(center = (390, (self.screen.get_height()) * 3 // 4))
        greenChipRect = greenChip.get_rect(center = (520,  (self.screen.get_height()) * 2 // 4))
        blackChipRect = blackChip.get_rect(center = (650,  (self.screen.get_height()) * 3 // 4))
        # endregion

        while(True):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

            self.screen.blit(betText, betTextRect)
            self.screen.blits([(whiteChip,whiteChipRect),(redChip, redChipRect),(blueChip,blueChipRect),(greenChip,greenChipRect),(blackChip,blackChipRect)])
            pg.display.update()
            self.frameSpeed.tick(60)

    def take_turn(self, playerName, betAmount):
        pass

newGame = Game(5000)