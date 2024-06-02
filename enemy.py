import pygame

class Enemy:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.speed = 2

    def move_towards(self, target):
        if self.x < target.x:
            self.x += self.speed
        elif self.x > target.x:
            self.x -= self.speed
        if self.y < target.y:
            self.y += self.speed
        elif self.y > target.y:
            self.y -= self.speed
        self.rect.topleft = (self.x, self.y)

    def reset_position(self):
        self.x = 650
        self.y = 500
        self.rect.topleft = (self.x, self.y)
