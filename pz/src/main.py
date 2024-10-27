import sys
import pygame
from pygame.locals import *
from const import *
from game import *

pygame.init()

DS=pygame.display.set_mode( GEME_SIZE )
game=Game(DS)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.mouseClickHandler(event.button)
    game.update()
    DS.fill( (255, 255, 255) )
    game.draw()
    pygame.display.update()

