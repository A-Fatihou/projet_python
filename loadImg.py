import pygame

surf = pygame.display.set_mode((800,600))

img = pygame.image.load("pyg.png")

def loadImg():
  run = True
  x = 200 # position x de l'image
  y = 200
  dx = 5 # déplacement de l'image
  dy = 5
  clock = pygame.time.Clock()
  
  while run:
    for event in pygame.event.get(): # parcourir la liste des événements
      if event.type == pygame.QUIT: # si l'événement est de type QUIT
        run = False # on arrête la boucle

    x = x + dx
    y = y + dy

    if x <= 0 or x >= 730:
      dx *= -1
    if y <= 0 or y >= 500:
      dy *= -1
    clock.tick(60)
    surf.fill((0,0,0))
    surf.blit(img, (x, y))
    pygame.display.flip()

  pygame.quit()

loadImg()

