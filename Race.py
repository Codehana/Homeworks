#! /usr/bin/env python3
import pygame
	
pygame.init()

d_width = 800
d_height = 600

black = (0,0,0)
white = (255,255,255)

Display = pygame.display.set_mode((d_width,d_height))
pygame.display.set_caption("Race")
time= pygame.time.Clock()

snakeImg = pygame.image.load("index.jpg")
x = (d_width * 0.5)
y = (d_width * 0.8)
x_change = 0

crashed = False

def snake(x,y):
	Display.blit(snakeImg,(x,y))

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
				crashed = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change = -5
			elif event.key == pygame.K_RIGHT:
				x_change = 5
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or pygame.K_RIGHT:
				x_change = 0	
	x+= x_change

	Display.fill(white)
	snake(x,y)
	pygame.display.update()
	time.tick(90)

pygame.quit()
quit()
