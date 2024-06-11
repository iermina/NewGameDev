import pygame
import random
from laser import Laser

class Enemy:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 2
        self.direction_change_time = pygame.time.get_ticks()
        self.direction = random.choice(["up", "down", "left", "right"])

    def move_randomly(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.direction_change_time > 1000:  # Change direction every second
            self.direction = random.choice(["up", "down", "left", "right"])
            self.direction_change_time = current_time

        if self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed

        # Ensure the enemy stays within the screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600

    def shoot_randomly(self, laser_image):
        directions = ["up", "down", "left", "right"]
        direction = random.choice(directions)
        if direction == "up":
            target_x, target_y = self.rect.centerx, 0
        elif direction == "down":
            target_x, target_y = self.rect.centerx, 600
        elif direction == "left":
            target_x, target_y = 0, self.rect.centery
        elif direction == "right":
            target_x, target_y = 800, self.rect.centery
        return Laser(self.rect.centerx, self.rect.centery, target_x, target_y, laser_image, 'goomba')

    def draw(self, screen):
        screen.blit(self.image, self.rect)
