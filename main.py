import pygame
import random
from bed import Bed
from mario import Mario
from enemy import Enemy
from weapon import Weapon
from laser import Laser

# Pygame
pygame.init()
pygame.font.init()

# Set up display and colors
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bed Siege!")


# Load images
bed_load = pygame.image.load("bedsprite.png")
enemy_load = pygame.image.load("goomba_sprite.png")
mario_load = pygame.image.load("mariospritesheet.png")
laser_img = pygame.image.load("laser.png")  # Laser image for weapons
weapon_img = pygame.image.load("weapon.png")  # Example weapon image

# Create objects
bed = Bed(115, 150, bed_load)
enemy = Enemy(650, 500, enemy_load)
mario = Mario(100, 50, mario_load)
mario_weapon = Weapon("Blaster", weapon_img, 10, 15, laser_img)
lasers = []

# Game variables
game_over = False
start_time = None
score = 1000  # Starting health for enemy
bed_health = 1000

# Fonts
my_font = pygame.font.SysFont('Comic Sans', 30)

clock = pygame.time.Clock()

# Game state
state = "menu"  # "menu", "playing", "game_over"

# Difficulty levels
difficulties = {
    "easy": 500,
    "medium": 1000,
    "hard": 1500
}
selected_difficulty = None

# Function for when the game is in the menu
def game_menu():
    global state, selected_difficulty, score, bed_health, start_time
    screen.fill((0,0,255))
    menu_text = my_font.render("Choose Difficulty: Easy, Medium, Hard", True, (255, 255, 255))
    easy_button = my_font.render("Easy", True, (0, 255, 0))
    medium_button = my_font.render("Medium", True, (255, 255, 0))
    hard_button = my_font.render("Hard", True, (255, 0, 0))

    screen.blit(menu_text, (200, 200))
    screen.blit(easy_button, (350, 250))
    screen.blit(medium_button, (350, 300))
    screen.blit(hard_button, (350, 350))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if 350 <= mouse_x <= 450:
                if 250 <= mouse_y <= 280:
                    selected_difficulty = "easy"
                elif 300 <= mouse_y <= 330:
                    selected_difficulty = "medium"
                elif 350 <= mouse_y <= 380:
                    selected_difficulty = "hard"
                if selected_difficulty:
                    score = difficulties[selected_difficulty]
                    bed_health = 1000
                    start_time = pygame.time.get_ticks()
                    state = "playing"
    return True

# Function for when the game is still going on
def game_play():
    global score, game_over, state, bed_health
    screen.fill((234, 0, 255))
    current_time = (pygame.time.get_ticks() - start_time) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if enemy.rect.collidepoint(mouse_x, mouse_y):
                laser = mario_weapon.fire(mario.rect.centerx, mario.rect.top, enemy.rect.centerx, enemy.rect.centery)
                if laser:
                    lasers.append(laser)

    # Mario movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mario.move("left")
    if keys[pygame.K_RIGHT]:
        mario.move("right")
    if keys[pygame.K_UP]:
        mario.move("up")
    if keys[pygame.K_DOWN]:
        mario.move("down")

    if mario.rect.colliderect(enemy.rect): #if mario and enemy collide
        state = "game_over"

        game_over = True

    # Enemy
    enemy.move_randomly()
    if random.randint(1, 60) == 1:  # Random shooting by enemy more frequent
        lasers.append(enemy.shoot_randomly(laser_img))

    # Draw lasers
    for laser in lasers[:]:
        laser.move()
        if laser.rect.y < 0 or laser.rect.y > 600 or laser.rect.x < 0 or laser.rect.x > 800:
            lasers.remove(laser)
        else:
            screen.blit(laser.image, laser.rect)
            if laser.source == 'mario' and laser.rect.colliderect(enemy.rect):
                if score > 0:
                    score -= mario_weapon.damage
                    if score < 0:
                        score = 0
                lasers.remove(laser)
            elif laser.source == 'goomba' and laser.rect.colliderect(mario.rect):
                bed_health -= 100
                if bed_health < 0:
                    bed_health = 0
                lasers.remove(laser)
            elif laser.source == 'goomba' and laser.rect.colliderect(bed.rect):
                bed_health -= 100
                if bed_health < 0:
                    bed_health = 0
                lasers.remove(laser)

    # Draw objects
    screen.blit(bed.image, bed.rect)
    screen.blit(enemy.image, enemy.rect)
    screen.blit(mario.image, mario.rect)

    # Display score and bed health
    score_text = my_font.render(f"Enemy Health: {score}", True, (255, 255, 255))
    bed_health_text = my_font.render(f"Bed Health: {bed_health}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(bed_health_text, (10, 40))

    if current_time > 60 or score <= 0 or bed_health <= 0:
        state = "game_over"
        game_over = bed_health > 0

    return True

# Function for when the game ends
def game_over_screen():
    screen.fill((0, 0, 0))
    if game_over:
        result_text = my_font.render("You Won!", True, (0, 255, 0))
    else:
        result_text = my_font.render("You Lost!", True, (255, 0, 0))
    screen.blit(result_text, (350, 300))
    pygame.display.flip()
    pygame.time.wait(3000)
    return False


# Main game loop
running = True
while running:
    if state == "menu":
        running = game_menu()
    elif state == "playing":
        running = game_play()
    elif state == "game_over":
        running = game_over_screen()

    pygame.display.flip()
    clock.tick(60)

# End game
pygame.quit()
