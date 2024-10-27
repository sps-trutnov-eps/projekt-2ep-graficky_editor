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
brush_size = 50
brush_preview = brush1
canvas = pygame.Surface(window_size)
canvas.fill((255, 255, 255))

brush_color1 = (0, 0, 255)
while True:
    
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    stisknute = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    brush_preview.center = mouse_pos
    if mouse_pressed[0]: #0 je levý tlačítko na myši
        brush_rect = pygame.Rect(0, 0, brush_size, brush_size)
        brush_rect.center = mouse_pos
        pygame.draw.ellipse(canvas, brush_color1, brush1)
    
    if stisknute[pygame.K_PLUS]:
        brush_size += 1
    if stisknute[pygame.K_MINUS]:
        brush_size -= 1
    
    window.blit(canvas, (0, 0))
    pygame.draw.ellipse(window, (0, 0, 255), brush1)
    pygame.draw.ellipse(window, (0, 0, 0), brush_preview, width=2)
    pygame.draw.rect(window, (200, 200, 200), gui)
    pygame.draw.rect(window, (175, 175, 175), size_slider)
    pygame.display.flip()

