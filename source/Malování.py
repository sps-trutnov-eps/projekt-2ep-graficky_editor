import sys
import pygame
from pygame.locals import *
import os
from datetime import datetime
from pathlib import Path

pygame.init()
window_size = 1920, 1025
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Kreslící aplikace")

# GUI konstanty
GUI_WIDTH = 300
gui = pygame.Rect(0, 0, GUI_WIDTH, window_size[1])
slider = pygame.Rect(25, 50, 250, 25)
slider_handle = pygame.Rect(25, 50, 25, 25)

# Tlačítka pro barvy a nástroje
light_blue_button = pygame.Rect(175, 225, 55, 55)
blue_button = pygame.Rect(100, 225, 55, 55)
dark_blue_button = pygame.Rect(25, 225, 55, 55)
red_button = pygame.Rect(25, 375, 55, 55)
green_button = pygame.Rect(25, 300, 55, 55)
black_button = pygame.Rect(25, 150, 55, 55)
eraser_button = pygame.Rect(100, 150, 55, 55)
clear_button = pygame.Rect(25, 555, 250, 50)  # Nové tlačítko pro vymazání plátna
save_button = pygame.Rect(25, 630, 250, 50)   # Nové tlačítko pro uložení
button_selector = pygame.Rect(20, 145, 65, 65)

# Inicializace plátna
brush_size = 50
canvas = pygame.Surface(window_size)
canvas.fill((255, 255, 255))
brush_color = (0, 0, 0)

# Historie pro Undo/Redo
canvas_history = [pygame.Surface.copy(canvas)]
history_position = 0
MAX_HISTORY = 10

def save_state():
    global history_position
    # Oříznutí historie od současné pozice
    del canvas_history[history_position + 1:]
    # Přidání nového stavu
    canvas_history.append(pygame.Surface.copy(canvas))
    if len(canvas_history) > MAX_HISTORY:
        canvas_history.pop(0)
    else:
        history_position += 1

def undo():
    global history_position
    if history_position > 0:
        history_position -= 1
        canvas.blit(canvas_history[history_position], (0, 0))

def redo():
    global history_position
    if history_position < len(canvas_history) - 1:
        history_position += 1
        canvas.blit(canvas_history[history_position], (0, 0))

def save_canvas():
    # Získání cesty ke složce Stažené soubory
    downloads_path = str(Path.home() / "Downloads")
    
    # Vytvoření názvu souboru s časovou značkou
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"kresba_{timestamp}.png"
    
    # Kompletní cesta k souboru
    full_path = os.path.join(downloads_path, filename)
    
    # Uložení obrázku
    pygame.image.save(canvas, full_path)
    return full_path

# Font pro text
font = pygame.font.SysFont(None, 25)

last_pos = None
drawing = False

while True:
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Zachycení začátku a konce kreslení pro historii
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not gui.collidepoint(mouse_pos):
                drawing = True
                last_pos = mouse_pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                drawing = False
                save_state()
        
        # Klávesové zkratky
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]):
                undo()
            elif event.key == pygame.K_y and (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]):
                redo()
    
    # Zpracování kliknutí na GUI prvky
    if mouse_pressed[0]:
        if slider.collidepoint(mouse_pos):
            rel_x = max(0, min(mouse_pos[0] - slider.x, slider.width))
            brush_size = int(10 + (rel_x / slider.width) * 290)
            slider_handle.centerx = slider.x + rel_x
        
        # Tlačítka barev
        elif black_button.collidepoint(mouse_pos):
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
        elif eraser_button.collidepoint(mouse_pos):
            brush_color = (255, 255, 255)
            button_selector.center = eraser_button.center
        # Nová tlačítka
        elif clear_button.collidepoint(mouse_pos):
            canvas.fill((255, 255, 255))
            save_state()
        elif save_button.collidepoint(mouse_pos):
            filename = save_canvas()
            print(f"Uloženo jako: {filename}")

    # Vylepšené kreslení s plynulými tahy
    if drawing and not gui.collidepoint(mouse_pos):
        current_pos = mouse_pos
        if last_pos:
            # Výpočet vzdálenosti mezi body
            distance = pygame.math.Vector2(current_pos[0] - last_pos[0], 
                                         current_pos[1] - last_pos[1]).length()
            # Pokud je vzdálenost příliš velká, interpolujeme body
            if distance > brush_size/2:
                steps = int(distance / (brush_size/4))
                for i in range(steps):
                    t = i / steps
                    x = int(last_pos[0] + (current_pos[0] - last_pos[0]) * t)
                    y = int(last_pos[1] + (current_pos[1] - last_pos[1]) * t)
                    brush_rect = pygame.Rect(0, 0, brush_size, brush_size)
                    brush_rect.center = (x, y)
                    pygame.draw.ellipse(canvas, brush_color, brush_rect)
            else:
                brush_rect = pygame.Rect(0, 0, brush_size, brush_size)
                brush_rect.center = current_pos
                pygame.draw.ellipse(canvas, brush_color, brush_rect)
        last_pos = current_pos

    # Vykreslení všeho na obrazovku
    window.blit(canvas, (0, 0))
    pygame.draw.rect(window, (200, 200, 200), gui)
    pygame.draw.rect(window, (175, 175, 175), slider)
    pygame.draw.rect(window, (50, 50, 50), slider_handle)
    
    # Vykreslení tlačítek
    pygame.draw.rect(window, (100, 100, 255), light_blue_button)
    pygame.draw.rect(window, (0, 0, 255), blue_button)
    pygame.draw.rect(window, (0, 0, 155), dark_blue_button)
    pygame.draw.rect(window, (255, 0, 0), red_button)
    pygame.draw.rect(window, (0, 255, 0), green_button)
    pygame.draw.rect(window, (0, 0, 0), black_button)
    pygame.draw.rect(window, (255, 255, 255), eraser_button)
    pygame.draw.rect(window, (200, 200, 200), clear_button)
    pygame.draw.rect(window, (200, 200, 200), save_button)
    pygame.draw.rect(window, (100, 100, 100), button_selector, 2)
    
    # Texty na tlačítkách
    eraser_text = font.render("Guma", True, (0, 0, 0))
    clear_text = font.render("Vymazat vše", True, (0, 0, 0))
    save_text = font.render("Uložit", True, (0, 0, 0))
    
    window.blit(eraser_text, eraser_text.get_rect(center=eraser_button.center))
    window.blit(clear_text, clear_text.get_rect(center=clear_button.center))
    window.blit(save_text, save_text.get_rect(center=save_button.center))
    
    # Náhled štětce
    if not gui.collidepoint(mouse_pos):
        brush_preview = pygame.Rect(0, 0, brush_size, brush_size)
        brush_preview.center = mouse_pos
        pygame.draw.ellipse(window, (0, 0, 0), brush_preview, width=2)
    
    pygame.display.flip()