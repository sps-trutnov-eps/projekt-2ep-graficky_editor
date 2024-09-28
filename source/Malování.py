import sys
import pygame
import os
from pygame.locals import *

pygame.init
window_size = 1200, 900
window = pygame.display.set_mode(window_size)

brush1 = pygame.Rect(50, 50, 50, 50)
while True:
    
    window.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    brush1.center = pygame.mouse.get_pos()
    
    pygame.draw.rect(window, (0, 0, 255), brush1)
    pygame.display.flip()

