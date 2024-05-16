import pygame
import random
from bed import Bed
from block import Block
from mario import Mario
from enemy import Enemy

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("Game Name*")


# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
BED_START_X = 500

bed_load = pygame.image.load("bedsprite.png")
enemy_load = pygame.image.load("goomba_sprite.png")
block_load = pygame.image.load("block.png")



bed = Bed(BED_START_X, 250)
enemy = Enemy(505,300)
block = Block(200,350)


INITIAL_HOUSE_X = random.randint(0,600)
INITIAL_TREE_X = random.randint(0,600)
house_x = INITIAL_HOUSE_X
tree_x = INITIAL_TREE_X


# render the text for later

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------
clock = pygame.time.Clock()
frame = 0
while run:
    # --- Main event loop
    clock.tick(60)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((0,0,0))
    screen.blit(bed.image, bed.rect)
    screen.blit(enemy.image, enemy.rect)
    screen.blit(block.image, block.rect)
    pygame.display.update()

    frame += 1

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()