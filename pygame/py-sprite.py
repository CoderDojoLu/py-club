#!/usr/bin/env python3
import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((800,600))

black = (0,0,0)
white = (255,255,255)

moveX,moveY = 0,0

clock = pygame.time.Clock()

class Sprite:

	def __init__(self, x ,y):

		self.x = x
		self.y = y
		self.width = 50
		self.height = 50

	def changeColor(self):
		playerColor = (r, g, b)


	def render(self):
		pygame.draw.rect(window, white, (self.x,self.y,self.width,self.height))

player = Sprite(100,150)
player2 = Sprite(100,150)
gameLoop = True

while gameLoop:
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			gameLoop = False

		if(event.type == pygame.KEYDOWN):

			if(event.key == pygame.K_LEFT):
				moveX = -5

			if(event.key == pygame.K_RIGHT):
				moveX = 5

			if(event.key == pygame.K_UP):
				moveY = -5

			if(event.key == pygame.K_DOWN):
				moveY = 5

		if(event.type == pygame.KEYUP):
			if(event.key == pygame.K_LEFT):
				moveX = 0

			if(event.key == pygame.K_RIGHT):
				moveX = 0

			if(event.key == pygame.K_UP):
				moveY = 0

			if(event.key == pygame.K_DOWN):
				moveY = 0

	window.fill(black)
	player.x += moveX
	player.y += moveY
	player.render()
	player2.render()
	clock.tick(50)
	pygame.display.flip()

pygame.quit()
