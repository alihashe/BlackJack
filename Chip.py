import pygame as pg

class Chip(pg.sprite.Sprite):

    def __init__(self, value, color, image, width, height):
        super().__init__()
        self.value = value
        self.color = color
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image,(120,120))
        self.rect = self.image.get_rect(center = (width,height))

    def get_value(self):
        return self.value

    def get_color(self):
        return self.color

    def scale_image(self):
        self.image = pg.transform.scale(self.image,(160,160))

    def descale_image(self):
        self.image = pg.transform.scale(self.image,(120,120))