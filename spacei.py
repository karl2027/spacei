import pygame
from pygame.math import Vector2
from random import randint
import math

pygame.init()

fps = 60

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Screen
size = [400, 700]
screen = pygame.display.set_mode(size)

# Objects and variables
done = False
clock = pygame.time.Clock()


class Ship(pygame.sprite.Sprite):
    def __init__(self, start_pos):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface([50, 50])
        self.image = pygame.image.load('rocket.png')
        self.image = pygame.transform.scale(self.image, (76, 92))
        self.rect = self.image.get_rect()
        self.rect.x = start_pos.x
        self.rect.y = start_pos.y

    def update(self):
        self.rect.update()


x_speed = 0
y_speed = 0

class Laser(pygame.sprite.Sprite):
    def __init__(self, start_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('laser.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = start_pos.x
        self.rect.y = start_pos.y
        self.y_speed = 20


    def update(self):
        self.rect.update()

    def move(self):
        self.rect.y -= self.y_speed




all_sprites = pygame.sprite.Group()
all_lasers = pygame.sprite.Group()
player = Ship(Vector2(165, 600))
all_sprites.add(player)

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_speed = -5
            elif event.key == pygame.K_d:
                x_speed = 5
            if event.key == pygame.K_q:
                pygame.quit()
            if event.key == pygame.K_SPACE:
                laser = Laser(Vector2(player.rect.x, player.rect.y))
                all_sprites.add(laser)
                all_lasers.add(laser)

        #elif event.type == pygame.KEYUP:
            #if event.key == pygame.K_a or event.key == pygame.K_d:
                #x_speed = 0

    # --- Game Logic

    screen.fill((255, 255, 255))

    player.rect.x += x_speed

    for laser in all_lasers:
        laser.move()

    all_sprites.draw(screen)


    #Update screen
    pygame.display.flip()
    clock.tick(30)

# Close the window and quit.
pygame.quit()
