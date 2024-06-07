import pygame # importer la bibliothèque pygame
# Surf permet de créer la "surface" 
import math

def mouv():
    pygame.init()
    surf = pygame.display.set_mode((900, 600))
    run = True
    x1 = 50
    y1 = 50
    x2 = 850
    y2 = 550
    dx1 = 1
    dy1 = 1
    dx2 = -1
    dy2 = -1
    rayon = 30

    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        clock.tick(250) # 250 images par seconde
        surf.fill((0, 0, 0)) # couleur de fond de l'écran

        pygame.draw.circle(surf, (255, 255, 255), (x1, y1), rayon, 5)
        pygame.draw.circle(surf, (255, 0, 0), (x2, y2), rayon, 5)

        x1 = x1 + dx1 # déplacer le cercle , on peux aussi utiliser x1 += dx1
        y1 = y1 + dy1
        x2 = x2 + dx2
        y2 = y2 + dy2

        if x1 <= rayon or x1 >= 900 - rayon: # si le cercle touche le bord de l'écran
            dx1 = -dx1
        if y1 <= rayon or y1 >= 600 - rayon:
            dy1 = -dy1
        if x2 <= rayon or x2 >= 900 - rayon:
            dx2 = -dx2
        if y2 <= rayon or y2 >= 600 - rayon:
            dy2 = -dy2

        # Calculer la distance entre les centres des deux cercles
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if distance <= 2 * rayon:
            # les cercle change de direction
            dx1 = -dx1
            dy1 = -dy1
            dx2 = -dx2
            dy2 = -dy2 

        pygame.display.flip() # mettre à jour l'écran

    pygame.quit() # quitter pygame

mouv()