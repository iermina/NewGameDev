import pygame
import random
from bed import Bed
from block import Block
from mario import Mario
from enemy import Enemy
pygame.init
# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("Game Name*")

background_image = pygame.image.load("background.png")
pygame.display.set_icon(background_image)
# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
BED_START_X = 500

bed_load = pygame.image.load("bedsprite.png")
enemy_load = pygame.image.load("goomba_sprite.png")
block_load = pygame.image.load("block.png")
mario_load = pygame.image.load("mariospritesheet.png")



bed = Bed(BED_START_X, 250)
enemy = Enemy(650,500)
block = Block(200,350)
mario = Mario(100,50)


INITIAL_HOUSE_X = random.randint(0,600)
INITIAL_TREE_X = random.randint(0,600)
mario_x = INITIAL_HOUSE_X
enemy_x = INITIAL_TREE_X


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
        if pygame.K_RIGHT:
            direction = "right"
        if pygame.K_LEFT:
            direction = "left"
        if pygame.K_UP:
            direction = "up"
        if pygame.K_DOWN:
            direction = "down"
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                mario.moveLeft(10)
            if keys[pygame.K_RIGHT]:
                mario.moveRight(10)
            if keys[pygame.K_DOWN]:
                mario.moveForward(10)


            pygame.display.flip()
            clock.tick(60)
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((0,0,0))
    screen.blit(bed.image, bed.rect)
    screen.blit(enemy.image, enemy.rect)
    screen.blit(block.image, block.rect)
    screen.blit(mario.image, mario.rect)
    pygame.display.update()

    frame += 1

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()