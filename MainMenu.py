import pygame as pg
import Button
import Game
from sys import exit

class MainMenu:
    
    def __init__(self, totalAmount):
        # region Pygame Set-Up
        pg.init() # Initialize Pygame
        self.screen = pg.display.set_mode((1200,750)) # Set size of the window
        self.screen.fill('forestgreen') # Set Background Image
        pg.display.set_caption('BlackJack') # Name the window
        pg.display.set_icon(pg.image.load('Images/Chips/green_chip.png').convert()) # Set Icon
        self.frameSpeed = pg.time.Clock() # Framerate variable
        self.smallUIFont = pg.font.Font(None, 35)  # <-- Do Later
        self.medUIFont = pg.font.Font(None, 60)  # <-- Do Later
        self.bigUIFont = pg.font.Font(None, 80)  # <-- Do Later
        selectSound = pg.mixer.Sound("Sounds/select-button.wav")
        # endregion
        while True:
            self.mousePos = pg.mouse.get_pos()
            self.startButton = Button.Button(image=pg.image.load('Images/default_button_1.png'),pos=((self.screen.get_width() * 0.5),(self.screen.get_height() * 0.45)),text_input='Begin Game',font=self.medUIFont,base_color='white',hovering_color='yellow')
            self.quitButton = Button.Button(image=pg.image.load('Images/default_button_1.png'),pos=((self.screen.get_width() * 0.5),(self.screen.get_height() * 0.65)),text_input='Quit Game',font=self.medUIFont,base_color='white',hovering_color='yellow')
            self.titleText = self.bigUIFont.render('Welcome to BlackJack!', True, 'White','forestgreen')

            self.titleTextRect = self.titleText.get_rect(center = (self.screen.get_width() * 0.5, self.screen.get_height() * 0.1))
            self.startButton.changeColor(self.mousePos)
            self.startButton.resize(350, 100)
            self.startButton.update(self.screen)
            self.quitButton.changeColor(self.mousePos)
            self.quitButton.resize(350, 100)
            self.quitButton.update(self.screen)
            self.screen.blit(self.titleText, self.titleTextRect)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.quitButton.checkForInput(self.mousePos):
                        pg.mixer.Sound.play(selectSound,loops=0)
                        pg.quit()
                        exit()
                    if self.startButton.checkForInput(self.mousePos):
                        pg.mixer.Sound.play(selectSound,loops=0)
                        Game.Game(totalAmount)

            pg.display.update()
            pg.display.flip()
            self.frameSpeed.tick(60)