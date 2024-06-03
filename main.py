import pygame
import random
from bed import Bed
from block import Block
from mario import Mario
from enemy import Enemy

# Initialize Pygame
pygame.init()
pygame.font.init()

# Set up display
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bed Wars")

# Load images
bed_load = pygame.image.load("bedsprite.png")
enemy_load = pygame.image.load("goomba_sprite.png")
block_load = pygame.image.load("block.png")
mario_load = pygame.image.load("mariospritesheet.png")

# Create objects
bed = Bed(500, 250, bed_load)
enemy = Enemy(650, 500, enemy_load)
block = Block(200, 350, block_load)
mario = Mario(100, 50, mario_load)
blocks = []
# Game variables
score = 0

# Create font object for score display
my_font = pygame.font.SysFont('Arial', 30)

clock = pygame.time.Clock()
frame = 0
rounds = 5
placing_blocks = True
blocks_placed = 0
current_round = 1
placing_time = 15
start_ticks = pygame.time.get_ticks()
enemy_try = False

# Main game loop
run = True
clock = pygame.time.Clock()
game_start = False
while game_start == False:
    pygame.display.set_caption("MENU")
while run and current_round <= rounds:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and placing_blocks and blocks_placed < 2:
            x,y = pygame.mouse.get_pos()
            blocks.append(Block(x,y, block_load))
            blocks_placed += 1
            if blocks_placed == 2:
                placing_blocks = False
    current_time = (pygame.time.get_ticks() - start_ticks) / 1000
    score += 100
    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mario.move("left")
    if keys[pygame.K_RIGHT]:
        mario.move("right")
    if keys[pygame.K_UP]:
        mario.move("up")
    if keys[pygame.K_DOWN]:
        mario.move("down")
    if not placing_blocks or current_time > placing_time:
    # Move enemy towards the bed
        enemy.move_towards(bed)
    for block in blocks:
        if enemy.rect.colliderect(block.rect):
            if not enemy_try:
                enemy_try = True
                enemy.rect.y += (enemy.rect.height // 2) * (1 if enemy.rect.centery < screen.get_height() // 2 else -1)
                break
    else:
        enemy_try = False

    if enemy_try and (enemy.rect.top<= 0) or enemy.rect.bottom >= screen.get_height():
        current_round += 1
        enemy.reset_position()
        enemy_try = False
        if current_round > rounds:
            run = False
    if enemy.rect.colliderect(bed.rect):
        current_round+= 1
        enemy.reset_position()
        if current_round>rounds:
            run = False

    # Check for collisions
    if mario.rect.colliderect(enemy.rect):
        pass
    if enemy.rect.colliderect(bed.rect):
        # Enemy reached the bed
        current_round += 1
        enemy.reset_position()
        if current_round > rounds:
            run = False

    # Draw objects
    screen.blit(bed.image, bed.rect)
    screen.blit(enemy.image, enemy.rect)
    screen.blit(block.image, block.rect)
    screen.blit(mario.image, mario.rect)
    for block in blocks:
        screen.blit(block.image, block.rect)

    # Display score
    score_text = my_font.render(f"Score: {score}", True, (100, 200, 0))
    screen.blit(score_text, (10, 10))
    if placing_blocks:
        time_text = my_font.render(f"Place blocks: {int(placing_time - current_time)}s left", True,(255,255,255))
        screen.blit(time_text, (500,10))
    # Update the display
    pygame.display.flip()
    clock.tick(60)

# End game
pygame.quit()

