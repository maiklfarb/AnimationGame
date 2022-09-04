import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, screen, tileMap):
        super().__init__()
        self.tileMap = tileMap
        self.JumpingHeight = None
        self.images = {"stay": "1.png", "left": "2.png", "right": "3.png"}

        self.screen = screen
        self.scrinRect = screen.get_rect()

        self.image = pygame.image.load(f"Images/{self.images['stay']}")
        self.rect = self.image.get_rect()

        self.anim_right = [pygame.image.load("images/pygame_right_1.png"),
                           pygame.image.load("images/pygame_right_2.png"),
                           pygame.image.load('images/pygame_right_3.png'),
                           pygame.image.load('images/pygame_right_4.png'),
                           pygame.image.load('images/pygame_right_5.png'),
                           pygame.image.load('images/pygame_right_6.png')]
        self.anim_left = [pygame.image.load("images/pygame_left_1.png"),
                           pygame.image.load("images/pygame_left_2.png"),
                           pygame.image.load('images/pygame_left_3.png'),
                           pygame.image.load('images/pygame_left_4.png'),
                           pygame.image.load('images/pygame_left_5.png'),
                           pygame.image.load('images/pygame_left_6.png')]
        self.anim_idle = pygame.image.load("images/pygame_idle.png")


        self.rect.midbottom = self.scrinRect.midbottom

        self.JUMP_PX = 180
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.isRight = False
        self.isLeft = False
        self.isJumping = False
        self.isUp = False
        self.isDown = False
        self.getJumpingHeght()

    def getJumpingHeght(self):
        self.JumpingHeight = self.y - self.JUMP_PX

    def StartJumping(self):
        self.isJumping = True
        self.isUp = True
        self.getJumpingHeght()

    def update(self):
        if self.isLeft and self.rect.left > 0:
            self.x -= 2
        elif self.isRight and self.rect.right < self.scrinRect.right:
            self.x += 2

        if self.isJumping:
            if self.isUp:
                self.y -= 10
                if self.y <= self.JumpingHeight:
                    self.isUp = False
                    self.isDown = True
            elif self.isDown:
                if not self.checkStopJumping():
                    self.y += 10
                else:
                    self.isJumping = False
                    self.isDown = False
        elif not self.checkStopJumping():
            self.y += 10

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self, animCount):
        if self.isLeft:
            self.screen.blit(self.anim_left[animCount // 10], self.rect)
        elif self.isRight:
            self.screen.blit(self.anim_right[animCount // 10], self.rect)
        else:
            self.screen.blit(self.anim_idle, self.rect)

    def checkStopJumping(self):
        collideTile = pygame.sprite.spritecollideany(self, self.tileMap)

        if collideTile != None:
            return True
        else:
            return False





