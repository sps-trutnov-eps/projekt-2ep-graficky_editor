import sys
import pygame
import os
from pygame.locals import *

pygame.init
window_size = 1500, 900
window = pygame.display.set_mode(window_size)
gui = pygame.Rect(0, 0, 300, 900)

brush1 = pygame.Rect(50, 50, 50, 50)
background = 1
while True:
    if background == 1:
        window.fill((255,255,255))
        background = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_SPACE]:
        brush1.center = pygame.mouse.get_pos()
            
        
    
    
    
    pygame.draw.rect(window, (0, 0, 255), brush1)
    pygame.draw.rect(window, (200, 200, 200), gui)
    pygame.display.flip()

