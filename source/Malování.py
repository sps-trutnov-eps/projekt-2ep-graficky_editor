import sys
import pygame
from pygame.locals import *

pygame.init()
window_size = 1500, 900
window = pygame.display.set_mode(window_size)
canvas = pygame.Surface(window_size)  # Vytvoření plátna pro kreslení
canvas.fill((255, 255, 255))  # Bílé pozadí na plátně
gui = pygame.Rect(0, 0, 300, 900)
size_slider = pygame.Rect(25, 50, 250, 30)

brush1 = pygame.Rect(50, 50, 50, 50)  # Výchozí velikost štětce
brush_size = 50  # Proměnná pro uchování velikosti štětce
brush_color = (0, 0, 255)  # Barva štětce

while True:
    mouse_pressed = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_KP_PLUS:  # zvětšit velikost štětce při stisknutí +
                brush_size += 5
            elif event.key == K_KP_MINUS:  # zmenšit velikost štětce při stisknutí -
                brush_size = max(5, brush_size - 5)  # Minimální velikost je 5, aby štětec nezmizel

    # Pokud je levé tlačítko myši stisknuté, kresli na plátno
    if mouse_pressed[0]:
        brush1.size = (brush_size, brush_size)
        brush1.center = pygame.mouse.get_pos()
        # Vykreslení elipsy na plátno na pozici myši
        pygame.draw.ellipse(canvas, brush_color, brush1)

    # Aktualizace okna - vykreslení plátna a GUI
    window.blit(canvas, (0, 0))  # Vykresli plátno do okna
    pygame.draw.rect(window, (200, 200, 200), gui)  # Vykreslení GUI
    pygame.draw.rect(window, (175, 175, 175), size_slider)  # Vykreslení slideru velikosti
    pygame.display.flip()
