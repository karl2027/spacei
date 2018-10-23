import pygame

# Setup
pygame.init()

# Screen
size = [400, 700]
screen = pygame.display.set_mode(size)

# Objects and variables
done = False
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game Logic

    screen.fill((255, 255, 255))

    #Update screen
    pygame.display.flip()
    clock.tick(30)

# Close the window and quit.
pygame.quit()
