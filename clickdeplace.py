import pygame
import random

surf = pygame.display.set_mode((800,600))
img = pygame.image.load("pyg.png")
action = True

def click(run):
  window_width = surf.get_width()# DKD
  window_height = surf.get_height()
  
  x = random.randint(0, window_width)
  y = random.randint(0, window_height)
  width = random.randint(50, 150)
  height = random.randint(50, 10)
  
  while run :
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if event.type == pygame.MOUSEBUTTONDOWN : #evenemnt du clic sousir
        if pygame.mouse.get_pressed() == (1,0,0) :#clic gauche
          mouse_pos = pygame.mouse.get_pos()
          if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
            x = random.randint(0, window_width)
            y = random.randint(0, window_height)
          
    surf.fill((0,0,0))
    # pygame.draw.rect(surf, (0, 0, 200), pygame.Rect(x, y, width, height))
    surf.blit(img, (x, y))
    pygame.display.flip()
  pygame.quit()
  
click(run=action)
