import pygame


class Mario:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("mariospritesheet.png")
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 3

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 1.5, self.image_size[1] * 1.5)
        self.image = pygame.transform.scale(self.image, scale_size)

    def move_mario(self, direction):
        # move the balloon up or down based on the direction!
        # don't let the balloon move if it's at the bottom or top of the screen
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
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
                if keys[pygame.K_UP]:
                    mario.moveUp(10)
