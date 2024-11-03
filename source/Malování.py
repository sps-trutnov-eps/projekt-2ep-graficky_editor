import sys
import pygame
import os
from pygame.locals import *

pygame.init()
window_size = 1500, 900
window = pygame.display.set_mode(window_size)
gui = pygame.Rect(0, 0, 300, 900)
size_slider = pygame.Rect(25, 50, 250, 30)

brush_size = 50  # počáteční velikost štětce
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
            
    # Aktualizace pozice a velikosti štětce
    brush_rect = pygame.Rect(0, 0, brush_size, brush_size)
    brush_rect.center = mouse_pos

    # Kreslení na plátno
    if mouse_pressed[0]:  # levé tlačítko myši
        pygame.draw.ellipse(canvas, brush_color1, brush_rect)
    
    # Změna velikosti štětce pomocí + a -
    if stisknute[pygame.K_PLUS] or stisknute[pygame.K_KP_PLUS]:  # přidání i klávesnice s numerickými klávesami
        brush_size += 1
    if stisknute[pygame.K_MINUS] or stisknute[pygame.K_KP_MINUS]:
        brush_size = max(1, brush_size - 1)  # velikost štětce nemůže být menší než 1

    # Vykreslení na obrazovku
    window.blit(canvas, (0, 0))
    pygame.draw.ellipse(window, brush_color1, brush_rect)  # náhled štětce v aktuální velikosti a pozici
    pygame.draw.rect(window, (200, 200, 200), gui)
    pygame.draw.rect(window, (175, 175, 175), size_slider)
    pygame.display.flip()

