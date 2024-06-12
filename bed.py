import pygame

class Bed:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        # Scale the image to a larger size
        new_width = int(image.get_width() * 1)  # Example scaling factor of 2x
        new_height = int(image.get_height() * 1)  # Example scaling factor of 2x
        self.image = pygame.transform.scale(image, (new_width, new_height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def rescale_image(self, image):
        # Scale size to a larger size, adjust scaling factor as needed
        new_width = int(image.get_width() * 1)  # Example scaling factor of 2x
        new_height = int(image.get_height() * 1)  # Example scaling factor of 2x
        self.image = pygame.transform.scale(image, (new_width, new_height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def move_bed(self, direction):
        # Update the rectangle size
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

