import pygame
import random

# Initialisation de pygame
pygame.init()

# Initialisation de la fenêtre graphique
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Rectangle aléatoire")
window.fill((255, 255, 255))

# Création d'une surface pour dessiner
surface = pygame.Surface((window_width, window_height))
surface.fill((255, 255, 255))

# Génération de positions aléatoires pour le rectangle
x = random.randint(0, window_width)
y = random.randint(0, window_height)
width = random.randint(50, 150)
height = random.randint(50, 150)

# Dessin du rectangle
pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(x, y, width, height))

# Affichage de la surface sur la fenêtre
window.blit(surface, (0, 0))
pygame.display.flip()

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Fermeture de pygame
pygame.quit()