#!/usr/bin/env python3
import pygame
from random import randint
from pygame.locals import QUIT


class Box(pygame.sprite.Sprite):

    def __init__(self, w, h, color):
        super().__init__()
        self.x_max, self.y_max = w, h
        self.x = randint(0, w)
        self.y = randint(0, h)
        self.x_speed = 10
        self.y_speed = 10
        self.width = 50
        self.height = 50

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.move_right = True
        self.move_down = True

    def bounce(self):
        self.move_right = not self.move_right
        self.move_down = not self.move_down

    def update(self):
        # Bounce on walls
        if self.x <= 0 or self.x + self.width >= self.x_max:
            self.move_right = not self.move_right
        if self.y <= 0 or self.y + self.height >= self.y_max:
            self.move_down = not self.move_down

        if self.move_right:
            self.x += self.x_speed
        else:
            self.x -= self.x_speed
        if self.move_down:
            self.y += self.y_speed
        else:
            self.y -= self.y_speed

        self.rect.x = self.x
        self.rect.y = self.y

if __name__ == '__main__':
    pygame.init()
    width = 300
    height = 400

    window = pygame.display.set_mode((width, height))
    black = (0, 0, 0)
    white = (255, 255, 255)
    clock = pygame.time.Clock()

    box1 = Box(width, height, white)
    box2 = Box(width, height, white)
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(box1)
    all_sprites_list.add(box2)
    background = pygame.Surface(window.get_size())

    while True:
        for i in pygame.event.get():
            if i.type == QUIT:
                exit()

        window.fill(black)

        # Call update on all the strites in the group
        all_sprites_list.update()

        if pygame.sprite.collide_rect(box1, box2):
            box1.bounce()
            box2.bounce()

        # all_sprites_list.clear(window, background)

        all_sprites_list.draw(window)
        clock.tick(30)
        pygame.display.flip()
