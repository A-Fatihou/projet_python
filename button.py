import pygame

surf = pygame.display.set_mode((800,600))
bool_run = True

def ma_fonction(run):
  while run :
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if event.type == pygame.MOUSEBUTTONDOWN : #evenemnt du clic sousir
        if pygame.mouse.get_pressed() == (1,0,0) :#clic gauche
          print ("clic bouton gauche")
          pos = pygame.mouse.get_pos() #POSITION en x,y
          print(pos)
          
        if pygame.mouse.get_pressed() == (0,0,1) :# clic droit 
          print ("clic bouton droit")
          pos = pygame.mouse.get_pos()
          print(pos)
          
      if pygame.mouse.get_pressed() == (0,1,0) : #clic mid
          print ("mid")
          pos = pygame.mouse.get_pos()
          print(pos)
    surf.fill((0,0,0))
    pygame.display.flip()
  pygame.quit()
  
ma_fonction(bool_run)