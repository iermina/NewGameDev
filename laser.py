import pygame
import math

class Laser:
    def __init__(self, x, y, target_x, target_y, image, source):
        self.image = pygame.transform.scale(image, (10, 30))  # Smaller laser
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.speed = 10
        self.source = source

        # Calculate direction
        dx = target_x - x
        dy = target_y - y
        distance = math.hypot(dx, dy)
        self.dx = dx / distance * self.speed
        self.dy = dy / distance * self.speed

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def draw(self, screen):
        screen.blit(self.image, self.rect)

