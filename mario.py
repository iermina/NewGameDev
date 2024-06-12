import pygame
class Mario:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.speed = 5

    def move(self, direction):
        if direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed
        elif direction == "up":
            self.y -= self.speed
        elif direction == "down":
            self.y += self.speed
        self.rect.topleft = (self.x, self.y)
