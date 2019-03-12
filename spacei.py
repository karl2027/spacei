import pygame
from pygame.math import Vector2
import random
import math

pygame.init()

fps = 600

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
myfont = pygame.font.SysFont('Comic Sans MS', 50)
myfont2 = pygame.font.SysFont('Comic Sans MS', 25)
x_speed = 0
y_speed = 0
game_over = False
enemy_speed = 3
kill_count = 0
start_hp = 1

SPAWN_TIMER = pygame.USEREVENT + 1
spawn_interval = 3000
pygame.time.set_timer(SPAWN_TIMER, spawn_interval)
SPAWN_TIMER_EL = pygame.USEREVENT + 2
spawn_interval_el = 30000
pygame.time.set_timer(SPAWN_TIMER_EL, spawn_interval)

class Ship(pygame.sprite.Sprite):
    def __init__(self, start_pos):
        pygame.sprite.Sprite.__init__(self)
        self.all_sprites = pygame.sprite.Group()
        self.image = pygame.image.load('rocket.png')
        self.image = pygame.transform.scale(self.image, (76, 92))
        self.rect = self.image.get_rect()
        self.rect.x = start_pos.x
        self.rect.y = start_pos.y
        self.rect.centerx = 38
        self.ship = pygame.sprite.Group()
        self.player = Ship(Vector2(165, 580))
        self.ship.add(player)
        self.all_sprites.add(player)

    def update(self):
        self.rect.update()

    def draw(self):



class Laser(pygame.sprite.Sprite):
    def __init__(self, start_pos):
        pygame.sprite.Sprite.__init__(self)
        self.all_lasers = pygame.sprite.Group()
        self.image = pygame.image.load('laser2.png')
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.centerx = start_pos.x
        self.rect.centery = start_pos.y
        self.y_speed = 30


    def update(self):
        self.rect.update()

    def move(self):
        self.rect.y -= self.y_speed


class Enemies(pygame.sprite.Sprite):
    def __init__(self, start_pos):
        pygame.sprite.Sprite.__init__(self)
        self.all_enemies = pygame.sprite.Group()
        self.image = pygame.image.load('enemy2.png')
        self.image = pygame.transform.scale(self.image, (60, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.generate_random_start_pos()
        self.rect.centery = start_pos.y
        self.y_speed = enemy_speed
        self.enemy = Enemies(Vector2())
        self.all_sprites.add(enemy)
        self.all_enemies.add(enemy)

    def generate_random_start_pos(self):
        start_pos_x = random.randint(10, 340)
        return start_pos_x

    def update(self, time_passed):
        self.rect.update()

    def move(self):
        self.rect.y += self.y_speed


class Ekstra_life(pygame.sprite.Sprite):
    def __init__(self, start_pos):
        pygame.sprite.Sprite.__init__(self)
        self.ekstra_lifes = pygame.sprite.Group()
        self.image = pygame.image.load('ekstra_life.png')
        self.image = pygame.transform.scale(self.image, (60, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.generate_random_start_pos()
        self.rect.centery = start_pos.y
        self.y_speed = enemy_speed
        self.ekstra_life = Ekstra_life(Vector2())
        self.ekstra_lifes.add(ekstra_life)
        self.all_sprites.add(ekstra_life)

    def generate_random_start_pos(self):
        start_pos_x = random.randint(10, 340)
        return start_pos_x

    def update(self, time_passed):
        self.rect.update()

    def move(self):
        self.rect.y += self.y_speed

class Spacei():
    def __init__(self):
        self.screen = pygame.display.set_mode([400,800])
        self.all_sprites = pygame.sprite.Group()

    def event_loop(self):
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
                    laser = Laser(Vector2(player.rect.centerx, player.rect.top))
                    all_sprites.add(laser)
                    all_lasers.add(laser)







# -------- Main Program Loop -----------
while not done:
    # --- Event Processing

        elif event.type == SPAWN_TIMER:
            pygame.time.set_timer(SPAWN_TIMER, 0)
            e = Enemies(Vector2())
            all_sprites.add(e)
            all_enemies.add(e)
            spawn_interval -= 100
            spawn_interval = max(spawn_interval, 500)
            pygame.time.set_timer(SPAWN_TIMER, spawn_interval)
        elif event.type == SPAWN_TIMER_EL:
            pygame.time.set_timer(SPAWN_TIMER_EL, 0)
            el = Ekstra_life(Vector2())
            all_sprites.add(el)
            ekstra_lifes.add(el)
            spawn_interval_el -= 5000
            spawn_interval_el = max(spawn_interval, 5000)
            pygame.time.set_timer(SPAWN_TIMER_EL, 30000)
        #elif event.type == pygame.KEYUP:
            #if event.key == pygame.K_UP:

    # --- Game Logic

    screen.fill((0, 0, 0))

    player.rect.x += x_speed

    for laser in all_lasers:
        laser.move()

    for enemy in all_enemies:
        enemy.move()

    for ekstra_life in ekstra_lifes:
        ekstra_life.move()

    instruction_text = myfont2.render('Kill the enemies and collect ekstra lives', False, (255, 255, 255))
    collisions_1 = pygame.sprite.groupcollide(all_lasers, all_enemies, True, True)
    collisions_2 = pygame.sprite.groupcollide(ship, all_enemies, False, True)
    collisions_3 = pygame.sprite.groupcollide(ship, ekstra_lifes, False, True)
    collisions_4 = pygame.sprite.groupcollide(all_lasers, ekstra_lifes, True, True)
    if start_hp == 0:
        game_over_text = myfont.render('GAME OVER', False, (255, 255, 255))
        game_over = True
        player.kill()
    if collisions_2:
        start_hp -= 1
    if collisions_1:
        kill_count += 1
        enemy_speed += 0.2
        e = Enemies(Vector2())
        #all_sprites.add(e)
        #all_enemies.add(e)
    if collisions_3:
        start_hp += 1
    if enemy.rect.y > 700:
        start_hp -= 1
        player.kill()
    if player.rect.centerx > 365:
        x_speed = 0
    if player.rect.centerx < 35:
        x_speed = 0
    kill_counter = myfont.render("Score: %d"%(kill_count), True, (255, 255, 255))
    game_hp = myfont.render("Lives: %d"%(start_hp), True, (255, 255, 255))
    screen.blit(kill_counter, (5, 5))
    screen.blit(game_hp, (5, 45))
    if player.rect.x > 340:
        kill_count += 1
    if done == True:
        print ('Score:', kill_count)




    all_sprites.draw(screen)
    if game_over == True:
        screen.blit(game_over_text,(90, 350))
    if done == False:
        screen.blit(instruction_text, (35, 680))






    #Update screen
    pygame.display.flip()
    clock.tick(30)

# Close the window and quit.
pygame.quit()

#High score = 73
