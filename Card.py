import pygame as pg
class Card:

    def __init__(self, value, suit, color, image):
        """Defines the variables that comprise a playing card."""
        self.value = value
        self.suit = suit
        self.color = color
        self.image = pg.image.load(image)
        self.image = pg.transform.smoothscale(self.image,(88,125))

    def get_value(self):
        return self.value

    def set_value(self, aNum):
        self.value = aNum

    def get_suit(self):
        return self.suit

    def set_suit(self, aSuit):
        self.suit = aSuit

    def get_color(self):
        return self.color

    def set_color(self, col):
        self.color = col

    def get_image(self):
        return self.image

    def set_image(self, aPic):
        self.value = aPic

    def draw(self,screen,x_pos,y_pos):
        self.rect = self.image.get_rect(center=(x_pos,y_pos))
        if self.image is not None:
            screen.blit(self.image, self.rect)