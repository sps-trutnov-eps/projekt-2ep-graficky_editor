import sys
import pygame
from pygame.locals import *

pygame.init()
window_size = 1920, 1025
window = pygame.display.set_mode(window_size)
gui = pygame.Rect(0, 0, 300, window_size[1])
slider = pygame.Rect(25, 50, 250, 25)  # Posuvník
slider_handle = pygame.Rect(25, 50, 25, 25)  # Posuvné tlačítko

black_button = pygame.Rect(25, 150, 110, 110)
blue_button = pygame.Rect(25, 285, 110, 110)
red_button = pygame.Rect(165, 285, 110, 110)
green_button = pygame.Rect(25, 420, 110, 110)
button_selector = pygame.Rect(20, 280, 120, 120)

brush_size = 50
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
    
    # Handle mouse click events for slider
    if mouse_pressed[0]:  # Left mouse button clicked
        if slider.collidepoint(mouse_pos):
            # Calculate brush size based on mouse position relative to slider
            rel_x = mouse_pos[0] - slider.x  # Relative position within the slider
            rel_x = max(0, min(rel_x, slider.width))  # Clamp within slider range
            brush_size = int(10 + (rel_x / slider.width) * 290)  # Map to range 10-300
            slider_handle.centerx = slider.x + rel_x  # Move handle to the correct position

        # Handle color change buttons
        if black_button.collidepoint(mouse_pos):
            brush_color = (0, 0, 0)
            button_selector.center = black_button.center
        elif blue_button.collidepoint(mouse_pos):
            brush_color = (0, 0, 255)
            button_selector.center = blue_button.center
        elif red_button.collidepoint(mouse_pos):
            brush_color = (255, 0, 0)
            button_selector.center = red_button.center
        elif green_button.collidepoint(mouse_pos):
            brush_color = (0, 255, 0)
            button_selector.center = green_button.center
    
    # Drawing with the brush
    if mouse_pressed[0]:  # Left mouse button pressed
        if not gui.collidepoint(mouse_pos):  # Only draw outside GUI
            brush_rect = pygame.Rect(0, 0, brush_size, brush_size)
            brush_rect.center = mouse_pos
            pygame.draw.ellipse(canvas, brush_color, brush_rect)
    
    # Render everything to the screen
    window.blit(canvas, (0, 0))
    pygame.draw.rect(window, (200, 200, 200), gui)
    pygame.draw.rect(window, (175, 175, 175), slider)  # Draw slider
    pygame.draw.rect(window, (50, 50, 50), slider_handle)  # Draw slider handle
    
    # Draw buttons
    pygame.draw.rect(window, (0, 0, 255), blue_button)
    pygame.draw.rect(window, (255, 0, 0), red_button)
    pygame.draw.rect(window, (0, 255, 0), green_button)
    pygame.draw.rect(window, (0, 0, 0), black_button)
    pygame.draw.rect(window, (100, 100, 100), button_selector, 2)
    
    # Dynamic brush preview
    brush_preview = pygame.Rect(0, 0, brush_size, brush_size)  # Dynamically adjust size
    brush_preview.center = mouse_pos
    pygame.draw.ellipse(window, (0, 0, 0), brush_preview, width=2)  # Draw preview outline
    
    pygame.display.flip()
