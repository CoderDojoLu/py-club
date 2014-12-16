#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Modules
import sys, pygame, inputbox
from pygame.locals import *


# Constants
WIDTH=640
HEIGHT=480


# Classes
class Ball(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = loadImage("images/ball.png", True)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH / 2
		self.rect.centery = HEIGHT / 2
		self.speed = [ 0.5, -0.5]

	def refresh(self, time, gamePaddle):
		self.rect.centerx += self.speed[0] * time
		self.rect.centery += self.speed[1] * time
		if self.rect.left <= 0 or self.rect.right >= WIDTH:
			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time
		if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
			self.speed[1] = -self.speed[1]
			self.rect.centery += self.speed[1] * time

		if pygame.sprite.collide_rect(self, gamePaddle):
			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time

class Paddle(pygame.sprite.Sprite):
	def __init__(self, x):
		pygame.sprite.Sprite.__init__(self)
		self.image = loadImage("images/paddle.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = HEIGHT / 2
		self.speed = 0.5

	def move(self, time, keys):
		if self.rect.top >= 0:
			if keys[K_UP]:
				self.rect.centery -= self.speed * time
		if self.rect.bottom <= HEIGHT:
			if keys[K_DOWN]:
				self.rect.centery += self.speed * time




# Functions

def loadImage(filename, transparent=False):
	try: image = pygame.image.load(filename)
	except pygame.error as message:
		raise SystemExit(message)
	image = image.convert()
	if transparent:
		color = image.get_at((0,0))
		image.set_colorkey(color, RLEACCEL)
	return image



def main():
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Pygame Tests :)")

	backgroundImage = loadImage('images/bg.png')
	answer = inputbox.ask(screen, "Your name")
	ball = Ball()
	gamePaddle = Paddle(30)

	clock = pygame.time.Clock()

	while True:
		time = clock.tick(60)
		keys = pygame.key.get_pressed()
		for events in pygame.event.get():
			if events.type == QUIT:
				sys.exit(0)

		ball.refresh(time, gamePaddle)
		gamePaddle.move(time, keys)
		screen.blit(backgroundImage, (0,0))
		screen.blit(ball.image, ball.rect)
		screen.blit(gamePaddle.image, gamePaddle.rect)
		pygame.display.flip()
	return 0

if __name__ == '__main__':
	pygame.init()
	main()
