import sys
import pygame
import os
from pygame.locals import *

pygame.init()
window_size = 1500, 900
window = pygame.display.set_mode(window_size)
gui = pygame.Rect(0, 0, 300, 900)
size_slider = pygame.Rect(25, 50, 250, 25)
black_button = pygame.Rect(25, 150, 110, 110)
blue_button = pygame.Rect(25, 285, 110, 110)
red_button = pygame.Rect(165, 285, 110, 110)
green_button = pygame.Rect(25, 420, 110, 110)

brush_size = 50
brush1 = pygame.Rect(50, 50, brush_size, brush_size)
brush_preview = pygame.Rect(50, 50, brush_size, brush_size)
canvas = pygame.Surface(window_size)
canvas.fill((255, 255, 255))

brush_color = (0, 0, 255)  # Default color is blue

while True:
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    stisknute = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle mouse click events for changing brush color
    if mouse_pressed[0]:  # Left mouse button clicked
        if black_button.collidepoint(mouse_pos):
            brush_color = (0, 0, 0)  # Set brush to black
        elif blue_button.collidepoint(mouse_pos):
            brush_color = (0, 0, 255)  # Set brush to blue
        elif red_button.collidepoint(mouse_pos):
            brush_color = (255, 0, 0)  # Set brush to red
        elif green_button.collidepoint(mouse_pos):
            brush_color = (0, 255, 0)  # Set brush to green
    
    # Update brush preview position
    brush_preview.center = mouse_pos
    
    # Drawing with the brush
    if mouse_pressed[0]:  # Left mouse button pressed
        brush_rect = pygame.Rect(0, 0, brush_size, brush_size)
        brush_rect.center = mouse_pos
        pygame.draw.ellipse(canvas, brush_color, brush_rect)
    
    # Resize brush size with arrow keys
    if stisknute[pygame.K_UP]:
        if brush_size <= 300:
            brush_size += 1
            brush_preview.width += 1
            brush_preview.height += 1
    if stisknute[pygame.K_DOWN]:
        if brush_size >= 10:
            brush_size -= 1
            brush_preview.width -= 1
            brush_preview.height -= 1
    
    # Render everything to the screen
    window.blit(canvas, (0, 0))
    pygame.draw.ellipse(window, (0, 0, 255), brush1)  # Static brush preview
    pygame.draw.ellipse(window, (0, 0, 0), brush_preview, width=2)  # Dynamic brush preview
    
    # Draw GUI elements (buttons, sliders)
    pygame.draw.rect(window, (200, 200, 200), gui)
    pygame.draw.rect(window, (175, 175, 175), size_slider)
    
    pygame.draw.rect(window, (0, 0, 255), blue_button)  # Blue button
    pygame.draw.rect(window, (255, 0, 0), red_button)  # Red button
    pygame.draw.rect(window, (0, 255, 0), green_button)  # Green button
    pygame.draw.rect(window, (0, 0, 0), black_button)  # Black button
    
    pygame.display.flip()
