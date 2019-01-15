import pygame
from pygame.math import Vector2
import random
import math

pygame.init()

fps = 60

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen
size = [400, 700]
screen = pygame.display.set_mode(size)

# Objects and variables
done = False
clock = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman', 30)
x_speed = 0
y_speed = 0
game_over = False
enemy_speed = 3
kill_count = 0

class Ship(pygame.sprite.Sprite):
    def __init__(self, start_pos):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface([50, 50])
        self.image = pygame.image.load('rocket.png')
        self.image = pygame.transform.scale(self.image, (76, 92))
        self.rect = self.image.get_rect()
        self.rect.x = start_pos.x
        self.rect.y = start_pos.y
        self.rect.centerx = 38

    def update(self):
        self.rect.update()

class Laser(pygame.sprite.Sprite):
    def __init__(self, start_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('laser2.png')
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.x = start_pos.x
        self.rect.y = start_pos.y
        self.y_speed = 20


    def update(self):
        self.rect.update()

    def move(self):
        self.rect.y -= self.y_speed


class Enemies(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('enemy.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.generate_random_start_pos()
        self.rect.y = 30
        self.y_speed = enemy_speed
        self.image = pygame.transform.rotate(self.image, 180)

    def generate_random_start_pos(self):
        start_pos_x = random.randint(0, 340)
        return start_pos_x

    def update(self, time_passed):
        self.rect.update()

    def move(self):
        self.rect.y += self.y_speed



#class Background(pygame.sprite.Sprite):
    #def __init__(self):
    #    self.image = pygame.image.load('background.png')
    #    self.image = pygame.transform.scale(self.image, (50, 50))


all_sprites = pygame.sprite.Group()
all_lasers = pygame.sprite.Group()
all_enemies = pygame.sprite.Group()
ship = pygame.sprite.Group()
player = Ship(Vector2(165, 600))
enemy = Enemies()
#background = Background()
ship.add(player)
#all_sprites.add(background)
all_sprites.add(enemy)
all_enemies.add(enemy)
all_sprites.add(player)

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -7
            if event.key == pygame.K_RIGHT:
                x_speed = 7
            if event.key == pygame.K_q:
                done = True
            if event.key == pygame.K_UP:
                laser = Laser(Vector2(player.rect.x, player.rect.y))
                all_sprites.add(laser)
                all_lasers.add(laser)

        #elif event.type == pygame.KEYUP:
            #if event.key == pygame.K_a or event.key == pygame.K_d:
                #x_speed = 0

    # --- Game Logic

    screen.fill((0, 0, 0))

    player.rect.x += x_speed

    for laser in all_lasers:
        laser.move()

    for enemy in all_enemies:
        enemy.move()

    collisions_1 = pygame.sprite.groupcollide(all_lasers, all_enemies, True, True)
    collisions_2 = pygame.sprite.groupcollide(ship, all_enemies, True, True)
    if collisions_2:
        game_over_text = myfont.render('GAME OVER', False, (255, 255, 255))
        game_over = True
    if collisions_1:
        kill_count += 1
        print (kill_count)
        #enemy_speed += 0.2
        e = Enemies()
        #all_sprites.add(e)
        #all_enemies.add(e)
    if enemy.rect.y > 700:
        game_over_text = myfont.render('GAME OVER', False, (255, 255, 255))
        game_over = True
        player.kill()
    if player.rect.centerx > 400:
        x_speed = 0
    if player.rect.centerx < 0:
        x_speed = 0
    kill_counter = myfont.render("Score: %d"%(kill_count), True, (255, 255, 255))
    screen.blit(kill_counter, (5, 30))




    all_sprites.draw(screen)
    if game_over == True:
        screen.blit(game_over_text,(100, 350))





    #Update screen
    pygame.display.flip()
    clock.tick(30)

# Close the window and quit.
pygame.quit()

#65
