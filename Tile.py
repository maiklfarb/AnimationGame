import pygame
from pygame.sprite import Sprite

class Tile(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load(f"Images/q.png")
        self.rect = self.image.get_rect()

    def pos(self,x,y):
        self.rect.x = x
        self.rect.y = y
        return self

    def blitme(self):
        self.screen.blit(self.image, self.rect)