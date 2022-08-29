#pygame шаблон

import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

#Colors (R, G, B)

BLACK = (0, 0, 0)

#render
screen.fill(BLACK)

pygame.display.flip()


#Create window

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

#game loop

running = True
while running:
	clock.tick(FPS)
	
	#quit
	if event.type == pygame.QUIT:
		running = False
	
pygame.quit()	
