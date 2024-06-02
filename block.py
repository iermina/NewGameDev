import pygame

class Block:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
