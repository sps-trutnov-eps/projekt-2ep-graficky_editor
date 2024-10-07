import sys
import pygame
import os
from pygame.locals import *

pygame.init
window_size = 1500, 900
window = pygame.display.set_mode(window_size)
gui = pygame.Rect(0, 0, 300, 900)
size_slider = pygame.Rect(25, 50, 250, 30)

brush1 = pygame.Rect(50, 50, 50, 50)
background = 1
while True:
    
    mouse_pressed = pygame.mouse.get_pressed()
    
    if background == 1: #původní zbarvení pozadí
        window.fill((255,255,255))
        background = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if mouse_pressed[0]: #0 je levý tlačítko na myši
        brush1.center = pygame.mouse.get_pos()
    
    pygame.draw.ellipse(window, (0, 0, 255), brush1)
    pygame.draw.rect(window, (200, 200, 200), gui)
    pygame.draw.rect(window, (175, 175, 175), size_slider)
    pygame.display.flip()

