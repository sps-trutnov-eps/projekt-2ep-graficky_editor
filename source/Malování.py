import sys
import pygame
import os

pygame.init
window_size = 1200, 900
window = pygame.display.set_mode(window_size)

while True:
    
    window.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()

