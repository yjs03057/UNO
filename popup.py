import pygame
from pygame.locals import *

class Popup(pygame.sprite.Sprite):
    def __init__(self, name, position):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.image.load('./img/'+name+'.png')
        self.position = position
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def get_name(self):
        return self.name
    def get_rect(self):
        return self.rect
