""" moveCircle.py
    create a blue circle sprite and have it
    follow the mouse"""
    
import pygame, random
pygame.init()

screen = pygame.display.set_mode((640, 480))

class Circle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        pygame.draw.circle(self.image, (0, 0, 255), (25, 25), 25, 0)
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

def main():
    pygame.display.set_caption("move the circle with the mouse")
    
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    
    circle = Circle()
    allSprites = pygame.sprite.Group(circle)
    
    #hide mouse
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
        
    #return mouse
    pygame.mouse.set_visible(True)
    
if __name__ == "__main__":
    main()
    