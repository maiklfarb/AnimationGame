import pygame
import sys

from Tile import Tile
from Player import Player


class Two:
    def __init__(self):
        # Инициализация игры и движка pygame
        pygame.init()
        # Установи полноэкранный режим дисплея
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Animation Game")
        self.clock = pygame.time.Clock()

        self.animCount = 0
        self.TileMap = pygame.sprite.Group()
        self.player = Player(self.screen,self.TileMap)
        self.SetTiles()

    def SetTiles(self):
        self.TileMap.add(Tile(self.screen).pos(0, self.screen.get_height() - 50))
        self.TileMap.add(Tile(self.screen).pos(150, self.screen.get_height() - 50))
        self.TileMap.add(Tile(self.screen).pos(300, self.screen.get_height() - 50))
        self.TileMap.add(Tile(self.screen).pos(450, self.screen.get_height() - 50))
        self.TileMap.add(Tile(self.screen).pos(600, self.screen.get_height() - 50))
        self.TileMap.add(Tile(self.screen).pos(750, self.screen.get_height() - 50))
        self.TileMap.add(Tile(self.screen).pos(900, self.screen.get_height() - 50))
        self.TileMap.add(Tile(self.screen).pos(1050, self.screen.get_height() - 50))
        self.TileMap.add(Tile(self.screen).pos(1200, self.screen.get_height() - 50))
        self.TileMap.add(Tile(self.screen).pos(100, self.screen.get_height() * 3 / 4 + 10))
        self.TileMap.add(Tile(self.screen).pos(270,self.screen.get_height() * 2 / 3 - 40))
        self.TileMap.add(Tile(self.screen).pos(470,self.screen.get_height() * 2 / 4 - 20))
        self.TileMap.add(Tile(self.screen).pos(700,self.screen.get_height() * 2 / 4 - 20))
        self.TileMap.add(Tile(self.screen).pos(1050,self.screen.get_height() * 2 / 4 - 20))
        self.TileMap.add(Tile(self.screen).pos(870,self.screen.get_height() * 2 / 6 - 10))
        self.TileMap.add(Tile(self.screen).pos(700,self.screen.get_height() * 2 / 8 - 50))
        self.TileMap.add(Tile(self.screen).pos(500, self.screen.get_height() * 2 / 10 - 70))
        self.TileMap.add(Tile(self.screen).pos(300, self.screen.get_height() * 2 / 10 - 70))
    def BlitTileMap(self):
        for tile in self.TileMap.sprites():
            tile.blitme()

    # Метод проверки нажатия клавиши
    def CheckDown(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.isRight = True
        elif event.key == pygame.K_LEFT:
            self.player.isLeft = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            if not self.player.isJumping:
                self.player.StartJumping()


    def CheckUp(self,event):
        # Метод проверки отпускания клавиши
        if event.key == pygame.K_RIGHT:
            self.player.isRight = False
        elif event.key == pygame.K_LEFT:
            self.player.isLeft = False


    def CheckEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.CheckDown(event)
            elif event.type == pygame.KEYUP:
                self.CheckUp(event)

    def Jump(self):
        if self.player.isJumping:
            maxY = 500
            while (self.player.rect.y > maxY):
                pygame.time.delay(10)
                self.player.rect.y -= 10
                self.UpdateScreen()
                print(f"y персонажа: {self.player.rect.y}")

            while (self.player.rect.bottom < self.screen.get_height()):
                pygame.time.delay(10)
                self.player.rect.y += 10
                self.UpdateScreen()
                print(f"y персонажа: {self.player.rect.y}")

            self.isJumping = False

    def UpdateScreen(self):
        self.screen.fill((0,255,0))

        if self.animCount > 59:
            self.animCount = 0
        self.player.blitme(self.animCount)
        self.BlitTileMap()
        self.animCount += 1

        pygame.display.flip()

    def start(self):
        # Бесконечно делаем
        while True:
            self.clock.tick(60)

            self.CheckEvent()

            self.player.update()

            self.UpdateScreen()


if __name__ == '__main__':
    game = Two()
    game.start()